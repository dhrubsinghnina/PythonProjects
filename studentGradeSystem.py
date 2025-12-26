import json

with open("students.json", "r") as f:
    data = json.load(f)
students=data

def add_stu(students):
    roll=input("Enter roll number to add :")
    if roll not in students:
        name=input("Enter name :")
        marks=float(input("Enter marks :"))
        students[roll]={'Name':name,'Marks':marks}
        with open("students.json", "w") as f:
            json.dump(students, f,indent=4)
    else:
        print(f"{roll} is already exist.")

def delete_stu(students):
    roll=input("Enter roll number to delete :")
    if roll in students:
        del students[roll]
        with open("students.json", "w") as f:
            json.dump(students, f,indent=4)
    else:
        print(f"{roll} does not exit.")
        
def update_stu(students):
    roll=input("Enter roll number to update marks :")
    if roll in students:
        marks=int(input("Enter new marks :"))
        students[roll]['Marks']=marks
        with open("students.json", "w") as f:
            json.dump(students, f,indent=4)
    else:
        print(f"{roll} does not exit.")
        
def showstudent(students):
    roll=input("Enter a roll number to show record :")
    if roll in students:
        print(students[roll])
    else:
        print(f"{roll} does not exit.")
        
def showall(students):
    for i in students:
        print(f"{i}:{students[i]}")
        
i=1
while(i!=-1):
    print("""Enter 
          1 for add :
          2 for delete:
          3 for update:
          4 for display 1 student:
          5 for display all :""")
    i=int(input("Enter choice:"))
    if i==1:
        add_stu(students)
    elif i==2:
        delete_stu(students)
    elif i==3:
        update_stu(students)
    elif i==4:
        showstudent(students)
    elif i==5:
        showall(students)
    else:
        print("Invalid entry:")
        i=int(input("Enter 1 to try again else -1 to end :"))
    i=int(input("Enter 1 to do again else -1 :"))
