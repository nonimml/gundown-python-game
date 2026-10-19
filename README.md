# 🎯 GunDown - Grid-Based Hidden Object Game

**GunDown** is a CLI grid-based puzzle game developed in Python. Players configure a custom grid size and guess hidden locations within the matrix. The game logs final gameplay statistics with timestamps and automatically exports session summaries to text files.

---

## 🚀 Features

* **Custom Grid Setup:** Define row and column dimensions (`Rows >= 3` and `Columns <= 5`).
* **Hidden Target Placement:** Random placement of hidden objects with user-selected counts.
* **Game Modes:**
  * **Normal Mode:** Play without target visibility.
  * **Cheat Mode (`show`):** Reveals target locations on the board before guessing.
* **Help System:** Command-line argument to display instructions.
* **Result Logging:** Automatic output of gameplay results (found vs. missed targets) saved to time-stamped text files.

---

## 🛠️ Requirements

* Python 3.x installed on your operating system.

---

## 🎮 How to Play

Run the main file `gundown.py` from your terminal using command-line arguments:

### 1. View Help Instructions
```bash
python gundown.py help