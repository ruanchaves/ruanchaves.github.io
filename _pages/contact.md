---
layout: single
title: "Contact"
permalink: /contact/
excerpt: "Best ways to reach me for roles, consulting, or collaboration."
---

{% assign candidate = site.data.candidate %}

<section class="post-feature">
  <h2>Let's talk</h2>
  <p>I'm open to senior and staff AI engineer roles, with a preference for remote positions. I'm comfortable working across U.S., European, and Latin American time zones and have done so throughout my career.</p>
  <p>I'm a strong fit for teams building production GenAI, RAG, or applied NLP systems — especially where evaluation rigor and shipping discipline matter.</p>
  <p><a class="btn btn--primary" href="mailto:{{ candidate.contact.email }}">{{ candidate.contact.email }}</a></p>
</section>

<section class="editorial-grid">
  <div class="content-panel content-panel--dense">
    <p class="panel-label">Profiles</p>
    <ul class="compact-list">
      <li><a href="{{ candidate.contact.linkedin }}">LinkedIn</a></li>
      <li><a href="{{ candidate.contact.github }}">GitHub</a></li>
      <li><a href="{{ candidate.contact.scholar }}">Google Scholar</a></li>
    </ul>
  </div>
  <div class="content-panel content-panel--dense">
    <p class="panel-label">More context</p>
    <ul class="compact-list">
      <li><a href="/work/">Work and case studies</a></li>
      <li><a href="/cv/">Resume and PDF download</a></li>
    </ul>
  </div>
</section>
