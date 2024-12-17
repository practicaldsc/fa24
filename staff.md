---
layout: page
title: 👩‍🏫 Staff
description: A listing of all the course staff members.
nav_order: 6
---

{: .red }
**This is the course website for a previous iteration of the course. If you're looking for the most recent course website, look at [practicaldsc.org](https://practicaldsc.org).**

# 👩‍🏫 Staff

## Instructor

{% assign instructors = site.staffers | where: 'role', 'Instructor' %}
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}

## GSIs/IAs

{% assign tas = site.staffers | where: 'role', 'TA' %}
{% for staffer in tas %}
{{ staffer }}
{% endfor %}

## Graders

{% assign tas = site.staffers | where: 'role', 'Grader' %}
{% for staffer in tas %}
{{ staffer }}
{% endfor %}

## Alumni

{% assign tas = site.staffers | where: 'role', 'Alumni' %}
{% for staffer in tas %}
{{ staffer }}
{% endfor %}