from keyboard import is_pressed


def up_arrow():
    if(is_pressed('up')):
        return True
    else:
        return False


def down_arrow():
    if(is_pressed('down')):
        return True
    else:
        return False


def left_arrow():
    if(is_pressed('left')):
        return True
    else:
        return False


def right_arrow():
    if(is_pressed('right')):
        return True
    else:
        return False
