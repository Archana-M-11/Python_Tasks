'''
Creates a generator function newsletter_emails(customers) that:
Accepts the list of customer email IDs as a parameter.
Uses the yield keyword to return one email address at a time.
Iterate through the generator using a for loop.
Display the following message for each email:
Newsletter sent to rahul@gmail.com
'''
customers = [
    "rahul@gmail.com",
    "archana@gmail.com",
    "priya@gmail.com",
    "arun@gmail.com"
]
def newsletter_emails(customers):
    for email in customers:
        yield email
emails=newsletter_emails(customers)

for email in emails:
    print(f'Newsletter sent to {email}')
