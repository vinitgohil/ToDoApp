from modules import utils
import PySimpleGUI as sg
import time
import os

FILENAME = "todotasks.txt"

if not os.path.exists("todotasks.txt"):
    utils.create_taskfile(fileName=FILENAME)
    pass

# Apply GUI Theme
# sg.theme("SystemDefault")


# Define labels
timeLabel = sg.Text("", key="clock")
label = sg.Text("Type in a To-Do Task")

# Add an input text instance and add a key for the to-do task to add
input_box  = sg.InputText(tooltip="Enter a to-do task", key="TaskItem")
create_file_box = sg.InputText("Create a TaskFile: ", key="FILENAME")

create_file_button = sg.Button("Create File")
add_button = sg.Button("Add")



list_box = sg.Listbox(values=utils.read_taskfile(fileName=FILENAME), key='TaskITEMS',
                      enable_events=True, size=[45, 20])

edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

appWindow = sg.Window("My To-do App",
                      layout=[[timeLabel],
                              [label],
                              [input_box, add_button],
                              [list_box, edit_button, complete_button],
                              [exit_button]],
                      font=('Helvetica', 12))


while True:
    task, values = appWindow.read(timeout=200)
    appWindow['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    # print(1, task)
    # print(2, values)
    # print(3, values['TaskITEMS'])

    match task:
        case "Add":
            todos = utils.read_taskfile(fileName=FILENAME)
            new_task = values['TaskItem'] + "\n"
            todos.append(new_task.capitalize())
            utils.write_taskfile(todos, fileName=FILENAME)
            appWindow['TaskITEMS'].update(values=todos)
            appWindow['TaskItem'].update(value='')

        case "Edit":
            try:
                edit_task = values['TaskITEMS'][0]
                new_task = values['TaskItem'].capitalize()

                todos = utils.read_taskfile(fileName=FILENAME)
                index = todos.index(edit_task)
                todos[index] = new_task
                utils.write_taskfile(todos, fileName=FILENAME)
                appWindow['TaskITEMS'].update(values=todos)
            except IndexError as e:
                sg.Popup("Please select an Item for edit", font=('Helvetica', 12))

        case "Complete":
            try:
                complete_task = values['TaskITEMS'][0]
                todos = utils.read_taskfile(fileName=FILENAME)
                todos.remove(complete_task)
                utils.write_taskfile(todos, fileName=FILENAME)
                appWindow['TaskITEMS'].update(values=todos)
                appWindow['TaskItem'].update(value="")
            except IndexError as e:
                sg.Popup("Please select an Item to complete", font=('Helvetica', 12))

        case "Exit":
            break

        case 'TaskITEMS':
            appWindow['TaskItem'].update(value=values['TaskITEMS'][0])

        case sg.WIN_CLOSED:
            break

appWindow.close()