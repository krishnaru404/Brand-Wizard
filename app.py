import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io
import random

st.set_page_config(page_title="Brand Wizard", page_icon="🧠")
st.title("🧠 Build Your Brand")
st.write("Get your unique brand name, logo, bio, and more instantly!")

# --- User Input ---
prompt = st.text_input("📌 Describe your brand or niche (e.g. gaming, fashion, skincare):", "")

# --- Helpers ---
def generate_brand_names(prompt):
    prompt = prompt.lower()
    if "game" in prompt:
        return ["PixelRush", "GameNova", "ShadowCore"]
    elif "fashion" in prompt:
        return ["StyleHive", "ModaMuse", "Trendora"]
    elif "tech" in prompt:
        return ["TechNest", "VoltEdge", "NexaBit"]
    elif "mobile" in prompt:
        return ["Mobify", "PocketNova", "QuickCell"]
    else:
        return ["Brandly", "EchoCraft", "NamoZen"]

def generate_logo_image(text):
    img = Image.new("RGB", (500, 300), color=random.choice(["#1E1E1E", "#111827", "#202124"]))
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 60)
    except:
        font = ImageFont.load_default()
    color = random.choice(["#00FFB7", "#FFD700", "#FF6F61", "#00D1FF", "#90EE90"])
    draw.text((50, 120), text, fill=color, font=font)
    return img

def generate_bio(prompt, brand_name):
    return f"{brand_name} is a modern brand inspired by {prompt}. Built to stand out, connect emotionally, and grow fast."

def generate_colors():
    return random.sample(["#FF6F61", "#6B5B95", "#88B04B", "#F7CAC9", "#92A8D1", "#955251", "#B565A7", "#009B77"], 3)

def generate_handles(brand_name):
    username = brand_name.lower()
    return {
        "Instagram": f"@{username}_official",
        "Twitter": f"@{username}_hq",
        "YouTube": f"{username}tv"
    }

# --- Main Action ---
if st.button("🚀 Generate"):
    if prompt.strip() == "":
        st.warning("Please describe your brand first.")
    else:
        st.subheader("🏷️ Brand Name Ideas")
        names = generate_brand_names(prompt)
        st.write("\n".join([f"{i+1}. {name}" for i, name in enumerate(names)]))

        # First name used for logo + other sections
        selected_name = names[0]

        # --- Logo ---
        st.subheader("🎨 Auto-Generated Logo")
        logo = generate_logo_image(selected_name)
        st.image(logo, caption=f"Logo for '{selected_name}'", use_container_width=True)

        # Download Button
        buf = io.BytesIO()
        logo.save(buf, format="PNG")
        st.download_button("📥 Download Logo", buf.getvalue(), file_name=f"{selected_name}_logo.png", mime="image/png")

        # --- Bio ---
        st.subheader("📝 Brand Bio")
        st.success(generate_bio(prompt, selected_name))

        # --- Color Palette ---
        st.subheader("🌈 Brand Colors")
        colors = generate_colors()
        cols = st.columns(3)
        for i, c in enumerate(colors):
            with cols[i]:
                st.color_picker(f"Color {i+1}", c, label_visibility="collapsed")

        # --- Social Media Handle Ideas ---
        st.subheader("📱 Social Media Handles")
        handles = generate_handles(selected_name)
        for platform, handle in handles.items():
            st.write(f"**{platform}:** {handle}")
