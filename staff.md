---
layout: page
title: 👩‍🏫 Staff
description: A listing of all the course staff members.
nav_order: 6
---

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