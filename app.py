import streamlit as st
from faker import Faker
import random

fake = Faker()

st.set_page_config(page_title="🧠 Build Your Brand", layout="centered")

st.title("🧠 Build Your Brand")
st.caption("Generate random brand names, bios, and taglines instantly!")

st.markdown("### 🔍 What's your niche or style?")
niche = st.text_input("e.g. gaming, skincare, fashion, productivity", "")

st.markdown("---")

if st.button("🎲 Generate Brand Kit"):
    if not niche:
        st.warning("Please enter a niche or style!")
    else:
        # 🔤 Brand Name Generator
        name_prefix = ["Zen", "Nova", "Pixel", "Eco", "Meta", "Bright", "Hyper", "Snap", "Vibe", "Neo"]
        name_suffix = ["Labs", "Wave", "Zone", "Verse", "Core", "Nest", "Hive", "World", "Net", "Gen"]
        brand_name = f"{random.choice(name_prefix)}{random.choice(name_suffix)}"

        # 💬 Bio Generator
        bios = [
            f"{niche.capitalize()} lover | Building dreams one step at a time.",
            f"Exploring the world of {niche}.",
            f"Crafting cool things in the {niche} space.",
            f"Where {niche} meets creativity ✨",
            f"Your daily dose of {niche} goodness.",
            f"{niche.capitalize()} + passion = 🚀",
            f"Creating a wave in the {niche} world 🌊",
            fake.catch_phrase(),  # bonus random bio
        ]
        brand_bio = random.choice(bios)

        # 🎯 Tagline Generator
        taglines = [
            f"{brand_name} – Your {niche} Companion.",
            f"Power up your {niche} journey with {brand_name}.",
            f"Redefining {niche}, the {brand_name} way.",
            f"{brand_name}: Think {niche}, Think Innovation.",
            f"Where {niche} meets bold design.",
            fake.bs().capitalize(),  # bonus random
        ]
        brand_tagline = random.choice(taglines)

        # 📦 Output
        st.markdown("### 🏷️ Brand Name")
        st.success(brand_name)

        st.markdown("### 🧬 Bio")
        st.info(brand_bio)

        st.markdown("### 💡 Tagline / Slogan")
        st.code(brand_tagline)

        st.markdown("---")
        st.markdown("🌀 *Click again for new ideas!*")
