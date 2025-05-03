import streamlit as st
import random

# Page config
st.set_page_config(page_title="Guess The Number!", page_icon="🎯", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #fceae8, #f8d3c7);
        color: #4b2c2c;
        font-family: 'Segoe UI', sans-serif;
    }

    .title-style {
        font-size: 36px;
        font-weight: bold;
        color: #b76e79;  /* Rose Gold text */
        text-align: center;
        margin-top: 20px;
        text-shadow: 1px 1px 2px #f5c6c6;
    }

    .subtitle-style {
        font-size: 20px;
        color: #7a4e4e;
        text-align: center;
        margin-bottom: 30px;
    }

    .stButton>button {
        background-color: #e8b4b8;
        color: white;
        border-radius: 10px;
        padding: 10px 25px;
        font-weight: bold;
        border: 1px solid #d291bc;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .stButton>button:hover {
        background-color: #d291bc;
        color: #fff;
    }

    .stNumberInput>div>input {
        background-color: #fff5f7;
        color: #4b2c2c;
        border: 1px solid #f4c2c2;
        border-radius: 6px;
    }

    </style>
""", unsafe_allow_html=True)


st.markdown('<p class="title-style">🎯 Number Guessing Game</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-style">Try to guess the number I have in mind!</p>', unsafe_allow_html=True)

# Initialize session state
if "secret_number" not in st.session_state:
    st.session_state.secret_number = None
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "max_attempts" not in st.session_state:
    st.session_state.max_attempts = 0
if "game_started" not in st.session_state:
    st.session_state.game_started = False
if "upper_limit" not in st.session_state:
    st.session_state.upper_limit = 0

# Step 1: Choose difficulty
if not st.session_state.game_started:
    difficulty = st.selectbox("Choose Difficulty", ["Easy (1-10)", "Medium (1-50)", "Hard (1-100)"])

    if difficulty == "Easy (1-10)":
        st.session_state.upper_limit = 10
    elif difficulty == "Medium (1-50)":
        st.session_state.upper_limit = 50
    else:
        st.session_state.upper_limit = 100

    if st.button("Start Game"):
        st.session_state.secret_number = random.randint(1, st.session_state.upper_limit)
        st.session_state.max_attempts = max(3, st.session_state.upper_limit // 10 + 2)
        st.session_state.attempts = 0
        st.session_state.game_started = True
        st.success("Game started! Make your first guess.")

# Step 2: Game in progress
if st.session_state.game_started:
    st.info(f"Guess a number between **1** and **{st.session_state.upper_limit}**")
    guess = st.number_input("Enter your guess:", min_value=1, max_value=st.session_state.upper_limit, step=1)

    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        if guess == st.session_state.secret_number:
            st.balloons()
            st.success(f"✅ Correct! You guessed it in {st.session_state.attempts} tries. 🎉")
            st.session_state.game_started = False
        elif guess < st.session_state.secret_number:
            st.warning("🔺 Too low! Try a higher number.")
        else:
            st.warning("🔻 Too high! Try a lower number.")

        if st.session_state.attempts >= st.session_state.max_attempts and st.session_state.game_started:
            st.error(f"❌ You're out of attempts! The correct number was {st.session_state.secret_number}.")
            st.session_state.game_started = False

    if st.button("Restart Game"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.experimental_rerun()
