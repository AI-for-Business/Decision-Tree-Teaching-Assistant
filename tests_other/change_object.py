class Test:
    Name = ""

    def __init__(self, n):
        self.Name = n


def add_name(t):
    x = t.Name
    y = x + " Hallo"
    t.Name = y
    return t


t1 = Test("Boring")
t1 = add_name(t1)
print(t1.Name)
