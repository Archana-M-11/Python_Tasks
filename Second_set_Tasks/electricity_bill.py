'''
3.Calculate Electricity Bill
 
Example
 
0-100 units 
101-200
201-500
Above 500
Different price for each slab.
'''

units = int(input("Enter units: "))
bill = 0
if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = (100 * 2) + ((units - 100) * 3)
elif units <= 500:
    bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)
else:
    bill = (100 * 2) + (100 * 3) + (300 * 5) + ((units - 500) * 7)

print("Electricity Bill: ", bill)