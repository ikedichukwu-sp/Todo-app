import FreeSimpleGUI as sg
import functions

label = sg.Text("type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
Delete_button = sg.Button("Delete")
Exit_Button = sg.Button("Exit")

window = sg.Window('My TO_Do_App', layout=[[label, input_box, add_button],
                                           [list_box, edit_button,  Delete_button],
                                           [Exit_Button]], font=('Helvetica', 20))

while True:
    event, values = window.read()

    # Handle the window close event
    if event == sg.WIN_CLOSED:
        break

    # Add new todo item
    if event == "Add":
        todos = functions.get_todos()
        new_todo = values['todo'] + "\n"
        todos.append(new_todo)
        functions.write_todos(todos)
        window['todos'].update(values=todos)  # Update the listbox with new todos

    # Edit selected todo item
    if event == "Edit":
        try:
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + "\n"
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)  # Update the listbox with new values
        except IndexError:
            sg.popup("Please select an item first")  # Handle no selection error

    # Delete selected todo item
    if event == "Delete":
        try:
            todo_to_delete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_delete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)  # Update the listbox with new values
        except IndexError:
            sg.popup("Please select an item first")  # Handle no selection error
    if event == "Exit":
        break

window.close()
