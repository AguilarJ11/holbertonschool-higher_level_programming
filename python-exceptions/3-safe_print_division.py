#!/usr/bin/python3

def safe_print_division(a, b):
    result = 0
    try:
        resutl = a / b
    except Exception:
        return None
    finally:
        print("Inside result: {}".format(result))
    return result
