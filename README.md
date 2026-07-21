# 🎓 DecodeLabs Python Internship — Projects Portfolio

Welcome to my professional development portfolio! This repository tracks my hands-on core backend engineering, GUI application development, and automated computation progress during the **Python Backend Developer Internship (Batch 2026)** powered by **DecodeLabs**.

---

## 📁 Repository Structure

All projects are strictly decoupled into individual execution modules following enterprise system guidelines:

```text
├── 📁 Project-01-Todo-List
│   └── 📄 main.py                 # Core Task Management CLI Script
│
├── 📁 Project-02-Expense-Tracker
│   └── 📄 main.py                 # Graphical GUI Expense Tracker Application
│
├── 📁 Project-03-Password-Generator
│   └── 📄 main.py                 # Enterprise GUI Password Generator & Security Tool
│
└── 📁 Project-04-Quiz-Game
    └── 📄 main.py                 # Modern GUI Interactive Quiz Engine & State Tracker
```
---

## 🚀 Projects Overview

### 🔹 Project 1: Terminal-Based Todo List App
A clean, terminal-driven application engineered to manage operational workflows using advanced data structures and dynamic user validation.
* **Data Architecture:** Utilized a collection of isolated Python dictionaries nested inside a global runtime list (`my_tasks = []`) to mimic database records.
* **Dynamic State Isolation:** Managed a safe auto-incrementing task ID tracker (`task_id_counter`) passed strictly between execution streams without global variable dependency.
* **Format Alignments:** Implemented professional tabular layouts using string alignment formatting modifiers (`<2`, `<9`) for real-time presentation feeds.

---

### 🔹 Project 2: Graphical Expense Tracker App
A modern desktop application built with `CustomTkinter` engineered to process real-time financial tracking and dynamic transaction logging.
* **Modern Desktop UI:** Replaced the terminal workflow with a dark-themed GUI featuring real-time total updates, interactive entry forms, and a reset system.
* **Dynamic Scrollable History:** Engineered an auto-updating `CTkScrollableFrame` to log individual expense items with description and monetary breakdown.
* **Digital Poka-Yoke & Validation:** Integrated robust input shields (`try-except ValueError`) and modal message popups to prevent garbage entries or negative values.

---

### 🔹 Project 3: Enterprise GUI Password Generator
An industrial-grade credential tool engineered with a dark-purple `CustomTkinter` interface and cryptographic backend modules.
* **Cryptographic Security:** Built on Python's `secrets` module (`secrets.choice`) utilizing hardware-level OS entropy to ensure absolute randomness.
* **Real-Time Entropy Calculation:** Calculates and logs information entropy ($E = L \times \log_2(R)$) in real-time, adjusting a visual progress bar across Weak, Medium, and Strong (Enterprise Grade) statuses.
* **Interactive Controls & Toast Notifications:** Features an interactive length slider, granular character pool checkboxes, clipboard copying, and custom auto-closing toast overlays.

---

### 🔹 Project 4: Interactive GUI Quiz Engine
A modern desktop application engineered with a graphical user interface for real-time knowledge assessment and metric tracking.
* **Event-Driven Architecture:** Engineered a responsive, dark-themed UI using `CustomTkinter`, transitioning from procedural execution to asynchronous event-driven programming.
* **Data Persistence:** Integrated the `json` and `os` modules to serialize and securely read/write high-score configurations directly to local disk storage, ensuring state continuity across sessions.
* **Dynamic Task Scheduling:** Implemented an asynchronous 15-second recursive countdown mechanism utilizing GUI mainloop scheduling (`self.after()`), completely bypassing thread-blocking delays.
* **Session Analytics:** Engineered an ephemeral review log matrix that tracks boolean outcomes and user inputs, rendering a scrollable post-game analytical review screen for the user.

---

## 🛠️ Tech Stack & Core Concepts Covered

| Category | Technologies / Patterns Covered |
| :--- | :--- |
| **Language & Core** | Python 3.x, Standard Libraries (`secrets`, `string`, `math`, `json`, `os`) |
| **Frontend & UI** | CustomTkinter (CTk), Event-Driven Desktop Design, Custom Modals & Toasts |
| **Architecture** | Object-Oriented Programming (OOP), State Management, Event Handling |
| **Data Structures** | Lists, Dictionaries, Tuples, Scrollable Frames, Dynamic Buffers |
| **Security & Math** | Cryptographic Pseudo-Randomness, Information Entropy Calculation, Exception Safety |

---

> 🌐 *Internship Track managed under industrial simulation protocols powered by DecodeLabs.*
