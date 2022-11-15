# https://replit.com/@appbrewery/tip-calculator-end

GREETING = 'Welcome to the tip calculator!'
ASK_TOTAL_BILL = 'What was the total bill?'
ASK_TIP_PERCENT = 'How much tip would you like to give? 10, 12, or 15?'
ASK_NUMBER_OF_PEOPLE = 'How many people to split the bill?'
TELL_THE_RESULT = 'Each person should pay: ${:.2f}'

print(GREETING)

bill = float(input(ASK_TOTAL_BILL))
tip_percent = int(input(ASK_TIP_PERCENT))
num_of_people = int(input(ASK_NUMBER_OF_PEOPLE))

bill_with_tip = bill + tip_percent * bill / 100
part_of_bill_divivded = bill_with_tip / num_of_people

print(TELL_THE_RESULT.format(part_of_bill_divivded))
