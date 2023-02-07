from functions import get_todos, write_todos

while True:
    user_action = input("Type add, show, edit or exit: ").strip().lower()

    if user_action.startswith("add"):
        if len(user_action.split()) < 2:
            todo = input("Enter a todo: ") + "\n"
        else:
            todo = ' '.join(user_action.split()[1:]) + "\n"

        todos = get_todos('files/todos.txt')

        todos.append(todo)

        write_todos('files/todos.txt', todos)

    elif user_action.startswith('show'):
        todos = get_todos('files/todos.txt')

        for index, item in enumerate(todos):
            row = f"{index + 1}-{item}"
            print(row, end ='')

    elif user_action.startswith('edit'):
        number = input("Number of the todo to edit: ")
        new_todo = input("Enter new todo: ")
        todos[number-1] = new_todo
    elif user_action.startswith('complete'):
        number = int(input("Number of the todo to complete: "))

        todos = get_todos('files/todos.txt')

        todo_to_remove = todos[number - 1].strip('\n')
        todos.pop(number -1)

        write_todos('files/todos.txt', todos)

        message = f"Todo {todo_to_remove} was removed from the list"
        print(message)
    elif user_action.startswith('exit'):
        break
    else:
        print("Unknown command")

print("Bye!")
