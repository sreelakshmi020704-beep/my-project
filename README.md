# Automated Birthday Wisher 🎂📧

A Python automation project that automatically sends a personalized **Happy Birthday email** to a person on their birthday.

The program reads birthday information from a CSV file, checks whether today matches anyone's birthday, randomly selects a birthday message template, personalizes it with the person's name, and sends the message through Gmail.

## Features

* 🎂 Automatically checks for birthdays every time the program runs.
* 📅 Reads birthday information from a CSV file.
* 🎲 Randomly selects one of three birthday letter templates.
* ✍️ Personalizes the message using the recipient's name.
* 📧 Sends the birthday email automatically using Gmail SMTP.
* 🔐 Supports using an email password or environment variables for authentication.

## Technologies Used

* **Python**
* **Pandas** – for reading and processing the birthday data.
* **SMTP** – for sending emails.
* **EmailMessage** – for working with email messages.
* **Datetime** – for checking the current date.
* **Random** – for selecting a random birthday template.

## Project Structure

```text
Automated-Birthday-Wisher/
│
├── birthday.py
├── birthdays.csv
├── letter_templates/
│   ├── letter_1.txt
│   ├── letter_2.txt
│   └── letter_3.txt
└── README.md
```

## How It Works

### 1. Get Today's Date

The program gets the current date and extracts the month and day:

```python
today = datetime.now()
today_tuple = (today.month, today.day)
```

### 2. Read Birthday Data

Birthday information is loaded from `birthdays.csv` using Pandas.

Example:

```text
name,email,year,month,day
John,john@example.com,1998,8,24
Anna,anna@example.com,2000,12,15
```

The program creates a dictionary using the person's birthday as the key.

### 3. Check for a Birthday

The program checks whether today's month and day exist in the birthday dictionary.

If there is a match, the person's information is retrieved.

### 4. Select a Random Letter

One of three birthday templates is randomly selected:

```python
file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
```

### 5. Personalize the Letter

The `[NAME]` placeholder in the template is replaced with the birthday person's name.

For example:

```text
Dear [NAME],

Happy Birthday! Have a wonderful day!
```

becomes:

```text
Dear John,

Happy Birthday! Have a wonderful day!
```

### 6. Send the Email

The program connects to Gmail's SMTP server and sends the personalized birthday message.

## Setup

Install the required dependency:

```bash
pip install pandas
```

Python's `datetime`, `random`, `smtplib`, and `email` modules are included with Python.

## Gmail Configuration

Replace:

```python
MY_EMAIL = "your email"
MY_PASSWORD = "your password"
```

with your email credentials.

For better security, **do not store your real password directly in the source code**. For Gmail accounts with 2-Step Verification enabled, use a **Google App Password** instead of your normal Gmail password.

## Running the Project

Make sure your project has the required CSV file and letter templates.

Then run:

```bash
python main.py
```

The program will check whether anyone has a birthday today.

If there is a birthday match, an email will automatically be sent to that person.

## Important Security Note 🔐

Never upload your real email password or App Password to GitHub.

Instead, use environment variables or another secure method to store credentials.

For example:

```python
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
```

## Purpose

This project was created to practice Python concepts such as:

* File handling
* Working with CSV files
* Pandas
* Dictionaries
* Datetime
* Random selection
* SMTP email automation
* String replacement
* Python automation

## Author

Created as a Python automation learning project.
