# @author: mohanlal.prajapati
# created date: 08-10-2021
import logging
from logging import LogRecord


class MyCustomFilter(logging.Filter):
    def filter(self, record):
        record.prefixname = "Twilio Log"
        return True


class CustomFileHandler(logging.FileHandler):

    def emit(self, record: LogRecord) -> None:
        record.msg = f'My Test File Prefix:{record.msg}'
        super()._open()
        super().emit(record)
        super().close()
        return None


class CustomLogHandler(logging.StreamHandler):

    def emit(self, record: LogRecord) -> None:
        record.msg = f'My Test Prefix:{record.msg}'
        msg = self.format(record)
        stream = self.stream
        stream.write(msg)
        self.flush()
        return None
        # return None
