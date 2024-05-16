#!/usr/bin/python3

e: def safe_print_division(a, b):
    result = 0
    try:
        resutl = a / b
    except ValueError:
        return None
    finally:
        print("{}".format(result))
    return result