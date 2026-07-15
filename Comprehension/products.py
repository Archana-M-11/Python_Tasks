'''
apply discount of 20% to all products costing morethan 1000Rs
'''
products = [
    {"name": "Laptop", "price": 55000},
    {"name": "Mouse", "price": 600},
    {"name": "Keyboard", "price": 1500},
    {"name": "Monitor", "price": 12000}
]

discount=[
    {
        product['name']:product['price']-(product["price"] * 20 / 100) if product['price'] >1000
        else product['price']
    }for product in products
]
print(discount)