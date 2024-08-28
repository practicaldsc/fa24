---
layout: default
title: "📚 Resources"
nav_order: 5
description: Supplementary resources around the internet – some made for this class, some not.
---

# {{ page.title }}
{:.no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Past Exams

While this class specifically hasn't been offered yet, it is inspired by a few different courses that have been offered many times, many of which have banks of old exams available online. In particular, refer to:
- [practice.dsc80.com](https://practice.dsc80.com) – most similar to our course.
- [practice.dsc40a.com](https://practice.dsc40a.com) – more theoretical than our course, but some problems will be relevant.
- [practice.dsc10.com](https://practice.dsc10.com) – more introductory-level than our course, but some DataFrame-related problems will be relevant.

We're working on putting together a similar site for our course, which will be used in discussion section. Stay tuned!

---

## Readings

### Textbooks

- [Principles and Techniques of Data Science](https://www.textbook.ds100.org/), the textbook for Berkeley's [Data 100](https://ds100.org) course.
- [DSC 80 Course Notes](https://notes.dsc80.com). These notes were originally written for UCSD's version of this course, but have not been updated in a few years.
- [Python for Data Analysis](https://wesmckinney.com/book/), an online textbook by Wes Mickinney, the original developer of `pandas`. 
- [DSC 10 Course Notes](https://notes.dsc10.com). These notes were written for UCSD's more introductory data science course, which introduces Python and Jupyter Notebooks. You'll find a lot of the material here useful, too.

<!-- ### Lecture-Specific Readings

- [Fast Permutation Tests](resources/lectures/lec07/lec07-fast-permutation-tests.html).
- [More Missingness Examples](resources/lectures/lec12/lec12-more-examples.html). -->

### Articles

- [Views and Copies in `pandas`](https://www.practicaldatascience.org/html/views_and_copies_in_pandas.html) – a great read if you'd like to learn more about the infamous `SettingWithCopyWarning`.
<!-- - [jwilber.me/permutationtest](https://www.jwilber.me/permutationtest/), a great visual explanation of permutation testing. -->
- [A Visual Introduction to Machine Learning](http://www.r2d3.us/visual-intro-to-machine-learning-part-1/) and [Model Tuning and the Bias-Variance Tradeoff](http://www.r2d3.us/visual-intro-to-machine-learning-part-2/), excellent visual descriptions of the last few weeks of the course (some terminology is different, but the ideas are the same).
- [MLU Explain](https://mlu-explain.github.io/), a collection of interactive articles (prepared by [Jared Wilber](https://www.jwilber.me/)) that explain core machine learning ideas, like cross-validation, random forests, and precision and recall.

### Other Links
- [pythontutor.com](https://pythontutor.com), a tool to visualize the execution of Python programs.
- [pandastutor.com](https://pandastutor.com), the equivalent of [pythontutor.com](https://pythontutor.com) for DataFrame manipulation.

---

## Regular Expressions

- [regex101.com](https://regex101.com), a helpful site to have open while writing regular expressions.
- Python [`re` library documentation](https://docs.python.org/3/library/re.html) and [how-to](https://docs.python.org/3/howto/regex.html).
- [regex "cheat sheet"](https://dsc80.com/resources/other/berkeley-regex-reference.pdf) (taken from [here](https://ds100.org/sp22/resources/)).


---

## Finding Datasets

### Generic sources of data

These sites allow you to search for datasets (in CSV format) from a variety of different domains. Some may require you to sign up for an account; these are generally reputable sources.

- [Kaggle Datasets](https://www.kaggle.com/datasets).
- [Google’s dataset search](http://toolbox.google.com/datasetsearch).
- [FiveThirtyEight](https://data.fivethirtyeight.com/).
- [DataHub.io](https://datahub.io/collections).
- [Data.world.](https://data.world/)
- [CORGIS](https://corgis-edu.github.io/corgis/csv/).
- [R datasets](https://vincentarelbundock.github.io/Rdatasets/articles/data.html).
- Wikipedia. (use [this site](https://wikitable2csv.ggor.de/) to extract and download tables as CSVs)
- [Awesome Public Datasets GitHub repo](https://github.com/awesomedata/awesome-public-datasets).
- [Links to even more sources](https://rockcontent.com/blog/data-sources/)

### Domain-specific sources of data

- Sports: [Basketball Reference](https://www.basketball-reference.com/), [Baseball Reference](https://www.baseball-reference.com/), etc.
- US Government Sources: [census.gov](https://www.census.gov/data/tables.html), [data.gov](https://www.data.gov/), [data.ca.gov](https://data.ca.gov/), [data.sfgov.org](https://data.sfgov.org/browse?), [FBI’s Crime Data Explorer](https://crime-data-explorer.fr.cloud.gov/), [Centers for Disease Control and Prevention](https://data.cdc.gov/browse?category=NCHS).
- Global Development: [data.worldbank.org](https://data.worldbank.org/), [databank.worldbank.org](https://databank.worldbank.org/home.aspx), [WHO](https://apps.who.int/gho/data/node.home).
- Transportation: [New York Taxi trips](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page), [Bureau of Transportation Statistics](https://www.transtats.bts.gov/DataIndex.asp), [SFO Air Traffic Statistics](https://www.flysfo.com/media/facts-statistics/air-traffic-statistics).
- Music: [Spotify Charts](https://spotifycharts.com/regional).
- COVID: [Johns Hopkins](https://github.com/CSSEGISandData/COVID-19).
- Any Google Forms survey you’ve administered! (Go to the results spreadsheet, then go to “File > Download > Comma-separated values”.)

Tip: if a site only allows you to download a file as an Excel file, not a CSV file, you can download it, open it in a spreadsheet viewer (Excel, Numbers, Google Sheets), and export it to a CSV.

---