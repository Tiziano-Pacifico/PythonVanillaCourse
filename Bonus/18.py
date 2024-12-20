import FreeSimpleGUI as sg
from modules.zip_extractor import extract_archive

sg.theme("Black")

label1 = sg.Text("Select archive:")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="archive")

label2 = sg.Text("Select dest dir:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")
exit_button = sg.Button("Exit")

window = sg.Window("Arcive Extractor",
                   layout=[
                       [label1, input1, choose_button1],
                       [label2, input2, choose_button2],
                       [extract_button, exit_button, output_label]
                   ])

while True:
    event, values = window.read()
    match event:
        case "Exit":
            break
    archivepath = values["archive"]
    dest_dir = values["folder"]
    extract_archive(archivepath, dest_dir)
    window['output'].update(value="Extraction completed")

window.close()

