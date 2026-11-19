
print("WELCOME TO AMUSEMENT PARK!")

height = int(input("Enter your height in feet: "))

if height >= 3:
    print("YOU CAN RIDE!")

    total_bill = 0

    age = int(input("Enter your age: "))

    if age < 12:
        total_bill += 150
        print("Ticket charge: Rs.150")

    elif 12 <= age <= 18:
        total_bill += 250
        print("Ticket charge: Rs.250")

    elif age > 18:
        total_bill += 500
        print("Ticket charge: Rs.500")

    else:
        print("Invalid age")

    photo_choice = input(
        "Do you want to take photos (Yes/No)? "
    ).lower()

    if photo_choice == "yes":
        total_bill += 50
        print("Photography charge: Rs.50")

    print("--------------------------")
    print(f"Your total bill is Rs.{total_bill}")

else:
    print("Sorry, you are not eligible for the ride.")

print("THANK YOU! HAVE A GOOD DAY!")
