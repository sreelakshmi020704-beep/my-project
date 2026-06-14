# 🔐 PyPassword Generator

A simple Python password generator that creates strong, randomized passwords using letters, numbers, and special symbols.

This project allows users to customize the number of letters, numbers, and symbols included in their password, then generates a secure password by shuffling all selected characters.

---

## 📖 Description

PyPassword Generator creates random passwords based on user preferences.

The user specifies:

* Number of letters
* Number of numbers
* Number of symbols

The program then:

1. Randomly selects characters from predefined lists.
2. Combines them into a single password.
3. Shuffles the characters for better randomness.
4. Displays the generated password.

---

## ✨ Features

* Custom password length
* Includes letters, numbers, and symbols
* Randomized character order
* Easy-to-use command-line interface
* Beginner-friendly Python project

---

## 🚀 Getting Started

### Prerequisites

* Python 3.x

### Run the Program

```bash
python password_generator.py
```

---

## 📂 Project Structure

```text
PyPassword-Generator/
│
├── password_generator.py
└── README.md
```

---

## Example Usage

```text
Welcome to PyPassword Generator!

How many letters would you like in your password?
8

How many numbers would you like?
3

How many symbols would you like?
2

Your password is:
g7!k2#aPm5D
```

---

## 🛠️ Technologies Used

* Python
* Random Module

---

## Concepts Practiced

* Lists
* Loops (`for`)
* User Input
* String Concatenation
* Random Selection (`random.choice()`)
* List Shuffling (`random.shuffle()`)

---

## How It Works

1. Letters, numbers, and symbols are stored in separate lists.
2. Based on user input, random characters are selected.
3. Characters are stored in a temporary list.
4. The list is shuffled to randomize the order.
5. The list is converted into a string and displayed as the final password.

---

## Sample Generated Passwords

```text
a#5kM8!dP2
7g&T4mQ1@x
z9*Lp3#N8b
```

---




