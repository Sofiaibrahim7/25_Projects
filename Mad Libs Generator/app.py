import streamlit as st
import random

st.set_page_config(page_title="Mad Libs Generator", page_icon="📖")

st.markdown("<h1 style='text-align: center; color: #F63366;'>✨ Mad Libs Generator Web App ✨</h1>", unsafe_allow_html=True)

# Define story templates
stories = [
    {
        "title": "Jungle Adventure",
        "template": "Once upon a time in a <b style='color:#FFA500;'>{place}</b>, there lived a <b style='color:#1E90FF;'>{adjective}</b> <b style='color:#8A2BE2;'>{animal}</b>. It loved to eat <b style='color:#DC143C;'>{food}</b> and play with <b style='color:#32CD32;'>{plural_noun}</b>. One day, it found a <b style='color:#FF69B4;'>{object}</b> that changed its life forever.",
        "prompts": ["place", "adjective", "animal", "food", "plural_noun", "object"]
    },
    {
        "title": "Alien Encounter",
        "template": "On planet <b style='color:#20B2AA;'>{planet}</b>, a <b style='color:#FF4500;'>{adjective}</b> alien named <b style='color:#4B0082;'>{name}</b> landed on Earth. It met a <b style='color:#008080;'>{profession}</b> and offered them a <b style='color:#FFD700;'>{object}</b>. The alien then vanished into a <b style='color:#DA70D6;'>{adjective2}</b> portal.",
        "prompts": ["planet", "adjective", "name", "profession", "object", "adjective2"]
    },
    {
        "title": "Time Travel Trouble",
        "template": "In the year <b style='color:#CD5C5C;'>{year}</b>, a <b style='color:#00CED1;'>{adjective}</b> scientist built a <b style='color:#FF8C00;'>{invention}</b>. It could take you to <b style='color:#6A5ACD;'>{place}</b> in the year <b style='color:#2E8B57;'>{past_year}</b>. But something went <b style='color:#FF6347;'>{adverb}</b> wrong...",
        "prompts": ["year", "adjective", "invention", "place", "past_year", "adverb"]
    }
]

# Story selection
story_titles = [s["title"] for s in stories]
selected_title = st.selectbox("📚 Choose a story template:", story_titles)

story = next((s for s in stories if s["title"] == selected_title), None)

# Inputs
user_inputs = {}
st.subheader("📝 Fill in the blanks:")
for prompt in story["prompts"]:
    user_inputs[prompt] = st.text_input(f"Enter a {prompt.replace('_', ' ')}:")

# Generate story
if st.button("📖 Generate Story"):
    if all(user_inputs.values()):
        final_story = story["template"].format(**user_inputs)
        st.markdown("<h3 style='color:#4CAF50;'>🎉 Here's your story:</h3>", unsafe_allow_html=True)
        st.markdown(final_story, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please fill all the blanks first.")
