import random
x=random.randint(1,101)
guessee=0
i=int(input("Enter 1 if you want to play :"))
while(i==1):
    n=int(input("Guess the number :"))
    guessee+=1
    if(x==n):
        print(f"You guess correct number this time :{x}")
        break
    elif(x>n):
        print(f"guess higher number than {n} :")
    else:
        print(f"guess lower number than {n} :")

print(f"The number of guess needed :{guessee}")