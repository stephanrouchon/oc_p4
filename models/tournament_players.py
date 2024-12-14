class TournamentPlayer:
    def __init__(self, player, score=0,  opponents=None):
        self.player = player
        self.score = score
        self.opponents = [] if opponents is None else opponents

    def __to_dict__(self):
        return {
            "player": self.player.id,
            "score": self.score,
            "opponents": self.opponents
        }
    def __str__(self):
        return f"{self.player} - {self.score} - {self.opponents}"