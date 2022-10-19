class Disc():

    def __init__(self, size : int):
        self.size = size

    def size(self):
        return self.size
    
    def __lt__(self, other):
        return self.size < other.size

    def __str__(self):
        return f"Disc {self.size}"
'''
disc = Disc(1)
disc2 = Disc(2)
disc3 = Disc(3)
disc4 = Disc(4)

print(disc > disc2)
'''