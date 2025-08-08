from datetime import datetime

def log(func):
    def wrapper(*arg, **kwarg):
        with open("backend/logger.log", "a") as file:
            file.write(f"Function name {func.__name__} executed at {datetime.now()} \n")
        return func(*arg, **kwarg)
    return wrapper