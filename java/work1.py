# options = [1, 2, 3, 4, 5, 6, 7, 8]

# # Loop through the list in reverse order to avoid skipping elements
# for i in range(len(options) - 1, -1, -1):  # Reverse iteration
#     if options[i] % 2 == 0:  # Defined condition: Remove even numbers
#         del options[i]

# print(options)  # Output will be [1, 3, 5, 7]

# import random
# options = [
#     {"id": 1, "name": "Maaish"},
#     {"id": 2, "name": "Shidhaadh"},
#     {"id": 3, "name": "Meesam"},
# ]
# for option in options:
#     option["id"] = random.randint  



# User = random.choice(options)
# # Accessing an option by ID
# for option in options:
#     if option["id"] == 1:
#         print(option["name"])  # Output: Option 2
# # for option in options:
# #     if option["id"] == 1:
# #         print(option["name"])  # Output: Option 2
# # for option in options:
# #     if option["id"] == 3:
# #         print(option["name"])  # Output: Option 2

# # Updating an option by ID
# for option in options:
#     if option["id"] == 2:
#         option["name"] = "what is ur hobby"
#         print(option["name"])  # Output: Updated Option 2
#         for option in options:
#     if option["id"] == 1:
#         option["name"] = "what is ur hobby"
#         print(option["name"])  # Output: Updated Option 2

# for i in range(len(options) - 1, -1, -1):  # Reverse iteration
#     if options[i]["id"] == 1:  
#         del options[i]
#         break
#         print(options)



# import random
# options_1 = [
#     {"id": 1, "name": "Maaish"},
#     {"id": 2, "name": "Shidhaadh"},
#     {"id": 3, "name": "Meesam"}
# ]
# options_2 = [
#     {"id": 10, "name": "what is your favorite hobby"},
#     {"id": 5, "name": "what did you have for lunch"},
#     {"id": 6, "name": "what do you like about the class"}
# ]

# while options_1 and options_2:
#     selected_option_1 = random.choice(options_1)
#     selected_option_2 = random.choice(options_2)

#     options_1.remove(selected_option_1)
#     options_2.remove(selected_option_2)


#     print(f"Selected: {selected_option_1['name']} {selected_option_2['name']}")


# below 10 is the number / u have to guess it / how do u get it the fastest

x = int(input(""))
y= 8
if x =>4:
    print("above the integer limt")