from pathlib import Path

from ..base_logger import BaseLogger, LogLevel
from ..base_logger_adapter import BaseLoggerAdapter
from ..loggers.cli_logger import CliLogger
from ..utils import validate_adapter_init


class CliLoggerAdapter(BaseLoggerAdapter):
    """
    CliLogger Adapter for CliLogging.
    """

    def __init__(self, log_level: LogLevel, write_logfile: bool, **kwargs):
        validate_adapter_init(log_level, write_logfile)

        self.log_level = log_level
        self.write_logfile = write_logfile
        self.kwargs = kwargs

    def get_instance(self, path: Path | None) -> "BaseLogger":
        return CliLogger(self.log_level, self.write_logfile, path, **self.kwargs)
