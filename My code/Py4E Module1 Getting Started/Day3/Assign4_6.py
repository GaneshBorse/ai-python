"""Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
 Pay should be the normal rate for hours up to 40
 and time-and-a-half for the hourly rate for all hours worked above 40 hours.

Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
"""


def computepay(hrs, rate):
    if hrs >= 41:
        extrahrs = hrs - 40
        basehr = hrs - extrahrs
        pay = (basehr * rate) + extrahrs * (rate * 1.5)
    else:
        pay = hrs * rate
    return pay


hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
extrahrs = 0
basehr = 0

p = computepay(hrs, rate)
print("Pay", p)
