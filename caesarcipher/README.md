# Caesar Cipher Encryption Tool 🔐

A simple Python command-line application that encrypts and decrypts messages using the Caesar Cipher technique. The program allows users to encode or decode text by shifting letters through the alphabet by a specified number.

## Features

* Encrypt messages using the Caesar Cipher.
* Decrypt encrypted messages.
* Supports shift values larger than 26.
* Preserves spaces, numbers, and special characters.
* Interactive command-line interface.
* Option to continue encrypting/decrypting multiple messages.

## Project Structure

```text
project/
│
├── main.py
├── art.py
└── README.md
```

### `art.py`

Contains the ASCII logo displayed when the program starts.

Example:

```python
caesarlogo = """
  ____                           
 / ___|__ _  ___  ___  __ _ _ __ 
| |   / _` |/ _ \/ __|/ _` | '__|
| |__| (_| |  __/\__ \ (_| | |   
 \____\__,_|\___||___/\__,_|_|   
"""
```

## How Caesar Cipher Works

The Caesar Cipher is a substitution cipher where each letter in the message is shifted by a fixed number of positions in the alphabet.

Example with a shift of 3:

```text
Original: hello
Encrypted: khoor
```

To decrypt, the shift is applied in the opposite direction.

## How to Run

1. Ensure Python 3 is installed.
2. Download or clone the project.
3. Open a terminal in the project folder.
4. Run:

```bash
python main.py
```

## Usage

When the program starts, choose one of the following options:

```text
Type 'encode' to encrypt, type 'decode' to decrypt:
```

Enter your message:

```text
type your message:
hello world
```

Enter the shift value:

```text
type the shift number:
3
```

Output:

```text
here is the encoded result: khoor zruog
```

## Example Session

```text
Type 'encode' to encrypt, type 'decode' to decrypt:
encode

type your message:
python

type the shift number:
5

here is the encoded result: udymts

Type 'yes' if you want continue. Otherwise type 'no'.
```

## Technologies Used

* Python 3
* Functions
* Lists
* Loops
* String Manipulation
* Modular Programming

