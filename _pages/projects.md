---
layout: single
title: "Projects"
permalink: /projects/
author_profile: true
excerpt: "Selected open-source and engineering proof."
---

{% assign candidate = site.data.candidate %}

## Featured projects

{% for project in candidate.projects %}
<section class="content-panel">
  <h2><a href="{{ project.url }}">{{ project.name }}</a></h2>
  <p class="project-card__meta">{{ project.stars }}</p>
  <p>{{ project.summary }}</p>
  <ul>
    {% for item in project.proof %}
    <li>{{ item }}</li>
    {% endfor %}
  </ul>
</section>
{% endfor %}

## External open-source contributions

{% for item in candidate.open_source_contributions %}
<section class="content-panel">
  <h3><a href="{{ item.url }}">{{ item.project }}</a></h3>
  <p>{{ item.summary }}</p>
</section>
{% endfor %}

## Why this matters for hiring

<p>The best indicator of fit is not just having used the right tools. It is shipping systems, contributing fixes upstream, and demonstrating good judgment about where research ideas do and do not hold up in practice.</p>
