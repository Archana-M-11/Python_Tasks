'''
10.Write a function expensive_products(**products) that:
Accepts product names and prices.
Displays only products costing more than ₹1000.
'''
def expensive_products(**products):
    for product,price in products.items():
        if price>1000:
            print(f'{product} : {price}')
expensive_products(
    Laptop=55000,
    Mouse=600,
    Keyboard=1200,
    Monitor=15000,
    Pen=50
)