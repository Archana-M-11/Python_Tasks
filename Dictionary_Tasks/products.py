'''
apply discount of 20% to all products costing morethan 1000Rs
'''
products = [
    {"name": "Laptop", "price": 55000},
    {"name": "Mouse", "price": 600},
    {"name": "Keyboard", "price": 1500},
    {"name": "Monitor", "price": 12000}
]
for product in products:
    if product['price']>1000:
        new_price  = product['price'] - (product['price'] * 20 / 100)
        print(product['name'], ':', new_price)
    else:
        print(product['name'], ':', product['price'])