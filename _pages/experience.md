---
layout: single
title: "Experience"
permalink: /experience/
author_profile: true
excerpt: "Quantified experience, leadership signals, and case studies."
---

{% assign candidate = site.data.candidate %}

## Snapshot

<p>{{ candidate.hero.summary }}</p>

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

## Featured case studies

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

## Core strengths

<div class="skills-grid">
{% for group in candidate.skills %}
  <section class="content-panel">
    <h3>{{ group.category }}</h3>
    <p>{{ group.items | join: ", " }}</p>
  </section>
{% endfor %}
</div>
