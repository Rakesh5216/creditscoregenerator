import streamlit as st

st.set_page_config(page_title="Credit Score Simulator", layout="centered")

st.title("Credit Score Simulator")
st.caption("Simulate your credit score based on VantageScore 3.0 model and get recommendations.")

# Input Fields
st.header("1. Enter Your Credit Details")

late_payments = st.number_input("Late Payments", min_value=0, value=0)
oldest_account_years = st.number_input("Age of Oldest Account (Years)", min_value=0, value=0)
oldest_account_months = st.number_input("Months", min_value=0, max_value=11, value=0)
credit_usage = st.slider("Credit Usage (%)", 0, 100, 30)
total_balance = st.number_input("Total Balances ($)", min_value=0, value=0)
credit_checks = st.number_input("Recent Credit Checks (last 2 years)", min_value=0, value=0)
available_credit = st.number_input("Available Credit ($)", min_value=0, value=0)
total_credit_limit = st.number_input("Total Credit Limit ($)", min_value=1, value=1000)

# Score Calculation
def calculate_score(late, yrs, mos, usage, balance, checks, avail, limit):
    # Normalize inputs to 100-point scale for each factor
    score_components = {}

    # 1. Payment History (40%)
    if late == 0:
        score_components["payment_history"] = 100
    elif late <= 2:
        score_components["payment_history"] = 80
    elif late <= 4:
        score_components["payment_history"] = 60
    else:
        score_components["payment_history"] = 40

    # 2. Credit History (21%)
    age_months = yrs * 12 + mos
    if age_months >= 84:
        score_components["credit_history"] = 100
    elif age_months >= 60:
        score_components["credit_history"] = 80
    elif age_months >= 36:
        score_components["credit_history"] = 60
    else:
        score_components["credit_history"] = 40

    # 3. Credit Usage (20%)
    if usage <= 10:
        score_components["credit_usage"] = 100
    elif usage <= 30:
        score_components["credit_usage"] = 80
    elif usage <= 50:
        score_components["credit_usage"] = 60
    else:
        score_components["credit_usage"] = 30

    # 4. Total Balances (11%)
    if balance < 5000:
        score_components["total_balances"] = 100
    elif balance < 20000:
        score_components["total_balances"] = 70
    else:
        score_components["total_balances"] = 40

    # 5. Credit Checks (5%)
    if checks == 0:
        score_components["credit_checks"] = 100
    elif checks <= 3:
        score_components["credit_checks"] = 70
    else:
        score_components["credit_checks"] = 40

    # 6. Available Credit (3%)
    utilization = (limit - avail) / limit * 100
    if utilization <= 30:
        score_components["available_credit"] = 100
    elif utilization <= 50:
        score_components["available_credit"] = 70
    else:
        score_components["available_credit"] = 40

    # Weighted Score
    weights = {
        "payment_history": 0.40,
        "credit_history": 0.21,
        "credit_usage": 0.20,
        "total_balances": 0.11,
        "credit_checks": 0.05,
        "available_credit": 0.03
    }

    final_score = sum(score_components[factor] * weights[factor] for factor in score_components)
    scaled_score = round(300 + (final_score * 5.5))  # Scale to 300–850

    return scaled_score, score_components


# Recommendations
def get_recommendations(late, usage, balance, checks, avail, limit):
    tips = []
    if late > 0:
        tips.append("Make all future payments on time to improve your payment history.")
    if usage > 30:
        tips.append("Reduce credit usage below 30% of your limit.")
    if balance > 20000:
        tips.append("Pay down outstanding balances to reduce total debt.")
    if checks > 3:
        tips.append("Avoid applying for new credit in the next few months.")
    if (limit - avail) / limit > 0.5:
        tips.append("Increase your available credit or pay down balances.")
    if not tips:
        tips.append("You're doing great! Just continue managing your credit responsibly.")
    return tips


# Forecast
def forecast_score(current_score, tips):
    improvement = len(tips) * 10
    forecast = min(current_score + improvement, 850)
    return forecast


# Button trigger
if st.button("Calculate My Credit Score"):
    score, subscores = calculate_score(
        late_payments,
        oldest_account_years,
        oldest_account_months,
        credit_usage,
        total_balance,
        credit_checks,
        available_credit,
        total_credit_limit
    )
    st.subheader("Your Simulated Score:")
    st.metric(label="Estimated Score", value=score)

    st.subheader("What’s Helping or Hurting You:")
    for factor, val in subscores.items():
        st.write(f"**{factor.replace('_', ' ').title()}**: {val}/100")

    tips = get_recommendations(late_payments, credit_usage, total_balance, credit_checks, available_credit, total_credit_limit)
    st.subheader("Recommendations to Improve Your Score:")
    for tip in tips:
        st.write("- " + tip)

    projected = forecast_score(score, tips)
    st.subheader("Projected Score in 3–6 Months:")
    st.success(f"Your score could improve to **{projected}** with the above actions.")


