for i in range(40):
    if front_is_clear():
        move()
    else:
        if wall_in_front():
            turn_left()
        else:
            done()