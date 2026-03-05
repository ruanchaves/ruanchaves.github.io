---
layout: single
title: "Contact"
permalink: /contact/
author_profile: true
excerpt: "Best ways to reach me for roles, consulting, or collaboration."
---

{% assign candidate = site.data.candidate %}

## Contact

<p>Email is the fastest way to reach me.</p>

<section class="contact-grid">
  <div class="content-panel">
    <h2>Email</h2>
    <p><a href="mailto:{{ candidate.contact.email }}">{{ candidate.contact.email }}</a></p>
  </div>
  <div class="content-panel">
    <h2>LinkedIn</h2>
    <p><a href="{{ candidate.contact.linkedin }}">{{ candidate.contact.linkedin }}</a></p>
  </div>
  <div class="content-panel">
    <h2>GitHub</h2>
    <p><a href="{{ candidate.contact.github }}">{{ candidate.contact.github }}</a></p>
  </div>
  <div class="content-panel">
    <h2>Google Scholar</h2>
    <p><a href="{{ candidate.contact.scholar }}">{{ candidate.contact.scholar }}</a></p>
  </div>
</section>

## What to review first

<ul>
  <li><a href="/experience/">Experience</a> for quantified delivery and scope.</li>
  <li><a href="/cv/">Resume</a> for a quick screening summary.</li>
  <li><a href="/projects/">Projects</a> and <a href="/research/">research</a> for deeper proof.</li>
</ul>
