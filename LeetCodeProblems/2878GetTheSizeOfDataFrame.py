import pandas as pd

def getDataframeSize(players):
    sizeDF = list(players.shape)
    return sizeDF

players = pd.DataFrame({"playerID": [846, 749, 155, 583, 388, 883, 355, 247, 761, 642], "name": ["Mason", "Riley", "Bob", "Isabella", "Zachary", "Ava", "Violet", "Thomas", "Jack", "Charlie"], "age": [21,30,28,32,24,23,18,27,33,36], "position": ["Forward", "Winger", "Striker", "Goalkeeper", "Midfielder", " Defender", "Striker", "Striker", "Midfielder", "Center-back"], "team": ["RealMadrid", "Barcelona", "ManchesterUnited", "Liverpool", "BayernMunich", "Chelsea", "Juventus", "ParisSaint-German", "MachesterCity", "Arsenal"] })
print(players.head())
answer = getDataframeSize(players)
print(answer)
