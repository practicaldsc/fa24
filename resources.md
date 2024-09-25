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

While this class specifically hasn't been offered yet, it is inspired by a few different courses that have been offered many times, many of which have banks of old exams available online. **The most relevant problems will be posted at our brand-new [🧠 Study Site](https://study.practicaldsc.org/), which you'll use in discussion section.**

If you'd like some additional practice, you can refer to:
- [practice.dsc80.com](https://practice.dsc80.com) – most similar to our course.
- [practice.dsc40a.com](https://practice.dsc40a.com) – more theoretical than our course, but some problems will be relevant.
- [practice.dsc10.com](https://practice.dsc10.com) – more introductory-level than our course, but some DataFrame-related problems will be relevant.

---

## Textbooks

- [Principles and Techniques of Data Science](https://www.textbook.ds100.org/), the textbook for Berkeley's [Data 100](https://ds100.org) course.
    - These are also supplemented by a set of [Course Notes](https://ds100.org/course-notes/).
- [DSC 80 Course Notes](https://notes.dsc80.com). These notes were originally written for UCSD's version of this course, but have not been updated in a few years.
- [Python for Data Analysis](https://wesmckinney.com/book/), an online textbook by Wes Mickinney, the original developer of `pandas`. 
- [DSC 10 Course Notes](https://notes.dsc10.com). These notes were written for UCSD's more introductory data science course, which introduces Python and Jupyter Notebooks. You'll find a lot of the material here useful, too.
- [Stanford's Python Reference](https://cs.stanford.edu/people/nick/py/).
- [EECS 201: Computer Science Pragmatics](https://www.eecs.umich.edu/courses/eecs201/fa2024/schedule). This class covers "the essentials of using a computer effectively for EECS students," and covers Unix-like systems, shells, version control, build systems, debugging, and scripting.

---

## Topic-Specific Resources

There are lots of readings linked on the course website. Here, we're collecting other helpful resources that will help explain ideas in the course. If you found something online that was super helpful, let us know and we'll add it here!

### Python
- [pythontutor.com](https://pythontutor.com), a tool to visualize the execution of Python programs.
- [Facts and myths about Python names and values](https://nedbatchelder.com/text/names.html) – good to read if you're confused about how variables and mutability work in Python.

### `pandas`
- [pandastutor.com](https://pandastutor.com), the equivalent of [pythontutor.com](https://pythontutor.com) for DataFrame manipulation.
- [Views and Copies in `pandas`](https://www.practicaldatascience.org/html/views_and_copies_in_pandas.html) – a great read if you'd like to learn more about the infamous `SettingWithCopyWarning`.

### Visualization
- [UC Berkeley Data 100 Lecture 10 (by Suraj)](https://ds100.org/su20/lecture/lec10).
- [UCSD DSC 106: Data Visualization](https://dsc-courses.github.io/dsc106-wi24).
- [UW CSE 442: Data Visualization](https://courses.cs.washington.edu/courses/cse442/23au/).

### Missing Values

- [Concepts of MCAR, MAR and MNAR](https://stefvanbuuren.name/fimd/sec-MCAR.html).

### Web Scraping

- [STATS 701 notes](https://dept.stat.lsa.umich.edu/~jerrick/courses/stat701/notes/webscrape.html) – these are in R, but are still helpful for giving you a general idea of what you can scrape and how.

### Regular Expressions

- [regex101.com](https://regex101.com), a helpful site to have open while writing regular expressions.
- Python [`re` library documentation](https://docs.python.org/3/library/re.html) and [how-to](https://docs.python.org/3/howto/regex.html).
- [regex "cheat sheet"](https://dsc80.com/resources/other/berkeley-regex-reference.pdf) (taken from [here](https://ds100.org/sp22/resources/)).

### Machine Learning

- [A Visual Introduction to Machine Learning](http://www.r2d3.us/visual-intro-to-machine-learning-part-1/) and [Model Tuning and the Bias-Variance Tradeoff](http://www.r2d3.us/visual-intro-to-machine-learning-part-2/), excellent visual descriptions of the last few weeks of the course (some terminology is different, but the ideas are the same).
- [MLU Explain](https://mlu-explain.github.io/), a collection of interactive articles (prepared by [Jared Wilber](https://www.jwilber.me/)) that explain core machine learning ideas, like cross-validation, random forests, and precision and recall.


---

## Finding Datasets

### Generic Sources of Data

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
- [Awesome JSON Datasets GitHub repo](https://github.com/jdorfman/awesome-json-datasets).
- [Data from Introduction to the Digital Humanities at MSU](https://msuintrodhfall2020.hcommons.org/datasets/).
- [Sage Research Methods Datasets](https://methods.sagepub.com/datasets).
- [Links to even more sources](https://rockcontent.com/blog/data-sources/).

### Domain-Specific Sources of Data

- Sports: [Basketball Reference](https://www.basketball-reference.com/), [Baseball Reference](https://www.baseball-reference.com/), etc.
- US Government Sources: [census.gov](https://www.census.gov/data/tables.html), [data.gov](https://www.data.gov/), [data.ca.gov](https://data.ca.gov/), [data.sfgov.org](https://data.sfgov.org/browse?), [FBI’s Crime Data Explorer](https://crime-data-explorer.fr.cloud.gov/), [Centers for Disease Control and Prevention](https://data.cdc.gov/browse?category=NCHS).
- Environment: [National Centers for Environmental Information](https://www.ncei.noaa.gov/access) (e.g. [Oceanography data from NOAA](https://www.ncei.noaa.gov/products/world-ocean-database#)), [Environmental Data Initiative](https://edirepository.org/).
- Social Sciences: [Inter-university Consortium for Political Science Research](https://www.icpsr.umich.edu/web/pages/ICPSR/index.html), [General Social Survey](https://gss.norc.org/), [data.worldbank.org](https://data.worldbank.org/), [databank.worldbank.org](https://databank.worldbank.org/home.aspx), [WHO](https://apps.who.int/gho/data/node.home).
- Transportation: [New York Taxi trips](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page), [Bureau of Transportation Statistics](https://www.transtats.bts.gov/DataIndex.asp), [SFO Air Traffic Statistics](https://www.flysfo.com/media/facts-statistics/air-traffic-statistics).
- Music: [Spotify Charts](https://spotifycharts.com/regional).
- COVID: [Johns Hopkins](https://github.com/CSSEGISandData/COVID-19).
- Any Google Forms survey you’ve administered! (Go to the results spreadsheet, then go to “File > Download > Comma-separated values”.)

Tip: if a site only allows you to download a file as an Excel file, not a CSV file, you can download it, open it in a spreadsheet viewer (Excel, Numbers, Google Sheets), and export it to a CSV.

### University of Michigan Library Guides

The university library system maintains several guides on how to conduct research and where to find information. They contain lots of links to local data sources. Here are a few guides of interest:

- Guide on [Finding Data](https://guides.lib.umich.edu/c.php?g=282938&p=1885333).
- Guide on [Community Data](https://guides.lib.umich.edu/communityprofile).
- Guide on [Geospatial Data](https://guides.lib.umich.edu/c.php?g=283021&p=1885741).
    - Guide on [Detroit Maps](https://guides.lib.umich.edu/detroitmaps).
- Guide on [Political Science Data](https://guides.lib.umich.edu/polisci).
    - Watch [this video](https://www.mivideo.it.umich.edu/media/t/1_7fy6i5ze) for guidance on how to search for Political Science data.
- Guide on [News Data](https://guides.lib.umich.edu/news).
- General [Engineering](https://guides.lib.umich.edu/engineering) and [Computer Science](https://guides.lib.umich.edu/cse) research guides.

If you have questions about how to use any of these guides, or how to use any of the other resources our library has to offer, contact Sarah Barbrow (sbarbrow@umich.edu), our Engineering librarian (who also recorded [this video](https://www.mivideo.it.umich.edu/media/t/1_7fy6i5ze), of interest to students who are looking to get into social sciences research)!

---