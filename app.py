import streamlit as st
import openai
from PIL import Image, ImageDraw, ImageFont
import io

# Set up the page
st.set_page_config(page_title="Brand Name & Logo Generator", layout="centered")

# Load your API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Function to generate a brand name
def generate_brand_name(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or gpt-4o if you have access
            messages=[
                {"role": "system", "content": "You are a branding expert. Suggest 3 short, creative brand names."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=100
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {e}"

# Function to generate a basic logo image
def generate_logo_image(text):
    img = Image.new("RGB", (400, 200), color="#0a0a0a")
    draw = ImageDraw.Draw(img)

    # Use a built-in font
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        font = ImageFont.load_default()

    text_width, text_height = draw.textsize(text, font=font)
    position = ((400 - text_width) / 2, (200 - text_height) / 2)

    draw.text(position, text, font=font, fill=(255, 255, 255))
    return img

# --- Streamlit UI ---
st.title("🧠 Build Your Brand")
st.subheader("Get a unique brand name & logo instantly")

# Brand prompt
brand_description = st.text_input("Describe your brand or niche (e.g. gaming, fashion, eco-friendly skincare):")

if st.button("Generate Brand Kit") and brand_description:
    with st.spinner("Thinking of great brand ideas..."):
        names = generate_brand_name(brand_description)

    st.markdown("### 🏷️ Brand Name Ideas")
    st.write(names)

    # Generate logo using the first name only
    first_name = names.splitlines()[0].strip("-•123. ").split(" ")[0]
    logo_image = generate_logo_image(first_name)

    st.markdown("### 🖼️ Logo Example")
    st.image(logo_image, caption=f"Logo Preview for '{first_name}'", use_column_width=True)

    # Allow download
    buffer = io.BytesIO()
    logo_image.save(buffer, format="PNG")
    st.download_button("Download Logo", data=buffer.getvalue(), file_name=f"{first_name}_logo.png", mime="image/png")
