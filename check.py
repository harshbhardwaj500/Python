# 1. Write a Python Program to find maximum between two numbers.
# a = int(input("Enter the number :"))
# b = int(input("Enter the number :"))
# if a>b:
#     print("A is Max")
# else:
#     print("B is max")

# 2.Write a Python Program to find maximum between three numbers.
# a = int(input("Enter number :"))
# b = int(input("Enter number :"))
# c = int(input("Enter number :"))
# if a>b and a>c:
#     print(a)
# elif b>c and b>a:
#     print(b)
# else:
#     print(c)

# 3. Write a Python Program to check whether a number is negative, positive or zero.
# num = int(input("Enter the number :"))
# if num<0:
#     print("Negative number")
# elif num>0:
#     print("Positive number")
# else:
#     print("Zero")

# 4. Write a Python Program to check whether a number is divisible by 5 and 11 or not.
# num = int(input("Enter the number :"))
# if num%5==0 and num%11==0:
#     print("Divisible")
# else:
#     print("Not Divisible")

# 5. Write a Python Program to check whether a number is even or odd.
# a = int(input("Enter the number :"))
# if a%2==0:
#     print("even number")
# else:
#     print("odd")

# 6. Write a Python Program to check whether a year is leap year or not.
# year= int(input("Enter year"))
# if (year%4==0 and year%100!=0) or (year%400==0) :
#     print("Leap Year")
# else:
#     print("Not a leap year")

# 7. Write a Python Program to check whether a character is alphabet or not.
# char = input("Enter the character :")
# if (char>='a' and char<='z') or (char>='A' and char<='Z'):
#     print("This is Alphabate")
# else:
#     print("This is Not Alphabate")

# 8. Write a Python Program to input any alphabet and check whether it is vowel or consonant.
# char = input("Enter the Alphabate :")
# if char in 'aeiouAEIOU':
#     print("Vowel")
# else:
#     print("Consonant")

# 9. Write a Python Program to input any character and check whether it is alphabet, digit or special character.
# char = input("Enter character :")
# if (char>='a' and char<='z') or (char>='A' and char<='Z'):
#     print("Alphabate")
# elif char >= 0 and char <= 9:
#     print("Digit")
# else:
#     print("special character")

# 10. Write a Python Program to check whether a character is uppercase or lowercase alphabet.
# char = input("Enter the character :")
# if char>='a' and char <='z':
#     print("lowercase alphabate")
# elif char>='A' and char<= 'Z':
#     print("UPPERCASE ALPHABATE")
# else:
#     print("Not a Alphabate")


# 11. Write a Python Program to input week number and print week day.
# a = int(input("Enter number "))
# if a == 1:
#     print("Monday")
# elif a == 2:
#     print("Tuesday")
# elif a == 3:
#     print("Wednesday")
# elif a==4:
#     print("Thrusday")
# elif a==5:
#     print("Friday")
# elif a==6:
#     print("saturday")
# elif a == 7:
#     print("Sunday")
# else:
#     print("Invalid day")

# 12. Write a Python Program to input month number and print number of days in that month.
# month = int(input("Enter the number of month :"))
# if month == 1:
#     print("January")
# elif month == 2:
#     print("February")
# elif month == 3:
#     print("March")
# elif month == 4:
#     print("April")
# elif month == 5:
#     print("May")
# elif month == 6:
#     print("June")
# elif month == 7:
#     print("July")
# elif month == 8:
#     print("August")
# elif month == 9:
#     print("September")
# elif month == 10:
#     print("October")
# elif month == 11:
#     print("November")
# elif month == 12:
#     print("December")
# else:
#     print("Invailid Number")

# 13. Write a Python Program to count total number of notes in given amount.
# amount = int(input("Enter amount :"))

# 14. Write a Python Program to input angles of a triangle and check whether triangle is valid or not.
# angle_1 = int(input("Enter number :"))
# angle_2 = int(input("Enter number :"))
# angle_3 = int(input("Enter number :"))
# if angle_1 + angle_2 + angle_3 == 180:
#     print("Valid Triangle")
# else:
#     print("Invailid Triangle")

# 15. Write a Python Program to input all sides of a triangle and check whether triangle is valid or not.
# side1 = int(input("Enter side :"))
# side2 = int(input("Enter side :"))
# side3 = int(input("Enter side :"))
# if side1+side2+side3 == 180:
#     print("Valid Triangle")
# else:
#     print("Invailid Triangle")

# 16. Write a Python Program to check whether the triangle is equilateral, isosceles or scalene triangle.
# angle_1 = int(input("Enter number :"))
# angle_2 = int(input("Enter number :"))
# angle_3 = int(input("Enter number :"))

# if angle_1 == angle_2 == angle_3:
#     print("Triangle is equilateral")    # All angles are must be equal
# elif angle_1 == angle_2 or angle_2 == angle_3 or angle_3 == angle_1:
# # elif angle_1 == angle_2 != angle_3 or angle_2 == angle_3 != angle_1 or angle_3 == angle_1 != angle_2:
#     print("Triangle is isosceles")      # Two angles are must be equal and another one must be different
# else:
#     print("Triangle is scalene")         # All angles are must be different

# 17. Write a Python Program to find all roots of a quadratic equation.


# 18. Write a Python Program to calculate profit or loss.
# sell_cost = int(input("Enter selling amount :"))
# purchase_cost = int(input("Enter purchasing cost :"))
# calculation = sell_cost - purchase_cost
# if sell_cost>purchase_cost:
#     print("Profit")
# else:
#     print("Loss")

# Write a Python program to check if a number is a multiple of 3 and 5.
num = int(input("Enter the number :"))
# if num%3==0 and num%5==0:
#     print("Divisible")
# else:
#     print("Not Divisible")

# via function
# def check_multiple_of_3_and_5(number):
#     if number % 3 == 0 and number % 5 == 0:
#         return True
#     else:
#         return False

# num = int(input("Enter a number: "))

# if check_multiple_of_3_and_5(num):
#     print(f"{num} is a multiple of both 3 and 5.")
# else:
#     print(f"{num} is not a multiple of both 3 and 5.")



# Write a Python program to check if a number is a prime number.

# Write a Python program to check if a person is eligible for a driver's license (assuming the minimum age is 16).
# age = int(input("Enter the age :"))
# if age >= 16:
#     print('Eligible')
# else:
#     print('Not Eligible')

# . Write a Python program to check if a triangle is valid (assuming the sum of any two sides must be greater than the third side).

# . Write a Python program to check if a number is a perfect square.


# take 3 age of a person and find out the oldest one
# age1 = int(input("Enter the age ;"))
# age2= int(input("Enter the age ;"))
# age3 = int(input("Enter the age ;"))
# if age1>age2 and age1 > age3:
#     print(age1)
# elif age2>age3 and age2> age1:
#     print(age2)
# else:
#     print(age3)

# ang1= int(input("Enter the value"))
# ang2= int(input("Enter the value"))
# ang3= int(input("Enter the value"))

# if ang1+ang2+ang3 == 180 and (ang1>0 or ang2>0 or ang3>0 ):
#     print("Triangle")
# else:
#     print("Not a triangle")

# leap_year= int(input("Enter year"))
# if (leap_year%4==0 and leap_year%100!=0) or (leap_year%400==0) :
#     print("Leap Year")
# else:
#     print("Not a leap year")


# a = int(input("Enter number :"))
# b = int(input("Enter number :"))
# c = int(input("Enter number :"))
# if a == b == c:
#     print("Triangle is equilateral")
# elif a==b!=c or b==c!=a or c==a!=b:
#      print("Triangle is isosceles")
# else:
#     print("Triangle is scalene")

# unit = 80
# 50 = 1
# 100 = 2
# 200 = 10
# 200 > 15
# if unit<= 50:
#     unit= unit*1
# elif  unit <= 150:
#     unit = 50 +(unit - 50)*2
# elif unit>150 and unit<=250:
#     unit = 100+(unit - 150)*10
# else:
#     unit = unit*15

