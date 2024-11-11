import FreeSimpleGUI as sg

label1= sg.Text("Select file to compress")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose")

label2= sg.Text("Select destination folder:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose")

window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose_button1], #Il file scelto viene associato per default all'input precedente nel layout
                           [label2, input2, choose_button2]])

window.read()
window.close()

