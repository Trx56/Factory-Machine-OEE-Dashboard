import numpy as np
import matplotlib.pyplot as plt

# Simulated daily factory data for 3 robotic assembly stations
machines = ['Welding Arm', 'Pick-and-Place', 'Packaging Bot']

# Metrics (Total shift time = 480 minutes)
planned_production_time = 480 
operating_time = np.array([450, 400, 460]) # Downtime impacts this
ideal_cycle_time = 1.5 # minutes per part
total_parts_produced = np.array([290, 250, 300])
defective_parts = np.array([10, 20, 5])

# OEE Calculation Formula: Availability * Performance * Quality
availability = operating_time / planned_production_time
performance = (ideal_cycle_time * total_parts_produced) / operating_time
quality = (total_parts_produced - defective_parts) / total_parts_produced

# Calculate final OEE percentage
oee_scores = (availability * performance * quality) * 100

# Visualization
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(machines, oee_scores, color=['#4C72B0', '#DD8452', '#55A868'])

# Add target line (85% is world-class manufacturing standard)
ax.axhline(85, color='red', linestyle='--', linewidth=2, label='World-Class Target (85%)')

ax.set_ylim(0, 100)
ax.set_ylabel('OEE Score (%)')
ax.set_title('Daily Factory OEE Dashboard')
ax.legend()

# Add percentage text on top of bars
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height:.1f}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
