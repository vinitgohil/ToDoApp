import modules
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do Task")
input_box  = sg.InputText(tooltip="Enter a to-do task")
add_button = sg.Button("Add")

appWindow = sg.Window("My To-do App", layout=[[label, input_box, add_button]])
appWindow.read()
appWindow.close()