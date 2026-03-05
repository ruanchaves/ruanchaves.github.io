---
layout: single
title: "Resume"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
excerpt: "Recruiter-ready summary, resume download, and core fit."
---

{% assign candidate = site.data.candidate %}

## Summary

<section class="cta-panel">
  <h2>{{ candidate.resume.summary }}</h2>
  <p><a class="btn btn--primary" href="{{ candidate.resume.pdf_url }}">Download PDF resume</a></p>
</section>

## Why I fit senior AI roles

<div class="highlight-list">
{% for item in candidate.fit_summary %}
<p>{{ item }}</p>
{% endfor %}
</div>

## Experience

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

## Skills

<div class="skills-grid">
{% for group in candidate.skills %}
  <section class="content-panel">
    <h3>{{ group.category }}</h3>
    <p>{{ group.items | join: ", " }}</p>
  </section>
{% endfor %}
</div>

## Education

<ul>
{% for item in candidate.resume.education %}
  <li>{{ item }}</li>
{% endfor %}
</ul>

## Selected research and awards

<ul>
{% for win in candidate.research.wins %}
  <li>{{ win }}</li>
{% endfor %}
</ul>

<p>For deeper proof, see <a href="/projects/">projects</a>, <a href="/research/">research</a>, and <a href="/writing/">writing</a>.</p>
