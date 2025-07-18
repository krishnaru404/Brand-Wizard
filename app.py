import streamlit as st
import random

# Sample words for brand name generation
prefixes = ["Go", "Quick", "Super", "Bright", "Neo", "Insta"]
suffixes = ["Hub", "Nest", "Verse", "Lab", "Nation", "Craft"]

def generate_names(keyword, count=5):
    names = []
    for _ in range(count):
        name = random.choice(prefixes) + keyword.capitalize() + random.choice(suffixes)
        names.append(name)
    return names

st.title("🧠 Brand Wizard")
st.subheader("✨ Generate brand names + check domain availability (basic)")

keyword = st.text_input("Enter a keyword (e.g. fitness, tech, art):")

if keyword:
    st.markdown("#### 🔮 Generated Names:")
    suggestions = generate_names(keyword)
    for name in suggestions:
        st.write(f"**{name}**.com  ❌ (demo only)")
        # Later: add live domain check using an API
