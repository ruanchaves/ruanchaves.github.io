#!/usr/bin/env python3
import csv
import json
import re
import time
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://scholar.google.com"
PROFILE_URL = "https://scholar.google.com/citations?user=3JDK8KEAAAAJ&hl=en"
WORKDIR = Path('/home/user/files')
RAW_HTML = WORKDIR / 'scholar_profile_raw.html'


def clean_text(value: str) -> str:
    if value is None:
        return ""
    value = value.replace('\u202a', '').replace('\u202c', '').replace('\u202b', '').replace('\u202d', '').replace('\u202e', '')
    value = re.sub(r'\s+', ' ', value)
    return value.strip()


def parse_profile(soup: BeautifulSoup):
    name = clean_text((soup.select_one('#gsc_prf_in') or {}).get_text(' ', strip=True) if soup.select_one('#gsc_prf_in') else "")
    affiliation = clean_text((soup.select_one('.gsc_prf_il .gsc_prf_ila') or {}).get_text(' ', strip=True) if soup.select_one('.gsc_prf_il .gsc_prf_ila') else "")

    ilines = [clean_text(x.get_text(' ', strip=True)) for x in soup.select('.gsc_prf_il')]
    verified_email = ""
    homepage = ""
    interests = [clean_text(x.get_text(' ', strip=True)) for x in soup.select('#gsc_prf_int a')]

    for line in ilines:
        if 'Verified email' in line:
            verified_email = line

    homepage_a = soup.select_one('#gsc_prf_ivh a.gsc_prf_ila')
    if homepage_a and homepage_a.get('href'):
        homepage = homepage_a['href']

    metrics = {}
    stats_rows = soup.select('#gsc_rsb_st tbody tr')
    for row in stats_rows:
        tds = row.select('td')
        if len(tds) >= 3:
            k = clean_text(tds[0].get_text(' ', strip=True)).lower().replace('-', '_')
            metrics[k] = {
                'all': clean_text(tds[1].get_text(' ', strip=True)),
                'since_2021': clean_text(tds[2].get_text(' ', strip=True)),
            }

    yearly = []
    years = [clean_text(x.get_text(' ', strip=True)) for x in soup.select('.gsc_g_t')]
    counts = [clean_text(x.get_text(' ', strip=True)) for x in soup.select('.gsc_g_al')]
    if years and counts and len(years) == len(counts):
        yearly = [{'year': y, 'citations': c} for y, c in zip(years, counts)]

    return {
        'name': name,
        'affiliation': affiliation,
        'verified_email': verified_email,
        'homepage': homepage,
        'research_interests': interests,
        'metrics': metrics,
        'yearly_citations': yearly,
    }


def parse_coauthors(soup: BeautifulSoup):
    coauthors = []
    for item in soup.select('#gsc_rsb_co li .gsc_rsb_aa'):
        a = item.select_one('.gsc_rsb_a_desc a')
        ext = item.select('.gsc_rsb_a_ext')
        coauthors.append({
            'name': clean_text(a.get_text(' ', strip=True)) if a else "",
            'profile_url': urljoin(BASE_URL, a.get('href', '')) if a else "",
            'affiliation_or_desc': clean_text(ext[0].get_text(' ', strip=True)) if len(ext) > 0 else "",
            'verified_email': clean_text(ext[1].get_text(' ', strip=True)) if len(ext) > 1 else "",
        })
    return coauthors


def parse_articles(soup: BeautifulSoup):
    articles = []
    for row in soup.select('#gsc_a_b tr.gsc_a_tr'):
        title_a = row.select_one('a.gsc_a_at')
        sub = row.select('td.gsc_a_t .gs_gray')
        cited_a = row.select_one('td.gsc_a_c a.gsc_a_ac')
        year_span = row.select_one('td.gsc_a_y span.gsc_a_h')

        title = clean_text(title_a.get_text(' ', strip=True)) if title_a else ""
        details_url = urljoin(BASE_URL, title_a.get('href', '')) if title_a else ""
        authors = clean_text(sub[0].get_text(' ', strip=True)) if len(sub) > 0 else ""
        venue = clean_text(sub[1].get_text(' ', strip=True)) if len(sub) > 1 else ""
        cited_by = clean_text(cited_a.get_text(' ', strip=True)) if cited_a else ""
        cited_by_url = cited_a.get('href', '').strip() if cited_a else ""
        cited_by_url = urljoin(BASE_URL, cited_by_url) if cited_by_url else ""
        year = clean_text(year_span.get_text(' ', strip=True)) if year_span else ""

        articles.append({
            'title': title,
            'authors': authors,
            'venue': venue,
            'year': year,
            'cited_by': cited_by,
            'cited_by_url': cited_by_url,
            'details_url': details_url,
        })
    return articles


def fetch_article_details(session: requests.Session, articles):
    details = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': PROFILE_URL,
    }

    for idx, article in enumerate(articles, start=1):
        url = article.get('details_url')
        if not url:
            continue

        item = {
            'title': article.get('title', ''),
            'details_url': url,
            'fields': {},
            'description': '',
        }

        try:
            resp = session.get(url, headers=headers, timeout=20)
            if resp.status_code != 200:
                item['error'] = f'HTTP {resp.status_code}'
                details.append(item)
                continue

            soup = BeautifulSoup(resp.text, 'html.parser')
            for row in soup.select('#gsc_oci_table .gs_scl'):
                label = row.select_one('.gsc_oci_field')
                value = row.select_one('.gsc_oci_value')
                if label and value:
                    k = clean_text(label.get_text(' ', strip=True))
                    v = clean_text(value.get_text(' ', strip=True))
                    item['fields'][k] = v

            desc = soup.select_one('#gsc_oci_descr .gsh_small')
            if desc:
                item['description'] = clean_text(desc.get_text(' ', strip=True))

            cited_link = soup.select_one('#gsc_oci_table .gsc_oci_value a[href*="scholar?oi=bibs"]')
            if cited_link and cited_link.get('href'):
                item['cited_by_url'] = urljoin(BASE_URL, cited_link['href'])

        except Exception as exc:
            item['error'] = str(exc)

        details.append(item)
        time.sleep(0.8)

    return details


def write_csv(path: Path, rows, fieldnames):
    with path.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in rows:
            writer.writerow(r)


def build_markdown(profile, coauthors, articles, details):
    lines = []
    lines.append('# Google Scholar Profile Export')
    lines.append('')
    lines.append(f"- Source: {PROFILE_URL}")
    lines.append(f"- Retrieved from raw HTML file: {RAW_HTML.name}")
    lines.append('')

    lines.append('## Profile')
    lines.append(f"- Name: {profile.get('name','')}")
    lines.append(f"- Affiliation: {profile.get('affiliation','')}")
    lines.append(f"- Verified email: {profile.get('verified_email','')}")
    lines.append(f"- Homepage: {profile.get('homepage','')}")
    lines.append(f"- Interests: {', '.join(profile.get('research_interests', []))}")
    lines.append('')

    lines.append('## Metrics')
    metrics = profile.get('metrics', {})
    for k, v in metrics.items():
        lines.append(f"- {k}: all={v.get('all','')}, since_2021={v.get('since_2021','')}")
    lines.append('')

    lines.append('## Yearly Citations')
    for p in profile.get('yearly_citations', []):
        lines.append(f"- {p['year']}: {p['citations']}")
    lines.append('')

    lines.append(f"## Co-authors ({len(coauthors)})")
    for c in coauthors:
        lines.append(f"- {c['name']} | {c['affiliation_or_desc']} | {c['verified_email']} | {c['profile_url']}")
    lines.append('')

    lines.append(f"## Articles ({len(articles)})")
    for a in articles:
        lines.append(f"- {a['title']} ({a['year']}) | Cited by {a['cited_by'] or '0'}")
        lines.append(f"  - Authors: {a['authors']}")
        lines.append(f"  - Venue: {a['venue']}")
        lines.append(f"  - Details: {a['details_url']}")
    lines.append('')

    lines.append(f"## Article Details Retrieved ({len(details)})")
    for d in details:
        lines.append(f"- {d.get('title','')}")
        if d.get('error'):
            lines.append(f"  - Error: {d['error']}")
            continue
        if d.get('fields'):
            for fk, fv in d['fields'].items():
                lines.append(f"  - {fk}: {fv}")
        if d.get('description'):
            lines.append(f"  - Description: {d['description']}")

    return '\n'.join(lines) + '\n'


def main():
    html = RAW_HTML.read_text(encoding='utf-8', errors='replace')
    soup = BeautifulSoup(html, 'html.parser')

    profile = parse_profile(soup)
    coauthors = parse_coauthors(soup)
    articles = parse_articles(soup)

    session = requests.Session()
    article_details = fetch_article_details(session, articles)

    data = {
        'source_url': PROFILE_URL,
        'profile': profile,
        'coauthors': coauthors,
        'articles': articles,
        'article_details': article_details,
    }

    (WORKDIR / 'scholar_profile_data.json').write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8'
    )

    write_csv(
        WORKDIR / 'scholar_articles.csv',
        articles,
        ['title', 'authors', 'venue', 'year', 'cited_by', 'cited_by_url', 'details_url'],
    )

    write_csv(
        WORKDIR / 'scholar_coauthors.csv',
        coauthors,
        ['name', 'affiliation_or_desc', 'verified_email', 'profile_url'],
    )

    # Flatten details for csv
    flat_details = []
    for d in article_details:
        flat_details.append({
            'title': d.get('title', ''),
            'details_url': d.get('details_url', ''),
            'error': d.get('error', ''),
            'description': d.get('description', ''),
            'authors': d.get('fields', {}).get('Authors', ''),
            'publication_date': d.get('fields', {}).get('Publication date', ''),
            'journal': d.get('fields', {}).get('Journal', ''),
            'conference': d.get('fields', {}).get('Conference', ''),
            'publisher': d.get('fields', {}).get('Publisher', ''),
            'pages': d.get('fields', {}).get('Pages', ''),
            'volume': d.get('fields', {}).get('Volume', ''),
            'issue': d.get('fields', {}).get('Issue', ''),
            'description': d.get('description', ''),
            'total_citations': d.get('fields', {}).get('Total citations', ''),
            'scholar_articles': d.get('fields', {}).get('Scholar articles', ''),
        })

    write_csv(
        WORKDIR / 'scholar_article_details.csv',
        flat_details,
        [
            'title', 'details_url', 'error', 'authors', 'publication_date', 'journal',
            'conference', 'publisher', 'pages', 'volume', 'issue', 'description',
            'total_citations', 'scholar_articles'
        ],
    )

    (WORKDIR / 'scholar_profile_summary.md').write_text(
        build_markdown(profile, coauthors, articles, article_details), encoding='utf-8'
    )

    print('Wrote files:')
    for name in [
        'scholar_profile_raw.html',
        'scholar_profile_data.json',
        'scholar_profile_summary.md',
        'scholar_articles.csv',
        'scholar_coauthors.csv',
        'scholar_article_details.csv',
    ]:
        p = WORKDIR / name
        print(f'- {p} ({p.stat().st_size} bytes)')


if __name__ == '__main__':
    main()
