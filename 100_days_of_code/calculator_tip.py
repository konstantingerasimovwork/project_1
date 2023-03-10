print('Welcome to the tip calculator!')
bill = float(input('What was the total bill?$'))
tip = int(input('How much tip would you like to give? 10, 12, or 15?'))
split = int(input('How many people to split the bill?'))
total_bill = ((tip / 100) * bill) + bill
total_tip = total_bill / bill

each_person_pay = (bill / split) * total_tip
each_person_pay_2_digits = format(each_person_pay, '.2f')
print(f'Each person should pay: {each_person_pay_2_digits}')
