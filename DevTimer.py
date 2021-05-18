from datetime import datetime

def functimer(func):
    def wrapper():
        start = datetime.now()
        result = func()
        print(datetime.now() - start)
        return result
    return wrapper()

@functimer
def listgen():
    l = [x for x in range(10000) if x % 2 == 0]
    return l


print(listgen)