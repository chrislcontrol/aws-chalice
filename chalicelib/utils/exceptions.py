from chalice import ChaliceUnhandledError


class IntegrityError(Exception):
    pass


class HttpError(ChaliceUnhandledError):
    def __init__(self, message: str, status: int = 400, code: str = "Invalid"):
        self.message = message
        self.status = status
        self.code = code

    def get_detail(self) -> dict:
        return {
            "Code": self.code,
            "Message": self.message
        }
