import sys
from books_recommender.exception.exception_handler import AppException

try:
    a = 3/0

except Exception as e:
    raise AppException(e, sys) from e