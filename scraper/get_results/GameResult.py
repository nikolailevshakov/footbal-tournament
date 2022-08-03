
class GameResult():
    def __init__(self, team_1, team_2, result):
        self.team_1 = team_1
        self.team_2 = team_2
        self.result = result

    def desc(self):
        print(self.team_1 + ":" + self.team_2 + " " + self.result)