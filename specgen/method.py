from enum import Enum


class Method(Enum):
    POST = 1
    GET = 2
    PATCH = 3
    DELETE = 4

    ADD = -1
    PRINT = -2
    SET = -3
    REMOVE = -4

    def __str__(self):
        return self.value.lower()

    def to_mikrotik(self):
        return Method(-abs(self.value))

    def to_http(self):
        return Method(abs(self.value))

    @classmethod
    def mikrotik_methods(cls):
        return filter(lambda method: method.value < 0, iter(cls))

    @classmethod
    def http_methods(cls):
        return filter(lambda method: method.value > 0, iter(cls))

    @classmethod
    def unsafe_methods(cls):
        return filter(lambda method: abs(method.value) != 2, iter(cls))