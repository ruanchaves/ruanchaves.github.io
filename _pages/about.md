---
permalink: /
title: ""
excerpt: "Senior AI Engineer building production GenAI systems with measurable impact."
author_profile: true
redirect_from: 
  - /about.html
  - /about/
---
{% assign candidate = site.data.candidate %}

<section class="recruiter-hero">
  <p class="recruiter-hero__eyebrow">{{ candidate.hero.eyebrow }}</p>
  <h1 class="recruiter-hero__title">{{ candidate.hero.title }}</h1>
  <p class="recruiter-hero__summary">{{ candidate.hero.summary }}</p>
  <div class="recruiter-hero__actions">
    <a class="btn btn--primary" href="{{ candidate.hero.primary_cta.url }}">{{ candidate.hero.primary_cta.label }}</a>
    <a class="btn btn--inverse" href="{{ candidate.hero.secondary_cta.url }}">{{ candidate.hero.secondary_cta.label }}</a>
  </div>
</section>

<section class="proof-bar">
  {% for point in candidate.proof_points %}
  <div class="proof-bar__item">{{ point }}</div>
  {% endfor %}
</section>

<section class="metric-grid">
  {% for item in candidate.featured_metrics %}
  <div class="metric-card">
    <p class="metric-card__value">{{ item.value }}</p>
    <p class="metric-card__label">{{ item.label }}</p>
    <p class="metric-card__detail">{{ item.detail }}</p>
  </div>
  {% endfor %}
</section>

## Selected work

<div class="highlight-list">
{% for item in candidate.fit_summary %}
<p>{{ item }}</p>
{% endfor %}
</div>

## Case studies

{% for case in candidate.case_studies %}
<section class="case-study">
  <p class="case-study__meta">{{ case.company }}</p>
  <h3>{{ case.title }}</h3>
  <p class="case-study__outcome">{{ case.outcome }}</p>
  <p>{{ case.challenge }}</p>
  <ul>
    {% for step in case.approach %}
    <li>{{ step }}</li>
    {% endfor %}
  </ul>
  <p><strong>Stack:</strong> {{ case.stack | join: ", " }}</p>
</section>
{% endfor %}

## Highlights

<div class="two-column-grid">
  <section class="content-panel">
    <h3>Recent delivery</h3>
    <ul>
      <li>6x lower acquisition cost from a production AI sales assistant.</li>
      <li>90% lower inference cost on a production RAG workflow.</li>
      <li>Hours-to-minutes indexing reduction for retrieval over proprietary product data.</li>
    </ul>
  </section>
  <section class="content-panel">
    <h3>Open source and research</h3>
    <ul>
      <li><a href="/projects/">Projects</a> covers Napolab, Hashformers, and external contributions.</li>
      <li><a href="/research/">Research</a> covers selected publications and benchmark work.</li>
      <li><a href="/blog/">Blog</a> collects on-site writing on evaluation and applied AI.</li>
    </ul>
  </section>
</div>

<section class="cta-panel">
  <h2>Start with experience, projects, or the resume.</h2>
  <p><a href="/experience/">Experience</a>, <a href="/projects/">projects</a>, <a href="/research/">research</a>, and the <a href="/cv/">resume</a> cover the strongest proof first.</p>
  <p><a class="btn btn--primary" href="/contact/">Get in touch</a></p>
</section>
