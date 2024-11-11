from modules import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
#add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=[45,10])
#edit_button = sg.Button("Edit")

button_labels = ["Add","Edit"]
input_box_list = [input_box, list_box]
layout = [[label]]
for index, bl in enumerate(button_labels):
    layout.append([input_box_list[index], sg.Button(bl)])


window = sg.Window('My TODO app',
                   layout=layout,
                   font=('Helvetica',20))
while True:
    event, values = window.read()
    print(event, values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] +"\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + "\n"

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break


window.close()

