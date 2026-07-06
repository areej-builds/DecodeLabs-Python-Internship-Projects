# ==========================================
# 1. FUNCTIONS (Process & Output)
# ==========================================

def add_task(my_tasks, task_id_counter, title):
    # Creating a dictionary 
    task = {
        "id": task_id_counter,
        "title": title,
        "status": "Pending"
    }
    
    # Appending the dictionary to the main list passed from main()
    my_tasks.append(task)
    print(f"\nTask '{title}' added successfully!")
    
    # Returning the updated counter value back to main()
    return task_id_counter + 1

def view_tasks(my_tasks):
    if not my_tasks:
        print("\nYour task list is empty!")
        return
        
    print("\n" + "="*45)
    print(" ID | STATUS    | TASK TITLE")
    print("="*45)
    
    for task in my_tasks:
        print(f" {task['id']:<2} | {task['status']:<9} | {task['title']}")
    
    print("="*45 + "\n")
    
def complete_task(my_tasks, task_id):
    # Searching for the task by its ID and updating status
    for task in my_tasks:
        if task["id"] == task_id:
            task["status"] = "Completed"
            print(f"\nTask ID {task_id} has been marked as Completed!")
            return
            
    print(f"\nTask with ID {task_id} not found!")

# ==========================================
# 2. MAIN LOOP (Interactive CLI Menu)
# ==========================================
def main():
    # Storing data safely inside main() instead of using global variables
    my_tasks = []
    task_id_counter = 1
    
    print("\n" + "="*40)
    print("Welcome to CLI To-Do List Application!")
    print("="*40)
    
    while True:
        print("\nOptions:")
        print("1. Add a New Task")
        print("2. View All Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            task_title = input("Enter task title: ")
            if task_title.strip(): 
                # Passing data and updating the counter with returned value
                task_id_counter = add_task(my_tasks, task_id_counter, task_title)
            else:
                print("Task title cannot be empty!")
                
        elif choice == '2':
            # Passing the local list to view function
            view_tasks(my_tasks)
            
        elif choice == '3':
            if not my_tasks:
                print("\nNo tasks available to update!")
                continue
            try:
                task_id = int(input("Enter task ID to mark as completed: "))
                # Passing the local list and ID to complete function
                complete_task(my_tasks, task_id)
            except ValueError:
                print("Invalid input! Please enter a numeric ID.")
                
        elif choice == '4':
            print("Goodbye! Happy Coding!")
            break 
            
        else:
            print("Invalid input! Please choose 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
