class Camera:
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
        x = -entity.x + int(self.width / 2)
        y = -entity.y + int(self.height / 2)

        # if x < 0:
        #     print('x < 0')
        #     x = 0
        # if y < 0:
        #     print('y < 0')
        #     y = 0
        if x > self.map_width - int(self.width / 2): 
            x = self.map_width - int(self.width / 2)
            print('x>')
        if y > self.map_height - int(self.height / 2): 
            print('y>')
            y = self.map_height - int(self.height / 2)

        # # limit scrolling to map size
        #x = min(0, x)  # left
        #y = min(0, y)  # top
        # # x = max(-(self.width - self.map_width), x)  # right
        # print(f'maxx: {max((self.map_width-self.width), x)}')
        # #x = max((self.map_width-self.width), x)
        # # y = max(-(self.height - self.map_height), y)  # bottom
        # print(f'maxy: {max((self.map_height - self.height), y)}')
        # #y = max((self.map_height - self.height), y)

        self.x, self.y = (x, y)