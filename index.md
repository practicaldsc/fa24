---
layout: minimal
title: Practical Data Science 🛠️
description: >-
    Information about Practical Data Science, offered as EECS 398-003 in Fall 2024 at the University of Michigan.
---

# {{ site.title }} 🛠️
{: .no_toc }
{: .mb-2 }
EECS 398-003, Fall 2024 at the <b><span style="background-color: #FFCB05; color: #00274C">University of Michigan</span></b>
{: .no_toc }
{: .fs-6 .fw-300 .mb-2 }
**Lecture**: TuTh 1:30-3:00PM, [1013 DOW](https://maps.app.goo.gl/Sw7tgHarQKJ9SBrFA); **Discussion**: F 2:30-3:30PM, [1670 BBB](https://maps.app.goo.gl/wuMosGqmKQ4KUmqdA)


{% assign instructors = site.staffers | where: 'role', 'Instructor' %}
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}

{: .success }
<!-- <small><b>What's this class about? 🙋</b></small><br> -->
Skills and tools for building practical data science projects, along with their theoretical underpinnings. `pandas`, `numpy`, `scikit-learn`, `BeautifulSoup`, and Jupyter Notebooks, and also the math behind loss functions, gradient descent, and linear and logistic regression.

<center>
<iframe width="560" height="315" src="https://www.youtube.com/embed/lOnq_nwpJPg?si=gT7krC_Sf5IpFknA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</center>

---

### Content

The course will roughly be split into two halves:
<center>
<div class="two-columns-grid">
    <div>
    <b>First Half</b><br>
    <small>
        Python and Jupyter Notebooks<br>
        <code><small>numpy</small></code> arrays<br>
        Tabular Data Manipulation in <code><small>pandas</small></code><br>
        Exploratory Data Analysis and Data Visualization<br>
        Web Scraping and APIs<br>
        SQL<br>
        Regular Expressions and Text Processing<br>
        Inference and A/B Testing<br>
    </small>
    </div>
    <div>
    <b>Second Half</b><br>
    <small>
        Linear Regression through Linear Algebra<br>
        Feature Engineering in <code><small>scikit-learn</small></code><br>
        Regularization and Cross-Validation<br>
        Gradient Descent<br>
        Logistic Regression<br>
        Decision Trees and Random Forests<br>
        Clustering<br>
        Neural Networks<br>
    </small>
    </div>
</div>
</center>

The course will be based on courses I've taught in the past at both UC San Diego and UC Berkeley, including:
- [DSC 80: Practice of Data Science](https://dsc-courses.github.io/dsc80-2024-wi)
- [DSC 40A: Theoretical Foundations of Data Science](https://dsc-courses.github.io/dsc40a-2024-sp)
- [Data 100: Principles and Techniques of Data Science](https://ds100.org/su20)

If the lectures, videos, and assignments linked above seem interesting to you, I think you'll enjoy this course. With that said, I will tailor the course to best suit the needs of enrolled students – for instance, I know that students in the course haven't necessarily seen Python before, so we'll introduce it as necessary.

---

### Format and Assessment

Lectures will be held in-person and will be recorded. Discussions will be held in-person and run by GSIs/IAs. Office hours will largely be in-person, but there will be some remote options as well.

Students will be expected to complete **weekly homework assignments**, which will mostly comprise of programming assignments in Python and Jupyter Notebooks, with theoretical questions sprinkled throughout. The course will have **one midterm exam** and **one final exam** (dates TBD).

---

### Prerequisites

The enforced prerequisites are discrete math (EECS 203), programming (EECS 280), calculus I, calculus II, and linear algebra. To satisfy the calculus and linear algebra requirement, we'll accept:
- One of Math 214, Math 217, Math 296, Math 417, or Math 419.
- ROB 101, in combination with one of Math 116, Math 156, Math 176, or Math 186.

If you're interested in the class but don't meet one of the prerequisites, email me and we can chat about your background. I'm happy to support students of all backgrounds who are curious about data science!

---

### Credit

The course counts for 4 credits. It counts as an Upper Level CS (ULCS) elective course for Computer Science majors; any further credit will be listed here as it becomes available.

---

### Frequently Asked Questions

**If I plan to take EECS 445 (Machine Learning) in the future, should I still take this course?**

Yes, for two reasons:
1. There's a lot of content in this course that isn't covered in EECS 445 – specifically, the first ~half of the topics. Taking this course will build a diverse set of practical skills that aren't typically covered in machine learning courses, like using more sophisticated features in `pandas`, scraping data from the internet, finding patterns in text data, etc.
1. This course will provide a gentle introduction to the theoretical ideas that EECS 445 will expand on further. So, in that sense, it'll serve as good preparation for EECS 445.

**If I've already taken EECS 445 (Machine Learning), can I still take this course?**

No. While it's true that there's a lot in this class that isn't covered in EECS 445, the second half of the class would be review for you. If you fall in this boat and you're still interested, you'll be able to follow along with the course online – all materials (lectures, recordings, assignments) will be posted publicly here, at [practicaldsc.org](#).

**What specific topics from linear algebra will the course use?**

In addition to matrix-vector multiplication, we'll expect students to be familiar with the ideas of linear independence, spans, projections, and orthogonality. We'll review these ideas when necessary, but it'll help to have seen them already. Closer to the start of the semester, we'll provide links to linear algebra review material.