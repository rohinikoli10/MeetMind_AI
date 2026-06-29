from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class EmbeddingResult:
    id: str
    meeting_id: int
    chunk_id: int
    text: str
    vector: List[float]
    metadata: Dict = field(default_factory=dict)