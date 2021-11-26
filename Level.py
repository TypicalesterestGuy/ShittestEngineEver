class Level:
    def __init__(self, curr, bg, *args):
        self.objs = []
        self.solobjs = []
        self.curr = curr
        self.bg = bg
        self.player_start_pos = list(args)

    def addobj(self, *args):
        self.objs += list(args)
        for i in args:
            if i.__class__.__name__ == "SolidObject":
                self.solobjs.append(i)
