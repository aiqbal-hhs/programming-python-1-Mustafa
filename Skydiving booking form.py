print("Welcom to Skydiving, we need some information in order to book for the jump")
name = input("What is your name?")
age = int(input("How old are you?"))
if age < 15:
    print("Skydives are limited to those who are 15 years or over.")
skydive_altitude = int(input("From what hieght would you like to jump?"))
if skydive_altitude < 9000:
    print("The minimum height is 9000ft")
weight = int(input("How much do you weight?"))
if weight > 100:
    print("We are sorry but the maximum weight is 100kg")
phone_number = int(input("Your phone number"))
print("We will call you to confirm the price and the date, thank you")
