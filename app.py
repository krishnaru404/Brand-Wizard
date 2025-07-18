import streamlit as st
import random
import io
from PIL import Image, ImageDraw, ImageFont
import base64

# --------- Brand Name Generator ---------
prefixes = ["Go", "Quick", "Super", "Bright", "Neo", "Insta"]
suffixes = ["Hub", "Nest", "Verse", "Lab", "Nation", "Craft"]

def generate_names(keyword, count=5):
    names = []
    for _ in range(count):
        name = random.choice(prefixes) + keyword.capitalize() + random.choice(suffixes)
        names.append(name)
    return names

# --------- Domain Checker (Simulated) ---------
def check_domain(name):
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

# --------- Logo Generator ---------
def generate_logo(text):
    img = Image.new("RGB", (400, 100), color=(random.randint(100,255), random.randint(100,255), random.randint(100,255)))
    d = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 36)
    except:
        font = ImageFont.load_default()
    d.text((10, 30), text, fill=(0, 0, 0), font=font)
    return img

# --------- Download Helper ---------
def get_image_download_link(img, filename="logo.png"):
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:file/png;base64,{img_str}" download="{filename}">📥 Download Logo</a>'
    return href

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

    # --- Logo Generator ---
    st.markdown("### 🖼️ Auto Logo Generator")
    selected_name = st.selectbox("Choose a name to generate logo:", names)
    if selected_name:
        logo = generate_logo(selected_name)
        st.image(logo, caption="Sample Logo")
        st.markdown(get_image_download_link(logo), unsafe_allow_html=True)

    st.markdown("---")
    st.success("✅ All brand essentials ready! More advanced tools coming soon.")
else:
    st.warning("👆 Start by entering a keyword above!")
