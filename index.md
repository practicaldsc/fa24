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

[Jump to the current week](#week-15-conclusion){: .btn }

{: .green }
> We're in the final stretch! Some updates:
> - **If at least 85% of the class fills out both the internal [End-of-Semester Survey](https://docs.google.com/forms/d/e/1FAIpQLSfM0KHvq71kkyYHAKXHAD4Dk_mJx1P38o7PKhaN4U_xequ00Q/viewform) and the [Official Course Evaluations](https://umich.bluera.com/umich/) by Tuesday 12/10 at 11:59PM, we'll add 1% of extra credit to everyone's overall grade.**
> - If you're still working on Homework 10 (submittable through Wednesday with slip days), read [**this Ed post**](https://edstem.org/us/courses/61012/discussion/5814556). The autograder denominator has been lowered from 24 to 22, and the deadline for the optional prediction competition has been extended until Monday 12/9.
> - **There will be no Homework 11** – everyone will receive 100% on it!
> - The [**Portfolio Homework**](portfolio) is due on Saturday 12/7; **no slip days** can be used on it.
> - We have exam review sessions on Monday and Tuesday of next week – scroll down to see topics, times, and locations.

{% for module in site.modules %}
{{ module }}
{% endfor %}
