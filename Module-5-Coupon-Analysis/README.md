# Coupon Acceptance Analysis
This module analyzes data provided in the data/coupons.csv file for trends in terms of who accepts and who does not accept coupons to a series of establishments. The data set addresses many establishment types (coffee houses, bars, restaurants) but I primarily focused on coffee houses.

## How to Run
The notebook to run is ./coupon_acceptance_analysis.ipynb

## Summary of Findings
### Who Accepted Coupons to Coffee Houses?
The analysis showed that healthcare workers and those in buildings & maintenance accepted coupons at a rate of 76%.

It also showed that retirees accepted relatively infrequently, at about 40%.

Other single-variable analyses were performed. For example, when looking at acceptance rate vs. the average number of visits to a coffee house, we found that people who visited 2 or more times on average accepted more than 60% of coupons, whereas people who reported 0 visits in the last month accepted only 34% of the time.

Looking at acceptance rate vs. average annual income revealed no consistent trend - acceptance rates over 50% were seen at both extrema as well as the center of the income scale.

I also performed a limited set of multi-variable analyses, such as combining both occupation and number of monthly visits to coffee houses. I found that healthcare workers who visited a coffee house 2 times in the last months accepted 90% of coupons, and those who visit 2 or 6 times accepted 92% of coupons. However, as the specificity of these experiments grows, the number of results over which this rate is computed necessarily drops. In this latter example just 36 records were considered, of which 92% accepted the coupon.

Another multi-variable experiment I considered was education, monthly coffee house visits, and marital status, and found that single people who had attended college (with or without obtaining a degree) and visited coffee houses twice in the last month accepted about 66% of coupons.

### Who Didn't Accepted Coupons to Coffee Houses?
When people were headed home, and could not redeem the coupon on the way (to home), the acceptance rate was low at about 30% or less, for any relationship status. This suggests that when people are heading home, they are really don't want to turn around to use a coupon

Surprisingly, 42% of people under 21 accepted coupons to bars. Maybe the bars sell food too.

## Future Work
The limited multi-variable analysis revealed the need for multi-outcome, multi-variable analysis. For example, instead of analyzing just "occupation is healthcare worker" and "visited a coffee house twice last month" we need to look at more complex outcomes, such as "occupation is healthcare worker or student or unemployed" and "visited a coffee house at least twice in the last month" and "age is between 20-40". To do so requires an update to the existing approach wherein multiple outcomes per categorical variable are considered.





