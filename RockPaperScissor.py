import random
choiceuser={"R":"Rock","P":"Paper","S":"Scissor"}
all={"R":0,"P":1,"S":2}
choice=["Rock","Paper","Scissor"]
li=[0,1,2]
c=0
u=0
i = 1
while(i!=-1):
        # user input
        userinput=input(f"""Enterchoice R:Rock
            P:Paper
            S:Scissor :""").upper()
        if userinput in "RPS":
            user=all[userinput]
        else:
            print("You entered invaled choice:")
            try:
                i = int(input("Enter 1 to paly again :"))
            except Exception:
                print("Invalid input")
                i = int(input("Enter 1 to paly again :"))
            continue
        # computer choice
        comp=random.choice(li)
        # all condition
        if user-comp==0:
            print(f"🫵  {choiceuser[userinput]}-🤖 {choice[comp]}= tie 🤝")
        elif user-comp==-1 or user-comp==2 :
            print(f"🫵  {choiceuser[userinput]}-🤖 {choice[comp]}= computer won 🤖")
            c+=1
        else:
            print(f"🫵  {choiceuser[userinput]}-🤖 {choice[comp]}= you won 👍")
            u+=1
        try:
            i = int(input("Enter 1 to paly again else -1:"))
        except Exception as e:
            print(e)
            i = int(input("Enter 1 to paly again else -1:"))
else:
    print("-------Overall decision-------")
    if u>c:
        print(f"you won 👍:{u} times\ncomputer won 🤖:{c} times\nOverallYou won :🥳")
    elif u<c:
        print(f"you won 👍:{u} times\ncomputer won 🤖:{c} times\nOverall Computer won :💔")
    else:
        print(f"you won 👍:{u} times\ncomputer won 🤖:{c} times\nOverall tie :🆗")
            
    print("Thank you:🙏")