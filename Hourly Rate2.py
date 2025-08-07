# Prompt user for hours
hrs = input("Enter Hours: ")
rate = input("Enter Rate per Hour: ")

# Convert input to float
h = float(hrs)
r = float(rate)

# Compute gross pay with overtime
if h > 40:
    regular_pay = 40 * r
    overtime_pay = (h - 40) * r * 1.5
    gross_pay = regular_pay + overtime_pay
else:
    gross_pay = h * r

print("Pay:", gross_pay)
