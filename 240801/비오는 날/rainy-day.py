class Info:
    def __init__(self, time, day, weather):
        self.time = time
        self.day = day
        self.weather = weather

infos = []
answer = []
n = int(input())
for _ in range(n):
    a, b, c = input().split()
    infos.append(Info(a, b, c))
sorted_infos = sorted(infos, key=lambda x: x.time, reverse=True)
for i in range(n):
    if sorted_infos[i].weather == "Rain":
        answer = sorted_infos[i]
print(answer.time, answer.day, answer.weather)