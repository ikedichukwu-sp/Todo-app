import FreeSimpleGUI as sg

sg.theme("black")
# Conversion function
def converter(feet, inch):
    feet_to_meters = feet * 0.3048
    inch_to_meters = inch * 0.0254
    meter = feet_to_meters + inch_to_meters
    return meter


# Layout of the GUI
layout = [
    [sg.Text("Enter feet"), sg.InputText(key='-FEET-', tooltip="feet")],
    [sg.Text("Enter inch"), sg.InputText(key='-INCH-', tooltip="inch")],
    [sg.Button("Convert"), sg.Button("Exit"), sg.Text(size=(15, 1), key='-OUTPUT-')]
]

# Create the window
window = sg.Window('Converter', layout, font=('Helvetica', 20))

# Event loop to process user inputs
while True:
    event, values = window.read()

    # If user closes the window or presses "Convert"
    if event == sg.WIN_CLOSED:
        break
    if event == 'Exit':
        break

    if event == "Convert":
        try:
            # Get the inputs from the text boxes
            feet = float(values['-FEET-'])
            inch = float(values['-INCH-'])

            # Perform the conversion
            result = converter(feet, inch)

            # Output the result in the GUI
            window['-OUTPUT-'].update(f'{result:.4f} meters')
        except ValueError:
            # Handle the case where inputs are not numbers
            window['-OUTPUT-'].update('Invalid input')

# Close the window
window.close()
