def announce(f):
    def wrapper():
        print("About to run a function")
        f()
        print("Done!")
    return wrapper


@announce
def hello():
    print("Hola mundo")


hello()
