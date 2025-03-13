import asyncio
from evaluator.utils.evaldata import EvaluationData
from evaluator.utils.openaihelper import completion
from evaluator.evaluator import evaluate, read_file


async def main():
    # Load the evaluation JSON file in an EvaluationData object
    # file contains the evaluation prompts and the data
    ec = EvaluationData.from_json(read_file(
        "/home/alex/github/msalemor/genai-eval-engine/sample_evaluation.json"))

    # Perform the evaluation
    await evaluate(ec)


if __name__ == '__main__':
    asyncio.run(main())
