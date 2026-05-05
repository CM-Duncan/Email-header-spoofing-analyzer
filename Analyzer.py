"""
Caroline Duncan
5/1/25

Email Header Spoofing Analyzer
"""
import email
import re
import ipaddress
from email.utils import parseaddr, getaddresses
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class EmailHeaderAnalysis:
    from_address: str = ""
    from_name: str = ""
    