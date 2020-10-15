class LooprError(Exception):
    def __init__(self, error_message, reason=None):
        super().__init__(error_message, reason)
        self.message = error_message
        self.reason = reason

    def __str__(self):
        return self.message + str(self.args)


class LooprAuthenticationError(LooprError):
    pass


class LooprInternalServerError(LooprError):
    pass


class LooprAuthorizationError(LooprError):
    pass


class LooprInvalidResourceError(LooprError):
    pass


class LooprInvalidAttributeError(LooprError):
    pass
