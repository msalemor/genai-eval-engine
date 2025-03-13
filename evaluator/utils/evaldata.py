from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class EvaluationData:
    system: str
    criteria: str
    user: str
    data: list


def load_evaluation_data(file_path: str) -> EvaluationData:
    with open(file_path, 'r') as f:
        data = f.read()
    return EvaluationData.from_json(data)
