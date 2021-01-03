#Band-Name-Generator
#1. Create a greeting for your program.
print("Welcome to the Band Name Generator.")
user_name = input("What is your name?\n")

#2. Ask the user for the city that they grew up in.
print("Hello, " + user_name)
user_city = input("Which city did you grow up in?\n")

#3. Ask the user for the name of a pet.
user_pet_name = input("What was the name of your pet?\n")

#4. Combine the name of their city and pet and show them their band name.
band_name = user_city + " " + user_pet_name
print(user_name + ", your band name could be" + " " + band_name)
