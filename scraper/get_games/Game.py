import props


class Game(object):
    def __init__(self, date, time, team_1, team_2):
        self.date = date
        self.time = time
        self.team_1 = team_1
        self.team_2 = team_2
        self.score = 0
        self.set_score()

    def desc(self):
        print(self.date + " " + self.time + " " + self.team_1 + " : " + self.team_2 + "--" + str(self.score))

    def set_score(self):
        try:
            self.score = props.raitings[self.team_1] + props.raitings[self.team_2]
        except Exception:
            print("ERROR: set_score()")
            self.desc()
            print("==================")

    def __str__(self):
        return "{} at {}, {}:{}, score {}".format(self.date, self.time, self.team_1, self.team_2, self.score)