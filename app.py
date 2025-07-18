
import streamlit as st
import random

# --------- Brand Name Generator ---------
prefixes = ["Go", "Quick", "Super", "Bright", "Neo", "Insta"]
suffixes = ["Hub", "Nest", "Verse", "Lab", "Nation", "Craft"]

def generate_names(keyword, count=5):
    names = []
    for _ in range(count):
        name = random.choice(prefixes) + keyword.capitalize() + random.choice(suffixes)
        names.append(name)
    return names

# --------- Domain Checker (Simple Placeholder) ---------
def check_domain(name):
    domain = f"{name.lower()}.com"
    # NOTE: This is a fake checker. For real results, use an actual domain check API.
    return "✅ Available" if random.random() > 0.5 else "❌ Taken"

# --------- Instagram Bio Generator ---------
def generate_bios(keyword):
    return [
        f"Turning {keyword} dreams into reality ✨",
        f"Your daily dose of {keyword} inspiration",
        f"Level up your {keyword} game 💼"
    ]

# --------- Weekly Content Calendar ---------
def generate_calendar(keyword):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return [f"{day}: Post something about {keyword}" for day in days]

# --------- Streamlit UI ---------
st.set_page_config(page_title="Brand Wizard", page_icon="🧠")
st.title("🧠 Brand Wizard")
st.subheader("Everything you need to build your brand — in one tool!")

keyword = st.text_input("Enter a keyword for your brand (e.g. fitness, tech, art):")

if keyword:
    # --- Brand Names ---
    st.markdown("### 🔮 Brand Name Ideas")
    names = generate_names(keyword)
    for name in names:
        st.write(f"**{name}**.com → {check_domain(name)}")

    # --- Instagram Bios ---
    st.markdown("### 📱 Instagram Bio Ideas")
    bios = generate_bios(keyword)
    for bio in bios:
        st.write(f"- {bio}")

    # --- Content Calendar ---
    st.markdown("### 📅 Weekly Content Calendar")
    calendar = generate_calendar(keyword)
    for item in calendar:
        st.write(f"- {item}")

    st.markdown("---")
    st.info("More features coming soon: Logo generator, brand kit downloads, and more!")

else:
    st.warning("👆 Start by entering a keyword above!")
