from config import *
import myPygameWorkflow
import pygame, random

class SceneGame(myPygameWorkflow.presets.Scene):
    def start(self):
        self.snake = Snake(self, 2)
        self.fruit = Fruit(self, 3)
        self.score = Score(self, 1)
        
        self.GAME_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(self.GAME_UPDATE, 150)
    
    def update(self):
        self.screen.fill('#000000')
    
    def event(self, event):
        if event.type == self.GAME_UPDATE:
            self.fixed_update()
            
        if event.type == pygame.KEYDOWN:
            self.key_logic(event)
    
    def fixed_update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
    
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.place_random()
            self.score.score += 1
            self.score.write_score()
            self.snake.add_block()
    
    def check_fail(self):
        if not 0 <= self.snake.body[0].x < SIZEX or not 0 <= self.snake.body[0].y < SIZEY:
            self.running = False
        
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.running = False
        
    def key_logic(self, event):
        if event.key == UP:
            if self.snake.direction.y != 1:
                self.snake.direction = pygame.Vector2(0, -1)
        elif event.key == DOWN:
            if self.snake.direction.y != -1:
                self.snake.direction = pygame.Vector2(0, 1)
        elif event.key == LEFT:
            if self.snake.direction.x != 1:
                self.snake.direction = pygame.Vector2(-1, 0)
        elif event.key == RIGHT:
            if self.snake.direction.x != -1:
                self.snake.direction = pygame.Vector2(1, 0)

class Snake(myPygameWorkflow.presets.Sprite):
    def start(self):
        self.image = pygame.Surface((WIN_WID, WIN_HEI))
        self.image.set_colorkey('#000000')
        self.rect = self.image.get_rect(topleft=(0,0))
        
        self.body = [pygame.Vector2(5,10), pygame.Vector2(4,10), pygame.Vector2(3,10)]
        self.direction = pygame.Vector2(1, 0)
        self.new_block = False
        self.draw_snake()
    
    def update(self):
        pass
    
    def draw_snake(self):
        self.image.fill('#000000')
        for index, block in enumerate(self.body):
            block_rect = pygame.Rect(int(block.x * TILESIZE), int(block.y * TILESIZE), TILESIZE, TILESIZE)
            if not index:
                pygame.draw.rect(self.image, SNAKE_HEAD_COLOR, block_rect)
            else:
                pygame.draw.rect(self.image, SNAKE_BODY_COLOR, block_rect)
    
    def move_snake(self):
        if self.new_block:
            body_copy = self.body[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
        
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]
        self.draw_snake()
    
    def add_block(self):
        self.new_block = True

class Fruit(myPygameWorkflow.presets.Sprite):
    def start(self):
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(FRUIT_COLOR)
        
        self.place_random()
    
    def place_random(self):
        x = random.randint(0, SIZEX-1)
        y = random.randint(0, SIZEY-1)
        self.pos = pygame.Vector2(x, y)
        self.placement = (int(self.pos.x * TILESIZE), int(self.pos.y * TILESIZE))
        self.rect = self.image.get_rect(topleft=self.placement)
        
    def update(self):
        pass
    
class Score(myPygameWorkflow.presets.Sprite):
    def start(self):
        self.font = pygame.font.Font(None, 32)
        self.score = 0
        self.write_score()
    
    def update(self):
        pass

    def write_score(self):
        self.image = self.font.render(str(self.score), True, SCORE_COLOR)
        self.rect = self.image.get_rect(topleft=SCORE_POS)
