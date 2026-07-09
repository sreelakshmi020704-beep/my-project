# Quiz App 🧠

A simple command-line quiz application built with Python using Object-Oriented Programming (OOP). The program presents True/False questions, accepts user input, checks the answers, and keeps track of the score.

## Features

- Loads questions from a separate data file.
- Uses classes to organize the code.
- Displays one question at a time.
- Checks whether the user's answer is correct.
- Tracks the user's score throughout the quiz.
- Displays the final score after all questions are answered.

## Project Structure

```
quiz-project/
│
├── quizmain.py            # Main program
├── quiz.py            # Question class
├── quizbrain.py       # QuizBrain class
├── data.py            # Quiz questions
├── README.md          # Project documentation
```

## How It Works

1. Questions are stored in `data.py`.
2. Each question is converted into a `Question` object.
3. All questions are stored in a question bank.
4. `QuizBrain` displays each question one by one.
5. The user's answer is validated.
6. The score is updated after each question.
7. The final score is displayed when the quiz ends.

## Requirements

- Python 3.x

No external libraries are required.

## How to Run

1. Clone the repository.

```bash
git clone <repository-url>
```

2. Navigate to the project folder.

```bash
cd quiz-project
```

3. Run the program.

```bash
python quizmain.py
```

## Example Output

```
Q.1: A slug's blood is green. (True/False): True
You got it right!
The correct answer was: True
Your current score is: 1/1

Q.2: The loudest animal is the elephant. (True/False): False
You got it right!
The correct answer was: False
Your current score is: 2/2

You've completed the quiz
Your final score was: 2/2
```

## Concepts Used

- Python Classes
- Object-Oriented Programming (OOP)
- Loops
- Lists
- Modules
- User Input
- Conditional Statements

ractice project.
