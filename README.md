# A Lightweight Code Editor Written in Python

A lightweight code editor built with **Python** and  **PyQt6** , featuring a custom frameless window design and a modular user interface architecture.

---

## Features

* Custom title bar implementation
* Clean and modular PyQt6 architecture
* Lightweight and easy to extend

---

## 🛠️ Technologies Used

* Python 3
* PyQt6

---

## Architecture

### Custom Title Bar (`QFrame`)

The application uses:

```python
Qt.WindowType.FramelessWindowHint
```

to remove the default operating system window frame and replace it with a fully customized title bar.

#### Responsibilities:

* Window controls (minimize, maximize, close)
* Full-screen toggling
* Mouse-based window movement



### Main Window (`QWidget`)

The `MainWindow` class serves as the main application container holding the main layout structure and hosting the custom title bar neatly on top

#### Responsibilities:

* Managing the application layout
* Hosting the custom title bar
* Providing the main user interface structure

---

## Installation

### Install the required dependency:

First make sure you have Python installed :

```bash
python --version
```

Then install the required PyQt6 bindings :

```bash
pip install PyQt6
```

## Future Plans

* File explorer
* Tab support
* Themes
* Syntax highlighting
* Auto-completion
* Integrated terminal

---

## 👨‍💻 Author

**Rony Biswas**

Computer Science and Technology (CST) Student
Python & Data Science Enthusiast
