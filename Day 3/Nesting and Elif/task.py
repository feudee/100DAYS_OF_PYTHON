print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("what is ur age"))
    if age>18:
        print("10dollar ticket")
    else:
        print("7dollar ticket")

else:
    print("Sorry you have to grow taller before you can ride.")
