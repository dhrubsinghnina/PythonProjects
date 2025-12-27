import csv
# class for all empoyee record management:
class Employee():
    def __init__(self) -> None:
        pass
    # add employee:
    def addemp(self):
        id=int(input("Enter id :"))
        with open("employee.csv","r",newline='') as f:
            reader=csv.reader(f)
            next(reader) # skip the head
            for row in reader:
                if row[0]==str(id):
                    print(f"The Id {id} already exists:")
                    break
            else:
                name=input("Enter name :")
                dept=input("Enter department :")
                salary=int(input("Enter salary :"))
                with open("employee.csv","a",newline='') as f:
                    writer=csv.writer(f)
                    writer.writerow([id,name,dept,salary])
    # delete employee: 
    def deleteemp(self):
        id=int(input("Enter id to delete :"))
        temp_rows = []
        found=False
        with open("employee.csv", "r", newline='') as f:
            reader = csv.reader(f)
            header = next(reader)          # read header
            temp_rows.append(header)
            for row in reader:
                if row[0]==str(id):
                    found=True
                else:
                    temp_rows.append(row)
            else:
                if found:
                    with open("employee.csv", "w", newline='') as f:
                        writer = csv.writer(f)
                        writer.writerows(temp_rows)
                    print("Employee deleted successfully")
                else:
                    print(f"Id {id} does not exis:")
    # updating file: 
    def updateemp(self):
        id=int(input("Enter id to update:"))
        with open("employee.csv", "r", newline='') as f:
            reader = csv.reader(f)
            header = next(reader)
            rows = list(reader)
            for row in rows:
                if row[0] == str(id):
                    print("""
                          1 for update name:
                          2 for update dept:
                          3 for salary:""")
                    choice=int(input("Enter choice:"))
                    if choice==1:
                        name=input("Enter employee name :")
                        row[1]=name
                    elif choice==2:
                        dept=input("Enter depatment name :")
                        row[2]=dept
                    elif choice==3:
                        salary=(input("Enter salary:"))
                        row[3]=salary
                    else:
                        print("invalid entry:")
                    with open("employee.csv", "w", newline='') as f:
                        writer=csv.writer(f)
                        writer.writerow(header)
                        writer.writerows(rows)
                    break
            else:
                print(f"Id {id} does not exit:")
    # showing 1 employee records:
    def showemp(self):
        id=int(input("Enter id to show record:"))
        with open("employee.csv", "r", newline='') as f:
            reader=csv.reader(f)
            next(reader)
            for row in reader:
                if row[0]==str(id):
                    print(row)
                    break
            else:
                print(f"Id {id} does not exit :")
    # showing all records:
    def showall(self):
        with open("employee.csv", "r", newline='') as f:
            reader=csv.reader(f)
            for row in reader:
                print(row)
# making object:
emp=Employee()
# file manupulation:   
i=1
while(i!=-1):
    print("""
          1 for add employee:
          2 for delete employee:
          3 for update employee:
          4 for show 1 employee record:
          5 for showall:""")
    i=int(input("Enter choice:"))
    if i==1:
        emp.addemp()
    elif i==2:
        emp.deleteemp()
    elif i==3:
        emp.updateemp()
    elif i==4:
        emp.showemp()
    elif i==5:
        emp.showall()
    else:
        print("Invalid entry :")
        i=int(input("Enter 1 to try again else -1:"))
else:
    print("Thank you sir :")
        