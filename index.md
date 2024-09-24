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
<!-- **Lecture**: TuTh 1:30-3:00PM, [1500 EECS](https://maps.app.goo.gl/JBGihmGrYYsgcnwN8)<br>
**Discussions**: F 12:30-1:30PM, [2147 GGBL](https://maps.app.goo.gl/U6R5aH5cdY838Tj77), or F 2:30-3:30PM, [1670 BBB](https://maps.app.goo.gl/wuMosGqmKQ4KUmqdA)<br>
4 credits • ULCS for Computer Science majors, Advanced Technical Elective or Application Elective for Data Science majors, Flexible Technical Elective for Electrical Engineering majors

{: .success } -->

<!-- {% assign instructors = site.staffersnobio | where: 'role', 'Instructor' %} -->
{% for staffer in site.staffersnobio %}
{{ staffer }}
{% endfor %}


[Jump to the current week](#week-5-web-scraping-and-apis){: .btn }

{% for module in site.modules %}
{{ module }}
{% endfor %}
