# 🃏 Blackjack Game (Python)

A simple command-line implementation of the classic **Blackjack** card game built with Python. Play against the computer and try to get as close to **21** as possible without going over.

---

## 📌 Features

* Random card dealing
* Blackjack detection
* Automatic Ace value adjustment (11 → 1)
* Dealer follows Blackjack rules (draws until score reaches 17)
* Displays both player and dealer hands
* Win, lose, and draw outcomes
* ASCII Blackjack logo

---

## 🛠️ Technologies Used

* Python 3
* `random` module
* Custom `art.py` file for the game logo

---

## 📂 Project Structure

```
blackjack/
│── main.py          # Main game logic
│── art.py           # ASCII logo
└── README.md        # Project documentation
```

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/blackjack-game.git
```

2. Navigate to the project folder:

```bash
cd blackjack-game
```

3. Run the program:

```bash
python main.py
```

---

## 🎮 How to Play

* You and the computer are each dealt two cards.
* Your goal is to reach **21** or get as close as possible without exceeding it.
* Choose:

  * **y** → Draw another card.
  * **n** → Pass your turn.
* The dealer automatically draws cards until reaching at least **17**.
* The winner is determined according to standard Blackjack rules.

---

## 🃏 Card Values

| Card  |               Value |
| ----- | ------------------: |
| Ace   | 11 (or 1 if needed) |
| 2–10  |          Face value |
| Jack  |                  10 |
| Queen |                  10 |
| King  |                  10 |

---

## 🏆 Winning Rules

* Blackjack (21 with two cards) wins automatically.
* Going over 21 results in a loss.
* If the dealer goes over 21, you win.
* The higher score (without exceeding 21) wins.
* Equal scores result in a draw.

---

## 📸 Example Gameplay

```
Your cards: [10, 7], current score: 17
Computer's first card: 9

Type 'y' to get another card, type 'n' to pass: n

Your final hand: [10, 7], final score: 17
Computer's final hand: [9, 8], final score: 17

Draw
```

---

