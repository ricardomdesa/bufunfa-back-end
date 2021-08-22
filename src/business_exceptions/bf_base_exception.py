class BfBaseError(Exception):
    def __init__(self, message="Generic Error"):
        self.message = message
