# Introduction

A client set of used car dealerships has requested a model to predict the probable sale price of a car. Their stated purpose for obtaining such a model was to *fine tune their inventory* which we interpret to mean make more efficient transactions per vehicle, ultimately leading to a more profitable enterprise.

To obtain such a model we started with a large, publicly available [data set](./data/vehicles_no_nulls_shuffled_top_100.csv) from Kaggle on used car transactions that stretches back decades. A sample of this data set is here:

|id        |region                 |price|year  |manufacturer|model                |condition|cylinders  |fuel  |odometer|title_status|transmission|VIN              |drive|size     |type  |paint_color|state|
|----------|-----------------------|-----|------|------------|---------------------|---------|-----------|------|--------|------------|------------|-----------------|-----|---------|------|-----------|-----|
|7316155043|fort wayne             |54900|2019.0|ram         |3500 4x4 cummins     |excellent|6 cylinders|diesel|55822.0 |clean       |automatic   |3C7WR9CL5KG517631|4wd  |full-size|pickup|black      |in   |
|7303413468|rochester              |9900 |2017.0|ford        |focus titanium       |excellent|4 cylinders|gas   |26850.0 |salvage     |automatic   |1FADP3J22HL281300|fwd  |compact  |sedan |black      |mn   |
|7314409838|ventura county         |22995|2014.0|ford        |e250 super duty cargo|excellent|8 cylinders|gas   |65695.0 |clean       |automatic   |1FTNE2EWXEDA13774|rwd  |full-size|van   |white      |ca   |
|7316155043|fort wayne             |54900|2019.0|ram         |3500 4x4 cummins     |excellent|6 cylinders|diesel|55822.0 |clean       |automatic   |3C7WR9CL5KG517631|4wd  |full-size|pickup|black      |in   |
|7303413468|rochester              |9900 |2017.0|ford        |focus titanium       |excellent|4 cylinders|gas   |26850.0 |salvage     |automatic   |1FADP3J22HL281300|fwd  |compact  |sedan |black      |mn   |
|7314409838|ventura county         |22995|2014.0|ford        |e250 super duty cargo|excellent|8 cylinders|gas   |65695.0 |clean       |automatic   |1FTNE2EWXEDA13774|rwd  |full-size|van   |white      |ca   |
|7315439972|denver                 |4995 |2008.0|pontiac     |torrent              |good     |6 cylinders|gas   |221618.0|clean       |automatic   |2CKDL43F886056750|4wd  |mid-size |SUV   |yellow     |co   |
|7315295791|reno / tahoe           |5950 |2008.0|pontiac     |g6                   |excellent|6 cylinders|gas   |127600.0|clean       |automatic   |1G2ZG57N884113477|fwd  |compact  |sedan |silver     |ca   |
|7315499219|brownsville            |12350|2007.0|gmc         |sierra sle 1500      |like new |8 cylinders|gas   |167000.0|clean       |automatic   |1GCECT24LKJH73951|rwd  |full-size|pickup|white      |tx   |

Each record in this data set includes a vehicle's make, model, year, mileage, quality, and sale price. From this data set, we built several models and assessed their quality relative to a derived requirement.

# Approach
The overall process was done according to the CRISP-DM framework, which we believe afforded two critical benefits. For us, the practicioner, the framework provided a guided development process, which steps and checklists along the way, while being general enough that we could adapt as needed. For the client, the use of the framework meant we could describe up front how we planned to do the work, and then communicate our work along the way according to this structure. Given how complicated data mining can get, it should also comfort the client to know we are following a *process*.

# Results and Key Findings
To help guide the modeling process, we derived a requirement for the model to predict within **$3,000**, on average, of the correct sale price. The modeling thus far did not meet this requirement. The best performance seen thus far has been **$3,150**, so although we failed to meet the requirement, we got pretty close. The client can use this requirement to build in sufficient margin per transaction such that they obtain profitable sales.

# Next Steps and Recommendations
