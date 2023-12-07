todo_list = []
add_task = lambda task: todo_list.append(task)
view_tasks = lambda: [print(f"{i + 1}. {task}") for i, task in enumerate(todo_list)] if todo_list else print("No tasks in the list.")
complete_task = lambda index: todo_list.pop(index - 1) if 1 <= index <= len(todo_list) else print("Invalid index.")
delete_task = lambda index: todo_list.pop(index - 1) if 1 <= index <= len(todo_list) else print("Invalid index.")
while True:
    print("\nMain Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        task = input("Enter a task: ")
        add_task(task)
        print("Task added to the list.")
    elif choice == '2':
        task=view_tasks()
        if task:
            print("todo_list")
            for i, task in enumerate(tasks, 1):    
              print(f"{i}.{task}")
        else:
            print("Your list is empty")
    elif choice == '3':
        if not todo_list:
            print("No task to complete")
        else:
           index = int(input("Enter the index of the task to complete: "))
           complete_task(index)
           print("Task completed.")
    elif choice == '4':
        index = int(input("Enter the index of the task to delete: "))
        delete_task(index)
        print("Task deleted.")
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")