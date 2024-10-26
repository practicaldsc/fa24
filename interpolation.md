---
layout: default
nav_exclude: true
title: "🫧 Polynomial Interpolation"
liquid: false
---

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"> </script>


# 🫧 Polynomial Interpolation
{:.no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}


## Definition

A **polynomial** is a function that consists solely of terms of the form $$ax^k$$, where $$k$$ is a non-negative integer, and $$a$$ is a real number. As a function, it takes real numbers as an input and returns real numbers as outputs ($$f \colon \mathbb{R} \rightarrow \mathbb{R}$$). More formally, we define an $$n$$th degree polynomial in the following way:

<div align=center>

$$\boxed{p(x) = \sum_{k = 0}^{n} a_kx^k = a_0 + a_1x + a_2x^2 + ... + a_nx^n}$$

</div>

We say a polynomial has degree $$n$$ if $$x^{n}$$ is the largest power of $$x$$ that has a non-zero coefficent, i.e. 

<div align=center>

$$\textbf{deg}\left( p(x) \right) = \max_{k} \left(a_k \neq 0\right)$$

</div>

Here are examples of polynomials, along with their degrees:

| Polynomial | Degree |
| --- | --- |
| $$-5 + x$$ | $$1$$ |
| $$3 - 4x + 13x^2$$ | $$2$$ |
| $$x^{4} + x^{13} - x^{14}$$ | $$14$$ |
| $$4$$ | $$0$$ |

The examples above are all written in **standard form** – that is, the form defined in the box at the start of this page. We will look at different representations of polynomials shortly.

---

## Point Representation

The first key feature is that **a polynomial of degree $$n$$ is uniquely determined by a set of $$n+1$$ points**. This is a concept we've seen before, with regards to a line – in the $$xy$$-plane, there is exactly one line (i.e. a polynomial of degree 1) that passes through these points. It's impossible to draw a different line that also passes through these two points. However, given just one point in the plane, there are an infinite number of lines that pass through it.

This applies to polynomials of all degrees. Any three points uniquely determine a parabola (a polynomial of degree 2); however, given any two or fewer points, an infinite number of parabolas pass through them. 

Here, we see the only line that passes through the points $$(1, 4)$$ and $$(3, 10)$$:

<div align=center>

<img src="../assets/interpolation/linear.png" width="400">

</div>

<br>

However, there are infinitely many parabolas that pass through these two points. Three of them are shown below:

<div align=center>

<img src="../assets/interpolation/parabolas.png" width="400">

</div>

<br>

Consider the set of points $$S = \{(1, 3), (3, 19), (4, 33)\}$$. These three points uniquely determine a degree 2 polynomial - you should verify on your own that this polynomial is $$p(x) = 1 + 2x^2$$. Since $$1 + 2x^2$$ is the only polynomial of degree 2 that passes through these points exactly, the set of points $$S$$ is an equivalent way of representing $$p(x)$$. We call this the **point representation** of polynomials.

Note that the point representation of a polynomial is **not** unique, unlike the standard form representation, which is unique. For example, the set $$T = \{(-1, 3), (5, 51), (0, 1)\}$$ also represents $$p(x) = 1 + 2x^2$$. 

We can easily convert between standard form and the point representation - given some degree $$n$$ polynomial, we can plug in $$n+1$$ points into it and record the $$n+1$$ pairs $$(x_i, y_i)$$ and call this our point representation. The question you may be asking, though, is how can we do the opposite – how can we find the standard form of a polynomial given the point representation, without repeated guessing and checking? How can we find that $$p(x) = 1 + 2x^2$$ is the polynomial defined by $$S$$ (or $$T$$)? This process is called **interpolation**, and we will cover it now.

---

## Interpolation

The problem we're trying to solve is, **given a set of $$n+1$$ points, $$(x_1, y_1), (x_2, y_2), ..., (x_{n+1}, y_{n+1})$$, what is the equation of the degree $$n$$ polynomial that passes through all $$n+1$$ points?**

Note that it is possible that a set of $$n + 1$$ points uniquely determine a polynomial that has a degree **less than $$n$$**. For example, $$(1, 2)$$, $$(2, 4)$$, and $$(3, 6)$$ all lie on the polynomial $$p(x) = 2x$$ – here, we were given 3 points, but we didn't need to find a degree 2 polynomial in order to find a polynomial that passed through them all, since a degree 1 polynomial passed through them all. Fortunately, we won't have to consider this edge case; the polynomial that the process we're about to learn about works in general, **as long as there are no duplicate $$x_i$$ values in your dataset**.

You've seen the degree 1 case of interpolation before – and in fact, Question 4.2 of Homework 8 requires you to use it. Given two points $$(x_1, y_1)$$ and $$(x_2, y_2)$$, there are techniques from high school algebra that help us find the intercept and slope of the line that passes through $$(x_1, y_1)$$ and $$(x_2, y_2)$$. We need something more general that would work for cases with more than 2 points, though, and there's no natural extension to this process.

Suppose we're given five points, $$(0, -1), (1, 0), (2, -11), (3, 2)$$ and $$(4, 99)$$. Since we know that we're searching for a degree 4 polynomial, our desired polynomial will be of the form $$p(x) = a + bx + cx^2 + dx^3 + ex^4$$. Substituting each of the five points into $$p(x)$$ would give us a solvable system of 5 equations and 5 unknowns. These equations would be as follows:

<div align=center>

$$\begin{align*} a + b(0) + c(0)^2 + d(0)^3 + e(0)^4 &= -1 \\\ a + b(1) + c(1)^2 + d(1)^3 + e(1)^4 &= 0 \\\ a + b(2) + c(2)^2 + d(2)^3 + e(2)^4 &= -11 \\\ a + b(3) + c(3)^2 + d(3)^3 + e(3)^4 &= 2 \\\ a + b(4) + c(4)^2 + d(4)^3 + e(4)^4 &= 99\end{align*}$$

</div>

However, solving this system of equations and unknowns would take quite some time. Luckily, there exists a more intuitive way to find $$p(x)$$. Since there is only one such degree 4 polynomial that passes through these five points, both methods should (and do) result in the same $$p(x)$$.

---

## Lagrange Interpolation

Let's start by creating five smaller polynomials, formally called **Lagrange basis polynomials**, that we can then sum to find $$p(x)$$. For each provided point $$(x_i, y_i)$$, $$(x_1, y_1)$$ being the first point we were given, we will define a basis polynomial $$p_{i}(x)$$ with the following properties:

$$p_i(x_i) = 1$$

$$p_i(x_j) = 0,  \forall \: j \neq i$$

(The $$\forall$$ symbol means "for all" – that is, for every value of $$j$$ that is not equal to $$i$$.)

In other words, basis polynomial $$p_i(x)$$ should evaluate to 1 if $$x_i$$ is passed in, and to 0 if any of the other $$x_j$$s are passed in (we will see why this structure is important very soon). Intuitively, $$p_i(x)$$ "turns on" when $$x_i$$ is passed in and returns 1, and "turns off" when some other $$x_j \neq x_i$$ is passed in and returns 0. (When a value other than one of the $$x$$s in the dataset is passed in, $$p_i(x)$$ will return some other, unimportant number.)

We can create such a basis polynomial, for each $$i$$, as follows:

$$
p_{i}(x) = \frac{\Pi_{j \neq i} (x - x_j)}{\Pi_{j \neq i} (x_i - x_j)}
$$

($$\Pi$$ represents product notation, the same way $$\sum$$ represents summation notation.)

<br>

Remember, the five points we were given were $$(0, -1), (1, 0), (2, -11), (3, 2)$$ and $$(4, 99)$$. For clarity, let's calculate $$p_1(x)$$ and $$p_3(x)$$ (corresponding to $$(0, -1)$$ and $$(2, -11)$$, respectively, as these were the first and third points given to us).

<div align=center>
$$
p_1(x) = \frac{\Pi_{j \neq 1}(x - x_j)}{\Pi_{j \neq 1}(0 - x_j)} = \frac{(x-1)(x-2)(x-3)(x-4)}{(0-1)(0-2)(0-3)(0-4)} = \frac{1}{24}(x-1)(x-2)(x-3)(x-4)
$$

$$
p_3(x) = \frac{\Pi_{j \neq 3}(x - x_j)}{\Pi_{j \neq 3}(2 - x_j)} = \frac{(x-0)(x-1)(x-3)(x-4)}{(2-0)(2-1)(2-3)(2-4)} = \frac{1}{4}(x)(x-1)(x-3)(x-4)
$$
</div>

The second-to-last step of the above expansions best illustrate why we've chosen to craft our basis polynomials in this way. If we were to evaluate $$p_1(0)$$, the numerator and denominator would be exactly the same, so $$p_1(0) = 1$$. If we were to instead evaluate $$p_1(1), p_1(2), p_1(3)$$ or $$p_1(4)$$, since $$x-1, x-2, x-3, x-4$$ are all factors of the numerator, the result would be 0. Similarly, $$p_3(x_3) = p_3(2) = 1$$, but $$p_3(x_j)$$ for any other $$x_j$$ – that is, $$p_3(0)$$, $$p_3(1)$$, $$p_3(3)$$, or $$p_3(4)$$ – is 0. 

We're almost done. We can now say that our final polynomial $$p(x)$$ is constructed as follows:

<div align=center>
$$
p(x) = \sum_{i = 1}^{n+1} y_i p_i(x)
$$
</div>

<br>

This is where the $$y$$ values of each of the given points come into play. Looking at our example dataset of $$(0, -1), (1, 0), (2, -11), (3, 2)$$ and $$(4, 99)$$ more closely, we have:

<div align=center>
$$
p(x) = -p_1(x) + 0p_2(x) -11p_3(x) + 2p_4(x) + 99p_5(x)
$$
</div>

<br>

From the way each $$p_i(x)$$ was constructed:

$$\begin{align*} p(0) &= \boxed{(-1) \cdot 1}  + 0 \cdot 0 + (-11) \cdot 0 + 2 \cdot 0 + 99 \cdot 0 = -1 \\\ p(1) &= (-1) \cdot 0  + \boxed{0 \cdot 1} + (-11) \cdot 0 + 2 \cdot 0 + 99 \cdot 0 = 0 \\\ p(2) &= (-1) \cdot 0  + 0 \cdot 0 + \boxed{(-11) \cdot 1} + 2 \cdot 0 + 99 \cdot 0 = -11 \\\ p(3) &= (-1) \cdot 0  + 0 \cdot 0 + (-11) \cdot 0 + \boxed{2 \cdot 1} + 99 \cdot 0 = 2 \\\ p(4) &= (-1) \cdot 0  + 0 \cdot 0 + (-11) \cdot 0 + 2 \cdot 0 + \boxed{99 \cdot 1} = 99 \end{align*}$$

Since $$p(x)$$ passes through all 5 of our points, and theory tells that $$p(x)$$ is unique, we've found the polynomial we're looking for! All that's left is that we need to expand the right-hand side of the equation $$p(x) = -p_1(x) + 0p_2(x) -11p_3(x) + 2p_4(x) + 99p_5(x)$$. Yes, this is slightly annoying to work out by hand, but it finds us $$p(x) = -1 + 13x - 13x^2 + x^4$$.

<div align=center>

<img src="../assets/interpolation/quartic.png" width="400">

</div>

<br>

This entire process is known as **Lagrange Interpolation**. It is named after Lagrange, a famous French mathematician. Lagrange Interpolation is still tedious, though not nearly as tedious as the initial approach from the start of this section. You should practice this process on your own; create your own polynomial of degree $$n \leq 5$$, pick $$n+1$$ points on it, and see if you can correctly reconstruct your polynomial.

It should be noted though, that mastering the arithmetic, while important, isn't the main goal of learning this material. This material is presented so that you can add it to your mathematical toolbox.
