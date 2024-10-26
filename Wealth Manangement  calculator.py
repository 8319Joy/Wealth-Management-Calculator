#!/usr/bin/env python
# coding: utf-8

# Certainly! Below is a simple wealth management calculator in Python that helps Indian users plan their investments to achieve specific financial goals. This calculator considers factors like current investment, expected annual return rate, investment duration, and the goal amount.

# In[2]:


def wealth_management_calculator():
    print("Welcome to the Wealth Management Calculator!")
    
    # Input current investment amount
    current_investment = float(input("Enter your current investment amount (in INR): "))
    
    # Input expected annual return rate
    annual_return_rate = float(input("Enter the expected annual return rate (in %): ")) / 100
    
    # Input duration of investment in years
    years = int(input("Enter the duration of investment (in years): "))
    
    # Input goal amount
    goal_amount = float(input("Enter your financial goal amount (in INR): "))

    # Calculate the future value of the current investment
    future_value = current_investment * (1 + annual_return_rate) ** years
    
    # Additional investment needed to reach the goal
    if future_value >= goal_amount:
        print("\nCongratulations! Your current investment will meet your financial goal!")
        print(f"Future Value of your investment after {years} years will be: INR {future_value:,.2f}")
    else:
        additional_investment_needed = (goal_amount - future_value) / ((1 + annual_return_rate) ** years - 1) / annual_return_rate
        print("\nYou will need to make additional investments to reach your financial goal.")
        print(f"Future Value of your current investment after {years} years will be: INR {future_value:,.2f}")
        print(f"You need to invest an additional INR {additional_investment_needed:,.2f} per year.")

# Run the wealth management calculator
wealth_management_calculator()


# How to Use the Calculator:
# Run the code in a Python environment.
# Input the required values when prompted:
# Current investment amount in INR
# Expected annual return rate (in percentage)
# Duration of investment in years
# Your financial goal amount in INR
# The calculator will output whether your current investment will meet your goal or how much more you need to invest annually to reach it.

# In[ ]:




