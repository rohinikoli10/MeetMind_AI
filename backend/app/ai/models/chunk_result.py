from dataclasses import dataclass, field
from typing import Dict


@dataclass
class ChunkResult:
    """
    Represents a single chunk generated from
    a meeting transcript before embedding.
    """

    chunk_id: int

    meeting_id: int

    text: str

    metadata: Dict = field(default_factory=dict)