import streamlit as st
from prediction_helper import predict

st.title("Credit Risk Modelling")

with st.expander("ℹ️ How to use the app"):
    st.write("""
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
    """)

row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

with row1[0]:
    age = st.number_input('Age', min_value=18, step=1, max_value=100, value=28)
with row1[1]:
    income = st.number_input('Income', min_value=0, value=1200000)
with row1[2]:
    loan_amount = st.number_input('Loan Amount', min_value=0, value=2560000)

loan_to_income_ratio = loan_amount / income if income > 0 else 0
with row2[0]:
    st.text("Loan to Income Ratio:")
    st.text(f"{loan_to_income_ratio:.2f}")

with row2[1]:
    loan_tenure_months = st.number_input('Loan Tenure (months)', min_value=0, step=1, value=36)
with row2[2]:
    avg_dpd_per_delinquency = st.number_input('Avg DPD', min_value=0, value=20)

with row3[0]:
    delinquency_ratio = st.number_input('Delinquency Ratio', min_value=0, max_value=100, step=1, value=30)
with row3[1]:
    credit_utilization_ratio = st.number_input('Credit Utilization Ratio', min_value=0, max_value=100, step=1, value=30)
with row3[2]:
    num_open_accounts = st.number_input('Open Loan Accounts', min_value=1, max_value=4, step=1, value=2)

with row4[0]:
    residence_type = st.selectbox('Residence Type', ['Owned', 'Rented', 'Mortgage'])
with row4[1]:
    loan_purpose = st.selectbox('Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'])
with row4[2]:
    loan_type = st.selectbox('Loan Type', ['Unsecured', 'Secured'])

if st.button('Calculate Risk'):
    probability, credit_score, rating = predict(age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
                                                delinquency_ratio, credit_utilization_ratio, num_open_accounts,
                                                residence_type, loan_purpose, loan_type)

    st.write(f"Default Probability: {probability:.2%}")
    st.write(f"Credit Score: {credit_score}")
    st.write(f"Rating: {rating}")

with st.expander("🔮 Default Probability"):
    st.write("""
    The default probability is the likelihood that the borrower will fail to make payments. A higher percentage means a higher risk.
    """)
with st.expander("📊 Credit Score"):
    st.write("""
    The credit score is calculated based on the input data and reflects the borrower's creditworthiness. Scores typically range from 300 to 900.
    """)
with st.expander("🏅 Credit Rating"):
    st.write("""
    The credit rating is a qualitative measure of the borrower’s creditworthiness, typically rated as Poor, Average, Good, or Excellent.
    """)