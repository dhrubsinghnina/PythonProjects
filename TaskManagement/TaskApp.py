import csv

class TaskManager():
    def addtask(self):
        print("-------WELCOM TO THE TASK MANAGEMENT SYSTEM-------")
        c=-1
        with open("TaskManagement/task.csv","r",newline="") as f:
            reader=csv.reader(f)
            for rows in reader:
                print(rows)
                c+=1
        total_task=int(input("Enter how many task you want to add :"))
        for i in range(1,total_task+1):
            task_name=input(f"Enter task {i} = ")
            task_time=float(input("Enter task time:"))
            completed=False
            with open("TaskManagement/task.csv","a",newline="") as f:
                writer=csv.writer(f)
                writer.writerow([c+i,task_name,str(task_time),completed])
                
    def deletetask(self):
        task_name=input(f"Enter task to delete = ")
        new=[]
        found=False
        with open("TaskManagement/task.csv","r",newline="") as f:
            reader=csv.reader(f)
            header = next(reader)
            for row in reader:
                if row[1]!=task_name:
                    new.append(row)
                else:
                    found=True
            else:
                if found:
                    with open("TaskManagement/task.csv","w",newline="") as f:
                        writer=csv.writer(f)
                        writer.writerow(header)
                        writer.writerows(new)
                else:
                    print(f"{task_name} not found :")
    def updatetask(self):
        task_name=input(f"Enter task to update :")
        with open("TaskManagement/task.csv","r",newline="") as f:
            reader=csv.reader(f)
            rows = list(reader)
            for row in rows:
                if row[1]==task_name:
                    with open("TaskManagement/task.csv","a",newline="") as f:
                        writer=csv.writer(f)
                        print("""
                          1 for update name:
                          2 for update time:
                          3 for status of completion:""")
                    choice=int(input("Enter choice:"))
                    if choice==1:
                        name=input("Enter new task name :")
                        row[1]=name
                    elif choice==2:
                        time=float(input("Enter time :"))
                        row[2]=str(time)
                    elif choice==3:
                        status=int(input("Enter 1 for completion -1 for not :"))
                        if status==-1:
                            row[3]="False"
                        else:
                            row[3]="True"
                    else:
                        print("invalid entry:")
                    with open("TaskManagement/task.csv", "w", newline='') as f:
                        writer=csv.writer(f)
                        writer.writerows(rows)
                    break
            else:
                print(f"task {task_name} does not exit:")
    def showtask(self):
        with open("TaskManagement/task.csv","r",newline="") as f:
            reader=csv.reader(f)
            for row in reader:
                print(row)
            
                
tm=TaskManager()                
i=1
while(i!=-1):
    print("""
          1 for add task:
          2 for delete task:
          3 for update task:
          4 for show tasks:
          -1 to close:""")
    i=int(input("Enter choice:"))
    if i==1:
        tm.addtask()
    elif i==2:
        tm.deletetask()
    elif i==3:
        tm.updatetask()
    elif i==4:
        tm.showtask()
    elif i==-1:
        print("Thank you sir :")
        break
    else:
        print("Invalid entry :")
        i=int(input("Enter 1 to try again else -1:"))
else:
    print("Thank you sir :")
                      
                

        