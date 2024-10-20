import FreeSimpleGUI as sg
from zip_file_extractor import extract_archive
sg.theme("Black")

label1 = sg.Text("Select archive: ")
input1 = sg.Input()
choose_Button1 = sg.FileBrowse("Choose", key="archive")

label2 = sg.Text("Select destination directory: ")
input2 = sg.Input()
choose_Button2 = sg.FolderBrowse("Choose", key="folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")

window = sg.Window("Zip Extractor", layout=[[label1, input1, choose_Button1],
                                            [label2, input2, choose_Button2],
                                            [extract_button, output_label]])

while True:
    event, values = window.read()
    archivepath = values["archive"]
    dest_dir = values["folder"]
    print(event, values)
    extract_archive(archivepath, dest_dir)
    window["output"].update(value="Extraction completed")
window.read()
window.close()
