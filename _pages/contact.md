---
layout: single
title: "Contact"
permalink: /contact/
author_profile: true
excerpt: "Best ways to reach me for roles, consulting, or collaboration."
---

{% assign candidate = site.data.candidate %}

<section class="post-feature">
  <h2>{{ candidate.contact.email }}</h2>
  <p>Email is the fastest way to reach me.</p>
  <p><a class="btn btn--primary" href="mailto:{{ candidate.contact.email }}">Send email</a></p>
</section>

<section class="contact-inline">
  <a href="{{ candidate.contact.linkedin }}">LinkedIn</a>
  <a href="{{ candidate.contact.github }}">GitHub</a>
  <a href="{{ candidate.contact.scholar }}">Google Scholar</a>
  <a href="/cv/">Resume</a>
</section>
