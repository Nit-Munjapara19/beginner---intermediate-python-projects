Task = []
while True:
    print(" ==== TO-Do List ====")
    print(" 1. Add Task")
    print(" 2. Update Task")
    print(" 3. Show Task")
    print(" 4. Delete Task")
    print(" 5. Exit")

    choice=int(input("Enter your choice : "))

    if choice==1:
        add_task=input("Enter a Task : ")
        Task.append(add_task)
        print(f"Task {add_task} has been successfully added...")

    if choice==2:
        update_task=input("Which task you want to update : ")  
        if update_task in Task:
            new_task=input("Enter new Task : ")  
            index=Task.index(update_task)
            Task[index]=new_task
            print(f"Update task {new_task}")

    if choice==3:
        print(f"Total Task = {Task}")   

    if choice==4:
        delete_task=input("Which Task Do You Want To Delete : ")  
        if delete_task in Task: 
            index_delete=Task.index(delete_task) 
            del Task[index_delete]
            print("Successfully deleted")

    if choice==5:
        break       


        