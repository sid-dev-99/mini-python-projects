# Guess The Number Game(3 attempts):-
# computer has a magic number
# In this game you have to guess that magic number
# which is a single digit num b/w 1-10,



import random
print(f"welcome to mind reading game\nyou need to guess a number which was in my mind")
random_num = random.randint(1,11)
count_limit= 3
count = 1

while(count<=count_limit):
    guessing_num = int(input("enter a number: "))   
    if (guessing_num == random_num):
        print("correct answer")
        break
    else:
        print("that's not that one")
        print(f"you have {count-3} more attempt:")
    count += 1
    if(count==4) :
        print("oops! you tried, but no luck")

<<<<<<< HEAD
#the small mistake i'm making here is that not taking input inside the while loop
=======
>>>>>>> d60f4e9 (guessing_number.py)
