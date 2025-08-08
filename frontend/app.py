import streamlit as st
import requests
import pandas as pd

base_url = "http://127.0.0.1:5000/"

st.title("Task Manager", width="stretch")

action = st.selectbox(
    "Select an Option from below drop down",
    ("View Tasks", "Add Task", "Update Task", "Delete Task"),
)

if action == "View Tasks":
    response = requests.get(base_url + "tasks")
    if response.status_code == 200:
        tasks = response.json()
        if tasks:
            df = pd.DataFrame(tasks)
            # df = df[["id", "title", "description", "status"]]
            st.dataframe(df)
        else:
            st.warning(body= "NO Task Available", icon="🚨")
    else:
        st.warning(body= "NO Response From Backend Server Available", icon="🚨")

elif action == "Add Task":
    st.header("Add New Task")
    title = st.text_input("Enter Task Title")
    desc = st.text_input("Enter Task Description")
    status = st.text_input("Enter Task Status")
    button = st.button("Add Task")

    if button:
        payload = {
            "title" : title,
            "description" : desc,
            "status" : status
        }
        response = requests.post(base_url + "tasks", json=payload)
        if response.status_code == 200:
            tasks = response.content
            if tasks:
                st.success(tasks)
            else:
                st.warning(body= "NO Task Available", icon="🚨")
        else:
            st.warning(body= "NO Response From Backend Server Available", icon="🚨")

elif action == "Update Task":
    st.header("Update Task")
    id_ = st.text_input("Enter Task ID")
    desc = st.text_input("Enter Task Description")
    status = st.text_input("Enter Task Status")
    button = st.button("Update Task")

    if button:
        payload = {
            "id" : id_,
            "description" : desc,
            "status" : status
        }
        response = requests.put(base_url + "update/tasks", json=payload)
        if response.status_code == 200:
            tasks = response.json()
            if tasks:
                df = pd.DataFrame(tasks)
                st.success("Task Updated Successfully")
                st.dataframe(df)
            else:
                st.warning(body= "NO Task Available", icon="🚨")
        else:
            st.warning(body= "NO Response From Backend Server Available", icon="🚨")

elif action == "Delete Task":
    st.subheader("Delete Task")
    id_ = st.text_input("Enter Task ID")
    button = st.button("Delete Task")

    if button:
        print(base_url + "tasks/" + id_)
        response = requests.delete(base_url + "tasks/" + str(id_))
        if response.status_code == 200:
            tasks = response.content
            if tasks:
                st.success(tasks)
            else:
                st.warning(body= "NO Task Available", icon="🚨")
        else:
            st.warning(body= "NO Response From Backend Server Available", icon="🚨")
