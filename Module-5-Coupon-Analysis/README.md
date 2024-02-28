# Coupon Acceptance Analysis
This module analyzes data provided in the data/coupons.csv file for trends in terms of who accepts and who does not accept coupons to a series of establishments. The data set addresses many establishment types (coffee houses, bars, restaurants) but I primarily focused on coffee houses.

## How to Run
The notebook to run is ./coupon_acceptance_analysis.ipynb

## Summary of Findings
### Who Accepted Coupons to Coffee Houses?
The analysis showed that healthcare workers and those in buildings & maintenance accepted coffee coupons at a rate of 76%.

Other single-variable analyses were performed, such as
- vs. the average number of visits to a coffee house
- - People who visited 2 or more times on average accepted more than 60% of coupons
- - Whereas people who reported 0 visits in the last month accepted only 34% of the time
- vs. average annual income
- - Revealed no consistent trend - acceptance rates over 50% were seen at both extrema as well as the center of the income scale

I also performed a limited set of multi-variable analyses, such as combining both occupation and number of monthly visits to coffee houses. I found that healthcare workers who visited a coffee house 2 times in the last months accepted 90% of coupons, and those who visit 2 or 6 times accepted 92% of coupons. However, as the specificity of these experiments grows, the number of results over which this rate is computed necessarily drops. In this latter example just 36 records were considered, of which 92% accepted the coupon.

Another multi-variable experiment I considered was education, monthly coffee house visits, and marital status, and found that single people who had attended college (with or without obtaining a degree) and visited coffee houses twice in the last month accepted about 66% of coupons.

### Who Didn't Accept Coupons to Coffee Houses?
When people were headed home, and could not redeem the coupon on the way (to home), the acceptance rate was low at about 30% or less, for any relationship status. This suggests that when people are heading home, they are really don't want to turn around to use a coupon

## Future Work
The multi-variable analysis performed thus far considers only single events per variable such as *marital status is widowed* and *education is some college*.

But a complete picture would also include multiple events per variable, such as *marital status is widowed* or *marital status is divorced*, and *education is some college* or *education is bachelor's degree*. A benefit in including such experiments is that there will be more experiements with larger sample sizes (e.g. they are more people that are either widowed or divorced than just widowed).

The number of such experiments however (permutations) is large and so a computationally efficient approach would be essential.
