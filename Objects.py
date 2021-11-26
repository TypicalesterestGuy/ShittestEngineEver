class Object:
    def __init__(self, coords, spritepath, spritename, hitbox):
        self.coords = coords
        self.sprite_path = spritepath
        self.sprite_name = spritename
        self.hitbox = hitbox

class Player(Object):
    def __init__(self, coords, spritepath, spritename, hitbox):
        super().__init__(coords, spritepath, spritename, hitbox)
        self.jumping = False
        self.jCount = 5
        self.flighting = True
        self.speed = 5

    def moving(self, dir):
        self.coords[0] -= self.speed * dir

    def flight(self, dir):
        if self.flighting:
            self.coords[1] -= self.speed * dir

class SolidObject(Object):
    def __init__(self, coords, spritepath, spritename, hitbox):
        super().__init__(coords, spritepath, spritename, hitbox)

