class ExAuthorization(Exception):
    pass


class ErrorLoginPassword(ExAuthorization):
    pass


class ErrorPasswordRestriction(ExAuthorization):
    pass
