# 💘 Cupid's Arrow - Physics-Based Love Sim

A Valentine's Day themed precision game where you take on the role of Cupid. Your mission is to launch a "Heart Arrow" at a moving target to spread love. However, the winds of fate are fickle! You must calculate the perfect shot power while compensating for a randomized wind vector that can either help or hinder your arrow's flight.

This project focuses on teaching:
* **Environmental Modifiers:** Using variables (Wind) to alter user input (Power) before calculating the final state.
* **Absolute Variance:** Using `abs()` to determine "closeness" regardless of whether the player overshot or undershot the target.
* **Input Sanitization:** Using `try/except` to handle non-numeric inputs gracefully.
* **Logic Branching:** Providing specific feedback based on the relationship between the result and the target distance.

---

## ✨ Features

* **Procedural Wind:** Every game generates a new wind speed ($m/s$), requiring the player to adapt their strategy.
* **Proximity Feedback:** The game recognizes "Close Calls," giving the player a hint if they are within 3 meters of a bullseye.
* **Physics Engine:** Simple vector addition ($Result = Power + Wind$) simulates the effect of air resistance on a projectile.
* **Holiday Theme:** Festive UI and messaging tailored for a Valentine's Day coding session.

---

## 🚀 How to Run the Game

### 1. Prerequisites
You need **Python 3** installed.

### 2. Setup and Execution
1.  **Save the Code:** Save the script as `cupid_arrow.py`.
2.  **Open Terminal:** Navigate to your project folder.
3.  **Run the Script:**
    ```bash
    python cupid_arrow.py
    ```

### 3. Gameplay Instructions
1.  **Check the Wind:** Look at the current wind speed. A positive number pushes your arrow further; a negative number holds it back.
2.  **Calculate Power:** Subtract or add the wind value to the target distance to find your required input power.
3.  **Launch:** You have 3 arrows to hit the target exactly.

[attachment_0](attachment)

---

## 🧠 Code Structure Highlights

### Proximity Detection
Instead of just checking for a win or loss, we use the `abs()` function. This calculates the "distance" between two numbers without worrying about which one is larger.

```python
distance_diff = result - target_pos
if abs(distance_diff) <= 3:
    print("So close! You were within 3 meters!")
