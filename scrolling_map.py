class Camera:
    # the portion of the map displayed to the screen
    def __init__(self, camera_x: int, camera_y: int, screen_width: int,
                 screen_height: int):
        self.camera_x = camera_x
        self.camera_y = camera_y
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.half_width = int(self.screen_width / 2)
        self.half_height = int(self.screen_height / 2)

    def screen_to_map(self, x, y):
        # convert screen coordinates to map coordinates
        x = x + self.camera_x
        y = y + self.camera_y
        return x, y

    def map_to_screen(self, x, y):
        # convert map coordinates to screen coordinates
        x = x - self.camera_x
        y = y - self.camera_y
        return x, y

    def update(self, entity, map_width, map_height):
        # update camera position
        self.camera_x = entity.x - self.screen_width // 2
        self.camera_y = entity.y - self.screen_height // 2

        self.camera_x = min(self.camera_x, map_width - self.screen_width)
        self.camera_y = min(self.camera_y, map_height - self.screen_height)
        self.camera_x = max(0, self.camera_x)
        self.camera_y = max(0, self.camera_y)
