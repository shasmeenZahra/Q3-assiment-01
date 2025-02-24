import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ✅ Fix: Page Config at the very top
st.set_page_config(
    page_title="Growth Mindset Journey",
    page_icon="📊",
    layout="wide"
)

# Sidebar Navigation
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/6/6b/Growth_icon.svg", width=50)
st.sidebar.title("Growth Mindset")
st.sidebar.markdown("### Navigation")
menu = st.sidebar.radio("", ["Dashboard", "Daily Reflection", "Goal Setting", "Resources", "Progress Graphs"])  # ✅ Fix: Corrected "progress Graph" to "Progress Graphs"

# Dashboard Page
if menu == "Dashboard":
    st.markdown("<h1 style='text-align: center;'>🌱 Growth Mindset Journey</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Transform Your Learning Experience</h3>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📊 Your Growth Journey")
        st.write("Start adding daily reflections to see your progress!")
        st.button("Add Reflection", key="reflection")

    with col2:
        st.markdown("### 🎯 Active Goals")
        st.write("Set your first goal in the Goal Setting section!")
        st.button("Set Goal", key="goal")

# Daily Reflection Page
elif menu == "Daily Reflection":
    st.markdown("## ✍️ Daily Reflection")
    reflection = st.text_area("Write your daily reflection here:")
    if st.button("Save Reflection"):
        st.success("Your reflection has been saved!")

# Goal Setting Page
elif menu == "Goal Setting":
    st.markdown("## 🎯 Goal Setting")
    goal = st.text_input("Set a new goal:")
    if st.button("Add Goal"):
        st.success(f"Goal added: {goal}")

# Resources Page
elif menu == "Resources":
    st.markdown("## 📚 Learning Resources")
    st.write("- [Carol Dweck on Growth Mindset](https://www.mindsetworks.com)")
    st.write("- [TED Talk on Growth Mindset](https://www.ted.com/talks/carol_dweck_the_power_of_believing_that_you_can_improve)")

# ✅ Fix: Change `page` to `menu` for Progress Graphs Page
elif menu == "Progress Graphs":
    st.title("📊 Your Progress Over Time")
    st.write("Track your learning journey with visual graphs.")

    # ---- User Input for Progress ----
    st.markdown("### Enter Your Weekly Progress")

    # Default Values for Days
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    default_progress = [20, 40, 60, 80, 100, 90, 50]  # Default progress values

    # Sliders for Each Day
    progress_data = {}
    for i, day in enumerate(days):
        progress_data[day] = st.slider(f"{day} Progress (%)", 0, 100, default_progress[i])

    # ---- Convert Data to Pandas DataFrame ----
    df = pd.DataFrame({"Day": list(progress_data.keys()), "Progress": list(progress_data.values())})

    # ---- Matplotlib Graph ----
    fig, ax = plt.subplots()
    ax.plot(df["Day"], df["Progress"], marker="o", linestyle="-", color="#1DB954")
    ax.set_title("Your Weekly Progress")
    ax.set_xlabel("Days")
    ax.set_ylabel("Progress (%)")
    ax.grid(True)

    # ---- Display Graph ----
    st.pyplot(fig)

    # ---- Show Table Data ----
    st.markdown("### 📋 Your Weekly Data")
    st.write(df)

    # ---- Export Data Button ----
    st.download_button("📥 Download CSV", df.to_csv(index=False), "progress_data.csv", "text/csv")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>⭐ Stay Motivated | Version 2.0</p>", unsafe_allow_html=True)
