from fastapi import HTTPException, status

class TodoException(HTTPException):
    def __init__(self, detail: str, status_code: int = status.HTTP_400_BAD_REQUEST):
        super().__init__(status_code=status_code, detail=detail)

class UnauthorizedException(TodoException):
    def __init__(self, detail: str = "Unauthorized"):
        super().__init__(detail=detail, status_code=status.HTTP_401_UNAUTHORIZED)

class ForbiddenException(TodoException):
    def __init__(self, detail: str = "Forbidden"):
        super().__init__(detail=detail, status_code=status.HTTP_403_FORBIDDEN)

class NotFoundException(TodoException):
    def __init__(self, detail: str = "Not Found"):
        super().__init__(detail=detail, status_code=status.HTTP_404_NOT_FOUND)

class ValidationException(TodoException):
    def __init__(self, detail: str = "Validation Error"):
        super().__init__(detail=detail, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

# Default exception handlers
def handle_exception(e: Exception):
    """Generic exception handler"""
    if isinstance(e, TodoException):
        raise e
    else:
        raise TodoException(detail=str(e))