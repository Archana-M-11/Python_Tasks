'''
2.Create a dictionary of five countries and their capitals.
 Display:
All countries.
All capitals.
Each country with its capital.
'''
countries = {
    "India": "New Delhi",
    "USA": "Washington D.C.",
    "Japan": "Tokyo",
    "Australia": "Canberra",
    "France": "Paris"
}
print('all counteries: ',countries.keys())
print('all capitals: ',countries.values())
print('all counteries with the capitals:')
print(countries.items())
for key,values in countries.items():
    print(key,':',values)