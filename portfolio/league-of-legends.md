---
layout: page
title: League of Legends ⌨️
description: Description of the League of Legends dataset option for the Portfolio Homework.
nav_exclude: true
---

<small> <a href="../#choosing-a-dataset">go back to the Portfolio Homework spec</a> </small>

# League of Legends ⌨️
{:.no_toc}

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

Welcome to Summoner's Rift! This dataset contains information of players and teams from over 10,000 League of Legends competitive matches.

{: .note }
You'll probably want to be at least a little bit familiar with [*League of Legends*](https://en.wikipedia.org/wiki/League_of_Legends) and its terminology to use this dataset. If not, one of the other datasets may be more interesting to you.

---

## Getting the Data

The data can be found on the website [Oracle's Elixir](https://oracleselixir.com/tools/downloads) at the provided Google Drive link.

We've verified that it's possible to satisfy the requirements of the homework using match data from 2022. You're welcome to use newer or older datasets if you wish, but keep in mind that League of Legends changes significantly between years; this can make it difficult to combine or make comparisons between datasets from different years.

---

## Example Questions and Prediction Problems

Feel free to base your exploration into the dataset in Steps 1-2 around one of these questions, or come up with a question of your own.

- Looking at [tier-one professional leagues](https://en.wikipedia.org/wiki/List_of_League_of_Legends_leagues_and_tournaments), which league has the most "action-packed" games? Is the amount of "action" in this league significantly different than in other leagues? Note that you'll have to come up with a way of quantifying "action".
- Which competitive region has the highest win rate against teams outside their region? Note you will have to find and merge region data for this question as the dataset does not have it.
- Which role "carries" (does the best) in their team more often: ADCs (Bot lanes) or Mid laners?
- Is Talon (a former TA's favorite champion) more likely to win or lose any given match?

Feel free to use one of the prompts below to build your predictive model in Steps 3-5, or come up with a prediction task of your own.

* Predict if a team will win or lose a game.
* Predict which role (top-lane, jungle, support, etc.) a player played given their post-game data.
* Predict how long a game will take before it happens.
* Predict which team will get the first Baron.

Make sure to justify what information you would know at the "time of prediction" and to only train your model using those features.
---

## Special Considerations

### Step 2: Data Cleaning and Exploratory Data Analysis

- Each `'gameid'` corresponds to up to 12 rows – one for each of the 5 players on both teams and 2 containing summary data for the two teams (try to find out what distinguishes those rows). After selecting your line of inquiry, make sure to remove either the player rows or the team rows so as not to have issues later in your analysis.
- Many columns should be of type `bool` but are not.