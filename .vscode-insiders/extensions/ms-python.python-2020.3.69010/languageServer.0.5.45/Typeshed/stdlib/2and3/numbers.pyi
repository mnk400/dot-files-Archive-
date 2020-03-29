# Stubs for numbers (Python 3.5)
# See https://docs.python.org/2.7/library/numbers.html
# and https://docs.python.org/3/library/numbers.html
#
# Note: these stubs are incomplete. The more complex type
# signatures are currently omitted.

from typing import Optional, SupportsFloat
from abc import ABCMeta, abstractmethod
import sys

class Number(metaclass=ABCMeta):
    @abstractmethod
    def __hash__(self) -> int: ...

class Complex(Number):
    @abstractmethod
    def __complex__(self) -> complex: ...
    if sys.version_info >= (3, 0):
        def __bool__(self) -> bool: ...
    else:
        def __nonzero__(self) -> bool: ...
    @property
    @abstractmethod
    def real(self): ...
    @property
    @abstractmethod
    def imag(self): ...
    @abstractmethod
    def __add__(self, other): ...
    @abstractmethod
    def __radd__(self, other): ...
    @abstractmethod
    def __neg__(self): ...
    @abstractmethod
    def __pos__(self): ...
    def __sub__(self, other): ...
    def __rsub__(self, other): ...
    @abstractmethod
    def __mul__(self, other): ...
    @abstractmethod
    def __rmul__(self, other): ...
    if sys.version_info < (3, 0):
        @abstractmethod
        def __div__(self, other): ...
        @abstractmethod
        def __rdiv__(self, other): ...
    @abstractmethod
    def __truediv__(self, other): ...
    @abstractmethod
    def __rtruediv__(self, other): ...
    @abstractmethod
    def __pow__(self, exponent): ...
    @abstractmethod
    def __rpow__(self, base): ...
    def __abs__(self): ...
    def conjugate(self): ...
    def __eq__(self, other: object) -> bool: ...
    if sys.version_info < (3, 0):
        def __ne__(self, other: object) -> bool: ...

class Real(Complex, SupportsFloat):
    @abstractmethod
    def __float__(self) -> float: ...
    @abstractmethod
    def __trunc__(self) -> int: ...
    if sys.version_info >= (3, 0):
        @abstractmethod
        def __floor__(self) -> int: ...
        @abstractmethod
        def __ceil__(self) -> int: ...
        @abstractmethod
        def __round__(self, ndigits: Optional[int] = ...): ...
    def __divmod__(self, other): ...
    def __rdivmod__(self, other): ...
    @abstractmethod
    def __floordiv__(self, other): ...
    @abstractmethod
    def __rfloordiv__(self, other): ...
    @abstractmethod
    def __mod__(self, other): ...
    @abstractmethod
    def __rmod__(self, other): ...
    @abstractmethod
    def __lt__(self, other) -> bool: ...
    @abstractmethod
    def __le__(self, other) -> bool: ...
    def __complex__(self) -> complex: ...
    @property
    def real(self): ...
    @property
    def imag(self): ...
    def conjugate(self): ...

class Rational(Real):
    @property
    @abstractmethod
    def numerator(self) -> int: ...
    @property
    @abstractmethod
    def denominator(self) -> int: ...
    def __float__(self) -> float: ...

class Integral(Rational):
    if sys.version_info >= (3, 0):
        @abstractmethod
        def __int__(self) -> int: ...
    else:
        @abstractmethod
        def __long__(self) -> long: ...
    def __index__(self) -> int: ...
    @abstractmethod
    def __pow__(self, exponent, modulus=None): ...
    @abstractmethod
    def __lshift__(self, other): ...
    @abstractmethod
    def __rlshift__(self, other): ...
    @abstractmethod
    def __rshift__(self, other): ...
    @abstractmethod
    def __rrshift__(self, other): ...
    @abstractmethod
    def __and__(self, other): ...
    @abstractmethod
    def __rand__(self, other): ...
    @abstractmethod
    def __xor__(self, other): ...
    @abstractmethod
    def __rxor__(self, other): ...
    @abstractmethod
    def __or__(self, other): ...
    @abstractmethod
    def __ror__(self, other): ...
    @abstractmethod
    def __invert__(self): ...
    def __float__(self) -> float: ...
    @property
    def numerator(self) -> int: ...
    @property
    def denominator(self) -> int: ...
