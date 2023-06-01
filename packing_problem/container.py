class Container:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.items = []

    def can_fit(self, item):
        return item.width <= self.width and item.height <= self.height

    def place(self, item):
        self.items.append(item)
        self.width -= item.width
        self.height -= item.height

    def remaining_area(self):
        occupied_area = sum(item.width * item.height for item in self.items)
        return self.width * self.height - occupied_area
