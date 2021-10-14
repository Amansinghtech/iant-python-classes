class Marks:
    def __init__(self, m1, m2) -> None:
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):  # magic method
        r1 = self.m1 + other.m1
        r2 = self.m2 + other.m2
        return Marks(r1, r2)

    def __str__(self) -> str:
        return "{} {}".format(self.m1, self.m2)


t1 = Marks(10, 20)
t2 = Marks(40, 30)

out = t1 + t2

print(out)
