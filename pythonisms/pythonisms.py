def say_hi():
    return 'hi'


def count_down(func):
    def inner(*args, **kwargs):
        print(3)
        print(2)
        print(1)
        return func(*args, **kwargs)
        
    return inner

@count_down
def say_hey():
    return 'hey'


print(say_hey())