from abc import ABCMeta
from typing import Any


class SingletonMeta(ABCMeta):
    instances = {}

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls not in cls.instances:
            cls.instances[cls] = super().__call__(*args, **kwds)

        return cls.instances[cls]
    
