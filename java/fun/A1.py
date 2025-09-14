# control and / for note and to keep away from running
# variables and data types

#1. multiline strings
# print(""" hello
#        bye
#        sup
# farewell""")

# 2. multiple variables and integers 
# | have to assign type for each else wrong |
# x= 3
# y= 6.5
# z= False

# print (type(x), type(y), type(z)) 

#3. type . list 
# square bracket is used for indexing
# food = ["bread", "egg", "rice"] 
# print(food[2]) |starts with 0|
# print(type(food))
# food[2] = "banana" |replacing number 2 which is rice|
# print(food)

# 4. type . tuple
# food = ("bread", "egg", "rice")
# print(type(food))
# print(food)

# 5. type . set
# food = {"bread", "egg", "rice"} | if theres a duplicate they remove it |
# print(type(food))
# print(food)

# 6. slicing 
# | works for both list and tuple |
# | make sure range always +1 |
# | if u put -1 it will start reading from the right to the left |
# food = ("bread", "egg", "rice")
# foods = (food[0:])  | this will print out from the first to the end | 
# foods = (food[:3])   | this will print out the items in order  depending on the number  |
# foods = (food[0:3]) | this will print out until the third item |
# print(foods)

# 7. adding and removal within the list
# works with list only
# food = ["bread", "egg", "rice"]
# print(food.pop(2), food.pop(1))  | removes items from the list |
# print(food.pop(2))
# print(food.append("fish")) | adds item to the list |
# print(food.insert(1,"fish")) | adds item to the spot u have assigned ( starts with 0) |
# foodie = ["smoothie" , "shakes", "jugo"] 
# print(food.extend(foodie)) | adds another list into the main list |
# print(food)


# 8. position 
# name = "Zetra" 
# print(name[0]) | starts from 0 counts from the starting letter |
 
#  9. easy input style
#  | format the word doesnt work hence f only works |
# firstname = "Zetra"
# lastname = "Petra"
# print(f"my first name is {firstname} and my last name is {Lastname}") 
# print(id(firstname), id(lastname))
# char2 = firstname[1] = 'o' | you cant replace in a string |
# print(id(firstname))

# 10. if condition use 
# x = eval(input ("enter ur grades "))     | eval for evaluation and can input any numbers /dont have to use int or float |
# A = 75
# B = 50
# C = 25
# D = 0 

# if x >= A:
#     print("you have got an A")
# elif x > B:
#     print("you have got a B")
# elif x > C:
#     print("you have got a c")
# elif x > D:
#     print("you have got a d")
# else: 
#     print("invalid")

# 11. another example of if case with two inputs and different outputs
# import random                            | this is a part playing against random |
# AI = ("rock ", "paper" , "scissor " )    | basically making u play against a rando(AI) by giving them choices to play with | --> and fortunately lose 99%
# player2 = random.choice(AI)              | a part to make player 2 randomised |
# player1 = input("player 1 choose ur hand ")
# # player2 = input("player 2 choose ur hand ")
# if player1 == player2: 
#     print("its a tie")
# elif player1 == "paper" and player2 == "rock" or player1 == "rock" and player2 == "scissor" or player1 == "scissor" and player2 == "paper":
#     print("player 1 has won")
# else:
#     print(" player2 has won")

# 12. while loop 
# x = 0
# while x <= 50:  | until number 50 it will run |
    # print(x)
#     x= x + 1`

# 13. For loop
# foods = ("bread", "egg", "rice")
# for food in foods:  
#   print(food)  | if u write foods instead of food it will print 3 times according to the list |

# 14. range but adds 5 until it gets near to the limit 
# for x in range (0 ,30 , 5): 
#   print( " value of x =", x)
#   print("this is the end of the program") | This will print after every statement |

# 15. range
# for x in range(1, 30): 
#      print(x)


# 16. range with for loop
# confusion with variables !!!!!!
# n = int(input("how many number do u have"))
# sum  = 0
# for i in range(n):
#     x= int(input("enter a number:"))
#     sum = sum + x
# print("\n the  average of the numbers is", sum / n )  

# 17. while loop with a limit
# x = str(input("pls write something here "))
# i = 1
# while i <= 7:
#     print(x, i)
#     i = i + 1

# 18. it prints but does make sense while sum !!!
# n = int(input("write ur number mate   "),)
# i = 1
# sum  = 0
# while i <= n:
#     sum = sum + i
#     i = i + 1
#     print("sum of the first n counting numbers are ", n,"counting numbers are ", sum)

# 19. for loop with sum and range
# n = int(input("enter the value of n: "))
# odd_list = []
# sum_of_odds = 0
# for i in range (1, n+1):
#   sum_of_odds += (2 * i - 1)
#   odd_list.append(2 * i - 1)

# print ("sum of the first", n, "odd numbers is", sum_of_odds)
# print ("list of the first", n, "odd numbers is", odd_list)

# 20. range in for loop
# for x in range(2, 21, 2):
#   print (x)

# 21. multiplication table using for loop
# num = 9
# for i in range (1, 11):
#   print(num, "x", i, "=", num * i)

# 22. multiplication table using range  (nested loop)
# for i in range (1, 11):     | this will print until 10 times |
#   for j in range (1, 11 ,1):   | 1- 10 is the range and it will +1 for the next output |
#     print(i, "x", j, "=", i * j)

# 23. brain dead ................        
# color_to_fruit = {}
# for fruit in fruit_to_color:
#     color = fruit_to_color[fruit]
#     color_to_fruit[color] = fruit 
#     print ( color_to_fruit)

# 24. printing each tuple 
# tup1 = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
# tup2 = ("Apple", "Banana", "Cherry", "Dragon Fruit", "Eggplant", "Fig")
# for i in tup1:
# for o in tup2:
#     print 
# i = 1
# while i <= 1:
#     print  ( tup1 , tup2)
#     i = i + 1

# 25.
# for i in range(2):
#     user_guess = input("enter a number:")
#     print(user_guess)

# 26. brain dead: supposed to do the same work as 25th but not working ree
# assuming while function wont allow u to input further study needed
# User_guess = eval(input("enter a number:"))
# while User_guess <=2:
#     User_guess = User_guess + 1
#     print (User_guess)