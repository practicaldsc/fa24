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

### Why does `round`ing 0.5 sometimes round down?
#### Question
Sometimes when I try use `Series.round()` or `np.round()` on a number that's exactly x.5, it rounds **down**—why is this?

#### Answer
This is expected behavior by `pandas` and `numpy` ([documentation](https://numpy.org/doc/stable/reference/generated/numpy.round.html#numpy.round:~:text=For%20values%20exactly%20halfway%20between%20rounded%20decimal%20values%2C%20NumPy%20rounds%20to%20the%20nearest%20even%20value.%20Thus%201.5%20and%202.5%20round%20to%202.0%2C%20%2D0.5%20and%200.5%20round%20to%200.0%2C%20etc.)), even though Python's `round()` function does not do this:
> For values exactly halfway between rounded decimal values, NumPy rounds to the _nearest even value_. Thus 1.5 and 2.5 round to 2.0, -0.5 and 0.5 round to 0.0, etc.

<img src="/assets/site-images/pandas-rounding.png" alt="Illustration of Pandas series rounding" style="display: block; margin-left: auto; margin-right: auto;"/>

One reason to do this is to avoid biasing a dataset's average upwards by always rounding up at 0.5. From a great [StackOverflow answer](https://stackoverflow.com/a/68788317):
> This kind of rounding is called rounding to even (or banker’s rounding). It is the case because if we always round 0.5 up to the next largest number, then the average of a large data set rounded numbers is likely to be slightly larger than the average of the unrounded numbers: this bias or drift can have very bad effects on some numerical algorithms and make them inaccurate.



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

