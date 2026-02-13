# 🎮 Stone • Paper • Scissor (First to 5 Wins)

This is a simple and interactive **Stone • Paper • Scissor** game built using **Python and Streamlit**.

The player competes against the computer. The first to win 5 rounds wins the match. The game includes sound effects, a timer, and a leaderboard that records the fastest winners.



## ✨ Features

- 🎯 First to 5 wins system  
- 🏆 Automatic winner declaration  
- ⏱️ Match timer  
- 📊 Leaderboard with ranking (based on fastest time)  
- 🔄 Restart game option  
- 🔊 Background music and sound effects  
- 💾 CSV-based score storage (no database required)  
- 🧠 Clean session state handling  



## 🛠️ Tech Stack

- Python 3  
- Streamlit  
- Built-in modules: `random`, `time`, `csv`, `os`, `base64`

No external database or heavy dependencies are used.



## 📂 Project Structure

```
stone-paper-scissor/
│
├── app.py
├── leaderboard.csv  (auto-created)
├── Screenshots
├── README.md
│
└── assets/
    ├── bg_music.mp3
    ├── click.mp3
    ├── win.mp3
    └── lose.mp3
```



## 🚀 How to Run This Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/stone-paper-scissor.git
```

### 2️⃣ Go to the Project Folder

```bash
cd stone-paper-scissor
```

### 3️⃣ (Optional) Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**Mac / Linux**
```bash
source venv/bin/activate
```



### 4️⃣ Install Required Library

```bash
pip install streamlit
```



### 5️⃣ Run the App

```bash
streamlit run app.py
```

Then open:

```
http://localhost:8501
```



## 🎮 How the Game Works

- Choose Stone, Paper, or Scissor.
- Click “Play Round”.
- Scores update automatically.
- First to reach 5 wins ends the match.
- If you win, you can save your time to the leaderboard.
- Restart anytime to play again.



## 📊 Leaderboard

The leaderboard:

- Stores winner name and completion time
- Sorts players by fastest match
- Displays ranking automatically
- Uses a simple CSV file (no database)



## 📌 Why I Built This

This project demonstrates:

- Game logic implementation
- File handling with CSV
- Dynamic UI updates
- Clean and structured code

It’s a small project, but it reflects good problem-solving and practical application of Python concepts.

---


## 👨‍💻 Author

Vijay Prabhakar Nagane  
Python Developer | Backend Enthusiast  
