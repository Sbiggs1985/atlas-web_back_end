#!/usr/bin/env python3
"""Personal Data."""
import re
import logging
import csv
import os
from typing import List
"""Importing regex module."""


def filter_datum(fields, redaction, message, separator):