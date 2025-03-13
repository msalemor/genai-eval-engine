from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class EvaluationData:
    system: str
    criteria: str
    user: str
    data: list
