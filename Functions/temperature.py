'''
1.Write a function that accepts temperature in Celsius and returns Fahrenheit.
 '''
def temperature(temp):
    Fahrenheit=(temp*9/5)+32
    return Fahrenheit
temp=int(input('enter the temperature in celsius: '))
print(temperature(temp))