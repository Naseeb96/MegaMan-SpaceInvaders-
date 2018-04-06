import turtle
import os
import math
import random


# Screen Setup
window = turtle.Screen()
window.bgcolor("black")
window.title("Space Invaders")
window.bgpic("background.gif")
turtle.register_shape("player.gif")
turtle.register_shape("shot.gif")
turtle.register_shape("enemy.gif")
turtle.register_shape("bullet.gif")


# Border Patrol
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# ScoreBoard
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# Create Player
playerSpeed = 30
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

# Player Bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("bullet.gif")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()
bulletSpeed = 45
# Bullet States Ready (Ready to Fire) Fire (Bullet Firing)
os.system("afplay charge.wav&")
bulletState = "Ready"
player.shape("player.gif")

# Enemy
enemySpeed = 5

# Number Of Enemies
number_of_enemies = 7
enemies = []
for i in range(number_of_enemies):
    # Create the enemies
    enemies.append(turtle.Turtle())
for enemy in enemies:
    enemy.color("red")
    enemy.shape("enemy.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)


# Player Movement
def move_left():
    x = player.xcor()
    x -= playerSpeed
    if x < -280:
        x = -280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += playerSpeed
    if x > 280:
        x = 280
    player.setx(x)


def fire_bullet():
    global bulletState
    if bulletState == "Ready":
        bulletState = "Fire"
        player.shape("shot.gif")
        os.system("afplay bullet.wav&")
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()


def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False


# Keyboard bindings

turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")
createEnemy = True
# Main Game
while True:
    # Bullet Movement
    if bulletState == "Fire":
        y = bullet.ycor() + bulletSpeed
        bullet.sety(y)
    # Check if bullet reached the top
    if bullet.ycor() > 275:
        if bulletState == "Fire":
            os.system("afplay charge.wav&")
        bullet.hideturtle()
        bulletState = "Ready"
        player.shape("player.gif")
    for enemy in enemies:
        counter = 0
        ++counter
        # Move Enemy
        x= enemy.xcor()
        x += enemySpeed
        enemy.setx(x)
        # Enemy Boundaries
        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemySpeed *= -1

        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemySpeed *= -1
        # Check if bullet hit enemy
        if isCollision(bullet, enemy):
            os.system("afplay explode.wav&")
            # Reset bullet
            bullet.hideturtle()
            bulletState = "Ready"
            os.system("afplay charge.wav&")
            player.shape("player.gif")
            bullet.setposition(0, -400)
            # Reset Enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            # Update Score
            score += 10
            scorestring = "Score: %s" % score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
        if isCollision(player, enemy):
            os.system("afplay Deleted.wav&")
            player.hideturtle()
            enemy.hideturtle()
            print("GAME OVER")
            window.clearscreen()
            window.bgcolor("black")
            window.title("GAME OVER - Click to Exit")
            window.bgpic("GameOver.gif")
            os.system("afplay GameOver.wav&")

            # Border Patrol
            border_pen = turtle.Turtle()
            border_pen.speed(0)
            border_pen.color("white")
            border_pen.penup()
            border_pen.setposition(-300, -300)
            border_pen.pendown()
            border_pen.pensize(3)
            for side in range(4):
                border_pen.fd(600)
                border_pen.lt(90)
            border_pen.hideturtle()
            window.exitonclick()
            break

