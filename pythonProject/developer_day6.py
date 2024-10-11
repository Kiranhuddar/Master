def first_function():
    print("Hello")
    print("Bye")

#first_function()
#Reeborg's world
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def destination():
    jump()
    jump()
    jump()
    jump()
    jump()
    jump()

number_of_hurdles = 6
while number_of_hurdles > 0:
    print("hello",number_of_hurdles)
    number_of_hurdles -= 1





