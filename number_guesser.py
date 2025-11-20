import random

top_of_range = input("Enter a number:")

if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range<=0:
        print("Please enter number greater than or equal to zero.")
        quit()
else:
    print("Please Enter number not string")
    quit()
print(random.randrange(1,5))