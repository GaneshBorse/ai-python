"""3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
"""

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate/hr:"))
pay = 0
overtime = 0
basehr = 0
if hrs >= 41:
    overtime = hrs - 40
    basehr = hrs - overtime
    pay = (basehr * rate) + overtime * (rate * 1.5)
    print(pay)
else:
    pay = hrs * rate
    print(pay)
