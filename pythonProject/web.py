import streamlit as st
from modules import functions

def add_todo():
    todo = st.session_state['new_todo']
    todos.append(todo+"\n")
    functions.write_todos(todos)

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo: ", placeholder="Add here...", on_change=add_todo, key="new_todo")

st.session_state
