from typing import Any
from abc import ABCMeta


class SingletonMeta(ABCMeta):
    instances = {}

    def __call__(cls, *args, **kwargs) -> Any:
        if cls not in cls.instances:
            cls.instances[cls] = super().__call__(*args, **kwargs)
        return cls.instances[cls]
