---
layout: single
title: "Writing"
permalink: /writing/
author_profile: true
excerpt: "Selected essays and technical writing."
---

{% assign candidate = site.data.candidate %}

<p>{{ candidate.writing.intro }}</p>

{% for article in candidate.writing.articles %}
<section class="content-panel">
  <h2><a href="{{ article.url }}">{{ article.title }}</a></h2>
  <p class="project-card__meta">{{ article.year }}</p>
  <p>{{ article.summary }}</p>
</section>
{% endfor %}

<section class="cta-panel">
  <h2>More writing</h2>
  <p>Additional posts live on <a href="{{ candidate.contact.medium }}">Medium</a>, but the goal here is to surface the pieces most relevant to hiring decisions in GenAI and applied NLP roles.</p>
</section>
