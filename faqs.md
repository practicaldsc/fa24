---
layout: page
title: 🙋 FAQs (new!)
description: Answers to frequently asked questions each week.
nav_order: 7
---

# 🙋FAQs

Moving forward, we're going to **try** and update this page each week to provide answers to questions asked (1) live in lecture, (2) at [practicaldsc.org/q](https://practicaldsc.org/q) during lecture, and (3) on Ed. If you have other related questions, feel free to post them on Ed.

Jump to:

- [DataFrame Manipulation](#dataframe-manipulation)

---

## DataFrame Manipulation

### Why do we pass in just `iqr` to `agg`?

#### Question 
In lecture, we defined `iqr` as a function that takes in a series, why here we don't pass any argument explicitly as `agg(iqr(s))`, where `s` is the Series we get by `groupby('species')[body_mass_g]`?

```py
def iqr(s): 
    # s is a series
    # return the interquartile range for s
    return np.percentile(s, 75) - np.percentile(s, 25)

# Here, the argument to agg a function which
# takes in a Series and returns a scalar.
(
    penguins
    .groupby('species')
    ['body_mass_g']
    .agg(iqr)
)
```


#### Answer:
There's a subtle difference between `.agg(iqr)` and `.agg(iqr(s))`. If you actually tried `.agg(iqr(s))`, you'd get an error saying `s` is not defined, since that will try and evaluate `iqr(s)` before talking to `.agg`, and in the global scope of your notebook, there (most likely) aren't any variables named `s`. (There is an `s`, but it's the input to `iqr`.)

But also, `.agg`  takes as input a function. `iqr` is a function, hence why we call `.agg(iqr)`. Even if `s` was a Series defined in your notebook and `iqr(s)` worked and returned the difference between the 75th percentile and 25th percentile of this globally-defined `s`, then `.agg(iqr(s))` would end up being something like `.agg(17.39)`. Then, the input to `.agg` isn't a function, as we need it to be, but rather it's a number.

