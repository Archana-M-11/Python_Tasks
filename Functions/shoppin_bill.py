'''
9.Write a function shopping_bill(**kwargs) where:
Keys represent product names.
Values represent prices.
Display each product with its price.
Display the total bill amount.
'''
def shopping_bill(**kwargs):
    total = 0
    print('Shopping Bill ')
    for product, price in kwargs.items():
        print(f'{product}: ₹{price}')
        total += price
    print('')
    print(f'Total Bill: ₹{total}')
shopping_bill(
    Rice=120,
    Milk=60,
    Bread=40,
    Eggs=90
)