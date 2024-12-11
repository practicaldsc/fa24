---
layout: page
title: 🏡 Home
description: >-
  Course homepage.
nav_order: 1
---

# Practical Data Science 🛠️

{: .no_toc }
{: .mb-2 }
EECS 398-003, Fall 2024 at the <b><span style="background-color: #FFCB05; color: #00274C">University of Michigan</span></b>
{: .no_toc }
{: .fs-6 .fw-300 .mb-2 }

<small>
Interested in taking the course next semester? Read [**this page**](next).
</small>

<!-- {% assign instructors = site.staffersnobio | where: 'role', 'Instructor' %} -->
{% for staffer in site.staffersnobio %}
{{ staffer }}
{% endfor %}

[Jump to the current week](#week-16-final-exam){: .btn }

{: .green }
The Final Exam is on Thursday 12/12 from 4-6PM! Read [this post on Ed](https://edstem.org/us/courses/61012/discussion/5866998) for information on how to study. Recordings and materials from this week's review sessions can be found below.

{% for module in site.modules %}
{{ module }}
{% endfor %}
