def government_tax_income(filing_status, taxable_income):
    tax_status = {
        0: [(8350, 0.10), (33950, 0.15), (82250, 0.25), (171550, 0.28), (372950, 0.33), (float('inf'), 0.35)],
        1: [(16700, 0.10), (67900, 0.15), (137050, 0.25), (208850, 0.28), (372950,0.33), (float('inf'), 0.35)],
        2: [(8350, 0.10), (33950, 0.15), (68525, 0.25), (104425, 0.28), (186475, 0.33), (float('inf'), 0.35)],
        3: [(11950, 0.10), (45500, 0.15), (117450, 0.25), (190200, 0.28), (372950, 0.33), (float('inf'), 0.35)]
    }
    
    tax = 0
    prev_limit = 0

    for limit, taxRate in tax_status[filing_status]:
        if taxable_income > limit:
            tax += (limit - prev_limit) * taxRate
            prev_limit = limit
        else: 
            tax += (taxable_income - prev_limit) * taxRate
            break
    return tax


print("filing Status? ")
print("0 = Single")
print("1 = Married jointly")
print("2 = Married seperately")
print("3 = Head of Household")

filing_status = int(input("Enter your filing status: "))
taxable_income = float(input("Enter your income: "))

tax = government_tax_income(filing_status, taxable_income)
print(f"Your total tax is: ${tax: 2f}")