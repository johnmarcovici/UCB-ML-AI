# Coupon Acceptance Analysis
This module analyzes data provided by the *UCI Machine Learning* repository to understand who accepts coupons offered for various eating & drinking establishments. The data set includes coupon offerings for coffee houses, bars, and restaurants but I primarily focused on coffee houses.

## What to Run
Run the Jupyter notebook called [coupon_acceptance_analysis.ipynb](./coupon_acceptance_analysis.ipynb).

## Summary of Findings
### Who Accepted Coupons to Coffee Houses?
#### Single-Variable Analyses
I looked at acceptance rates vs several single variables at a time.

##### By Occupation
Those with occupations of healthcare worker and buildings & maintenance accepted coffee coupons at a rate of 76%.

##### By Number of Visits to Coffee Houses in the Last Month
People who visited 2 or more times on average accepted more than 60% of coupons, whereas people who reported 0 visits in the last month accepted only 34% of the time.

##### By Average Annual Income
There is no clear relationshp to income - acceptance rates over 50% were seen at the income extrema as well as the center of the income scale.

#### Multi-Variable Analyses
I also performed a limited set of multi-variable analyses.

##### By Occupation and Number of Visits to Coffee Houses in the Last Month
- Healthcare workers who visited a coffee house 2 times in the last month accepted 90% of coupons
- Those who visited 6 times accepted 100% of coupons
- And those who visited 2 or 6 times accepted 92% of coupons  

##### By Education, Number of Visits to Coffee Houses in the Last Month, and Marital Status
Single people who had attended college (with or without obtaining a degree) and visited coffee houses twice in the last month accepted about 66% of coupons.

##### Caveat
As the specificity of these experiements increases, the sample size per experiment drops. Some of the rates above were calculated over just 10 or 20 samples.

### Who Didn't Accept Coupons to Coffee Houses?
Considering a Driver's Destination, Gender, Passengers in the Car, and if the Coupon is Redeemable En Route

#### Without Regard to Age
Female drivers with no passengers in the car that were heading home or to work and could not redeem the coupon en route accepted about 29% of the offered coupons

#### Considering Drivers at Least 45 Years of Age
Males or females aged 45 and up driving to work with no passengers that could not redeem the coupon en route accepted only about 19% of the offered coupons

## Future Work
The multi-variable analysis performed thus far considers only single events per variable such as *marital status is widowed* and *education is some college*.

But a complete picture would also include multiple events per variable, such as *marital status is widowed* or *marital status is divorced*, and *education is some college* or *education is bachelor's degree*. A benefit in including such experiments is that there will be more experiements with larger sample sizes (e.g. because there are more people that are either widowed or divorced than just widowed).

However, the possible number of such experiments is quite large, so a computationally efficient approach would be essential.
