# Vijio Telecom – Customer Churn Analysis & Prediction

img

## Overview  
This project focuses on analyzing and predicting **customer churn** for **Vijio Telecom**, a simulated telecom company.  
The goal is to combine ** exploratory analysis, machine learning, and business intelligence** into one end-to-end solution.  

Key steps include:  
- **Data Extraction & ETL:** Clean and transform telecom customer data in MySQL.  
- **Exploratory Analysis:** Identify churn trends by contracts, services, payments, and demographics.  
- **Machine Learning:** Build and evaluate predictive models in Python (Jupyter Notebook) to forecast churn probability.  
- **Visualization:** Develop interactive Power BI dashboards for historical churn insights and ML predictions.  
- **Business Insights:** Translate findings into recommendations to reduce churn and protect revenue.  

This project demonstrates the integration of **Data Analysis + Machine Learning + Business Analytics** to solve a real-world business challenge.

## Technical Requirements  

### 1. Software & Tools  
- **Python 3.9+** (with Jupyter Notebook)  
- **MySQL Workbench** (for data preparation and queries)  
- **Power BI Desktop / Power BI Service** (for dashboards)   

### 2. Python Libraries  
- `pandas` → data cleaning & manipulation  
- `numpy` → numerical computations  
- `scikit-learn` → machine learning (modeling & evaluation)  
- `matplotlib` / `seaborn` → visualizations & EDA  
- `mysql-connector-python` → MySQL database connection  

### 3. Dataset  
## 📑 Dataset Description  

The raw dataset **`Customer_Data.csv`** contains **6,418 rows** and **32 features**, covering customer demographics, service subscriptions, billing details, and churn status.  

### Features (Columns)  

| Column Name                  | Description |
|------------------------------|-------------|
| **Customer_ID**              | Unique identifier for each customer |
| **Gender**                   | Customer gender (Male/Female) |
| **Age**                      | Customer age |
| **Married**                  | Whether the customer is married (Yes/No) |
| **State**                    | Customer’s state of residence |
| **Number_of_Referrals**      | Number of referrals made by the customer |
| **Tenure_in_Months**         | Number of months the customer has stayed with Vijio Telecom |
| **Value_Deal**               | Customer’s subscribed value deal (Deal 1, Deal 2, etc.) |
| **Phone_Service**            | Whether the customer has phone service (Yes/No) |
| **Multiple_Lines**           | Whether the customer has multiple phone lines (Yes/No) |
| **Internet_Service**         | Whether the customer has internet service (Yes/No) |
| **Internet_Type**            | Type of internet service (DSL, Fiber Optic, Cable, etc.) |
| **Online_Security**          | Whether the customer has online security (Yes/No) |
| **Online_Backup**            | Whether the customer has online backup (Yes/No) |
| **Device_Protection_Plan**   | Whether the customer has device protection (Yes/No) |
| **Premium_Support**          | Whether the customer has premium tech support (Yes/No) |
| **Streaming_TV**             | Whether the customer has streaming TV (Yes/No) |
| **Streaming_Movies**         | Whether the customer has streaming movies (Yes/No) |
| **Streaming_Music**          | Whether the customer has streaming music (Yes/No) |
| **Unlimited_Data**           | Whether the customer has unlimited data (Yes/No) |
| **Contract**                 | Customer contract type (Month-to-month, One year, Two year) |
| **Paperless_Billing**        | Whether the customer uses paperless billing (Yes/No) |
| **Payment_Method**           | Payment method (Electronic check, Mailed check, Bank withdrawal, Credit card) |
| **Monthly_Charge**           | Monthly charges billed to the customer |
| **Total_Charges**            | Total charges billed to the customer |
| **Total_Refunds**            | Total amount refunded to the customer |
| **Total_Extra_Data_Charges** | Total charges for extra data usage |
| **Total_Long_Distance_Charges** | Total charges for long-distance services |
| **Total_Revenue**            | Total revenue generated from the customer |
| **Customer_Status**          | Whether the customer Stayed, Churned, or Joined |
| **Churn_Category**           | Category of churn (e.g., Competitor, Dissatisfaction, etc.) |
| **Churn_Reason**             | Specific reason for churn (if applicable) |

---

### Processed Versions in SQL  
- **`stg_churn.csv`** → Raw import & initial cleaning (staging layer)  
- **`prod_churn.csv`** → Production-ready cleaned dataset  
- **`vw_churndata.csv`** → SQL view with churn metrics  
- **`vw_joindata.csv`** → SQL view joining demographics, contracts, billing & churn status  
