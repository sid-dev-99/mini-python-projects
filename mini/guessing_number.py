import random
print(f"welcome to mind reading game\nyou need to guess a number which was in my mind")
random_num = random.randint(1,11)
count_limit= 3
count = 0

while(count<=count_limit):
    guessing_num = int(input("enter a number: "))   
    if (guessing_num == random_num):
        print("correct answer")
        break
    else:
        print("that's not that one")
        print(f"you have {count - 2} more attempt:")
    count += 1

#the small mistake i'm making here is that not taking inside the while loop
