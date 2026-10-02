import random

guess=random.randint(1, 100)
a=-1
s=0
while a!=guess:
    try :
        s+=1
        a=int(input("Enter the guess:"))
        if a==guess:
            print(f"\nHOORAYY! The correct num is {guess}")
            print(f"You Took {s} tries")
            if s<=5:
                print("HARD")
            elif s>=5:
                print("MEDIUM")
            elif s>=10:
                print("EASY")
        elif a>guess:
            print("Too High")
        elif a<guess:
            print("Too Low")
    except :
        print("Invalid Input")