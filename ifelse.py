m_price = 1000000
has_goodcredit = False

if has_goodcredit:
    downpayment = 0.1 * m_price
else:
    downpayment = 0.2 * m_price

print(f'Downpayment: ${downpayment}')


has_high_income = True
has_good_credit = True
has_criminal_record = False

if has_high_income or has_good_credit:
    print('Eligible for loan')
if has_good_credit and not has_criminal_record:
    print('Ramro manchey raicha kto')