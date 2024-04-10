import turtle
import random

#definindo tamanho da tela e da comida
w = 1000
h = 800
food_size = 20
delay = 100

#definindo direções dos controles
offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

#definindo a função que inicia junto com o jogo, a cobra se move pra cima e no tamanho "X"
def reset():
    global snake, snake_dir, food_position, pen
    snake = [[0,0], [0,20], [0,40], [0,60], [0,80]]
    snake_dir = "up"
    food_position = get_random_food_position()
    food.goto(food_position)
    move_snake()
   
#definindo a função que faz a cobra se mover, e que adiciona um novo retangulo se ela comer
def move_snake():
    global snake_dir
    
    new_head = snake[-1].copy()
    new_head[0] = snake[-1][0] + offsets[snake_dir][0]
    new_head[1] = snake[-1][1] + offsets[snake_dir][1]
    
    if new_head in snake[:-1]:
        reset()
    else:
        snake.append(new_head)
        
        if not food_collision():
            snake.pop(0)
            
        if snake[-1][0] > w / 2:
            snake[-1][0] -= w
        elif snake[-1][0] < - w / 2:
            snake[-1][0] += w
        elif snake[-1][1] > h / 2:
            snake[-1][1] -= h
        elif snake[-1][1] < -h / 2:
            snake[-1][1] += h
            
        pen.clearstamps()
        
        for segment in snake:
            pen.goto(segment[0], segment[1])
            pen.stamp()
            
        screen.update()
        
        turtle.ontimer(move_snake, delay)
 
#definindo oq acontece com a comida apos ela ser tocada        
def food_collision():
    global food_position
    if get_distance(snake[-1], food_position) < 20:
        food_position = get_random_food_position()
        food.goto(food_position)
        return True
    return False
 
#definindo spawn da comida  
def get_random_food_position():
    x = random.randint(- w / 2 + food_size, w / 2 - food_size)
    y = random.randint(- h / 2 + food_size, h / 2 - food_size)
    return (x, y)
  
def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance

#definindo direções e controles
def go_up():
    global snake_dir
    if snake_dir != "down":
        snake_dir = "up"   
def go_right():
    global snake_dir
    if snake_dir != "left":
        snake_dir = "right"       
def go_down():
    global snake_dir
    if snake_dir != "up":
        snake_dir = "down"      
def go_left():
    global snake_dir
    if snake_dir != "right":
        snake_dir = "left"
        
screen = turtle.Screen()
screen.setup(w, h)
screen.title("Snake")
screen.bgcolor('#ACD473')
screen.setup(w, h)
screen.tracer(0)

pen = turtle.Turtle("square")
pen.color("#373635")
pen.penup()

food = turtle.Turtle()
food.shape("square")
food.color("pink")
food.shapesize(food_size / 20)
food.penup()

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_left, "Left")
screen.onkey(go_down, "Down")

reset()
turtle.done()
