from datetime import datetime


def measure_time(base_function):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()

        return_value = base_function(*args, **kwargs)

        end_time = datetime.now()
        duration = end_time - start_time
        print(f'Function "{base_function.__name__}" ran {duration.microseconds} microseconds.')

        return return_value

    return wrapper


def block_odd_minutes(base_function):
    def block_odd_minutes_wrapper(*args, **kwargs):
        minutes = datetime.now().minute
        if minutes % 2 == 0:
            return_value = base_function(*args, **kwargs)
            return return_value
        else:
            return 'Access denied', 403

    return block_odd_minutes_wrapper


@measure_time
def get_squares(to):
    squares = []
    for i in range(1, int(to)):
        squares.append(i * i)

    return squares
