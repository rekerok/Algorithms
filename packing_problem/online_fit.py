import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import random


class Item:
    def __init__(self, item_id, width, height):
        self.id = item_id
        self.width = width
        self.height = height
        self.x = None
        self.y = None


class OnlineFitAlgorithm:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def pack_items(self):
        self.items.sort(key=lambda item: item.width * item.height, reverse=True)
        floor = np.zeros((self.height, self.width), dtype=bool)

        for item in self.items:
            packed = False

            for y in range(self.height - item.height + 1):
                for x in range(self.width - item.width + 1):
                    if not floor[y : y + item.height, x : x + item.width].any():
                        floor[y : y + item.height, x : x + item.width] = True
                        item.x = x
                        item.y = y
                        packed = True
                        break
                if packed:
                    break

            if not packed:
                new_floor = np.zeros((self.height, self.width), dtype=bool)
                for y in range(self.height - item.height + 1):
                    for x in range(self.width - item.width + 1):
                        if not new_floor[y : y + item.height, x : x + item.width].any():
                            new_floor[y : y + item.height, x : x + item.width] = True
                            item.x = x
                            item.y = y
                            packed = True
                            break
                    if packed:
                        break
                floor = np.logical_or(floor, new_floor)

        return self.items


def generate_items(item_count, min_width, max_width, min_height, max_height):
    items = []
    for i in range(1, item_count + 1):
        width = random.randint(min_width, max_width)
        height = random.randint(min_height, max_height)
        item = Item(i, width, height)
        items.append(item)
    return items


def visualize_packing(items, width, height):
    fig, ax = plt.subplots()
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlim([0, width])
    ax.set_ylim([0, height])
    ax.set_xticks([])
    ax.set_yticks([])

    colors = ["red", "green", "blue", "orange", "purple", "yellow", "cyan", "magenta"]
    random.shuffle(colors)

    for item, color in zip(items, colors):
        rect = Rectangle(
            (item.x, item.y),
            item.width,
            item.height,
            facecolor=color,
            edgecolor="black",
        )
        ax.add_patch(rect)

        ax.annotate(
            f"Item {item.id}\n{item.width}x{item.height}",
            (item.x + item.width / 2, item.y + item.height / 2),
            color="black",
            weight="bold",
            fontsize=8,
            ha="center",
            va="center",
        )

    plt.show()


def print_coordinates(items):
    for item in items:
        print(f"Item {item.id} - x: {item.x}, y: {item.y}")


width = 10
height = 10
item_count = 5
min_width = 1
max_width = 4
min_height = 1
max_height = 6

algorithm = OnlineFitAlgorithm(width, height)
items = generate_items(item_count, min_width, max_width, min_height, max_height)
for item in items:
    algorithm.add_item(item)

packed_items = algorithm.pack_items()
print_coordinates(packed_items)
visualize_packing(packed_items, algorithm.width, algorithm.height)
