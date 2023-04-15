def logger_parametr(n):
    def logger(function):
        def wrapper(*args, **kwargs):
            for i in range(n):
                print("start", function.__name__)
                output = function(*args, **kwargs)
                print("end", function.__name__)
            return output

        return wrapper

    return logger


@logger_parametr(2)
def some_function(text):
    print(text)


some_function("Привет")
