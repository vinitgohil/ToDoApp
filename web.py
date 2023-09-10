import streamlit as st
from modules import utils

taskList = utils.read_taskfile()

def addTask():
    task = st.session_state['newTask'] + "\n"
    taskList.append(task.capitalize())
    utils.write_taskfile(taskList)



st.title("My Todo App")
st.subheader("Web Application to add tasks to your to-do list")
st.text("This is to manage your tasks and your productivity")

for task in taskList:
    st.checkbox(task)

st.text_input(label="Enter a Task to do:", placeholder="Add task...",
              on_change=addTask, key='newTask')

print("Hello!")
st.session_state