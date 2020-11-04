class LooprError(Exception):
    """
    Base Class For Exception.
    """

    def __init__(self, error_message, reason=None):
        """
        Args:
            error_message (str): Error Message about the exception.
            reason (str): Reason that cause the exception.
        """
        super().__init__(error_message, reason)
        self.message = error_message
        self.reason = reason

    def __str__(self):
        return self.message + str(self.args)


class LooprAuthenticationError(LooprError):
    """Raised when API KEY fails Authentication """


class LooprInternalServerError(LooprError):
    """Raised when the Loopr Server encounters an unexpected condition """


class LooprAuthorizationError(LooprError):
    """Raised when a user is unauthorized to perform a particular task """


class LooprInvalidResourceError(LooprError):
    """Raised when there is invalid resource """


class LooprInvalidAttributeError(LooprError):
    """Raised when there is invalid attribute"""
