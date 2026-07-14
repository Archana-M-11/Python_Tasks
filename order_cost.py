'''
Write a program that prints the price of a sandwich order according to the  
sandwich filling a customer chooses. First you need to check whether the customer
 has ordered the item that is in our menu then print the price to the console
   according to his/her order?
'''
m= {
    "veg": 50,
    "chicken": 80,
    "cheese": 70,
    "egg": 60
}
ord =input("Enter sandwich filling: ").split()
total=0
for item in ord:
    if item in m:
       total+=m[item]
    else:
        print("Sorry! This item is not available in our menu.")
print(total)