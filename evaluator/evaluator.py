import asyncio
import json
from typing import Any

from evaluator.utils.evaldata import EvaluationData
from evaluator.utils.openaihelper import completion


def read_file(path: str) -> dict:
    """
    Load the evaluation file.
    """
    with open(path, "r") as file:
        return file.read()


async def evaluate(eval_data: EvaluationData) -> dict:
    """
    Evaluate the actual output against the expected output using the base output as a reference.
    """
    # Load the base, expected, and actual outputs
    criteria = eval_data.criteria
    system = eval_data.system.replace("<CRITERIA>", criteria)
    user_tempate = eval_data.user

    for data in eval_data.data:
        # Prepare the messages
        baseline = data["baseline"]
        expected = data["output"]
        user_content = user_tempate.replace("<BASELINE>", baseline)
        user_content = user_content.replace("<OUTPUT>", expected)
        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": user_content},
        ]

        # Get the evaluation completion
        res = await completion(messages)

        # Print the results
        print("Baseline:", baseline)
        print("Output:", expected)
        print(f"Evaluation results:\n{res}")
