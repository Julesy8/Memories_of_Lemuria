class Camera:
    # courtesy of Harry Wykman
    # https://code.harrywykman.com/the-python-revised-roguelike-tutorial-with-a-scrolling-map.html
    def __init__(self, x: int, y: int, width: int, height: int, map_width: int, map_height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.map_width = map_width
        self.map_height = map_height

    def apply(self, x, y):
        x = x + self.x
        y = y + self.y
        return (x, y)

    def update(self, entity):
        if entity.x < int(self.width / 2):
            y = -entity.y + int(self.height / 2)
            x = self.x
            self.x, self.y = (x, y)

        if entity.y < int(self.width / 2):
            x = -entity.x + int(self.width / 2)
            y = self.y
            self.x, self.y = (x, y)
