# Python-Mini-Projects
# Collection of beginner-friendly Python Mini Projects to demonstrate core programming concepts, logic building, and hands-on coding practice.




def task():


    tasks = []  # Initialize an empty list to store tasks
    
    
    print("----WELCOME TO THE TASK MANAGEMENT APP----")

    total_task = int(input("Enter How Many Tasks You Want to Add = "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter Task {i} = ")
        tasks.append(task_name)
    print(f"Today's Tasks are\n{tasks}")
    
    while True:
        try:
            operation = int(input("Enter \n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop\n"))
            if operation == 1:
                add = input("Enter Task You Want to Add = ")
                tasks.append(add)
                print(f"Task '{add}' has been Successfully Added.")
            elif operation == 2:
                updated_val = input("Enter the Task Name You Want to Update = ")
                if updated_val in tasks:
                    up = input("Enter New Task = ")
                    ind = tasks.index(updated_val)
                    tasks[ind] = up
                    print(f"Updated task '{updated_val}' to '{up}'.")
                else:
                    print("Task Not Found.")
            elif operation == 3:
                del_val = input("Which Task You Want to Delete = ")
                if del_val in tasks:
                    ind = tasks.index(del_val)
                    del tasks[ind]
                    print(f"Task '{del_val}' has been Deleted.")
                else:
                    print("Task Not Found.")
            elif operation == 4:
                print(f"Total tasks = {tasks}")
            elif operation == 5:
                print("Closing the Program....")
                break
            else:
                print("Invalid Input. Please Enter a Number from 1 to 5.")
        except ValueError:
            print("Invalid Input. Please Enter a Valid Number.")

task()

