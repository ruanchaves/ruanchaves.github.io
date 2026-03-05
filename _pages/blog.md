---
layout: single
title: "Blog"
permalink: /blog/
author_profile: true
excerpt: "Notes on evaluation, retrieval, prompting, and applied AI."
---

{% assign featured = site.posts.first %}

<section class="post-feature">
  <p class="panel-label">Latest</p>
  <h2><a href="{{ featured.url }}">{{ featured.title }}</a></h2>
  <p class="project-card__meta">{{ featured.date | date: "%B %d, %Y" }}</p>
  <p>{{ featured.excerpt }}</p>
  <p><a class="btn btn--primary" href="{{ featured.url }}">Read post</a></p>
</section>

<section class="topic-list">
  {% assign sorted_tags = site.tags | sort %}
  {% for tag in sorted_tags %}
    {% assign name = tag[0] %}
    {% if name != "medium" %}
    <a class="chip" href="/tags/#{{ name | slugify }}">{{ name }}</a>
    {% endif %}
  {% endfor %}
</section>

<section class="feature-grid">
{% for post in site.posts offset: 1 limit: 6 %}
  <article class="feature-card feature-card--post">
    <p class="project-card__meta">{{ post.date | date: "%Y" }}</p>
    <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
    <p>{{ post.excerpt }}</p>
    <p class="feature-card__footer">
      {% for tag in post.tags %}
        {% if tag != "medium" %}
          <span class="inline-chip">{{ tag }}</span>
        {% endif %}
      {% endfor %}
    </p>
  </article>
{% endfor %}
</section>

## Archive

{% assign current_year = "" %}
{% for post in site.posts %}
  {% assign post_year = post.date | date: "%Y" %}
  {% if post_year != current_year %}
    {% assign current_year = post_year %}
    <h2 class="archive__subtitle">{{ current_year }}</h2>
  {% endif %}
  <article class="archive-row">
    <div class="archive-row__meta">{{ post.date | date: "%b %d" }}</div>
    <div class="archive-row__body">
      <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
      <p>{{ post.excerpt }}</p>
    </div>
  </article>
{% endfor %}
