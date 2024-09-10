#!/usr/bin/env python3
"""Personal Data."""
import re
"""Importing regex module."""


def filter_datum(fields, redaction, message, separator):
    pattern = r'({})=([^{sep}]+)'.format('|'.join(fields), sep=re.escape(separator))
    return re.sub(pattern, r'\1={}'.format(redaction), message)
