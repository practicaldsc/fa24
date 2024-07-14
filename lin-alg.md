---
layout: minimal
title: Linear Algebra Review Resources
---

[⬅️ back home](../)

# Linear Algebra Review Resources
{: .no_toc }
{: .mb-2 }
EECS 398-003, Fall 2024 at the <b><span style="background-color: #FFCB05; color: #00274C">University of Michigan</span></b>
{: .no_toc }
{: .fs-6 .fw-300 .mb-2 }

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"> </script>

<!-- ## Overview
{: .no_toc } -->

Linear algebra is a formal prerequisite of this course. However, many students either (1) expressed interest in taking the course but didn't satisfy the prerequisite, and hence were granted a waiver, or (2) have some linear algebra experience but would like a refresher before the course.

The goal of the videos and problems below is to get you up to speed on the linear algebra you'll need to know later on in this course. Most of the videos are taken from [DSC 40A](https://dsc-courses.github.io/dsc40a-2024-sp), a class I taught in my final quarter at UCSD. This content **is not** replacement for a formal linear algebra course – there are lots of ideas that are important in linear algebra that aren't touched on here at all – but it should give you enough to get by. 

<!-- TODO: mention that 40A assumed a prior linear algebra course -->

<!-- My hope is that these resources are useful not only to the students in this class, but also to students in other machine learning classes that have linear algebra as a prerequisite. (When I taught similar classes at UCSD and Berkeley, students always seemed to struggle with linear algebra.)  -->

<!-- TODO: what do students need to be able to do? work through the practice problems. -->

---

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


## Vectors and the dot product

<iframe width="800" height="225" src="https://www.youtube.com/embed/wT2wI9FuYZw?si=FPVqCerYGxSqLqWs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<small>
[📝 slides](../resources/lin-alg/1-vectors-dot-product.pdf){: .btn }
[🎥 video on YouTube](https://youtu.be/wT2wI9FuYZw){: .btn }
</small>

<details markdown="1">

<summary><b>Practice questions</b></summary>

**Question 1**

Consider the vectors $$\vec{u}$$ and $$\vec{v}$$ defined below:

$$\vec{u} = \begin{bmatrix} 1 \\ -3 \\ 8 \end{bmatrix} \qquad \vec{v} = \begin{bmatrix} 3 \\ 0 \\ -1 \end{bmatrix}$$

Determine the values of the following quantities.

**1.1.** $$\lVert \vec u \rVert$$

**1.2.** $$\vec u \cdot \vec v$$

**1.3.** $$\vec v^T \vec u$$

<!-- <center>
$$\lVert \vec u \rVert \qquad\qquad \vec u \cdot \vec v \qquad\qquad \vec v^T \vec u$$
</center> -->

<br>

**Question 2**

Suppose that on your way home from discussion section on North Campus, you drive 2 miles east and 7 miles north. How far away from North Campus do you live, and in what direction do you live relative to North Campus?

</details>

---

## The dot product, angles, and orthogonality

<iframe width="800" height="225" src="https://www.youtube.com/embed/-PrfZdGh11g?si=sIKE-MPmrMI_q9B3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<small>
[📝 slides](../resources/lin-alg/2-dot-product-angle-orthogonality.pdf){: .btn } &nbsp; [🎥 video on YouTube](https://youtu.be/-PrfZdGh11g){: .btn }
</small>

<details markdown="1">

<summary><b>Practice questions</b></summary>

**Question 3**

Consider the vectors $$\vec{u}$$ and $$\vec{v}$$ defined below:

$$\vec{u} = \begin{bmatrix} 1 \\ -3 \\ 8 \end{bmatrix} \qquad \vec{v} = \begin{bmatrix} 3 \\ 0 \\ -1 \end{bmatrix}$$

Determine the angle between $$\vec u$$ and $$\vec v$$ in the form of $$\cos^{-1} ( \cdot )$$.

<br>

**Question 4**

_Note: In addition to reviewing the concepts in the video, this question is also designed to refresh your understanding of limits from Calculus 1._

Consider the vectors $$\vec{x}$$ and $$\vec{y}$$ defined below:

$$\vec{x} = \begin{bmatrix} -4 \\ 3 \end{bmatrix} \qquad \vec{y} = \begin{bmatrix} 3 \\ c \end{bmatrix}$$

Here, $$c$$ is an unknown real number.

**4.1.** Determine the maximum possible angle between $$\vec x$$ and $$\vec y$$.

</details>

---

<!-- ## Span -->

<!-- ---

### Video 3: Projecting 1D


### Video 4: XYZ -->


---

<!-- ## Other Resources

The videos below are more detailed than those above, covering lots of important ideas we didn't touch on above (and won't get a chance to touch on in the course).

### Khan Academy

Take a look at Khan Academy's [linear algebra](https://www.khanacademy.org/math/linear-algebra) course. Specifically, look at:
- All of [Unit 1: Vectors and spaces](https://www.khanacademy.org/math/linear-algebra/vectors-and-spaces).

https://www.khanacademy.org/math/linear-algebra/matrix-transformations

-  Specific topics:
    https://www.khanacademy.org/math/multivariable-calculus/thinking-about-multivariable-function https://www.khanacademy.org/math/multivariable-calculus/thinking-about-multivariable-function/x786f2022:vectors-and-matrices/a/multivariable-calculus-prerequisites vectors and matrices
    - 

### 3blue1brown -->