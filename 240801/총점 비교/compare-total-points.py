class Score:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

scores = []
answer = []
n = int(input())
for _ in range(n):
    a, b, c, d = input().split()
    scores.append(Score(a, int(b), int(c), int(d)))
sorted_scores = sorted(scores, key=lambda x: (x.kor + x.eng + x.math))

for i in range(n):
    print(sorted_scores[i].name, sorted_scores[i].kor, sorted_scores[i].eng, sorted_scores[i].math)