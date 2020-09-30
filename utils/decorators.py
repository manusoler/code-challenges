def challenge(*args, **kwargs):
    def inner(func):
        def wrapper(*args1, **kwargs1):
            print("Running challenge from {}...\nName: {} ({})\nDescription:{}".format(kwargs["website"],kwargs["name"],kwargs["level"],kwargs["desc"]))
            func(*args1, **kwargs1)
        return wrapper
    return inner