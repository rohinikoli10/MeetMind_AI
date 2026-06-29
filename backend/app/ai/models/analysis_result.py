from dataclasses import dataclass, field
from typing import List


@dataclass
class AnalysisResult:
    """
    Standard output returned by any
    LLM meeting analysis engine.
    """

    summary: str

    minutes_of_meeting: str

    action_items: List[str] = field(default_factory=list)

    decisions: List[str] = field(default_factory=list)

    key_topics: List[str] = field(default_factory=list)

    sentiment: str = "Neutral"

    model_name: str = ""