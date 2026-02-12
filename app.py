import streamlit as st
import random
import time
import os
import csv
import base64

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Stone Paper Scissor", page_icon="🎮")

st.title("🎮 Stone • Paper • Scissor")

# -----------------------------
# Initialize Session State
# -----------------------------
if "user_score" not in st.session_state:
    st.session_state.user_score = 0

if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

if "game_over" not in st.session_state:
    st.session_state.game_over = False

# -----------------------------
# Function to Play Hidden Audio
# -----------------------------
def autoplay_audio(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()

    md = f"""
    <audio autoplay>
    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """
    st.markdown(md, unsafe_allow_html=True)

# -----------------------------
# Background Music
# -----------------------------
if os.path.exists("assets/bg_music.mp3"):
    autoplay_audio("assets/bg_music.mp3")

# -----------------------------
# User Info
# -----------------------------
name = st.text_input("Enter Your Name")

elapsed_time = int(time.time() - st.session_state.start_time)
st.write(f"⏳ Time Played: {elapsed_time} seconds")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🧑 Your Score")
    st.write(st.session_state.user_score)

with col2:
    st.subheader("🤖 Computer Score")
    st.write(st.session_state.computer_score)

st.divider()

# -----------------------------
# Check if Game Over
# -----------------------------
if st.session_state.user_score == 5:
    st.success("🏆 YOU WON THE MATCH! ")
    st.session_state.game_over = True

elif st.session_state.computer_score == 5:
    st.error("💀 COMPUTER WON THE MATCH!")
    st.session_state.game_over = True

# -----------------------------
# Game Logic (Only if not over)
# -----------------------------
choices = ["Stone", "Paper", "Scissor"]

if not st.session_state.game_over:

    user_choice = st.radio("Choose your move:", choices)

    if st.button("🚀 Play Round"):

        if os.path.exists("assets/click.mp3"):
            autoplay_audio("assets/click.mp3")

        computer_choice = random.choice(choices)
        st.write(f"🤖 Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            st.info("🤝 It's a Draw!")

        elif (
            (user_choice == "Stone" and computer_choice == "Scissor")
            or (user_choice == "Paper" and computer_choice == "Stone")
            or (user_choice == "Scissor" and computer_choice == "Paper")
        ):
            st.success("🎉 You Win This Round!")
            st.session_state.user_score += 1

            if os.path.exists("assets/win.mp3"):
                autoplay_audio("assets/win.mp3")

        else:
            st.error("😢 You Lose This Round!")
            st.session_state.computer_score += 1

            if os.path.exists("assets/lose.mp3"):
                autoplay_audio("assets/lose.mp3")

else:
    st.warning("🚫 Game Over! Start a new game.")

# -----------------------------
# Restart Game Button
# -----------------------------
if st.button("🔄 Restart Game"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.start_time = time.time()
    st.session_state.game_over = False
    st.rerun()

# -----------------------------
# Leaderboard Save Function
# -----------------------------
def save_score(player_name, time_taken):
    file_exists = os.path.isfile("leaderboard.csv")

    with open("leaderboard.csv", "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Name", "Time"])

        writer.writerow([player_name, time_taken])

# -----------------------------
# Save Score Only If User Won
# -----------------------------
if st.session_state.user_score == 5:
    if st.button("🏆 Save Winning Score"):
        if name:
            save_score(name, elapsed_time)
            st.success("Score Saved to Leaderboard!")
        else:
            st.warning("Enter your name first!")

# -----------------------------
# Display Leaderboard
# -----------------------------
# -----------------------------
# Display Leaderboard
# -----------------------------
st.divider()
st.markdown("## 🏆 Leaderboard (Fastest to 5 Wins)")

if os.path.exists("leaderboard.csv"):

    with open("leaderboard.csv", "r") as file:
        reader = csv.reader(file)
        data = list(reader)

    if len(data) > 1:

        # Remove header
        records = data[1:]

        # Sort by time
        records = sorted(records, key=lambda x: int(x[1]))

        # Prepare clean structured data
        leaderboard_data = []
        for i, row in enumerate(records, start=1):
            leaderboard_data.append({
                "Rank": i,
                "Name": row[0],
                "Time (sec)": row[1]
            })

        # Display properly
        st.dataframe(leaderboard_data, use_container_width=True)

    else:
        st.info("No scores yet. Win a match to appear here!")

else:
    st.info("Leaderboard file not found.")

