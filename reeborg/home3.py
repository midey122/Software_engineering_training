while not at_goal():
    if front_is_clear():
        move()
    else:
        if wall_in_front():
            turn_left()
        else :move()
            
