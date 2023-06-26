#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0

    for i in range(0, 3):
        try:
            if i > a:
                raise Exception('Too far')
            result += a ** b / i
        except ZeroDivisionError:
            result = a + b
        except Exception:
            result = a + b
            break
    else:
        result = result + 3

    return result
