from modules import functions
import FreeSimpleGUI as sg
import time

sg.theme("LightGreen1")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
list_box = sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=[45,10])

button_labels = ["Add","Edit"]
input_box_list = [input_box, list_box]
layout = [[clock],[label]]
for index, bl in enumerate(button_labels):
    layout.append([input_box_list[index], sg.Button(bl)])
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

layout.append([complete_button, exit_button])

window = sg.Window('My TODO app',
                   layout=layout,
                   font=('Helvetica',20))
while True:
    event, values = window.read(timeout=10)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] +"\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))
        case 'Complete':
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break


window.close()

