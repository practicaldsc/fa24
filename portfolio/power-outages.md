---
layout: page
title: Power Outages 🔋
description: Description of the power outages dataset option for the Portfolio Homework.
nav_exclude: true
---

<small> <a href="../#choosing-a-dataset">go back to the Portfolio Homework spec</a> </small>

# Power Outages 🔋
{:.no_toc}

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

This dataset has major power outage data in the continental U.S. from January 2000 to July 2016.

---

## Getting the Data

The data is downloadable [here](https://engineering.purdue.edu/LASCI/research-data/outages/outagerisks).

***Note***: If you are having a hard time with the "This dataset" link, hold shift and click the link to open it into a new tab and then refresh that new tab.

A data dictionary is available at this [article](https://www.sciencedirect.com/science/article/pii/S2352340918307182) under *Table 1. Variable descriptions*.

---

## Example Questions and Prediction Problems

Feel free to base your exploration into the dataset in Steps 1-2 around one of these questions, or come up with a question of your own.

- Where and when do major power outages tend to occur?
- What are the characteristics of major power outages with higher severity? Variables to consider include location, time, climate, land-use characteristics, electricity consumption patterns, economic characteristics, etc. What risk factors may an energy company want to look into when predicting the location and severity of its next major power outage?
- What characteristics are associated with each category of cause?
- How have characteristics of major power outages changed over time? Is there a clear trend?

Feel free to use one of the prompts below to build your predictive model in Steps 3-5, or come up with a prediction task of your own.

* Predict the severity (in terms of number of customers, duration, or demand loss) of a major power outage.
* Predict the cause of a major power outage.
* Predict the number and/or severity of major power outages in the year 2022.
* Predict the electricity consumption of an area.

Make sure to justify what information you would know at the "time of prediction" and to only train your model using those features.

---

## Special Considerations

### Step 2: Data Cleaning and Exploratory Data Analysis
- The data is given as an Excel file rather than a CSV. Open the data in Google Sheets or another spreadsheet application and determine which rows and columns of the sheet should be ignored when loading the data in `pandas`.
    - Note that `pandas` can load multiple filetypes: `pd.read_csv`, `pd.read_excel`, `pd.read_html`, `pd.read_json`, etc.
- The power outage start date and time is given by `'OUTAGE.START.DATE'` and `'OUTAGE.START.TIME'`. It would be preferable if these two columns were combined into one `pd.Timestamp` column. Combine `'OUTAGE.START.DATE'` and `'OUTAGE.START.TIME'` into a new `pd.Timestamp` column called `'OUTAGE.START'`. Similarly, combine `'OUTAGE.RESTORATION.DATE'` and `'OUTAGE.RESTORATION.TIME'` into a new `pd.Timestamp` column called `'OUTAGE.RESTORATION'`.
    - `pd.to_datetime` and `pd.to_timedelta` will be useful here.
- To visualize geospatial data, consider [Folium](https://python-visualization.github.io/folium/) or another geospatial plotting library. You can even embed Folium maps in your website! If `fig` is a `folium.folium.Map` object, then `fig._repr_html_()` evaluates to a string containing your plot as HTML; use `open` and `write` to write this string to an `.html` file.