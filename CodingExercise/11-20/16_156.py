import FreeSimpleGUI as sg

input1 = sg.Input(key="feet")
label1 = sg.Text("Enter feet")

input2 = sg.Input(key="inches")
label2 = sg.Text("Enter inches")

button_convert = sg.Button("Convert")
output = sg.Text(key = "output")

window = sg.Window("Convertor", layout=[[label1, input1], [label2, input2], [button_convert, output]])
while True:
    event, values = window.read()
    match event:
        case sg.WIN_CLOSED:
            break
    feet = int(values['feet'])
    inches = int(values['inches'])
    result = feet * inches
    window['output'].update(value=result)
window.close()
