# https://replit.com/@appbrewery/tip-calculator-end

GREETING = 'Welcome to the tip calculator!'
ASK_TOTAL_BILL = 'What was the total bill?'
TIP_PERCENTS = (10, 12, 15)
ASK_TIP_PERCENT = 'How much tip would you like to give? {}, {}, or {}?'.format(*TIP_PERCENTS)
ASK_NUMBER_OF_PEOPLE = 'How many people to split the bill?'
TELL_THE_RESULT = 'Each person should pay: ${:.2f}'
VALUE_ERROR_MESSAGE = 'What you entered is not a number.'

print(GREETING)

while True:
    try:
        bill = float(input(ASK_TOTAL_BILL))
        tip_percent = int(input(ASK_TIP_PERCENT))
    except ValueError:
        print(VALUE_ERROR_MESSAGE)
        continue
    if tip_percent not in TIP_PERCENTS:
        print('Please, choose the tip amount from the given options.')
        continue
    try:
        num_of_people = int(input(ASK_NUMBER_OF_PEOPLE))
    except ValueError:
        print('What you entered is not a number.')
        continue

    bill_with_tip = bill + tip_percent * bill / 100
    part_of_bill_divided = bill_with_tip / num_of_people

    print(TELL_THE_RESULT.format(part_of_bill_divided))
    break
