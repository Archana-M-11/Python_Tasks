available = 5
booked = 0
while True:
    print("\n----- Railway Reservation -----")
    print("1. Book Ticket")
    print("2. Cancel Ticket")
    print("3. Check Availability")
    print("4. Print Ticket")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            if available > 0:
                booked += 1
                available -= 1
                print("Ticket Booked Successfully")
            else:
                print("No Tickets Available")
        case 2:
            if booked > 0:
                booked -= 1
                available += 1
                print("Ticket Cancelled Successfully")
            else:
                print("No Ticket to Cancel")
        case 3:
            print("Available Tickets:", available)
        case 4:
            print("Booked Tickets:", booked)
        case 5:
            print("Thank You")
            break
        case _:
            print("Invalid Choice")