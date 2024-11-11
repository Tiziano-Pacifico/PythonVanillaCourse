#finito day 15
from modules import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("IT is: ", now)

print(help(functions.get_todos))
while True:

    user_actions = input("type add, show, edit, complete or exit: ")
    user_actions = user_actions.strip()

    if user_actions.startswith('add'):
        todo = user_actions[4:]

        todos = functions.get_todos()

        todos.append(todo)
        todos = [item.strip('\n') + "\n" for item in todos]

        functions.write_todos(todos)

    elif user_actions.startswith('show'):

        todos = functions.get_todos()

        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):
            row = f"{index + 1}-{item}"
            print(row)

    elif user_actions.startswith('edit'):
        try:
            number = int(user_actions[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
            todos = [item.strip('\n') + "\n" for item in todos]

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_actions.startswith('complete'):
        try:
            number = int(user_actions[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index]
            todos.pop(number - 1)

            functions.write_todos(todos)

            message = f"todo {todo_to_remove} was removed from list"
            print(message)
        except IndexError:
            print("There is no such an index")
            continue

    elif user_actions.startswith('exit'):
        break
    else:
        print("Command is not valid")
print("Bye")