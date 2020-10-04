has_high_income = False
has_good_credit = True
has_criminal_record = False

if has_high_income and has_good_credit:
    print("AND: eligible for loan")

if has_high_income or has_good_credit:
    print("OR: eligible for loan")

if not has_criminal_record and has_good_credit:
    print("NOT: eligible for loan")
