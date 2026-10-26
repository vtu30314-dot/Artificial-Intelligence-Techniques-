"""Task 7 - Monkey Banana Problem (goal stack planning)"""
import matplotlib
import matplotlib.pyplot as plt

steps = ["Start", "Move to box", "Push box", "Climb box", "Grab banana", "Goal"]

# Goal-stack planning: print the plan in order
print("Goal: Monkey gets the banana\nPlan:")
for i, s in enumerate(steps, 1):
    print(f"  {i}. {s}")

# Layout of the flow chart (x, y) for each step
positions = [(0.10, 0.80), (0.45, 0.80), (0.80, 0.80),
             (0.80, 0.50), (0.45, 0.50), (0.45, 0.20)]

fig, ax = plt.subplots(figsize=(9, 5))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

for (x, y), step in zip(positions, steps):
    ax.text(x, y, step, ha='center', va='center', fontsize=11,
            bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue',
                      edgecolor='black'))

for i in range(len(positions) - 1):
    ax.annotate('', xy=positions[i + 1], xytext=positions[i],
                arrowprops=dict(arrowstyle='->', lw=1.5,
                                shrinkA=25, shrinkB=25))

plt.title("Monkey Banana Problem - Goal Stack Planning")
plt.savefig("monkey_banana.png")
if matplotlib.get_backend().lower() != 'agg':
    plt.show()
