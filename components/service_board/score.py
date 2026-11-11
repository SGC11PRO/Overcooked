class Score:
    def __init__(self):
        self.score = 0
        
    def add_score(self, points: int):
        """Add points to the score."""
        self.score += points
        # print(self.score)