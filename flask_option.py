# pylint: disable=missing-docstring

import os

def start():
    """returns the right message"""
    env = os.getenv("FLASK_ENV")
    if env == "production":
        return "Running in production mode"
    elif env == "development":
        return "Running in development mode"
    else:
        return "Running in unkown mode"

if __name__ == "__main__":
    print(start())
