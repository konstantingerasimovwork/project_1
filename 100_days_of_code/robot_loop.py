def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    while wall_in_front() and right_is_clear():
        turn_right()
        move()
    while wall_in_front():
        turn_left()
    while wall_on_right() and front_is_clear():
        move()
    
    
while not at_goal():
    if right_is_clear() and front_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        jump()