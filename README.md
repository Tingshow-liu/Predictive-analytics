## ML predictive analytics
### Goal: Apply ML models (predictive analytics) to company digital marketing campaigns to reach precision remarketing (Maximize the Return on Ad Spend)
---
* Data source: Customer "website behaviors"  
* Predict next purchases in 3 days with customer website behaviors in past 10 days
---
* Features:
  * Static feature, ex: time on website, total number of pages viewed, total number of buttons clicked, etc.  
  * Behavior feature, ex: buttoms clicked (add to cart, header, etc.)
---
* ML deployment:
  * Google Cloud Platform tools (BigQuery, Vertex AI)
  * Google APIs (GA Management API)
  * Google tools (Google Analytics, Google Ads)
---
* Code:
  > 1. Combine Google BigQuery (SQL syntax) & Vertex AI (Python syntax) to process data more efficiently; Utilize GitHub for automation on cloud  
  > 2. Class "Update_data":  
  >> (1) Update data daily for realtime predictive analytics  
  >> (2) Update both realtime "raw data (function: update_raw)" and "customer behavior data (function: update_pivot)"  
  >>     (customer behavior data is generated from raw data)  
  >> (3) History (training) data don't need to update daily (already stored on BigQuery)  
  > 3. Class "Queries":  
  >> (1) Combine SQL & Python: import data from BigQuery to Vertex AI  
  >> (2) Function "static_query": import static features/ behaviors  
  >> (3) Function "behavior_query": import behaviorial features/ behaviors  
  > 4. Class "Return_analysis":  
  >> (1) Create features that represents customer behaviors between the "last 2 visits" (conduct with "static features")  
  >> (2) Categorize customers into "purchasers" and "non-purchasers" for return analysis  
  > 5. Class "Data_cleansing":  
  >> (1) Merge "static features" and "behaviorial features" data  
  >> (2) Do filtering, drop NaNs, 0 columns, etc. (Steps haven't complete with SQL on BigQuery)  
  > 6. Class "Data_pre_processing":  
  >> (1) Do further data processing, ex: create dummy variable, address member info for later mapping  
  >> (2) Cut data: "History (training) data"  
  > 7. Class "Model_evaluation"  
  >> (1) Evaluate performance of different models based on different metrics  
  >> (2) Metrics used: balanced accuracy score (imbalanced dataset), AUC area, confusion metrix  
  > 8. Class "Models"  
  >> (1) Construct different ML models  
  >> (2) Models constructed: Gradient boosting (selected), Random forest, XGBoost, Stacking  
  > 9. Class "Tune_models"  
  >> (1) Tune the hyper-parameters of different models  
  > 10. Class "Export_output"  
  >> (1) Map model predictions with member info to find re-marketing targets  
  >> (2) Get "Next purchasers" (customers with high purchase propensity)  
  >> (3) Transfer the prediction result to the correct format for deployment on Google Ads  
