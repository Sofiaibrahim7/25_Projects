import streamlit as st

# Quiz questions and answers
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["Python", "HTML", "JavaScript", "All of the above"],
        "answer": "All of the above"
    },
    {
        "question": "Which one is a Python framework?",
        "options": ["React", "Flask", "Angular", "Vue"],
        "answer": "Flask"
    }
]

st.set_page_config(page_title="Quiz App", page_icon="🧠")
st.title("🧠 Simple Quiz App ")

# Initialize session state
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0

# Load current question
if st.session_state.question_index < len(quiz_data):
    q = quiz_data[st.session_state.question_index]
    st.subheader(f"Q{st.session_state.question_index + 1}: {q['question']}")
    user_answer = st.radio("Choose your answer:", q["options"], key=st.session_state.question_index)

    if st.button("Submit"):
        if user_answer == q["answer"]:
            st.success("✅ Correct!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Wrong! Correct answer is: {q['answer']}")

        st.session_state.question_index += 1
        st.rerun()  # ✅ Updated here
else:
    st.success(f"🎉 Quiz Finished! Your Score: {st.session_state.score}/{len(quiz_data)}")
    if st.button("Restart Quiz"):
        st.session_state.score = 0
        st.session_state.question_index = 0
        st.rerun()  # ✅ Updated here
