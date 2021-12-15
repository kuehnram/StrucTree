from dataclasses import dataclass, field
from typing import List


@dataclass
class Entry:
    name: str
    children: List["Entry"] = field(default_factory=list)
