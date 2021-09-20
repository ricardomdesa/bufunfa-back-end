class BfBaseError(Exception):
    message = "Generic Bf Error"

    def __init__(self, message: str = None, *args) -> None:
        if message is not None:
            self.message = message
        super().__init__(self.message, *args)
