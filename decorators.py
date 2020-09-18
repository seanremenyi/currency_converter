def format(func):
    def wrapper(*args, **kwargs):
        func_value = func(*args, **kwargs)
        formatted_value = "{:.2f}".format(func_value)
        return formatted_value
    return wrapper