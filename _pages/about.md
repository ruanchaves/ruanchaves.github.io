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
{% assign latest_post = site.posts.first %}

<section class="landing-stage">
  <div class="recruiter-hero">
    <p class="recruiter-hero__eyebrow">{{ candidate.hero.eyebrow }}</p>
    <h1 class="recruiter-hero__title">{{ candidate.hero.title }}</h1>
    <p class="recruiter-hero__summary">{{ candidate.hero.summary }}</p>
    <div class="recruiter-hero__actions">
      <a class="btn btn--primary" href="{{ candidate.hero.primary_cta.url }}">{{ candidate.hero.primary_cta.label }}</a>
      <a class="btn btn--inverse" href="{{ candidate.hero.secondary_cta.url }}">{{ candidate.hero.secondary_cta.label }}</a>
    </div>
  </div>
  <aside class="signal-panel">
    <p class="signal-panel__label">Recent outcomes</p>
    {% for item in candidate.featured_metrics %}
    <div class="signal-panel__metric">
      <p class="signal-panel__value">{{ item.value }}</p>
      <p class="signal-panel__meta">{{ item.label }}</p>
      <p class="signal-panel__detail">{{ item.detail }}</p>
    </div>
    {% endfor %}
  </aside>
</section>

<section class="proof-bar proof-bar--compact">
  {% for point in candidate.proof_points %}
  <div class="proof-bar__item">{{ point }}</div>
  {% endfor %}
</section>

## Work

<div class="highlight-list highlight-list--compact">
{% for item in candidate.fit_summary %}
<p>{{ item }}</p>
{% endfor %}
</div>

<section class="feature-grid">
{% for case in candidate.case_studies limit: 3 %}
  <article class="feature-card">
    <p class="case-study__meta">{{ case.company }}</p>
    <h2>{{ case.title }}</h2>
    <p class="case-study__outcome">{{ case.outcome }}</p>
    <p>{{ case.challenge }}</p>
    <ul>
      {% for step in case.approach limit: 2 %}
      <li>{{ step }}</li>
      {% endfor %}
    </ul>
    <p class="feature-card__footer">{{ case.stack | join: " · " }}</p>
  </article>
{% endfor %}
</section>

<section class="editorial-grid">
  <div class="content-panel content-panel--dense">
    <p class="panel-label">Flagship proof</p>
    {% for project in candidate.projects limit: 2 %}
    <article class="stack-card">
      <p class="project-card__meta">{{ project.label }} · {{ project.stars }}</p>
      <h3><a href="{{ project.url }}">{{ project.name }}</a></h3>
      <p>{{ project.summary }}</p>
    </article>
    {% endfor %}
  </div>
  <div class="content-panel content-panel--dense">
    <p class="panel-label">Selected writing</p>
    <article class="stack-card">
      <p class="project-card__meta">{{ latest_post.date | date: "%Y" }}</p>
      <h3><a href="{{ latest_post.url }}">{{ latest_post.title }}</a></h3>
      <p>{{ latest_post.excerpt }}</p>
    </article>
    <p><a href="/blog/">Browse all writing</a></p>
  </div>
</section>

<section class="cta-panel">
  <h2>Start with work, projects, or the resume.</h2>
  <p><a href="/work/">Work</a>, <a href="/projects/">projects</a>, <a href="/research/">research</a>, and the <a href="/cv/">resume</a> cover the strongest proof first.</p>
  <p><a class="btn btn--primary" href="/contact/">Get in touch</a></p>
</section>
