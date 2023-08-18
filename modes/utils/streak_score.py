class streak_score:
    def __init__(self):
        self.streak = 0
    
    def inc_point(self):
        self.streak += 1
    
    def reset_point(self):
        self.streak = 0
    
    def print_streak(self):
        print(self.streak)

streak = streak_score()