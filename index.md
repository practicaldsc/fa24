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

<!-- {: .green }
> Welcome to Practical Data Science! Remember to read the [**Syllabus**](syllabus).
> - **Read the [Syllabus](syllabus)**.
> - **Follow the instructions in [⚙️ Environment Setup](env-setup) – in particular, watch the new [Setup Walkthrough Video](https://www.loom.com/share/b74ed3c77fe74ef4a4fa4fcc2b247699) and work through the "Example Homework."**
> - **Fill out the [Welcome Survey](https://docs.google.com/forms/d/e/1FAIpQLSemfn-uzlSZUeY6rsonpboIv_6ANg9mGxWZ8tETDk4N4g4q_A/viewform)**.
> - **Make sure you can access [Ed](https://edstem.org/us/join/PKnfHw) (please post in [#4](https://edstem.org/us/courses/61012/discussion/5178244)!) and [Gradescope](https://www.gradescope.com/courses/823979).**
>
> On the waitlist? Make sure to still complete the Environment Setup and keep up with all assignments. We're trying to expand and will keep you posted. -->

{: .green }
**Welcome to Practical Data Science! 👋**

{% for module in site.modules %}
{{ module }}
{% endfor %}
