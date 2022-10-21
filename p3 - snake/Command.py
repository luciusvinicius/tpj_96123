from Snake import Snake

class Command:
    def __init__(self, snake):
        self.snake : Snake = snake
    
    def execute(self):
        raise NotImplemented
    
class Up(Command):
    def __init__(self, snake):
        super().__init__(snake)
    
    def execute(self):
        self.snake.direction = (0, -1)
        
        
class Down(Command):
    def __init__(self, snake):
        super().__init__(snake)
    
    def execute(self):
        self.snake.direction = (0, 1)
        
        
class Left(Command):
    def __init__(self, snake):
        super().__init__(snake)
    
    def execute(self):
        self.snake.direction = (-1, 0)

class Right(Command):
    def __init__(self, snake):
        super().__init__(snake)
    
    def execute(self):
        self.snake.direction = (1, 0)  
