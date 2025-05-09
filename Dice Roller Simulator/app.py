import streamlit as st
import random
import time

# Set Streamlit page title and icon
st.set_page_config(page_title="🎲 Dice Roller Simulator", page_icon="🎲")

# App title and instruction
st.title("🎲 Dice Roller Simulator")
st.write("Click the button below to roll the dice!")

# Dice images mapped with numbers
dice_images = {
    1: "dice1.png",
    2: "dice2.png",
    3: "dice3.png",
    4: "dice4.png",
    5: "dice5.png",
    6: "dice6.png"
}

# Roll dice button logic
if st.button("Roll Dice 🎯"):
    with st.spinner("Rolling..."):
        time.sleep(1)
        dice_number = random.randint(1, 6)
        st.image(dice_images[dice_number], caption=f"You rolled a {dice_number}!", width=200)
else:
    # Default dice face shown before rolling
    st.image("dice1.png", caption="Ready to roll!", width=200)
    
