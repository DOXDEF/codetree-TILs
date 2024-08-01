class Agent:
    def __init__(self, name, score):
        self.name = name
        self.score = score

agents = []
for _ in range(5):
    name, score = tuple(map(str, input().split()))
    agents.append(Agent(name, score))

low_score = 100
low_name = ''
for i in range(len(agents)):
    test = agents[i]
    if int(test.score) < low_score:
        low_score = int(test.score)
        low_name = test.name
print(low_name, low_score)