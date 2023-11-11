move()
while not at_goal():
    if object_here():
        take()
    else:
        if front_is_clear():
            move()
        else:
            if wall_in_front():
                turn_left()
            else:
                done()