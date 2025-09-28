# 🏰 Tower of Hanoi — Prolog & Lisp Implementations

This project provides **two implementations** of the classic **Tower of Hanoi** puzzle:  
one in **Prolog** and another in **Common Lisp**.

---

## 🧩 Overview

The **Tower of Hanoi** is a mathematical puzzle consisting of **three rods** and **N disks** of different sizes.  
The goal is to move all disks from the **source rod** to the **target rod**, following these rules:

1. Only **one disk** can be moved at a time.  
2. Each move consists of taking the **top disk** from one rod and placing it on top of another rod.  
3. **No larger disk** may be placed on top of a **smaller disk**.

The **minimum number of moves** required to solve the puzzle is:  
> `2ⁿ - 1` (where *n* is the number of disks)

---

## 🚀 Features

- Works for **any number of disks** (minimum 3)
- Displays the **step-by-step moves**
- Shows the **minimum number of moves**
- Fully interactive (prompts user for disk count)
- Implemented in both:
  - 🧠 **Prolog**
  - 🌀 **Common Lisp**

---

## ⚙️ Prolog Implementation

### 📄 File: `tower_of_hanoi.pl`

**Run using SWI-Prolog:**

```bash
swipl
?- [tower_of_hanoi].
?- run.
