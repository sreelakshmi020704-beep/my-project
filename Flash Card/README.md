# French Flash Card 🇫🇷

A simple **French-to-English flash card application** built with Python, Tkinter, and Pandas. The app helps you learn French vocabulary by displaying a French word first and automatically flipping the card to show its English translation after a few seconds.

## Features

* 🇫🇷 Displays a random French word.
* 🇬🇧 Automatically shows the English translation after 3 seconds.
* ❌ Allows you to mark a word as unknown.
* ✅ Allows you to mark a word as known.
* 💾 Saves your learning progress automatically.
* 🔄 Removes known words from the learning list so they won't appear again.
* 📊 Uses Pandas to manage the vocabulary data.
* 🖥️ Uses Tkinter to create the graphical user interface.

## Technologies Used

* **Python**
* **Tkinter** – for the graphical user interface
* **Pandas** – for reading and managing CSV files
* **Random** – for selecting flash cards randomly

## Project Structure

```text
French-Flash-Card/
│
├── flash_card.py
├── french_words.csv
├── words_to_learn.csv
├── card_front.png
├── card_back.png
├── right.png
├── wrong.png
└── README.md
```

## How It Works

When the application starts, it first checks whether `words_to_learn.csv` exists.

* If it exists, the app loads the remaining vocabulary from that file.
* If it doesn't exist, the app loads the original vocabulary from `french_words.csv`.

A random French word is then displayed on the front of the card.

After **3 seconds**, the card automatically flips and displays the English translation.

### Buttons

**❌ Wrong Button**

If you don't know the word, the card remains in the learning list and another random card is displayed.

**✅ Right Button**

If you know the word, it is removed from the learning list and the updated list is saved to `words_to_learn.csv`.

## Installation

Make sure Python is installed on your computer.

Install Pandas using:

```bash
pip install pandas
```

Tkinter is included with most standard Python installations.

## Running the Project

Clone or download this project and make sure all the image and CSV files are in the same directory as the Python file.

Then run:

```bash
python main.py
```

## Data

The vocabulary is stored in CSV files with two columns:

```text
French,English
```

Example:

```text
bonjour,hello
merci,thank you
chat,cat
```

## Learning Progress

The application creates `words_to_learn.csv` when you mark words as known.

This allows you to close and reopen the application without losing your progress.

If you want to **start learning all the words again**, delete `words_to_learn.csv`. The application will recreate the learning list from `french_words.csv`.

## Purpose

This project was created as a practical Python project to practice:

* Tkinter GUI development
* Working with CSV files
* Pandas DataFrames
* Functions and event handling
* Random selection
* File handling
* Basic application state management

## Author

Created as a Python learning project.

