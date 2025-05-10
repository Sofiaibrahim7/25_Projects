# Save as: todo_app.py

import streamlit as st

st.set_page_config(page_title="📝 To-Do List App", page_icon="📝")

st.title("📝 Simple To-Do List App")

# Initialize session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Add new task
new_task = st.text_input("➕ Add a new task")
if st.button("Add Task"):
    if new_task:
        st.session_state.tasks.append({"task": new_task, "done": False})
        st.success("Task added successfully!")
    else:
        st.warning("Please enter a task.")

# Display all tasks
st.subheader("📋 Your Tasks")
for i, task in enumerate(st.session_state.tasks):
    col1, col2, col3 = st.columns([0.05, 0.75, 0.2])
    with col1:
        st.session_state.tasks[i]["done"] = st.checkbox("", value=task["done"], key=i)
    with col2:
        task_text = task["task"]
        if task["done"]:
            st.markdown(f"~~{task_text}~~")
        else:
            st.write(task_text)
    with col3:
        if st.button("❌ Delete", key=f"delete_{i}"):
            st.session_state.tasks.pop(i)
            st.rerun()

# Clear all tasks
if st.button("🗑 Clear All Tasks"):
    st.session_state.tasks.clear()
    st.success("All tasks cleared!")
