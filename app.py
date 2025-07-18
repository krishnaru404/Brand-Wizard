import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from openai import OpenAI
import io

# Load API key from secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# --- BRAND NAME GENERATOR FUNCTION ---
def generate_brand_name(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You're a branding expert. Suggest 3 short, catchy brand names."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=100
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ OpenAI Error: {str(e)}"

# --- LOGO IMAGE GENERATOR FUNCTION ---
def generate_logo_image(text):
    img = Image.new('RGB', (512, 512), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Try to use a nice font, fallback to default
    try:
        font = ImageFont.truetype("arial.ttf", 60)
    except:
        font = ImageFont.load_default()

    # Calculate text size with textbbox (Pillow ≥10)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    position = ((512 - text_width) // 2, (512 - text_height) // 2)
    draw.text(position, text, fill=(0, 0, 0), font=font)

    return img

# --- STREAMLIT UI ---
st.title("🧠 Build Your Brand")
st.subheader("Get a unique brand name & logo instantly")

user_prompt = st.text_input("Describe your brand or niche (e.g. gaming, fashion, eco-friendly skincare):")

if st.button("✨ Generate Brand"):
    if not user_prompt.strip():
        st.warning("Please enter something first.")
    else:
        with st.spinner("Generating brand name..."):
            result = generate_brand_name(user_prompt)

            st.markdown("### 🏷️ Brand Name Ideas")
            st.success(result)

            first_name = result.split('\n')[0].strip("1234567890.:- ").split()[0]

            st.markdown("### 🎨 Auto-Generated Logo")
            logo_image = generate_logo_image(first_name)
            st.image(logo_image, caption=f"Logo for '{first_name}'", use_column_width=True)

            # Optional: Download button
            img_byte_arr = io.BytesIO()
            logo_image.save(img_byte_arr, format='PNG')
            st.download_button("⬇️ Download Logo", data=img_byte_arr.getvalue(), file_name=f"{first_name}_logo.png", mime="image/png")
