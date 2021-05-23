from datetime import datetime


def execution_time(func):
    def wrapper():
        start = datetime.now()
        result = func()
        print(datetime.now() - start)
        return result

    return wrapper()


@execution_time
def list_generator():
    return [x for x in range(10000) if x % 2 == 0]
