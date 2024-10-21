import streamlit as st

import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"]  # "new_todo" is a key for the text_input below
    if todo:  # Only add non-empty todos
        todos.append(todo + "\n")  # Append the new to-do
        functions.write_todos(todos)  # Write updated to-dos back to the file
        st.session_state["new_todo"] = ""  # Clear input after adding


st.title("My To-Do App")
st.subheader("This is my to-do app")
st.write("This app gives me joy as a new programmer")

# Loop through todos and assign a unique key to each checkbox using index
for index, todo in enumerate(todos):
    st.checkbox(todo, key=f'todo_{index}')

# Input for adding new todos with a button
st.text_input(label="", placeholder="Add a new todo", key='new_todo', on_change=add_todo)

st.session_state  # For debugging purposes (you can remove this later)
