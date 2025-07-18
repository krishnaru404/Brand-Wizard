import streamlit as st
import random
import openai
from PIL import Image, ImageDraw, ImageFont

# Load API key from Streamlit Secrets
openai.api_key = st.secrets.get("OPENAI_API_KEY")

# Title
st.title("🎯 Brand Builder Pro")
st.caption("Create your brand identity in seconds")

# Input from user
keyword = st.text_input("🔍 Enter a keyword for your brand (e.g., fitness, tech, fashion):")

# Domain status (simulated checker)
def check_domain(name):
    return "✅ Available" if random.choice([True, False]) else "❌ Taken"

# Brand name generator
def generate_names(keyword):
    prompt = f"Suggest 5 unique and catchy brand names based on the word '{keyword}'"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8,
            max_tokens=60
        )
        result = response['choices'][0]['message']['content']
        return [name.strip("-• \n") for name in result.split("\n") if name.strip()]
    except Exception as e:
        st.error(f"Error: {e}")
        return []

# Logo image generator
def generate_logo(text):
    colors = [(255, 200, 0), (50, 150, 255), (100, 255, 100), (255, 100, 200)]
    img = Image.new("RGB", (400, 100), color=random.choice(colors))
    d = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 36)
    except:
        font = ImageFont.load_default()
    d.text((20, 30), text, fill=(0, 0, 0), font=font)
    return img

# Bio generator
def generate_bio(keyword):
    prompt = f"Write a short, modern Instagram bio for a brand about {keyword}. Under 150 characters."
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=60
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {e}"

# Weekly content calendar generator
def generate_content_ideas(keyword):
    prompt = f"Create a weekly Instagram post plan (7 days) for a brand focused on {keyword}."
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8,
            max_tokens=150
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {e}"

# Main logic
if keyword:
    st.markdown("### 🔥 Brand Name Ideas")
    names = generate_names(keyword)
    for name in names:
        st.write(f"**{name}**.com → {check_domain(name)}")

    st.markdown("### 🖼️ Logo Preview")
    if names:
        logo = generate_logo(names[0])
        st.image(logo, caption=f"Logo for {names[0]}")
        st.download_button("⬇️ Download Logo", logo.tobytes(), file_name=f"{names[0]}_logo.png")

    st.markdown("### ✍️ Instagram Bio")
    st.success(generate_bio(keyword))

    st.markdown("### 📅 Weekly Content Plan")
    st.info(generate_content_ideas(keyword))

# Footer
st.markdown("---")
st.markdown("Brand Builder Pro • All rights reserved © 2025")
