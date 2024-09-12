#!/usr/bin/env python3
"""Personal Data."""
import re
import logging
import csv
from typing import List
"""Importing appropriate modules."""


PII_FIELDS: tuple = ("name", "email", "ssn", "password", "phone")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[Holberton] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = List[str] = fields

    def format(self, record: logging.LogRecord) -> str:
        """This is recieving data"""
        obfuscated_message: str = super().format(record)
        return filter_datum(
            self.fields, self.REDACTION, obfuscated_message, self.SEPARATOR
        )


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Obfuscate through parameters"""
    for field in fields:
        message = re.sub(field + "=.*?" + separator,
                         field + "=" + redaction + separator, message)
    return message


def main() -> None:
    """Main function to configure logger and process user data"""
    log: logging.logger = get_logger()
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM users;")

    for row in cursor:
        log.info(str(row[0]))
    cursor.close()
    db.close()


def get_logger() -> logging.Logger:
    """Return a configured logger."""
    log: logging.logger = logging.getLogger("user_data")
    log.setLevel(logging.INFO)
    log.propagate = False

    handler: logging.StreamHandler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))

    log.addHandler(handler)

    return log
