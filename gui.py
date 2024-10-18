import FreeSimpleGUI as sg
import functions

label = sg.Text("type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
window = sg.Window('My TO_Do_App', layout=[[label, input_box, add_button], [list_box, edit_button ]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

        case "Edit":
            todo_to_edit = values[todos][0]
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case sg.WIN_CLOSED:
            break


window.close()