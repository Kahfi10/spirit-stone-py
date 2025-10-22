# 💎 The Spirit Stone Project

This programme will manage a stone that can store ‘energy’ and has hidden elemental ‘affinities’ (Fire, Water, Air).
---
A simple project to demonstrate the core concepts of **Object-Oriented Programming (OOP)** in a unique and engaging way. Tired of `Car` or `Cat` examples? Let's manage a *magical item*!

| 🐍 Language | 📦 Concepts | 🎮 Theme |
| :--- | :--- | :--- |
| **Python 3.x** | **Full OOP** | **Game / Fantasy** |

---

## 📜 The Concept

Every great adventurer needs a magical artifact. The `SpiritStone` is an artifact that can absorb energy from its surroundings. However, this stone is fragile and holds a secret.

* Every stone has a **name** (public).
* Every stone stores **energy** (protected), which can be filled or set.
* Every stone has a **secret elemental affinity** (private) that is only revealed if its energy is high enough.
* If the stone is **overcharged with energy** (above 100), it will **crack** (a private status) and lose all its energy!

This project is a simple simulation to manage the *state* of this stone using all the pillars of OOP.

---

## 💡 OOP Concepts Demonstrated

This program is specifically designed to showcase:

1.  **Class & Object**
    * `SpiritStone` is the **Class** (the blueprint).
    * `sky_stone` or `mountain_stone` are the **Objects** (the actual instances of the class).

2.  **Encapsulation (Access Modifiers)**
    * **Public (`self.name`)**: An attribute that can be accessed and changed from anywhere.
    * **Protected (`self._energy`)**: An attribute that "should not" be accessed directly from outside, marked with a single `_`. We provide access via Getters & Setters.
    * **Private (`self.__elemental_affinity`, `self.__is_cracked`)**: Attributes that "cannot" be accessed from outside, marked with `__`. This is the stone's internal secret!

3.  **Getter & Setter (Traditional Methods)**
    * `get_stored_energy()`: A **Getter** method to retrieve the value of `_energy`.
    * `set_stored_energy(value)`: A **Setter** method that contains *validation logic*. This is where we check if the new `value` will cause the stone to crack.

4.  **Property (The Pythonic Way)**
    * `@property def affinity(self)`: This is a sophisticated **Pythonic Getter**.
    * It can be accessed like an attribute (`stone.affinity`) instead of a method (`stone.affinity()`).
    * It contains logic: It will only reveal the elemental affinity if the energy is over 50.
    * It is made *read-only* because we did not create an `@affinity.setter`.

5.  **Public vs. Private Methods**
    * `absorb_energy()` (Public) can be called by anyone.
    * `__crack_stone()` (Private) is an internal method that can only be called by other methods within the class (in this case, called by `set_stored_energy` or `absorb_energy` if overcharged).

---

## 🚀 Quick Start

Copy the `spirit_stone.py` code into your project, then import and use the class.

```python
# --- main.py ---
# (Assuming the class file is named spirit_stone.py)
from spirit_stone import SpiritStone 

# 1. Create a SpiritStone Object
first_stone = SpiritStone(stone_name="Pulsing Stone", initial_energy=30)
first_stone.display_info()

print("---")

# 2. Check the 'Property' (Affinity is still secret)
print(f"Affinity: {first_stone.affinity}") # Output: ??? (Not enough energy to see affinity)

print("---")

# 3. Use the 'Setter' to add energy
print("Setting energy to 80 via Setter...")
first_stone.set_stored_energy(80)

# 4. Check the 'Property' again (Now it's revealed!)
print(f"Affinity: {first_stone.affinity}") # Output: Fire (or Water/Air/Earth)

print("---")

# 5. Trigger the 'Cracked' condition
print("Trying to absorb too much energy...")
first_stone.absorb_energy(50) # Energy 80 + 50 = 130!
# Output: OVERWHELMING ENERGY! Pulsing Stone has cracked!

first_stone.display_info()
# Output:
# --- Stone Info: Pulsing Stone ---
# Stored Energy: 0
# Status: Cracked
