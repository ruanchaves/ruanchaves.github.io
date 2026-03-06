---
layout: single
title: "Projects"
permalink: /projects/
excerpt: "Selected open-source and engineering proof."
---

{% assign candidate = site.data.candidate %}

## Flagship projects

<section class="feature-grid">
{% for project in candidate.projects limit: 2 %}
<article class="feature-card">
  <p class="project-card__meta">{{ project.label }} · {{ project.stars }}</p>
  <h2><a href="{{ project.url }}">{{ project.name }}</a></h2>
  <p>{{ project.summary }}</p>
  <ul>
    {% for item in project.proof %}
    <li>{{ item }}</li>
    {% endfor %}
  </ul>
</article>
{% endfor %}
</section>

<section class="editorial-grid">
  <div class="content-panel content-panel--dense">
    <p class="panel-label">Selected code</p>
    {% assign supporting = candidate.projects | slice: 2, 1 %}
    {% for project in supporting %}
    <article class="stack-card">
      <p class="project-card__meta">{{ project.label }}</p>
      <h3><a href="{{ project.url }}">{{ project.name }}</a></h3>
      <p>{{ project.summary }}</p>
    </article>
    {% endfor %}
  </div>
  <div class="content-panel content-panel--dense">
    <p class="panel-label">More</p>
    <p>Additional code, experiments, and open-source work live on <a href="https://github.com/ruanchaves">GitHub</a>.</p>
  </div>
</section>

## Selected contributions

{% for item in candidate.open_source_contributions %}
<section class="content-panel content-panel--dense">
  <h3><a href="{{ item.url }}">{{ item.project }}</a></h3>
  <p>{{ item.summary }}</p>
</section>
{% endfor %}
