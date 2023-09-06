from modules import utils
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do Task")

# Add an input text instance and add a key for the to-do task to add
input_box  = sg.InputText(tooltip="Enter a to-do task", key="TaskItem")
add_button = sg.Button("Add")

appWindow = sg.Window("My To-do App",
                      layout=[[label, input_box, add_button]],
                      font=('Helvetica', 12))
while True:
    task, value = appWindow.read()
    print(task)
    print(value)

    match task:
        case "Add":
            todos = utils.read_taskfile(fileName="todoapptask.txt")
            new_task = value['TaskItem'] + "\n"
            todos.append(new_task.capitalize())
            utils.write_taskfile(todos, fileName="todoapptask.txt")

        case sg.WIN_CLOSED:
            break

appWindow.close()