import logging
from typing import Optional


class LoggerService:
    """
    Logger service used for logging operations and cache hits
    to a dedicated log file.
    """

    _logger: logging.Logger = logging.getLogger("math_api_logger")
    _initialized: bool = False

    @classmethod
    def _initialize_logger(cls) -> None:
        if not cls._initialized:
            logging.basicConfig(
                filename='math_api.log',
                level=logging.INFO,
                format='%(asctime)s - %(levelname)s - %(message)s'
            )
            cls._initialized = True

    @classmethod
    def log_operation(cls, op: str, x: int, y: Optional[int], result: int) -> None:
        """
        Logs a completed operation with input parameters and result.
        """
        cls._initialize_logger()
        cls._logger.info(f"Operation: {op}, x={x}, y={y}, result={result}")

    @classmethod
    def log_cache_hit(cls, op: str, x: int) -> None:
        """
        Logs a cache hit for a previously computed operation.
        """
        cls._initialize_logger()
        cls._logger.info(f"[CACHE HIT] {op}({x}) - value returned from cache")
