

class Game:
    def __init__(self, date, time, team_1, team_2):
        self.date = date
        self.time = time
        self.team_1 = team_1
        self.team_2 = team_2
        self.result = ""
        self.prediction = ""

    def __str__(self):
        return self.date + " " + self.time + " " + self.team_1 + " : " + self.team_2 + "--" + str(self.result)

    def set_result(self, result):
        self.result = result