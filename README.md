# 🎓 DecodeLabs Python Internship — Projects Portfolio

Welcome to my professional development portfolio! This repository tracks my hands-on core backend engineering and automated computation progress during the **Python Backend Developer Internship (Batch 2026)** powered by **DecodeLabs**.

---

## 📁 Repository Structure

All projects are strictly decoupled into individual execution modules following enterprise system guidelines:
```text
├── 📁 Project-01-Todo-List
│   └── 📄 main.py                 # Core Task Management CLI Script
│
├── 📁 Project-02-Expense-Tracker
│   └── 📄 main.py                 # State-Preserving Expense Tracker App
│
├── 📁 Project-03-Password-Generator
│   └── 📄 main.py                 # Enterprise Random Password Generator
│
└── 📁 Project-04-Quiz-Game
    └── 📄 main.py                 # GUI Interactive Quiz Engine & State Tracker
```
---

## 🚀 Projects Overview

### 🔹 Project 1: Terminal-Based Todo List App
A clean, terminal-driven application engineered to manage operational workflows using advanced data structures and dynamic user validation.
*   **Data Architecture:** Utilized a collection of isolated Python dictionaries nested inside a global runtime list (`my_tasks = []`) to mimic database records.
*   **Dynamic State Isolation:** Managed a safe auto-incrementing task ID tracker (`task_id_counter`) passed strictly between execution streams without global variable dependency.
*   **Format Alignments:** Implemented professional tabular layouts using string alignment formatting modifiers (`<2`, `<9`) for real-time presentation feeds.

---

### 🔹 Project 2: CLI Expense Tracker App
A console-based application engineered to process real-time financial tracking and numerical data compilation.
*   **State Management:** Fully isolated dynamic arithmetic operations (`total = total + new_expense`) without system state loss during iteration loops.
*   **Digital Poka-Yoke:** Implemented type-safety shields and robust exception-handling (`try-except ValueError`) to trap garbage entries and prevent sudden runtime engine failure.
*   **Modern Type Hinting:** Built with clean, production-ready function signatures for absolute code readability.

---

### 🔹 Project 3: Enterprise Random Password Generator
An industrial-grade credential architecture engineered for secure backend environments using Python's high-integrity modules.
*   **Cryptographic Security:** Replaced deterministic pseudo-random modules with the `secrets` module (`secrets.choice`) utilizing hardware-level operating system noise to ensure absolute unpredictability.
*   **Memory Optimization:** Overcame string immutability performance costs ($O(N^2)$ bottlenecks) by implementing the accumulator pattern using efficient linear-time complexity (`''.join()`).
*   **Information Entropy Validation:** Integrated real-time mathematical logging ($E = L \times \log_2(R)$) to calculate and output the precise information entropy score in bits, validating the password's resistance against modern GPU brute-force attacks.

---

### 🔹 Project 4: Interactive GUI Quiz Engine
A modern desktop application engineered with a graphical user interface for real-time knowledge assessment and metric tracking.
* **Event-Driven Architecture:** Engineered a responsive, dark-themed UI using `customtkinter`, transitioning from procedural CLI execution to asynchronous event-driven programming.
* **Data Persistence:** Integrated the `json` and `os` modules to serialize and securely read/write high-score configurations directly to local disk storage, ensuring state continuity across sessions.
* **Dynamic Task Scheduling:** Implemented an asynchronous 15-second recursive countdown mechanism utilizing GUI mainloop scheduling (`self.after()`), completely bypassing thread-blocking delays.
* **Session Analytics:** Engineered an ephemeral review log matrix that tracks boolean outcomes and user inputs, rendering a scrollable post-game analytical review screen for the user.

---

## 🛠️ Tech Stack & Core Concepts Covered

| Category | Technologies / Patterns Covered |
| :--- | :--- |
| **Language & Core** | Python 3.x, Standard Libraries (`string`, `secrets`, `math`, `json`, `os`) |
| **Frontend & UI** | CustomTkinter (CTk), Widget Configuration, Event Binding |
| **Architecture** | Object-Oriented Programming (OOP), Event-Driven UI, Modular Functions |
| **Data Structures** | Lists, Dictionaries, Nested Collections, String Buffers |
| **Security & Math** | Information Entropy, Cryptographic Pseudo-Randomness, Exception Handling |

---

> 🌐 *Internship Track managed under industrial simulation protocols powered by DecodeLabs.*
