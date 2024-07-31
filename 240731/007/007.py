class code:
    def __init__(self, name, place, length):
        self.name = name
        self.place = place
        self.length = length

a, b, c = map(str, input().split())
code1 = code(a, b, c)
print("secret code : " + code1.name)
print("meeting point : " + code1.place)
print("time : " + code1.length)