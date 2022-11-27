def dec_val(func):
    def wrapper_func():
        print("wrapped")
        return func
    return wrapper_func()


@dec_val
def my_func():
    print("hi")

my_func()