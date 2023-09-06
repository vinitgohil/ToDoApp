from modules import utils
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do Task")

# Add an input text instance and add a key for the to-do task to add
input_box  = sg.InputText(tooltip="Enter a to-do task", key="TaskItem")
add_button = sg.Button("Add")

list_box = sg.Listbox(values=utils.read_taskfile(fileName="todoapptask.txt"), key='TaskITEMS',
                      enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit")

appWindow = sg.Window("My To-do App",
                      layout=[[label], [input_box, add_button], [list_box, edit_button]],
                      font=('Helvetica', 12))
while True:
    task, values = appWindow.read()
    print(1, task)
    print(2, values)
    print(3, values['TaskITEMS'])

    match task:
        case "Add":
            todos = utils.read_taskfile(fileName="todoapptask.txt")
            new_task = values['TaskItem'] + "\n"
            todos.append(new_task.capitalize())
            utils.write_taskfile(todos, fileName="todoapptask.txt")
            appWindow['TaskITEMS'].update(values=todos)

        case "Edit":
            edit_task = values['TaskITEMS'][0]
            new_task = values['TaskItem'].capitalize()

            todos = utils.read_taskfile(fileName="todoapptask.txt")
            index = todos.index(edit_task)
            todos[index] = new_task
            utils.write_taskfile(todos, fileName="todoapptask.txt")
            appWindow['TaskITEMS'].update(values=todos)

        case 'TaskITEMS':
            appWindow['TaskItem'].update(value=values['TaskITEMS'][0])

        case sg.WIN_CLOSED:
            break

appWindow.close()