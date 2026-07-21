# 🍅 Pomodoro Timer

A simple and user-friendly **Pomodoro Timer desktop application** built using **Python and Tkinter**. This project follows the Pomodoro Technique to help users stay focused and manage their study or work sessions with regular breaks.

## 📌 About the Project

The Pomodoro Timer uses a structured work-and-break cycle:

* 🟢 **25 minutes** of focused work
* 🌸 **5 minutes** of short break
* 🔴 **20 minutes** of long break after 8 work sessions

The application also keeps track of completed work sessions using check marks.

## ✨ Features

* ⏱️ 25-minute work sessions
* ☕ 5-minute short breaks
* 🌴 20-minute long breaks
* 🔄 Automatic transition between work and break sessions
* ✅ Displays completed work sessions with check marks
* 🔁 Reset button to restart the timer
* 🍅 Simple graphical user interface using Tkinter
* 🖼️ Custom tomato image displayed in the timer
* 📱 Lightweight desktop application

## 🛠️ Technologies Used

* **Python**
* **Tkinter** – For creating the graphical user interface
* **Math** – For timer calculations
* **Pathlib** – For handling the tomato image file path

## 📂 Project Structure

```text
Pomodoro-Timer/
│
├── pomodora.py
├── tomato.png
└── README.md
```

> **Note:** The Python file can have any name, but in this example it is called `main.py`.

## ⚙️ How It Works

The timer follows the Pomodoro technique using the following cycle:

```text
Work (25 min)
      ↓
Short Break (5 min)
      ↓
Work (25 min)
      ↓
Short Break (5 min)
      ↓
...
      ↓
After 8 Work Sessions
      ↓
Long Break (20 min)
```

The timer automatically changes between work sessions and breaks.

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/pomodoro-timer.git
```

### 2. Navigate to the Project Directory

```bash
cd pomodoro-timer
```

### 3. Run the Python Application

```bash
python main.py
```

## 🖥️ How to Use

1. Open the application.
2. Click the **Start** button to begin the Pomodoro timer.
3. Focus on your work during the 25-minute work session.
4. Take a short break when the timer automatically switches to break mode.
5. Continue the cycle.
6. After completing 8 work sessions, take a 20-minute long break.
7. Click **Reset** to restart the timer and clear the completed session marks.

## 🎯 Pomodoro Technique

The **Pomodoro Technique** is a time-management method that divides work into focused intervals separated by short breaks. It can help improve concentration, reduce distractions, and make long study or work sessions easier to manage.

## 🔮 Future Improvements

Possible improvements for this project include:

* 🔊 Add sound notifications when a session ends
* ⚙️ Allow users to customize work and break durations
* ⏸️ Add a Pause/Resume button
* 🌙 Add dark mode
* 📊 Track daily productivity statistics
* 💾 Save completed sessions
* 🎨 Improve the user interface
* 🔔 Add desktop notifications



