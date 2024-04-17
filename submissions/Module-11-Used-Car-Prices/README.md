# Used Car Prices
This module analyzes used-car pricing data obtained from Craigslist vehicle sales. The original data set, which I think is [this one from Kaggle](https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data), was reduced for the students and provided as a csv file. A sample of this data set is here:

|id        |region                 |price|year  |manufacturer|model                |condition|cylinders  |fuel  |odometer|title_status|transmission|VIN              |drive|size     |type  |paint_color|state|
|----------|-----------------------|-----|------|------------|---------------------|---------|-----------|------|--------|------------|------------|-----------------|-----|---------|------|-----------|-----|
|7316155043|fort wayne             |54900|2019.0|ram         |3500 4x4 cummins     |excellent|6 cylinders|diesel|55822.0 |clean       |automatic   |3C7WR9CL5KG517631|4wd  |full-size|pickup|black      |in   |
|7303413468|rochester              |9900 |2017.0|ford        |focus titanium       |excellent|4 cylinders|gas   |26850.0 |salvage     |automatic   |1FADP3J22HL281300|fwd  |compact  |sedan |black      |mn   |
|7315499219|brownsville            |12350|2007.0|gmc         |sierra sle 1500      |like new |8 cylinders|gas   |167000.0|clean       |automatic   |1GCECT24LKJH73951|rwd  |full-size|pickup|white      |tx   |

The prompt was a hypothetical scenario where a used-car dealership wants to fine-tune their inventory, and to do so wants a model to predict a vehicle's eventual sales price. The prompt also required that the modeling be done according to the CRISP-DM framework, a standardized process for data mining.

The modeling and analysis is done in [this notebook](./used_car_prices.ipynb) and follows the framework through the high-level steps, ending with a short report for the clients.
