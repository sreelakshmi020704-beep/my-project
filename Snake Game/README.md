
# Snake Game 🐍

A classic Snake Game built with Python using the Turtle graphics library. Control the snake, collect food to grow longer, and avoid colliding with the walls or your own tail.

## Overview

This project recreates the classic Snake Game using Object-Oriented Programming (OOP). The game consists of separate classes for the snake, food, and scoreboard, making the code modular and easy to maintain.

## Features

- Control the snake using the arrow keys.
- Food appears at random locations.
- Snake grows after eating food.
- Real-time score tracking.
- Game over when the snake hits the wall.
- Game over when the snake collides with its own tail.
- Smooth animation using Turtle graphics.

## Project Structure

```
snake-game/
│
├── snakegame.py            # Main game loop
├── snake.py           # Snake class
├── food.py            # Food class
├── scoreboard.py      # Scoreboard class
├── README.md          # Project documentation
```

## Requirements

- Python 3.x

No external libraries are required. The project uses Python's built-in:

- `turtle`
- `time`
- `random`

## How to Run

1. Clone the repository.

```bash
git clone <repository-url>
```

2. Navigate to the project directory.

```bash
cd snake-game
```

3. Run the game.

```bash
python snakegame.py
```

## Controls

| Key | Action |
|-----|--------|
| ↑ Up Arrow | Move Up |
| ↓ Down Arrow | Move Down |
| ← Left Arrow | Move Left |
| → Right Arrow | Move Right |

## Gameplay

1. The snake starts with three body segments.
2. Use the arrow keys to control its direction.
3. Eat the food to increase your score.
4. Each food eaten makes the snake grow longer.
5. Avoid hitting the walls.
6. Avoid colliding with your own tail.
7. The game ends when a collision occurs.

## Concepts Used

- Python Object-Oriented Programming (OOP)
- Turtle Graphics
- Event Handling
- Keyboard Input
- Collision Detection
- Lists
- Loops
- Classes and Objects
- Animation
- Random Number Generation

## Future Improvements

- Add a high score system.
- Restart the game without closing the window.
- Multiple difficulty levels.
- Sound effects and background music.
- Pause and resume functionality.
- Obstacles and bonus food.
- Custom game themes.

## Sample Gameplay

```
Score: 8

🐍 ➜ ➜ ➜

        🍎

Avoid the walls and your own tail!
```

## Author

Developed as a Python Turtle Graphics and Object-Oriented Programming practice project.
