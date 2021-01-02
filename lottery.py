import random

lottery_number = (2, 34, "e", 77, "b", "c", 1, 12)
winning_x = random.sample(lottery_number, 4)
print(f"Any of these 4 numbers: {winning_x}, are prize winners!!")

my_ticket = ("e", 34, "c", 1)

for x in winning_x:
    print("Number: ", x)
    if x in my_ticket:
        print("You are a winner!!")
        break