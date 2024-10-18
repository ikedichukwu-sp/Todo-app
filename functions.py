def get_todos(filepath="projec.txt"):  # custom function to read todos from a file
    """ read a text and return the list of
    to_to items"""
    with open(filepath, 'r') as file_local:  # using 'with' to ensure the file is closed after reading
        todos_local = file_local.readlines()  # read all lines from the file and return as a list
    return todos_local





def write_todos(todos_arg, filepath="projec.txt"):  # function to write todos to a file
    """ write the to-do items list in the text file"""
    with open(filepath, 'w') as file:  # using 'with' to ensure the file is closed after writing
        file.writelines(todos_arg)  # writing the list of todos to the file