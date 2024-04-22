# -----------------------------------------------
# # Exercise 1.1
#
# print("Twinkle, twinkle, little star, \n"
#       "        How I wonder what you are! \n"
#       "                Up above the world so high, \n"
#       "                Like a diamond in the sky. \n"
#       "Twinkle, twinkle, little star, \n"
#       "        How I wonder what you are! \n")
# -----------------------------------------------
# # Exercise 1.2
#
# odd_even_number = int(input("Enter a whole number to check if it's an odd
# "or even number:"))
#
# if odd_even_number % 2 == 0:
#     print("Your number is even!")
# else:
#     print("Your number is odd!")
# ----------------------------------------------
# # Exercise 1.3
#
# number_1 = int(input("Enter the first number: "))
# number_2 = int(input("Enter the second number: "))
#
# result = number_1 * number_2
#
# if result > 1000:
#     print(number_1 + number_2)
# else:
#     print(result)
# -----------------------------------------------
# # Exercise 1.4
#
# user_input = int(input("Enter a number to reverse it, \n"
#                    "But remember it can only reverse a number between "
#                    "100-999!: "))
#
# final_result = 0
# temp = user_input
# while temp != 0:
#     last_digit = temp % 10
#     final_result = final_result * 10 + last_digit
#     temp = temp // 10
#
# if 1000 > final_result >= 100: print(f"Your reversed number of {
# user_input} is: {final_result}!") else: print("The value of the reversed
# number exceeds the corresponding range!\n" "Please try again!")
