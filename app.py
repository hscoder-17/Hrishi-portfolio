import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Hrishi's Portfolio",
    page_icon="👋",
    layout="wide"
)

# 2. Sidebar Navigation & Interactive Controls
with st.sidebar:
    st.title("Hrishi's Space")
    st.write("Welcome to my personal site!")
    
    st.write("---")
    st.subheader("⚙️ Quick Tools")
    
    st.info("💡 **Pro Tip:** Toggle light/dark mode using the 3 dots in the top-right corner of Streamlit!")
    
    st.subheader("⭐ Feedback")
    rating = st.slider("Rate my site:", 1, 5, 5)
    if st.button("Submit Rating"):
        st.toast(f"Thanks for rating {rating}/5 stars! 🎉")

# 3. Custom CSS Styling
st.markdown("""
<style>

.stApp {
    background-color: #f3f4f6;
}

.card {
    background-color: white;
    padding: 25px;
    border-radius: 15px;
    margin-bottom: 20px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

</style>
""", unsafe_allow_html=True)

# 4. Main Header
st.title("Hi, I'm Hrishi 👋")
st.caption("Grade 8 Student | Tech Enthusiast | Aspiring Developer")

# Social Link Button
st.link_button("🐙 Visit My GitHub Profile (@hscoder-17)", "https://github.com/hscoder-17")

st.write("---")

# 5. Content Layout
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.header("About Me")
    st.write("I'm Hrishi, a 13-year-old Grade 8 student who is interested in technology, programming, and creative projects. I'm currently learning Python and building my first websites.")
    
    # Interactive Skill Level Expander
    st.subheader("🚀 Tech Focus")
    with st.expander("Click to view my learning roadmap"):
        st.write("🐍 **Python:** Basic Syntax, Functions, Streamlit Apps")
        st.progress(90)
        st.write("🌐 **Web Dev:** HTML/CSS, Frontend Basics")
        st.progress(50)
        st.write("💻 **Tools:** VS Code, Git, GitHub")
        st.progress(75)

with col2:
    # Profile Picture Display Card
    st.markdown('<div class="card">', unsafe_allow_html=True)
    try:
        st.image("profile.jpg", caption="Hrishi", use_container_width=True)
    except Exception:
        st.info("💡 Place 'profile.jpg' in your project folder to show your photo.")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h2>💡 Interests & Skills</h2>
        <ul>
            <li>🐍 Python Programming</li>
            <li>🌐 Web Development</li>
            <li>💻 Creative Projects</li>
            <li>⚽ Sports & Gaming</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Styled Projects Card
    st.markdown("""
    <div class="card">
        <h2>🛠️ Featured Projects</h2>
        <p><b>🐍 Beginner Python Scripts</b><br>Exploring logic, loops, and mini CLI tools.</p>
        <p><b>🌐 Personal Streamlit Website</b><br>My custom interactive web portfolio built with Python!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive Celebration Button
    if st.button("🎉 Click to Celebrate!"):
        st.balloons()