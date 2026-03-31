import json

FILE_NAME = "athlete_tasks.json"

def load_tasks():
    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, 'w') as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    print("\n" + "="*30)
    print("      YOUR CURRENT TASKS      ")
    print("="*30)
    
    if not tasks:
        print("No tasks found! Time to hit the gym or relax.")
        return

    for task in tasks:
        status = "[X]" if task["completed"] else "[ ]"
        print(f"ID: {task['id']} | {status} {task['title']}")
        print(f"    Category: {task['category']} | Due: {task['due_date']}")
        print("-" * 30)

def add_task(tasks):
    print("\n--- Add a New Task ---")
    new_id = 1 if len(tasks) == 0 else max(t['id'] for t in tasks) + 1
    
    title = input("What do you need to do? (e.g., Finish Calculus Prep): ")
    category = input("Category (Academic / Fitness / Nutrition): ")
    due_date = input("Due Date (YYYY-MM-DD): ")
    
    new_task = {
        "id": new_id,
        "title": title,
        "category": category,
        "due_date": due_date,
        "completed": False
    }
    
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"\nTask '{title}' added successfully!")

def complete_task(tasks):
    display_tasks(tasks)
    if not tasks:
        return
        
    try:
        task_id = int(input("\nEnter the ID of the task you finished: "))
        for task in tasks:
            if task["id"] == task_id:
                if task["completed"]:
                    print("This task is already done!")
                else:
                    task["completed"] = True
                    save_tasks(tasks)
                    print(f"\nAwesome work! '{task['title']}' is marked as complete.")
                return
        print("Hmm, I couldn't find a task with that ID.")
    except ValueError:
        print("Please enter a valid numeric ID.")

def main():
    print("\n" + "*"*40)
    print("  STUDENT-ATHLETE TASK TRACKER v1.0  ")
    print("*"*40)
    
    my_tasks = load_tasks()

    while True:
        print("\nMAIN MENU:")
        print("1. View all tasks")
        print("2. Add a new task")
        print("3. Mark a task as complete")
        print("4. Exit")
        
        choice = input("\nChoose an option (1-4): ")
        
        if choice == '1':
            display_tasks(my_tasks)
        elif choice == '2':
            add_task(my_tasks)
        elif choice == '3':
            complete_task(my_tasks)
        elif choice == '4':
            print("\nSaving your progress... Keep grinding! Goodbye.")
            break
        else:
            print("\nInvalid choice. Please pick a number from 1 to 4.")
if __name__ == "__main__":
    main()
