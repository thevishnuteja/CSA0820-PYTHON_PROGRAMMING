def cal_income_tax(total_income):

    if total_income <= 10000:
        return 0
    elif total_income <= 20000:
        return (total_income - 10000) * 0.10
    else:
        return 10000 * 0.10 + (total_income - 20000) * 0.20

income = float(input("Enter your  income: $"))
if income >= 0:
    tax_payable = cal_income_tax(income)
    print(f"Income tax payable: ${tax_payable:.2f}")
else:
    print("Please enter a valid positive income.")
