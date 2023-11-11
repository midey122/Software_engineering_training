while not at_goal():
    if front_is_clear():
        move()
    else:
        done()