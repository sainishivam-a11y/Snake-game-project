import pygame
import time
import random

pygame.init()

#Define colors
white = (255,255,255)
yellow = (255,255,102)
black = (0,0,0)
red = (213,50.80)
green = (0,255,0)
blue = (50, 153,213)

#display dimension
dis_width = 600
dis_height = 400

#define display
dis = pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption("snake game")

#clock and font object
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 1

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

#function to display score
def your_score(score):
    value = score_font.render("your score:"+str(score), True, white)
    dis.blit(value,[0,0])


    #function to draw the snake
    def our_snake(snake_block,snake_List):
      for x in snake_List:
        pygame.drawrect(dis,green,[x[0],x[1], snake_block, snake_block])


#function to display the message
def message(msg, color):
   mesg=font_style.render(msg,True,color)
   dis.blit(mesg,[dis_width/6,dis_height/3])


   #game loop
   def gameLoop():
    game_over = False
    game_close = False

    #initial snake position
    x1 = dis_width/2
    y1 = dis_height/2

    #snake body
    x1_change = 0
    y1_change = 0

    #snake body
    snake_list = []
    Length_of_snake = 1


    #generate food position
    foodx = round(random.randrange(0,dis_width-snake_block)/10.0)*10.0
    foody = round(random.randrange(0,dis_height-snake_block)/10.0)*10.0

    #game loop
    while not game_over:
      
      while game_close:
        dis.fill(blue)
        message("You Lost! Press C-Play Again or Q-Quit", red)
        your_score(Length_of_snake-1)
        pygame.display.update()

        for event in pygame.event.get():
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
               game_over = True
               game_close = False
            if event.key == pygame.Kc:
                gameLoop()

      #Handling keypresses
      for event in pygame.event.get():
        if event.type == pygame.Quit:
           game_over = True
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
             x1_change = -snake_block
             y1_change = 0
          elif event.key == pygame.K_RIGHT:
             x1_change = snake_block
             y1_change = 0
          elif event.key == pygame.K_UP:
             x1_change = -snake_block
             y1_change = 0
          elif event.key == pygame.K_DOWN:
             x1_change = snake_block
             y1_change = 0


      #if the snake hits the wall
      if x1 >= dis_width or x1 <0 or y1 >= dis_height or y1 < 0:
         game_close = True
      x1 += x1_change
      y1 += y1_change
      dis.fill(blue)
      pygame.draw.rect(dis, yellow, [foodx, foody, snake_block, snake_block])
      snake_Head = []
      snake_Head.append(x1)
      snake_Head.append(y1)
      snake_list.append(snake_Head)
      if len(snake_list)> Length_of_snake:
         del snake_list[0]

      for x in snake_list[:-1]:
        if x == snake_Head:
           game_close = True
      our_snake(snake_block, snake_list)
      your_score(Length_of_snake-1)

      

      
    
     
              
        
      




     

