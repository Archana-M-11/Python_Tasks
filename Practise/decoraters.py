def greet(func):
    def work(name):
        print('welcome...')
        func(name)
        print('thankyou')
    return work


@greet
def hello(name):
    print(f'hello {name}')
name = input("Enter your name: ")
hello(name)