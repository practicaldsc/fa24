---
layout: page
title: Recipes and Ratings 🍽️
description: Description of the recipes and ratings dataset option for the Portfolio Homework.
nav_exclude: true
---

<small> <a href="../#choosing-a-dataset">go back to the Portfolio Homework spec</a> </small>

# Recipes and Ratings 🍽️
{:.no_toc}

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

This dataset contains recipes and ratings from [food.com](https://food.com). It was originally scraped and used by the authors of [this](https://cseweb.ucsd.edu/~jmcauley/pdfs/emnlp19c.pdf) recommender systems paper.

---

## Getting the Data

Download the data [here](https://drive.google.com/file/d/1kIbMz6jlhleiZ9_3QthmUnifoSds_2EI/view?usp=sharing). You'll download two CSV files:
- `RAW_recipes.csv` contains recipes.
- `RAW_interactions.csv` contains reviews and ratings submitted for the recipes in `RAW_recipes.csv`.

We've provided you with a subset of the raw data used in the original report, containing only the recipes and reviews posted since 2008, since the original data is quite large.

A description of each column in both datasets is given below.

#### Recipes

For context, you may want to look at an example recipe [directly on food.com](https://www.food.com/recipe/chickpea-and-fresh-tomato-toss-51631).

| Column         | Description                                                                                                                                       |
|:---------------|:--------------------------------------------------------------------------------------------------------------------------------------------------|
| `'name'`        | Recipe name                                                                                                                                       |
| `'id'`             | Recipe ID                                                                                                                                         |
| `'minutes'`        | Minutes to prepare recipe                                                                                                                         |
| `'contributor_id'` | User ID who submitted this recipe                                                                                                                 |
| `'submitted'`      | Date recipe was submitted                                                                                                                         |
| `'tags'`          | Food.com tags for recipe                                                                                                                          |
| `'nutrition'`      | Nutrition information in the form [calories (#), total fat (PDV), sugar (PDV), sodium (PDV), protein (PDV), saturated fat (PDV), carbohydrates (PDV)]; PDV stands for "percentage of daily value" |
| `'n_steps'`        | Number of steps in recipe                                                                                                                         |
| `'steps'`          | Text for recipe steps, in order                                                                                                                   |
| `'description'`    | User-provided description                                                                                                                         |

#### Ratings

| Column    | Description         |
|:----------|:--------------------|
| `'user_id'`   | User ID             |
| `'recipe_id'` | Recipe ID           |
| `'date'`      | Date of interaction |
| `'rating'`    | Rating given        |
| `'review'`    | Review text         |

After downloading the datasets, you **must** follow the following steps to merge the two datasets and create a column containing the average rating per recipe:
1. Left merge the recipes and interactions datasets together.
2. In the merged dataset, fill all ratings of 0 with `np.nan`. (Think about _why_ this is a reasonable step, and include your justification in your website.)
3. Find the average rating per recipe, as a Series.
4. Add this Series containing the average rating per recipe back to the recipes dataset however you'd like (e.g., by merging). **Use the resulting dataset for all of your analysis.**

---

## Example Questions and Prediction Problems

Feel free to base your exploration into the dataset in Steps 1-2 around one of these questions, or come up with a question of your own.

- What types of recipes tend to have the most calories?
- What types of recipes tend to have higher average ratings?
- What types of recipes tend to be healthier (i.e. more protein, fewer carbs)?
- What is the relationship between the cooking time and average rating of recipes?

Feel free to use one of the prompts below to build your predictive model in Steps 3-5, or come up with a prediction task of your own.

- Predict ratings of recipes.
- Predict the number of minutes to prepare recipes.
- Predict the number of steps in recipes.
- Predict calories of recipes.

Make sure to justify what information you would know at the "time of prediction" and to only train your model using those features.

---

## Special Considerations

### Step 2: Data Cleaning and Exploratory Data Analysis

Some columns, like `'nutrition'`, contain values that look like lists, but are actually strings that look like lists. You may want to turn the strings into actual lists, or create columns for every unique value in those lists. For instance, per the data dictionary, each value in the `'nutrition'` column contains information in the form `"[calories (#), total fat (PDV), sugar (PDV), sodium (PDV), protein (PDV), saturated fat (PDV), and carbohydrates (PDV)]"`; you could create individual columns in your dataset titled `'calories'`, `'total fat'`, etc.