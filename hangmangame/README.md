# Hangman Game 🎮

A simple command-line Hangman game written in Python. The player must guess the hidden word one letter at a time before running out of lives.

## Features

* Random word selection from a predefined word list.
* Visual hangman stages displayed after incorrect guesses.
* Tracks previously guessed letters.
* Win and lose conditions.
* Remaining lives counter.

## Project Structure

```
project/
│
├── main.py
├── hangman_words.py
├── hangman_art.py
└── README.md
```

### `hangman_words.py`

Contains a list of words used for the game.

Example:

```python
word_list = ["apple", "banana", "orange", "python"]
```

### `hangman_art.py`

Contains ASCII art for the hangman stages and the game logo.

Example:

```python
logo = "HANGMAN"

stages = [
    "...",
    "...",
]
```

## How to Run

1. Make sure Python 3 is installed.
2. Clone or download the project.
3. Open a terminal in the project directory.
4. Run:

```bash
python main.py
```

## How to Play

1. The game randomly selects a hidden word.
2. You start with 6 lives.
3. Enter one letter at a time.
4. Correct guesses reveal letters in the word.
5. Incorrect guesses reduce your lives by one.
6. Guess the entire word before your lives reach zero.

## Example

```
**************6/6 lives left**************
Word to guess: a

_a__a

**************5/6 lives left**************
Word to guess: p

appa_
```

## Winning

You win when all letters in the word are revealed.

```
**************YOU WIN**************
```

## Losing

You lose when all 6 lives are used.

```
**************YOU LOSE**************
```

The game then displays the correct word.

