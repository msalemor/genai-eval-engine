from evaluator.utils.evaldata import EvaluationData
from evaluator.utils.openaihelper import completion


async def evaluate(eval_data: EvaluationData) -> dict:
    """
    Evaluate the actual output against the expected output using the base output as a reference.
    """
    # Load the base, expected, and actual outputs
    criteria = eval_data.criteria
    system = eval_data.system.replace("<CRITERIA>", criteria)
    # with Jinja2 templates
    # system = render_template(eval_data.system, criteria=criteria)
    user_tempate = eval_data.user

    for data in eval_data.data:
        # Prepare the messages
        baseline = data["baseline"]
        output = data["output"]
        user_content = user_tempate.replace("<BASELINE>", baseline)
        user_content = user_content.replace("<OUTPUT>", output)
        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": user_content},
        ]

        # Get the evaluation completion
        # compare: baseline vs output against the criteria
        res = await completion(messages)

        # Print the results
        print(f"Baseline: {baseline}")
        print(f"Output: {output}")
        print(f"Evaluation results:\n{res}\n\n")
