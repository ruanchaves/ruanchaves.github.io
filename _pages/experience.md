---
layout: single
title: "Work"
permalink: /work/
author_profile: true
excerpt: "Quantified experience, leadership signals, and case studies."
redirect_from:
  - /experience/
---

{% assign candidate = site.data.candidate %}

<p class="page-intro">{{ candidate.hero.summary }}</p>

## Case studies

{% for case in candidate.case_studies %}
<section class="case-study case-study--expanded">
  <p class="case-study__meta">{{ case.company }}</p>
  <h2>{{ case.title }}</h2>
  <p class="case-study__outcome">{{ case.outcome }}</p>
  <p>{{ case.challenge }}</p>
  <div class="case-study__body">
    <div>
      <p class="panel-label">Approach</p>
      <ul>
        {% for step in case.approach %}
        <li>{{ step }}</li>
        {% endfor %}
      </ul>
    </div>
    <div>
      <p class="panel-label">Stack</p>
      <p class="stack-line">{{ case.stack | join: " · " }}</p>
    </div>
  </div>
</section>
{% endfor %}

## Career

{% for role in candidate.experience %}
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

## Strengths

<div class="chip-grid">
{% for group in candidate.skills %}
  {% for item in group.items %}
  <span class="chip">{{ item }}</span>
  {% endfor %}
{% endfor %}
</div>
