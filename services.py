from logger import LoggerService



class MathService:
    """
    Provides static methods for common mathematical operations.
    """

    _fib_cache: dict[int, int] = {}

    @staticmethod
    def pow_fn(x: int, y: int) -> int:
        """
        Computes x raised to the power of y
        """
        return x ** y

    @staticmethod
    def factorial(n: int) -> int:
        """
        Computes the factorial of a non-negative integer.
        Raises ValueError for negative inputs.
        """
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")

        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    @classmethod
    def fibonacci(cls, n: int) -> int:
        """
        Computes the n-th Fibonacci number with memoization.
        Raises ValueError for negative inputs.
        """
        if n < 0:
            raise ValueError("Fibonacci index cannot be negative.")

        if n in cls._fib_cache:
            LoggerService.log_cache_hit("fibonacci", n)
            return cls._fib_cache[n]

        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b

        cls._fib_cache[n] = a
        return a
