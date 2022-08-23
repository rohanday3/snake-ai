from food import Food

class Snake:
    def __init__(self) -> None:
        self.length = 0
        self.scale = 25
        self.head = [80, 80]
        # body length
        self.body = []
        self.direction = 'right'

    def move(self) -> None:
        # TODO: cant move into body stoopid
        if self.direction == 'right':
            self.head[0] += 5 if self.head[0] < (800/5)-5 else -(800/5)+5
        elif self.direction == 'left':
            self.head[0] -= 5 if self.head[0] > 0 else -(800/5)+5
        elif self.direction == 'up':
            self.head[1] -= 5 if self.head[1] > 0 else -(800/5)+5
        elif self.direction == 'down':
            self.head[1] += 5 if self.head[1] < (800/5)-5 else -(800/5)+5
        # move all body part to the head
        self.body.insert(0, self.head)
        for i in range(1,len(self.body)):
            self.body[i] = self.body[i-1]
        print(self.body)
        print(self.length)
        if len(self.body) > self.length:
            del self.body[-1]
            
        
    def turn(self, direction: str) -> None:
        self.direction = direction

    def isEating(self, Food) -> bool:
        if self.head[0] == Food.position[0] and self.head[1] == Food.position[1]:
            self.grow()
            return True
        return False

    def isInBody(self, x: int, y: int) -> bool:
        for i in range(len(self.body)):
            if self.body[i][0] == x and self.body[i][1] == y:
                return True
        return False

    def grow(self) -> None:
        self.length += 1
        print("grew")