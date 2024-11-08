# Credit Risk Prediction Model

This project implements a **Credit Risk Prediction Model** that predicts whether a loan applicant is likely to default. The project uses a machine learning model (**Logistic Regression with class imbalance handled using SMOTE Tomek** and parameter tuning via **Optuna**) and presents a web interface through **Streamlit** where users can input various personal and financial attributes to assess their creditworthiness.


## 1. Project Overview

The **Credit Risk Prediction Model** uses multiple borrower attributes such as age, income, loan amount, credit utilization, and more to calculate the likelihood of default, a credit score (ranging from 300 to 900), and a rating (Poor, Average, Good, Excellent). This project can help financial institutions or individual users assess credit risk more effectively.


## 2. Project Structure

The repository is structured as follows:

- `main.py` — Streamlit application file
- `prediction_helper.py` — Helper functions for preprocessing and making predictions
- `requirements.txt` — Python dependencies for the project
- `README.md` — Project README file
- `ml_credit_risk_model.ipynb` — Jupyter notebook for the entire project, including data exploration, preprocessing, and model training
- `artifacts/` — Directory containing model artifacts
  - `model_data.joblib` — Serialized model and scaler saved as a joblib file



## 3. Features

The model takes into account the following features:

- **Age**: Enter your age between 18-100. Younger borrowers might have different risk profiles.
- **Income**: Enter your annual income in INR. Higher income can reduce the likelihood of default.
- **Loan Amount**: The total loan amount you are applying for. Larger loans tend to carry more risk.
- **Loan to Income Ratio**: This is automatically calculated based on your income and loan amount.
- **Loan Tenure**: The duration (in months) for which the loan is being taken.
- **Average DPD**: The average number of days past due for your previous loans.
- **Delinquency Ratio**: The percentage of delinquent accounts in your credit history.
- **Credit Utilization Ratio**: The percentage of your credit that you're currently utilizing.
- **Number of Open Loan Accounts**: The total number of open credit accounts you have.
- **Residence Type**: Choose if you own, rent, or mortgage your home.
- **Loan Purpose**: The reason for taking the loan (e.g., education, home, personal).
- **Loan Type**: Whether the loan is secured or unsecured.



## 4. Installation Instructions

### Clone the repository
```bash
git clone https://github.com/Vraj-Data-Scientist/ml-project-credit-risk-model.git
cd ml-project-credit-risk-model

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt

streamlit run main.py
```

## 5. Modeling Approach

### Preprocessing:
- Missing values are handled, and categorical features are encoded.
- Numerical features are scaled to ensure the model performs well.

### Model:
The model uses **Logistic Regression with class imbalance handled using SMOTE Tomek** and parameter tuning via **Optuna** to calculate the default probability, which is converted into a credit score ranging from 300 (high risk) to 900 (low risk). The credit score is categorized into four ratings:
- **300-500:** Poor
- **500-650:** Average
- **650-750:** Good
- **750-900:** Excellent

### Feature Scaling:
- The input data is scaled before feeding it to the model to ensure uniformity and better performance.


## 6. Results

The best-performing model, **Logistic Regression with class imbalance handled using SMOTE Tomek** and parameter tuning via **Optuna**, achieved the following evaluation metrics:

- **Accuracy:** 93%
- **Recall:** 94%

### Key outputs from the model include:

- **Default Probability:** The likelihood that the applicant will default on their loan.
- **Credit Score:** A number between 300 and 900, indicating the creditworthiness.
- **Rating:** A categorical rating based on the credit score:


## 7. Usage

Users can run the **Streamlit** app locally, input their information (age, income, loan amount, etc.), and receive the default probability, credit score, and credit rating instantly.

### To use the model:

1. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```
   
2. Enter the required inputs into the web form.  

3. View the results for:  

Default Probability  
Credit Score  
Credit Rating  


## 8. Contributions

We welcome contributions from the community! If you'd like to improve the model or add new features, feel free to fork this repository and submit a pull request.
## Dataset Citation
This project uses a dataset provided by Codebasics as part of the Codebasics Data Science Bootcamp. The dataset is not included in this repository due to usage restrictions.

### Citation

If you would like to use the dataset, please reference it as follows:

```markdown
Codebasics. (n.d.). Dataset from the Codebasics Data Science Bootcamp. Retrieved from [Codebasics](https://codebasics.io/)
```

Note: Users interested in obtaining the dataset should contact Codebasics directly through their website to gain access. This citation is for reference purposes only.



