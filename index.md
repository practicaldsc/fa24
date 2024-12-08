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
> We're in the final stretch! Some updates:
> - We have two review sessions: Monday 12/9 from 6:30-8:30PM and Tuesday 12/10 from 5-7PM. Both are in 1670 BBB and are recorded. Scroll down to see the content covered in each one.
> - If at least 85% of the class fills out both the internal [End-of-Semester Survey](https://docs.google.com/forms/d/e/1FAIpQLSfM0KHvq71kkyYHAKXHAD4Dk_mJx1P38o7PKhaN4U_xequ00Q/viewform) and the [Official Course Evaluations](https://umich.bluera.com/umich/) by Tuesday 12/10 at 11:59PM, we'll add 1% of extra credit to everyone's overall grade. **As of Sunday 12/8, we're only at ~60% completion!**
> - The deadline for the optional prediction competition in Homework 10 has been extended until Monday 12/9.

{% for module in site.modules %}
{{ module }}
{% endfor %}
