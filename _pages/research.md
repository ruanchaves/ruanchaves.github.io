---
layout: single
title: "Research"
permalink: /research/
author_profile: true
excerpt: "Publications, awards, and research-backed credibility."
---

{% assign candidate = site.data.candidate %}

<p>{{ candidate.research.summary }}</p>

## Selected publications

{% for paper in candidate.research.publications %}
<section class="content-panel">
  <h2><a href="{{ paper.url }}">{{ paper.title }}</a></h2>
  <p class="project-card__meta">{{ paper.venue }} · {{ paper.year }}</p>
  <p>{{ paper.takeaway }}</p>
</section>
{% endfor %}

## Additional results

<div class="highlight-list">
{% for win in candidate.research.wins %}
<p>{{ win }}</p>
{% endfor %}
</div>
