from modules import utils
import time

# request for a filename for the tasks tobe added. If user selection is 'no'
# a default task file will be created.
file_input = input("Would you like to create a file? ")

if file_input.lower() == 'yes' or file_input.lower() == 'y':
    filename = input("Enter file name: ")
    filename += '.txt'
elif file_input.lower() == 'no' or file_input.lower() == 'n':
    filename = 'todos.txt'
    print("default file 'todos.txt' will be created")
else:
    pass

# Create file before you begin adding tasks.
try:
    todos = utils.create_taskfile(filename)
except FileExistsError:
    print(f"File {filename} already exists. Skipping creation of file..")

# print date time to the program when you run it
now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is {now}")

while True:

    user_action = input("Type add(a), show(sh), edit(ed), complete(c), remove(rm), deletefile(df) or exit(q) : ").strip()

    # match user_action:
    # check if user action is "add"
    if user_action.startswith('add') or user_action.startswith('a'):
        todo = user_action[2:] + '\n'
        # todo = input("Enter a todo task: ") + "\n"
        # create/open a text file to read data


        # check whether new task is entered after the add option. If task is empty
        # re-run program until a valid task is entered.

        # read file for any existing content. Call utils.utils.read_task function
        todos = utils.read_taskfile(filename)

        # add and append new task to the end of the existing tasks on file.
        todos.append(todo.capitalize())

        # Write inputs to a text file
        utils.write_taskfile(todos, fileName=filename)

        if len(todo[1:]) == 0:
            print("Please do not enter an empty task!!.")
            print("Re-run program to add valid task.")
            break
        else:
            continue

    # check if user action is "show"
    elif user_action.startswith('show') or user_action.startswith('sh'):

        todos = utils.read_taskfile(filename)

        print("Tasks to be done...", sep="\n")

        # iterate over the todos file and remove breakline at the end of every item ('\n')
        for idx, task in enumerate(todos):
            task = task.strip('\n')
            row = f"{idx+1}-{task}"
            print(row)

    # check if user action is "edit"
    elif user_action.startswith('edit') or user_action.startswith('ed'):
        try:
            print("Task to be edited...")

            for idx, task in enumerate(todos):
                task = task.strip('\n')
                print(f"{idx+1}-{task}")

            number = int(input("Which task do you want to edit? "))
            number -= 1

            # open text file to be edited with utils.utils.read_task function call
            todos = utils.read_taskfile(filename)

            try:
                new_task = input("Enter new task: ")
                todos[number] = new_task.capitalize() + '\n'
            except IndexError as e:
                print("Task number not on list. Please enter correct task number to edit.")

            # write the new edited task to file
            utils.write_taskfile(todos, fileName=filename)

        except ValueError as e:
            print("Wrong key entered!!!. Please try correct task number to edit...")
            continue


    # check if user action is "complete"
    elif user_action.startswith('complete') or user_action.startswith('c'):
        try:
            print("Task Completed")
            for idx, task in enumerate(todos):
                task = task.strip('\n')
                row = f"{idx+1}-{task}"
                print(row)

            number = int(input("Which task have you completed? "))
            number -= 1

            # open text file to be edited with utils.utils.read_task function call
            todos = utils.read_taskfile(filename)
            todos[number] = utils.strike(todos[number])

            # update and write to file for the completed task
            utils.write_taskfile(todos, fileName=filename)

            # todos.pop(number)
        except IndexError as e:
            print("Task number not on list. Please enter correct task number to complete.")
            continue

    elif user_action.startswith('remove') or user_action.startswith('rm'):
        try:
            print("Task to be removed..")
            for idx, task in enumerate(todos):
                task = task.strip('\n')
                row = f"{idx+1}-{task}"
                print(row)

            number = int(input("Which task do you want to remove? "))
            number -= 1

            # open text file to be edited with utils.utils.read_task function call
            todos = utils.read_taskfile(filename)

            # remove the numbered task from file
            todos.pop(number)

            # update and write to file for the completed task
            utils.write_taskfile(todos, fileName='todos.txt')

        except IndexError as e:
            print("Task number not on list. Please enter correct task number to remove.")
            continue

    # check if user action is to delete the task file.
    elif user_action.startswith('deletefile') or user_action.startswith('df'):
        filename = input("Enter name of task file to be deleted: ")
        filename += '.txt'

        # delete the task file from the system.
        utils.delete_taskfile(filename)

    # check if user action is to "exit" the program
    elif user_action.startswith('exit') or user_action.startswith('q'):
        break

    else:
        print("Invalid entry!!!. Please enter a valid user action..")
print("Bye Bye!!")