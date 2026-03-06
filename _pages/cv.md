---
layout: single
title: "Resume"
permalink: /cv/
redirect_from:
  - /resume
  - /resume/
excerpt: "Recruiter-ready summary, resume download, and core fit."
---

{% assign candidate = site.data.candidate %}

<section class="cta-panel">
  <h2>{{ candidate.resume.summary }}</h2>
  <p><a class="btn btn--primary" href="{{ candidate.resume.pdf_url }}">Download PDF resume</a></p>
</section>

<section class="metric-grid metric-grid--compact">
  <div class="metric-card">
    <p class="metric-card__value">5+</p>
    <p class="metric-card__label">Years in AI</p>
  </div>
  <div class="metric-card">
    <p class="metric-card__value">3</p>
    <p class="metric-card__label">Core environments</p>
    <p class="metric-card__detail">Banking, startups, open source</p>
  </div>
  <div class="metric-card">
    <p class="metric-card__value">2</p>
    <p class="metric-card__label">Flagship OSS projects</p>
    <p class="metric-card__detail">Napolab and Hashformers</p>
  </div>
</section>

## Selected experience

{% for role in candidate.experience limit: 4 %}
<section class="timeline-card">
  <div class="timeline-card__header">
    <div>
      <h2>{{ role.title }}</h2>
      <p class="timeline-card__company">{{ role.company }}</p>
    </div>
    <div class="timeline-card__meta">
      <p>{{ role.period }}</p>
      <p>{{ role.location }}</p>
    </div>
  </div>
  <ul>
    {% for item in role.highlights %}
    <li>{{ item }}</li>
    {% endfor %}
  </ul>
</section>
{% endfor %}

## Skills

{% for group in candidate.skills %}
<p class="panel-label">{{ group.category }}</p>
<div class="chip-row">
  {% for item in group.items %}
  <span class="chip">{{ item }}</span>
  {% endfor %}
</div>
{% endfor %}

<section class="editorial-grid">
  <div class="content-panel content-panel--dense">
    <p class="panel-label">Education</p>
    <ul class="compact-list">
    {% for item in candidate.resume.education %}
      <li>{{ item }}</li>
    {% endfor %}
    </ul>
  </div>
  <div class="content-panel content-panel--dense">
    <p class="panel-label">More proof</p>
    <p><a href="/projects/">Projects</a>, <a href="/research/">research</a>, and the <a href="/blog/">blog</a>.</p>
  </div>
</section>
