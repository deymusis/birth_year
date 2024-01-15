# This program will guess the year of your birth.

print("I’ll guess what year you were born.")
year_str = input("What year is it?\n")
year_num = int(year_str)
age_str = input("Enter your full age: ")
age_num = int(age_str)
b = year_num-age_num
c = b-1
d = b+1
print("You were born somewhere between", c, "and", d)