"""
Implements sensor class
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Set, Optional
import uuid
import logging

logger = logging.getLogger(__name__)


@dataclass
class Sensor:
    sensor_name: str
    sensor_type: str
    sensor_id: str = field(default_factory=lambda: str(uuid.uuid4()), init=True)
    dependencies: Set[str] = field(default_factory=set)

    def rename(self, new_name: str) -> None:
        pass

    



