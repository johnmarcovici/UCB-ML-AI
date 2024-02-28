# Coupon Acceptance Analysis
This module analyzes data provided by the *UCI Machine Learning* repository to understand who accepts coupons offered to them for a set of eating & drinking establishments. The data set covers establishment types of coffee houses, bars, and restaurants but I primarily focused on coffee houses.

## How to Run
The notebook to run is ./coupon_acceptance_analysis.ipynb

## Summary of Findings
### Who Accepted Coupons to Coffee Houses?
#### Single-Variable Analyses
I looked at acceptance rates as a function of several single variables at a time.

##### By Occupation
The analysis showed that healthcare workers and those in buildings & maintenance accepted coffee coupons at a rate of 76%.

##### By Number of Visits to Coffee Houses in the Last Month
People who visited 2 or more times on average accepted more than 60% of coupons, whereas people who reported 0 visits in the last month accepted only 34% of the time.

##### By Average Annual Income
Inconclusive - acceptance rates over 50% were seen at both extrema as well as the center of the income scale.

#### Multi-Variable Analyses
I also performed a limited set of multi-variable analyses.

##### By Occupation and Number of Visits to Coffee Houses in the Last Month
I found that healthcare workers who visited a coffee house 2 times in the last months accepted 90% of coupons, and those who visited 2 or 6 times accepted 92% of coupons.  

##### By Education, Number of Visits to Coffee Houses in the Last Month, and Marital Status
Another multi-variable experiment I considered was education, monthly coffee house visits, and marital status, and found that single people who had attended college (with or without obtaining a degree) and visited coffee houses twice in the last month accepted about 66% of coupons.

##### Caveats
As the specificity of these experiements increases grows, the sample size per experiment drops. Some of the rates above were calculated over just 10 or 20 samples.

### Who Didn't Accept Coupons to Coffee Houses?
When people were headed home, and could not redeem the coupon on the way (to home), the acceptance rate was low at about 30% or less, for any relationship status. This suggests that when people are heading home, they are really don't want to turn around to use a coupon

## Future Work
The multi-variable analysis performed thus far considers only single events per variable such as *marital status is widowed* and *education is some college*.

But a complete picture would also include multiple events per variable, such as *marital status is widowed* or *marital status is divorced*, and *education is some college* or *education is bachelor's degree*. A benefit in including such experiments is that there will be more experiements with larger sample sizes (e.g. they are more people that are either widowed or divorced than just widowed).

The number of such experiments however (permutations) rapdily grows with the number of variables included as well as the number of events per variable, so a computationally efficient approach would be essential.
