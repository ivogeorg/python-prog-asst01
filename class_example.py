class MicroBit(object):
    def __init__(self):
        self.LEDs = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.motion = True
        self.light = True
        self.acceleration = 9.7

    def display(self, array):
        for i in range(len(array)):
            for j in range(len(array[0])):
                self.LEDs[i][j] = array[i][j]

    def in_motion(self):
        return self.motion

    def lit_up(self):
        return self.light

    def go_faster(self):
        self.acceleration = self.acceleration * 0.2


m = MicroBit()
print(m.LEDs)
if m.in_motion():
    star = [[0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 1, 1, 1, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]]
    m.display(star)
    m.go_faster()

print(m.LEDs)
