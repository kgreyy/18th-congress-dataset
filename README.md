# The Congress Predicting Wizard
This project is developed by: 
- James Matthew G. Borines (Section: THW)
- Michael Benjamin C. Morco (Section: THX)
- Kyle Gabriel M. Reynoso (Section: THX)

# Goal
The project aims to predict whether the filed congressional bills pass depending on their titles, author affiliations (numbers belonging in political parties/partylists, regions of origin/representation, committee of referral and scope).

## Data Gathering
Congressional bills data was gathered from the [18th Philippine Congress Endpoint for House Bills](https://www.congress.gov.ph/legisdocs/?v=bills) using the notebook located in `18th-congress-bills/hor-extractor.ipynb`.
The list of members of House of Representatives was scraped from the [COMELEC List of Elected Representatives](https://comelec.gov.ph/php-tpls-attachments/2019NLE/ElectionResults/2019NLE_LIst_of_Elected_House_of_Rep_Candidates.pdf) using the scripts in the `congress-members-rip` folder.

To associate the list of representatives with the Congress authors dataset, cosine similarity was used to get the closest string match where exact matches cannot be obtained.

To combine the two datasets, the notebook `congress_dataset.ipynb` was used to create the association between bills and authors. The `Bills Status.ipynb` notebook then classifies the status as either 'Passed' or 'Not Passed'. The final dataset used for this project is `18th_hor_bills_dataset_with_status.csv`.

## Data Pre-Processing
- Text features will be generated from the bill titles using Term Frequency-Inverse Document Frequency (TF-IDF) with n-grams.
- The Principal Authors column will be joined with the List of Elected Members of the House of Representatives to produce the number of sponsors in each political party. A new column will be created for each political party in Congress containing the number of principal authors that belong to which for each bill. The respective regions and provinces that the authors represent are also considered. The column containing the names of principal authors will be dropped.
- The Primary Referral and Scope columns will be label encoded according to the one-to-one relationship for each bill and the respective column categories.
- The Mother Bill Status containing information on bills substituted or consolidated into a bill of larger scope will be used as proxy to the status of the bill in the Bill Status column.
- The Bill Status column will be labelled “1” or “0” in a new Final Status column according to whether the bill has been passed (into a Republic Act) or failed to pass (pending at the committee level or in the Senate) based on the presence of the word “enacted” or "Republic Act".

## Methods: Techniques and Models
The following were used to process the dataset and predict status. More details regarding the implementation of these procedures are available at the `18th HOR Bills Analysis.ipynb` notebook.
- Principal Component Analysis or Incremental Principal Component Analysis
- Logistic Regression
- Support Vector Machines

## Results
The results can be accessed in the `18th HOR Bills Analysis.ipynb` notebook as well.
