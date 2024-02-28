# Module 5 Practical Assignment on Coupon Acceptance Analysis
This module analyzes data provided in the data/coupons.csv file for trends in terms of who accepts and who does not accept coupons to a series of establishments. The data set addresses many establishment types (coffee houses, bars, restaurants) but I primarily focused on coffee houses.

## Setup
### Create a virtual environment  
```console
python -m venv venv && source ./venv/bin/activate
```

### Install requirements  
```console
pip3 install -r requirements.txt
```
## Run
The notebook to run is ./practical_application_assignment_5.1.ipynb

## Summary of Findings
### Who Accepted Coupons to Coffee Houses?
The analysis showed that healthcare workers and those in buildings & maintenance accepted coupons at a rate of 76%.

It also showed that retirees accepted relatively infrequently, at about 40%.

Other single-variable analyses were performed. For example, when looking at acceptance rate vs. the average number of visits to a coffee house, we found that people who visited 2 or more times on average accepted more than 60% of coupons, whereas people who reported 0 visits in the last month accepted only 34% of the time.

Looking at acceptance rate vs. average annual income revealed no consistent trend - acceptance rates over 50% were seen at both extrema as well as the center of the income scale.



