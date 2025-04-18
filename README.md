# creditscoregenerator
This app helps us to generate the latest credit score based on the bank's vantage model and also helps to improve the credit score 
# Credit Score Simulator

This Streamlit app simulates your credit score using the VantageScore 3.0 model.  
It takes key credit parameters as input and calculates a projected score, provides personalized recommendations to improve your credit health, and forecasts potential score improvement in 3–6 months.

---

## Features

- **User Inputs** for:
  - Late Payments
  - Credit History Age
  - Credit Usage (%)
  - Total Balances ($)
  - Recent Credit Checks
  - Available Credit ($)
  - Total Credit Limit ($)

- **Simulated Score** calculated using VantageScore 3.0 weights:
  - Payment History (40%)
  - Credit History (21%)
  - Credit Usage (20%)
  - Total Balances (11%)
  - Credit Checks (5%)
  - Available Credit (3%)

- **Smart Recommendations** based on your inputs  
- **Forecasted Score** for the next 3–6 months if improvements are followed

---

## How to Run Locally

1. **Clone the Repository**
```bash
git clone https://github.com/your-username/credit-score-simulator.git
cd credit-score-simulator
