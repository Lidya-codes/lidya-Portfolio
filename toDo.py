tasks=[]

def addTask():
    task=input("please enter a task:   ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def deleteTask():
    if tasks:
        displayTask()
        try:
            task_number = int(input("Enter the task number to delete: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Task '{removed_task}' has been deleted.")
            else:
                print("Invalid task number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No tasks to delete.")

def displayTask():
    if tasks:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("\nNo tasks to display!")


def options():
        print("\nChoose an option of action\n")
        print("1. Add task")
        print("2. Delete task")
        print("3. Display tasks")
        print("4. Quit")
def main():
    print("WELCOME!")
    print("this is the to-do list app")

    while True:
        options()
        try:
            option = int(input("Enter your choice: "))
            match option:
                case 1:
                    addTask()
                
                case 2:
                    deleteTask()
                
                case 3:
                    displayTask()
                
                case 4:
                    print("Goodbye!")
                    break
                
                case _:
                    print("Choose from the available options.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            

if __name__ == "__main__":
    main()