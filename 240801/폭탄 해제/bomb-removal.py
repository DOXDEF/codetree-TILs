class Bomb:
    def __init__(self, code, color, time):
        self.code = code
        self.color = color
        self.time = time

a, b, c = map(str, input().split())
bombs = Bomb(a, b, c)

print("code : " + bombs.code)
print("color : " + bombs.color)
print("second : " + bombs.time)