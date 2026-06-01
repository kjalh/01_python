# fruits/__init__.py
from .apple import info as apple_info, func1
from .banana import info as banana_info

# 예) import fruits
# 예) from fruits import apple_info, banana_info
# 예) from fruits import *(__all__ 등록한 것 만, 원래는 전부)
__all__ = ["apple_info", "banana_info", "func1"]   # __all__ 