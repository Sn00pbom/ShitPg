from src.Entity import Entity

class Basicbitch(Entity):
    anger = 5


    def rageHeal(self):
        if self.anger >10:
            self.hp += 7
