'''
Create a class named TransactionIterator.
The class should:
Accept a list of transactions through its constructor.
Maintain the current position using an index variable.
Implement the following special methods:
__iter__() to return the iterator object.
__next__() to return one transaction at a time.
'''
class  TransactionIterator():
    def __init__(self,transactions):
        self.transactions=transactions
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index<len(self.transactions):
             transaction = self.transactions[self.index]
             self.index+=1
             return transaction
        else:
            raise StopIteration
transactions = ["Deposit ₹1000", "Withdraw ₹500", "Deposit ₹2000"]
t=TransactionIterator(transactions)

for transactions in t:
    print(transactions)