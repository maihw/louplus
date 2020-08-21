"myfact module"

def factorial(num):
    """
    return get the number's *
    :arg num:we will counter the number's *
    :return:when then number is a fushu
    """
    if num >= 0:
        if num == 0:
            return 1
        return num * factorial(num - 1)
    else:
        return -1
