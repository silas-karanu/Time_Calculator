# Time_Calculator
Building a simple time calculator
---

# 🕒 Time Calculator

This is a Python project that calculates the new time after adding a duration to a given start time. It also optionally calculates the resulting day of the week and how many days later the time falls.
---

## 📌 Features

- Handles 12-hour AM/PM time format
- Adds hours and minutes accurately
- Calculates changes across AM/PM periods
- Tracks how many days have passed
- Optionally displays the day of the week
- Formats results like:
  - `5:42 PM`
  - `2:02 PM, Monday`
  - `1:40 AM (next day)`
  - `6:18 AM, Monday (20 days later)`

## 🧠 Function Signature

```python
def add_time(start, duration, starting_day=None):
```
---
## Parameters:
- `start` (str): Start time 12-hour format, eg, `'3:00pm'`
- `duration` (str): Duraton to add, in `hours:minutes` format, eg, `3:10`
- `starting_day` (optional, str): Day of week, eg, `Monday`(case-insensitive)

---
## Returns
- `str`: The new time formatted in 12 hour AM/PM style, optionally with day and day count.
---
## 🛠 How It Works
1. Convert Start Time to 24-hour format to simplify arithmetic.

2. Parse and add duration time, handling minute overflow to hours.

3. Calculate total days passed from the total hours.

4. Convert result back to 12-hour format with AM/PM.

5. Calculate new weekday using modulo arithmetic if day is given.

6. Format the final string with correct punctuation and optional annotations.

---

## 🔮 Future Improvements
- Add input validation with meaningful error messages

- Support for durations expressed in days, like `"2 days, 5:00"`

- Accept start time in 24-hour format (optional)

- Include support for internationalization (e.g., weekdays in other languages)

- Provide command-line interface (CLI) or GUI for easier interaction

- Write unit tests using `unittest` or `pytest`

- Package as a module or PyPI package for reuse



---

## Notes
- This project uses only built-in Python features — no external libraries.

- Input times are assumed to be valid.

- Minutes in duration will be less than 60; hours can be any whole number.

---
## 📄 License
This project is free to use and modify for learning or personal projects.

