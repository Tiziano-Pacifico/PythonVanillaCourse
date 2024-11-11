import FreeSimpleGUI as sg

input1 = sg.Input()
label1 = sg.Text("Enter feet")

input2 = sg.Input()
label2 = sg.Text("Enter inches")

button_convert = sg.Button("Convert")

window = sg.Window("Convertor", layout=[[label1, input1], [label2, input2], [button_convert]])

window.read()
window.close()
