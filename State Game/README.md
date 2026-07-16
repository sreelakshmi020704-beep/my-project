# U.S. States Game

A fun Python game built with the **Turtle** graphics library and **Pandas**. The goal is to guess all 50 U.S. states. Each correct guess is displayed on the U.S. map, and if you exit before completing the game, a list of the states you missed is saved for you to study later.

## 📸 Preview

The game displays a blank map of the United States. As you correctly guess state names, they appear in their correct locations on the map.

---

## ✨ Features

- 🗺️ Interactive U.S. map using Turtle graphics
- ✅ Guess all 50 U.S. states
- 📍 Correct guesses appear on the map
- 📊 Tracks your score
- 💾 Saves unguessed states to `states_to_learn.csv`
- 🚪 Exit anytime by typing **Exit**

---

## 🛠️ Technologies Used

- Python 3
- Turtle
- Pandas

---

## 📂 Project Structure

```
US-States-Game/
│
├── state_games.py
├── 50_states.csv
├── blank_states.gif
├── states_to_learn.csv   # Generated after exiting
└── README.md
```

---

## 📦 Requirements

Install Pandas:

```bash
pip install pandas
```

*Turtle comes pre-installed with Python.*

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/us-states-game.git
```

2. Navigate to the project folder:

```bash
cd us-states-game
```

3. Run the program:

```bash
python state_games.py
```

---

## 🎮 How to Play

1. A blank map of the United States will appear.
2. Enter the name of a U.S. state.
3. If your answer is correct:
   - The state name appears on the map.
   - Your score increases.
4. Continue until you've guessed all 50 states.
5. Type **Exit** at any time to quit.
6. The game creates a file called `states_to_learn.csv` containing the states you missed.

---

## 📄 Example

```
Score: 10/50

Enter another state's name:
Texas ✅

Enter another state's name:
Florida ✅

Enter another state's name:
Exit
```

A file named **states_to_learn.csv** will be created containing all remaining states.

---

## 📚 Learning Outcomes

This project demonstrates:

- Python loops
- Conditional statements
- Lists
- Turtle graphics
- Reading CSV files with Pandas
- Data filtering
- Creating CSV files
- Event-driven programming

---

## 🔮 Future Improvements

- Add hints for difficult states
- Scoreboard with timer
- Case-insensitive input
- Sound effects
- High score tracking
- Difficulty levels
- Interactive state highlighting

---

## 👨‍💻 Author

Created as a Python learning project using **Turtle Graphics** and **Pandas**.

---

