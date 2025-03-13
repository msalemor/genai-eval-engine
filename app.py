import asyncio
from evaluator.utils.evaldata import EvaluationData, load_evaluation_data
from evaluator.evaluator import evaluate


async def main():
    # Load the evaluation JSON file in an EvaluationData object
    # file contains the evaluation prompts and the data
    evaluation_data: EvaluationData = load_evaluation_data(
        "./genai-eval-engine/sample_evaluation.json")

    # Perform the evaluation
    await evaluate(evaluation_data)


if __name__ == '__main__':
    asyncio.run(main())
