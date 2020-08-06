# import math to use math functionalities
import math
# print an instruction that tells the user to choose between investment or bond
# print a statement explaining the prurpose of the investment
# print a statement explaining the prurpose of the bond
print("Choose either 'investment' or 'bond'from the menu below")
print("investment - to calculate the amount of interest you'll earn on interest ")
print("bond - to calculate the amount you will have to pay on a home loan ")
# request user to input the if he wants an investment or  bond
investment_bond = input("Do you want an [Investment] or [Bond]: ")
# if the user chose investment then;
# request the user to input the amount they want to deposit
# request user to input the interest rate in percentage
# divide the interest by 100
# request the user to input the period for investment
# request the user to input if he wants to calculated with compound interest or simple interest
if investment_bond == 'INVESTMENT' or investment_bond == 'Investment' or investment_bond == 'investment':
    principal_amount = float(input('Enter the amount of money that you are depositing: '))
    interest_rate = float(input('Enter the interest rate (as a percentage): '))
    rate = interest_rate/100
    period = float(input('Enter the number of years you plan on investing for: '))
    interest = input("What type of do you prefer: 'Simple'or 'Compound': ")
# if the user chose the simple interest
# create the final amount formula to calculate final total value of the investment
# then print the final amount of the investment
    if interest == 'Simple':
        final_amount = principal_amount*(1+rate*period)
        print('The final amount of your investment R',final_amount)
# else if the user chose the compound interest
# create the final amount formula to calculate final total value of the investment
# then print the final amount of the investment
    elif interest == 'Compound':
        final_amount = round(principal_amount*math.pow((1+rate),period),2)
        print('The final amount of your investment is R',final_amount)
# if the user chose the bond
# request the user to present value of the house
# request use to enter the interest rate
# divide the interest rate by 12 months
# request user to input the total repayment period
# create the formula to calculate total amount to be repaid
# then print the total amount to be repaid
elif investment_bond == 'BOND' or investment_bond == 'Bond' or investment_bond == 'bond':
    present_value = float(input('Enter the present value of the house: '))
    interest_rate = float(input('Enter the interest rate: '))
    rate = interest_rate /12
    period = float(input('Enter the repayment period in months: '))
    repayment = round((present_value*(rate*math.pow((1+rate),period)))/((math.pow((1+rate),period))-1),2)
    print('The total repayment will be R',repayment)
# print an error message if the user didnt choose bond or investment
else:
    print ("Error: you have selected a wrong entry!")
