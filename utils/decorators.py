"""
Module with some decorators used in the project
"""

def challenge(*args, **kwargs):
    def inner(func):
        def wrapper(*args1, **kwargs1):
            print("Running challenge from {}...\nName: {} ({})\nDescription:{}".format(kwargs.get("website","?"),kwargs["name"],kwargs["level"],kwargs["desc"]))
            func(*args1, **kwargs1)
        return wrapper
    return inner