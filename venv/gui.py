import FreeSimpleGUI as sg
from bonus_samples import functions

label = sg.Text("type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window('My TO_Do_App', layout=[[label, input_box, add_button]])
window.read()
print("hello")
window.close()