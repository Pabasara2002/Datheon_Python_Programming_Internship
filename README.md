# 🚀 Datheon Internship - Python Tasks & Utilities

Welcome to my repository containing all practical Python projects completed during my internship at **Datheon**. This repository contains 4 distinct scripts ranging from terminal games and financial tracking utilities to system file organization and rule-based AI chatbots.

---

## 📂 Repository Structure

```text
.
├── hangman.py                           # Task 1: Terminal Hangman Game
├── google-10000-english-no-swears.txt   # Task 1: Word list dataset
├── portfolio.py                         # Task 2: Investment Portfolio Tracker
├── constituents.csv                     # Task 2: S&P 500 Ticker dataset
├── organizer.py                         # Task 3: Desktop File Organizer Utility
├── chatbot.py                           # Task 4: Rule-Based Support Chatbot
├── sample_faq.json                      # Task 4: Knowledge base dataset
└── README.md                            # Documentation
```

---

## 🛠️ Tasks Overview & Features

### 1. 🕹️ Task 1: Interactive Hangman Game (`hangman.py`)
* **Description:** A classic console-based text game where players attempt to guess a hidden word letter-by-letter within 6 attempts.
* **Key Features:**
  * Connects directly to `google-10000-english-no-swears.txt` to select random target words.
  * Dynamic visual feedback using custom ASCII gallows art updates upon incorrect guesses.
  * Tracks previously guessed letters and prevents duplicate penalties.
* **How to Run:**
  ```powershell
  py hangman.py
  ```

---

### 2. 📈 Task 2: Investment Portfolio Tracking Utility (`portfolio.py`)
* **Description:** A financial utility designed to allow users to input stock tickers, buying prices, and quantities to evaluate total portfolio returns.
* **Key Features:**
  * Validates tickers against the provided S&P 500 dataset (`constituents.csv`).
  * Calculates invested capital vs. current market value and individual holding percentage gains/losses.
  * Automatically exports the formatted summary to an external `portfolio_summary.csv` file using Python's `csv` module.
* **How to Run:**
  ```powershell
  py portfolio.py
  ```

---

### 3. 🧹 Task 3: Autonomous Desktop File Organizer (`organizer.py`)
* **Description:** An automated desktop management utility that organizes cluttered folders by categorizing files into dynamic subdirectories (`/Documents`, `/Images`, `/Videos`, `/Archives`, `/Code`).
* **Key Features:**
  * Built using high-performance `os.scandir()`, `pathlib`, and `shutil`.
  * Collision handling logic that automatically generates incremental suffixes if duplicate filenames exist.
  * Robust `try-except` blocks catching `PermissionError` and `FileExistsError`.
* **How to Run:**
  ```powershell
  py organizer.py
  ```

---

### 4. 🤖 Task 4: Rule-Based Customer Support Chatbot (`chatbot.py`)
* **Description:** A rule-based conversational AI designed to handle user inquiries regarding business hours, project submissions, and certificate issuance.
* **Key Features:**
  * Reads intent responses directly from `sample_faq.json`.
  * Employs regex input normalization and keyword extraction for query matching.
  * Graceful fallback logic for low-confidence queries and clean exit handling (`exit`, `quit`, `bye`).
* **How to Run:**
  ```powershell
  py chatbot.py
  ```

---

## 💻 Tech Stack & Requirements

* **Language:** Python 3.x
* **Modules Used:** Standard Library (`random`, `csv`, `os`, `shutil`, `pathlib`, `re`, `json`)
* **External Dependencies:** None required (100% standard library implementation)

---

## 👨‍💻 Author
Developed during the **Datheon Internship Program**.