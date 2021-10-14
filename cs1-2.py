# Author: CRS 10/14/21
initial = int(input("Input an investment amount."))
rate = float(input("Input the annual interest rate."))
time = int(input("Input the time over which the investment will be compounded."))
value = initial * (1 + rate / 12) ** (12 * time)
value = str(value)
time = str(time)
print("Your investment after " + time + " years is " + value)
