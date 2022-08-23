from food import Food

class Snake:
    def __init__(self, scale=5, screen_size=800) -> None:
        self.length = 0
        self.screen_size = screen_size
        self.scale = scale
        self.size = scale**2
        self.head = [(screen_size/scale)//2, (screen_size/scale)//2]
        # body length
        self.body = []
        self.direction = 'right'

    def move(self) -> None:
        self.body.insert(0, self.head[::])
        if len(self.body) > self.length:
            del self.body[-1]
        if self.direction == 'right':
            self.head[0] += self.scale if self.head[0] < (self.screen_size/self.scale)-self.scale else -(self.screen_size/self.scale)+self.scale
        elif self.direction == 'left':
            self.head[0] -= self.scale if self.head[0] > 0 else -(self.screen_size/self.scale)+self.scale
        elif self.direction == 'up':
            self.head[1] -= self.scale if self.head[1] > 0 else -(self.screen_size/self.scale)+self.scale
        elif self.direction == 'down':
            self.head[1] += self.scale if self.head[1] < (self.screen_size/self.scale)-self.scale else -(self.screen_size/self.scale)+self.scale
            
        
    def turn(self, direction: str) -> None:
        self.direction = direction

    def isEating(self, Food) -> bool:
        if self.head[0] == Food.position[0] and self.head[1] == Food.position[1]:
            return True
        return False

    def isInBody(self, x: int, y: int) -> bool:
        for i in range(len(self.body)):
            if self.body[i][0] == x and self.body[i][1] == y:
                return True
        return False

    def grow(self) -> None:
        self.length += 1
