# ⏱️ Timer & Stopwatch Utility

A simple, command-line utility written in Python that provides two essential time-tracking functions: a **Countdown Timer** and a **Stopwatch**. This project is a great example of basic Python scripting for practical everyday tools.

## ✨ Features

* **Countdown Timer:** Allows the user to input a duration in seconds and displays the time remaining, updating every second.
* **Stopwatch:** Measures the time elapsed between two presses of the **Enter** key, displaying the result with two decimal places.
* **Command-Line Interface:** Easy to use and run directly from the terminal.

## 🛠️ Prerequisites

* **Python 3.x** (Standard installation is sufficient; no external libraries are strictly required as `time` is built-in.)

## 💻 Installation and Setup

1.  **Clone the repository** (if you're hosting this on GitHub):
    ```bash
    git clone https://github.com/Asura-824/Stop-timer.git
    cd timer-stopwatch-utility
    ```

2.  **No further installations are necessary** as the script only uses the standard `time` module.

## 🚀 How to Run

1.  Save the provided code as a Python file (e.g., `time_utility.py`).
2.  Run the script from your terminal:
    ```bash
    python time_utility.py
    ```

3.  The main menu will appear, prompting you to choose between the **Timer (1)** or **Stopwatch (2)**.

---

## ⏰ Using the Functions

### 1. Countdown Timer

1.  Select **'1'** from the main menu.
2.  The program will prompt you: `Enter the countdown time in seconds: `
3.  Enter an integer (e.g., `10`) and press **Enter**.
4.  The time will count down on the same line using `end="\r"`.
5.  When the timer reaches zero, it prints `Time's up!`.

### 2. Stopwatch

1.  Select **'2'** from the main menu.
2.  The program will wait. **Press Enter to start** the measurement.
3.  The program will wait again. **Press Enter to stop** the measurement.
4.  The total `Elapsed time` in seconds will be printed.

## 📁 Code Overview

| Function | Description |
| :--- | :--- |
| `countdown_timer()` | Takes input in seconds, uses a `while` loop and `time.sleep(1)` to decrement and display the time remaining. |
| `stopwatch()` | Uses `input()` to pause execution, records the start and end times using `time.time()`, and calculates the difference. |
| `main()` | The entry point of the script, presenting the user with the selection menu. |

---

## 🤝 Contributing

This is a simple project, but contributions are welcome! Ideas for enhancement include:

* Adding input validation (e.g., ensuring the timer input is a positive integer).
* Displaying the stopwatch time in H:M:S format.
* Implementing a simple graphical user interface (GUI) using `tkinter`.
