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
The specifications for the Portfolio Homework have been released; take a look [**here**](portfolio)! -->

{% for module in site.modules %}
{{ module }}
{% endfor %}
