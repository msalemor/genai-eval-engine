# GenAI Evaluation Engine

An a dynamic model evaluation engine that compares baseline text against generated text.

## Evalulation JSON data

> Note: The criteria here is for Clarity, Conciseness, etc., but this could change depending the required evaluation.

```json
{
    "system": "You are an AI that can help evaluate a baseline text agaisnt an output text. Use the following criteria for the evaluation:\n\n<CRITERIA>\nScore the criteria from 1-10 with 10 being the best score. Respond in JSON format only. No epilogue or prologue is needed.",
    "criteria": "Clarity\nConciseness\nCorrectness\nCompleteness\nConsistency\nCoherence\n",
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
Copilot baseline generation:

Write two similar sentences about Azure API Management. Make the second one unclear and incoherent.

Results:
1. Azure API Management is a platform that helps developers manage APIs by providing tools for security, monitoring, and scaling.
2.Azure API Management, being a thing with APIs and management, does the managing of APIs in a way that involves stuff like policies, gateways, and maybe clouds, but also other things that are important for APIs to be managed, somehow.
```


### Actua run results

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