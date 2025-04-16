# =============================== Python Website in 15 Minutes With Streamlit | By Muzna Amir Zubairi ===============================

import streamlit as st

def madlib(name, qualification, place, food, hobbies, skills, mentor):
    return (
        f"{name}, a brilliant individual with a degree in {qualification}, once visited the beautiful city of {place}. "
        f"During their journey, they indulged in their favorite meal {food}. "
        f"In their free time, they enjoyed {hobbies}, which helped sharpen their creative instincts. "
        f"With a strong set of skills like {skills}, {name} was determined to achieve greatness. "
        f"But they never walked the path alone they were always guided by their inspiring mentor, {mentor}, "
        f"who played a key role in shaping their journey."
    )

st.title("🚀 Craft a Fun, Personalized Story in Seconds! 🖋️")


name = st.text_input("👤 What's the name of your main character?")
qualification = st.text_input("🎓 Which academic background do they come from?")
place = st.text_input("📍 Name a place they have a special memory with:")
food = st.text_input("🍽️ What's one food they absolutely love?")
hobbies = st.text_input("🎨 What are some of their favorite hobbies?")
skills = st.text_input("💡 Mention a few standout skills they possess:")
mentor = st.text_input("🌟 Who has guided or inspired them the most?")

if st.button("✨ Generate Your Custom Madlib ✨"):
    if name and qualification and place and food and hobbies and skills and mentor:
        result = madlib(name, qualification, place, food, hobbies, skills, mentor)
        st.write("📖 **Your Personalized Story:**")
        st.success(result)
    else:
        st.error("⚠️ Please fill in **all** the fields to generate your story!")

st.markdown("<p style='text-align: right; font-size: 14px;'>❤️ Built with Streamlit by <strong>Muzna Amir Zubairi</strong> 💻</p>", unsafe_allow_html=True)
