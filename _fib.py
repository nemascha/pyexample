


class F;
    def __init__(self, x, y):
        self.x = x
        self.y = y

x = F(1, 1)
t = x.y

x.y = x.x + x.y
x.x = t