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
**Lecture**: TuTh 1:30-3:00PM, [1013 DOW](https://maps.app.goo.gl/Sw7tgHarQKJ9SBrFA); **Discussion**: F 2:30-3:30PM, [1670 BBB](https://maps.app.goo.gl/wuMosGqmKQ4KUmqdA)<br>
4 credits, ULCS for Computer Science majors; elective credit TBD for Data Science majors


{% assign instructors = site.staffers | where: 'role', 'Instructor' %}
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}

{: .success }
<!-- <small><b>What's this class about? 🙋</b></small><br> -->
Skills and tools for building practical data science projects, along with their theoretical underpinnings. `pandas`, `numpy`, `scikit-learn`, `BeautifulSoup`, and Jupyter Notebooks, and also the math behind loss functions, gradient descent, linear and logistic regression, and other key ideas in machine learning.

<center>

<iframe width="600" height="320" src="https://www.youtube.com/embed/Z75-_YK5_XM?si=ilsVZvq51tBPyHG3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

</center>

---

### Content

This course will train students to use industry-standard tools to solve real-world problems, while giving them an understanding of how these tools work under the hood. After taking this course, students will be prepared to build data science portfolios, participate in research across campus, and succeed in data science internships.

The course will roughly be split in two halves; while the topics in it may overlap with other existing courses, it will take a very practical approach.

<center>
<div class="two-columns-grid">
    <div>
    <b>Data Wrangling</b><br>
    <small>
        Python and Jupyter Notebooks<br>
        <code><small>numpy</small></code> arrays<br>
        Tabular Data Manipulation in <code><small>pandas</small></code><br>
        Exploratory Data Analysis and Data Visualization<br>
        Web Scraping and APIs<br>
        SQL<br>
        Regular Expressions and Text Processing<br>
    </small>
    </div>
    <div>
    <b>Applied Machine Learning</b><br>
    <small>
        Linear Regression through Linear Algebra<br>
        Feature Engineering in <code><small>scikit-learn</small></code><br>
        Regularization and Cross-Validation<br>
        Gradient Descent<br>
        Logistic Regression<br>
        Decision Trees and Random Forests<br>
        Unsupervised Learning<br>
    </small>
    </div>
</div>
</center>

The course will be based on courses I've taught in the past at both UC San Diego and UC Berkeley, including:
- [DSC 80: Practice of Data Science](https://dsc-courses.github.io/dsc80-2024-wi) (most similar)
- [DSC 40A: Theoretical Foundations of Data Science](https://dsc-courses.github.io/dsc40a-2024-sp)
- [Data 100: Principles and Techniques of Data Science](https://ds100.org/su20)

If the lectures, videos, and assignments linked above seem interesting to you, I think you will enjoy this course. With that said, I will tailor the course to best suit the needs of enrolled students – for instance, I know that students in the course won't have necessarily seen Python before, so we will introduce it as necessary.

---

### Format and Assessment

Lectures will be held in-person and recorded, and attendance will not be required. Discussions will be held in-person and run by GSIs/IAs, and attendance will also not be required. Office hours will largely be in-person, but there will be some remote options as well.

Students will be expected to complete **weekly homework assignments**, which will mostly comprise of programming assignments in Python and Jupyter Notebooks, with theoretical questions sprinkled throughout. The course will have **one midterm exam** and **one final exam** (dates TBD), both of which will be held in-person.

---

### Prerequisites

The course is open to students from all majors. The enforced prerequisites are discrete math (EECS 203), programming (EECS 280), calculus I, calculus II, and linear algebra.

<!-- - One of Math 214, Math 217, Math 296, Math 417, or Math 419, OR
- ROB 101, in combination with one of Math 116, Math 156, Math 176, or Math 186. (To be clear, ROB 101 itself is not a prereq. All you need to have taken is one linear algebra class, but if the linear algebra class you've taken is ROB 101, you need to also have taken a separate calculus class.) -->

If you're interested in the class but don't meet one of the prerequisites, email me and we can chat about your background. I encourage students of all backgrounds who are curious about data science to reach out!

---


### Frequently Asked Questions

**If I plan to take, or have already taken, a dedicated machine learning course (such as EECS 445), should I still take this course?**

Yes! The first half of this course introduces students to several tools and skills that aren't typically covered in other machine learning courses, like using more sophisticated features in `pandas`, scraping data from the internet, finding patterns in text data, etc. While the second half of the class does overlap a bit with more traditional machine learning courses, this course covers the content from a much more practical perspective. Students who have already seen machine learning will reinforce their understanding of the relevant concepts through hands-on, real-world examples (e.g. hyperparameter tuning in `sklearn`). Students who haven't already seen machine learning will develop an intuition for how various machine learning algorithms work, both practically and mathematically, giving them a strong foundation upon which further machine learning courses can build off of.

**What specific topics from linear algebra will the course use?**

In addition to matrix-vector multiplication, we will expect students to be familiar with the ideas of linear independence, spans, projections, and orthogonality. We will review these ideas when necessary, but it will help to have seen them already. We will provide links to linear algebra review material.

---

### Examples

The plots below are interactive, and involve examples we'll work on in the class.

<center>

<iframe src="assets/3d-plane.html" frameBorder="0" width="500" height="500"></iframe>

<br>

</center>

How do we find this "plane of best fit?" efficiently? How do we use it to make predictions?

<br>

<center>

<iframe src="assets/outages_by_year.html" frameBorder="0" width="600" height="425"></iframe>

<br>

</center>

What are the trends in power outages over time?