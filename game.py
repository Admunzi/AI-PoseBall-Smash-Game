class GameManager:
    def __init__(self):
        self.difficulty = None
        self.total_balls = None
        self.remaining_balls = None
        self.speed = None

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    def set_balls(self, difficulty):
        match difficulty:
            case "easy":
                self.total_balls = 10
                self.remaining_balls = 10
                self.speed = 5
            case "medium":
                self.total_balls = 15
                self.remaining_balls = 15
                self.speed = 10
            case "hard":
                self.total_balls = 20
                self.remaining_balls = 20
                self.speed = 20

    def get_remaining_balls(self):
        return self.remaining_balls

    def get_difficulty(self):
        return self.difficulty

    def decrement_ball(self):
        self.remaining_balls -= 1

    def get_total_balls(self):
        return self.total_balls

    def get_speed(self):
        return self.speed
