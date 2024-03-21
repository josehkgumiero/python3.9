class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return f'Line({self.p1.__repr__()}, {self.p2.__repr__()})'