# GenAI Evaluation Engine

An a dynamic GenAI evaluation engine that compares baseline text against generated text for multiple criteria. The system prompt, criteria, and evaluation prompts are customizble to suite any criteria evaluation.

## OpenAI Configuration

```json
response_format={"type": "json_object"}
```

## Evalulation JSON data

> Note: The criteria here is for Clarity, Conciseness, etc., but this could change depending the required evaluation.

```json
{
    "system": "You are an AI designed to evaluate a baseline text against an output text. Follow these instructions carefully:\n1. Use the following evaluation criteria:\n<CRITERIA>\n2.For each criterion, assign a score from 1 to 10, where:\n- 1 represents the lowest performance.\n- 10 represents the highest performance.\n3. Base your evaluation only on the provided baseline and output text. Do not use external knowledge or assumptions.\n-4. Provide your response exclusively in JSON format.",
    "criteria": "- Clarity\n- Conciseness\n- Correctness\n- Completeness\n- Consistency\n- Coherence\n",
    "user": "Baseline:\n\n<BASELINE>\n\nOutput:\n\n<OUTPUT>\n\n",
    "data": [
        {
            "baseline": "The water is clear.",
            "output": "The water is translucent."
        },
        {
            "baseline": "Azure API Management is a multifaceted platform designed to facilitate the orchestration, governance, and operational oversight of API ecosystems, encompassing a myriad of functionalities that cater to diverse integration scenarios and security paradigms.",
            "output": "Azure API Management, being a thing with APIs and management, does the managing of APIs in a way that involves stuff like policies, gateways, and maybe clouds, but also other things that are important for APIs to be managed, somehow."
        }
    ]
}
```

## Sample run

### Sample data generation

```text
Copilot:

Write two similar sentences about Azure API Management. Make the second one unclear and incoherent.

Copilot Result:
1. Azure API Management is a platform that helps developers manage APIs by providing tools for security, monitoring, and scaling.
2. Azure API Management, being a thing with APIs and management, does the managing of APIs in a way that involves stuff like policies, gateways, and maybe clouds, but also other things that are important for APIs to be managed, somehow.
```

### Actual run results

```text
Baseline: The water is clear.
Output: The water is translucent.
Evaluation results:
{
  "Clarity": 9,
  "Conciseness": 10,
  "Correctness": 8,
  "Completeness": 9,
  "Consistency": 7,
  "Coherence": 8
}

Baseline: Azure API Management is a multifaceted platform designed to facilitate the orchestration, governance, and operational oversight of API ecosystems, encompassing a myriad of functionalities that cater to diverse integration scenarios and security paradigms.
Output: Azure API Management, being a thing with APIs and management, does the managing of APIs in a way that involves stuff like policies, gateways, and maybe clouds, but also other things that are important for APIs to be managed, somehow.
Evaluation results:
{
  "Clarity": 3,
  "Conciseness": 4,
  "Correctness": 2,
  "Completeness": 3,
  "Consistency": 3,
  "Coherence": 2
}
```