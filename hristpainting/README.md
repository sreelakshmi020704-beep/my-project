# Hirst Dot Painting 🎨

A Python project that recreates a colorful dot painting inspired by the artwork of Damien Hirst using Python's built-in Turtle graphics library.

## Overview

This project generates a 10 × 10 grid of colorful dots. Each dot is randomly selected from a predefined color palette, creating a visually appealing piece of generative art.

The project demonstrates the use of:

- Python Turtle Graphics
- Random color selection
- Loops
- Coordinate movement
- Basic computer graphics

## Features

- Draws a 10 × 10 grid (100 dots)
- Randomly selects colors for each dot
- Uses RGB color mode
- Fast drawing speed
- Clean, minimal implementation

## Project Structure

```
hirst-dot-painting/
│
├── hrist.py        # Main Python program
├── README.md      # Project documentation
```

## Requirements

- Python 3.x

No external packages are required.

## How to Run

1. Clone the repository.

```bash
git clone <repository-url>
```

2. Navigate to the project directory.

```bash
cd hirst-dot-painting
```

3. Run the program.

```bash
python hrist.py
```

A Turtle graphics window will open and automatically draw the artwork.

## How It Works

1. Initializes the Turtle graphics screen.
2. Sets the turtle to RGB color mode.
3. Moves the turtle to the starting position.
4. Draws one colored dot at a time.
5. Randomly selects a color from the predefined palette.
6. Moves horizontally after each dot.
7. After every 10 dots, moves to the next row.
8. Continues until all 100 dots are drawn.

## Example

The program generates artwork similar to this:

```
● ● ● ● ● ● ● ● ● ●
● ● ● ● ● ● ● ● ● ●
● ● ● ● ● ● ● ● ● ●
● ● ● ● ● ● ● ● ● ●
● ● ● ● ● ● ● ● ● ●
● ● ● ● ● ● ● ● ● ●
● ● ● ● ● ● ● ● ● ●
● ● ● ● ● ● ● ● ● ●
● ● ● ● ● ● ● ● ● ●
● ● ● ● ● ● ● ● ● ●
```

Each dot is displayed in a randomly selected color from the palette.

## Concepts Used

- Python Turtle Graphics
- Object-Oriented Programming
- RGB Colors
- Lists
- Random Module
- Loops
- Coordinate System
- Procedural Drawing

## Future Improvements

- Allow users to customize the grid size.
- Generate a new random color palette for each run.
- Extract colors automatically from an image using the Colorgram library.
- Save the artwork as an image.
- Add animation while drawing.

## Author

Developed as a Python Turtle Graphics practice project inspired by Damien Hirst's famous dot paintings.
