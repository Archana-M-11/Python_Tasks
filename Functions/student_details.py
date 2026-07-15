'''
3.Create a function that accepts a dictionary containing student details and displays them neatly'''

def student_details(detail):
    print('student detail: ')
    for key,val in detail.items():
        print(key,val)

detail={
     "id": 101,
    "name": "Achu",
    "age": 21,
    "course": "Python"
}
student_details(detail)