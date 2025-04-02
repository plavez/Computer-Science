import matplotlib.pyplot as plt
import time


def visualize_insertion_sort(arr):
    snapshots = []
    a_list = arr[:]
    for i in range(1, len(a_list)):
        value = a_list[i]
        j = i
        while j > 0 and a_list[j - 1] > value:
            a_list[j] = a_list[j - 1]
            j -= 1
        a_list[j] = value
        snapshots.append((a_list[:], i, j))  # save snapshot with current state

    return snapshots


# Generate visualization data
input_list = [6, 5, 3, 8]
snapshots = visualize_insertion_sort(input_list)

# Plot snapshots step by step
figs = []
for step, (state, i, j) in enumerate(snapshots):
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(state)), state)
    for k in range(len(state)):
        if k == j:
            bars[k].set_edgecolor("red")
            bars[k].set_linewidth(3)
        elif k == i:
            bars[k].set_edgecolor("blue")
            bars[k].set_linewidth(2)
    ax.set_title(f"Шаг {step+1}: вставка элемента")
    ax.set_ylim(0, max(input_list) + 2)
    figs.append(fig)

plt.close('all')  # Prevent automatic inline display
figs

print(visualize_insertion_sort([2, 8, 1, 15, 6]))
