from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")  # Corrected %s to %S
print("It is", now)

while True:
    # Get user action (add, show, delete, edit, or exit)
    user_action = input("type add, show, delete, edit, or exit: ")
    user_action = user_action.strip()  # Remove any leading/trailing spaces

    # Check if user wants to add a todo
    if user_action.startswith('add'):
        todo = user_action[4:]  # Slice from index 4 to get the text after 'add'

        # Read the current list of todos from the file
        todos = get_todos()

        todos.append(todo + '\n')  # Append the new todo to the list, adding a newline

        # Write the updated list of todos back to the file
        write_todos(todos)

    # Check if user wants to show the todo list
    elif user_action.startswith('show'):
        # Read the current list of todos from the file
        todos = get_todos()

        # Loop through each todo item, strip newline characters, and print with index
        for index, item in enumerate(todos):
            item = item.strip('\n')  # Remove the newline character from each todo item
            row = f"{index + 1}-{item}"  # Create a formatted string with index and todo
            print(row)  # Print the formatted todo

    # Check if user wants to edit an existing todo
    elif user_action.startswith('edit'):
        try:  # Add error handling to catch invalid inputs
            number = int(user_action[5:])  # Extract the todo number to edit from the input
            print(number)  # Print the number for confirmation

            number = number - 1  # Adjust number to match the list index (0-based index)

            # Read the current list of todos from the file
            todos = get_todos()

            new_todo = input("Enter new todo: ")  # Prompt user for new todo text
            todos[number] = new_todo + '\n'  # Replace the old todo with the new one

            # Write the updated list of todos back to the file
            write_todos(todos)  # Here we save the edited todos

        except ValueError:  # Handle case where input isn't a valid number
            print("Your command is not valid.")
            continue  # Restart the loop to prompt for input again

    # Check if user wants to delete a todo
    elif user_action.startswith('delete'):
        try:
            # Safely extract the number of the todo to delete from the user input
            number = int(user_action.split()[1])  # Split the input and get the number
            index = number - 1  # Adjust to match the 0-based index of the list

            # Read the current list of todos from the file
            todos = get_todos()

            todo_to_delete = todos[index].strip('\n')  # Save the todo to be deleted for confirmation
            todos.pop(index)  # Remove the todo at the specified index

            # Write the updated list of todos back to the file
            write_todos(todos)  # Write remaining todos after deletion

            message = f"Todo '{todo_to_delete}' was deleted from the list."  # confirmation message
            print(message)

        except (IndexError, ValueError):  # Handle invalid input or out-of-range index
            print("Invalid input. Please enter a valid number.")
            continue  # Restart the loop to prompt for input again

    # Check if user wants to exit the program
    elif user_action.startswith('exit'):
        break  # Exit the loop and stop the program

    else:
        # If user enters an unknown command, print a message
        print("The command is not valid.")
        # case _:
        # print("Hey, you entered an unknown command")

print("bye")  # Print a goodbye message before exiting the program
