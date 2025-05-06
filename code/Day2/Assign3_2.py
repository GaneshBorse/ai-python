### same as 3.1 but using try-except.
"""3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
"""
# NOTE: whenever USING Try Except , try to put minimum/necesaary code only in them.

try:
    hrs = float(input("Enter Hours:"))
    rate = float(input("Enter Rate/hr:"))
except:
    print("Enter Valid INT/Float Numbers only")
    quit()
    # quit()= Quits the program, use it when no point continuing rest of program!

pay = 0
overtime = 0
basehr = 0

if (0 < hrs >= 41) & (rate > 0):
    overtime = hrs - 40
    basehr = hrs - overtime
    pay = (basehr * rate) + overtime * (rate * 1.5)
elif (0 < hrs < 41) & (rate > 0):
    pay = hrs * rate
else:
    print("+ve Value Only")

print(pay)
