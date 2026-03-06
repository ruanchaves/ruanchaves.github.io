---
layout: single
title: "Research"
permalink: /research/
excerpt: "Publications, awards, and research-backed credibility."
---

{% assign candidate = site.data.candidate %}

<p class="page-intro">{{ candidate.research.summary }}</p>

## Selected publications

<section class="feature-grid">
{% for paper in candidate.research.publications limit: 3 %}
<article class="feature-card">
  <h2><a href="{{ paper.url }}">{{ paper.title }}</a></h2>
  <p class="project-card__meta">{{ paper.venue }} · {{ paper.year }}</p>
  <p>{{ paper.takeaway }}</p>
  </article>
{% endfor %}
</section>

{% assign remaining_papers = candidate.research.publications | slice: 3, 10 %}
{% if remaining_papers.size > 0 %}
## More papers

{% for paper in remaining_papers %}
<section class="content-panel content-panel--dense">
  <h3><a href="{{ paper.url }}">{{ paper.title }}</a></h3>
  <p class="project-card__meta">{{ paper.venue }} · {{ paper.year }}</p>
  <p>{{ paper.takeaway }}</p>
</section>
{% endfor %}
{% endif %}

## Earlier distinctions

<div class="highlight-list">
{% for win in candidate.research.earlier_distinctions %}
<p>{{ win }}</p>
{% endfor %}
</div>
