salary = float(input("Enter your monthly salary: ₹"))
credit_score = int(input("Enter your credit score (300-850): "))
debt = float(input("Enter your existing monthly debt: ₹"))


def check_loan_eligibility(salary, credit_score, debt):
    # Debt-to-Income Ratio (VERY important in FinTech)
    dti_ratio = (debt / salary) * 100

    # Risk override rule
    if dti_ratio > 40:
        return "Rejected", "High Risk"

    # Core credit rules
    if credit_score >= 750 and salary >= 50000:
        return "Approved", "Low Risk"
    elif 650 <= credit_score < 750:
        return "Conditional Approval", "Medium Risk"
    else:
        return "Rejected", "High Risk"


eligibility_status, risk_level = check_loan_eligibility(salary, credit_score, debt)

print("\nLoan Decision Report:")
print(f"Eligibility Status: {eligibility_status}")
print(f"Risk Level: {risk_level}")
