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

[Jump to the current week](#week-13-classification-and-logistic-regression){: .btn }

<!-- {: .green }
> Note that we have three deadlines in the last week of class:
> - Homework 10, due Monday, December 2nd.
> - Homework 11, due Thursday, December 5th.
> - The Portfolio Homework, due Saturday, December 7th.<br>
> 
> Try and finish Homework 10 before the break, and come to office hours! -->

{% for module in site.modules %}
{{ module }}
{% endfor %}
