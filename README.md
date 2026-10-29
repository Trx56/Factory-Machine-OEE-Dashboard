# Factory Machine OEE Dashboard 

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Data%20Arrays-orange.svg)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Data%20Viz-green.svg)](https://matplotlib.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Factory Machine OEE Dashboard** is an industrial engineering data analysis script that calculates Overall Equipment Effectiveness (OEE). By processing daily production metrics (uptime, cycle times, and defect rates) for robotic assembly lines, it visually isolates efficiency bottlenecks to optimize factory facility planning.

---

## Key Features

* **Automated OEE Calculation:** Computes the industry-standard OEE score by multiplying three core manufacturing metrics: **Availability**, **Performance**, and **Quality**.
* **Multi-Machine Tracking:** Simultaneously processes data arrays for distinct factory stations (e.g., Welding Arms, Pick-and-Place robots, and Packaging Bots).
* **Target Benchmarking:** Generates a professional Matplotlib bar chart comparing individual machine efficiencies against a World-Class Manufacturing benchmark line (85%).
* **Actionable Output:** Provides immediate visual feedback to plant managers on which specific robotic station is causing a production bottleneck.

---

## Tech Stack & Libraries
* **Language:** Python
* **Data Processing:** NumPy
* **Visualization:** Matplotlib

---

##  Code Architecture
```text
 Factory-Machine-OEE-Dashboard
 ┣ oee_dashboard.py    # Metric calculators, array logic, and plot generation
 ┗  README.md           # Project documentation

## How to Run

pip install numpy matplotlib
python oee_dashboard.py

## Formula

OEE = Availability x Performance x Quality
- Availability = operating time / planned production time
- Performance = (ideal cycle time x parts produced) / operating time
- Quality = good parts / total parts

## Data Note

The production figures for the three stations (Welding Arm, Pick-and-Place, Packaging Bot) are simulated for demonstration. Replace the arrays in `oee_dashboard.py` with real shift data to analyse an actual line.
