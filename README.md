# General Guide for Olympic Trials prediction Scoring

For every olympic event please rank AT LEAST 6 swimmers from the psych sheet.  You may submit additional swimmers as alternates but these alternates only count IF ONE OF YOUR SWIMMERS SCRATCHES; does not count if they simply do not make the finals.  Alternated will be put in the back of your queue in the order that you submit them as alternates.
Please put all submissions here https://docs.google.com/spreadsheets/d/1dKke7kpVU5nQbJni7n31QwsKsMeiihX1RtTIsTNIlt8/edit?usp=sharing 

In addition to rankings, please submit a guess for the winning time (At finals) for the event.  Bonus points will go to the winner.
A perfect scores yields 100 points, while being the closest to the winning time yields 15 points, so the maximum number of points available for each event is 115.

The exact scoring procedure has been carefully devised, reviewed, and tested so to properly reward the best predictor and the code is in this repo under scoring.py 

i will write a briefly TLDR though to simplify and provide clarity and avoid dispute.

## Most Events (not 100 Free and 200 Free)

1. You lose points based on the distance from your predicted swimmers rank and their actual rank.  The amount of points loss is proportional to the SQUARE of the distance (i.e. a few swimmers really off is worse than many swimmer slightly off).  There are careful caps in place that prevent this from spiraling wildly.
2. The above penalty is slightly weighted towards the importance of the actual rank.  For example, if you top pick is way off you are penalized more than if your 6th pick is way off.
3. There are bonuses for correctly predicting olympic qualifiers (basically giving additional weight to the top 2 swimmers you predict)
4. There are bonuses for getting a swimmers exact place correct (mainly just to serve as a linear shift on the quadratic penalty to that people who have a bunch of "off by 1s" still miss out on something).
5. There is an extra penalty for every swimmer you pick that doesn't at least final

## 100 Free and 200 Free

To spice things up, these events are similar (still max 115 points), but scored a little differently in honor of the habitual 6 relay spots given out.  The scoring follows the same general rules, but parameters are tweaked as follows.

1. The "distance" penalty is less severe (exponent = 1.5 instead of 2).
2. The weighting on this penalty towards the important ranks is also less severe.
3. The bonus for correctly prediction the individual olympic qualifiers is still there but smaller
4. The not finaling bonus is now the "not getting in the top 6" bonus.  So basically within the top you get penalized less but outside the top 6 you get penalized more.  This penalty is a lot bigger than the previous "not finaling" penalty.







