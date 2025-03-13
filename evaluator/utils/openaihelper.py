from dataclasses import dataclass
from openai import AsyncAzureOpenAI
from evaluator.utils.settings import get_settings

settings = get_settings()

global _client
_client = None


def get_client():
    global _client
    if not _client:
        _client = AsyncAzureOpenAI(
            azure_endpoint=settings.endpoint,
            api_key=settings.api_key,
            api_version=settings.version

        )
    return _client


async def completion(messages: list[dict], temperature=0.1, max_tokens: int | None = None, model="gpt-4o") -> str:
    res = await get_client().chat.completions.create(model=model,
                                                     messages=messages,
                                                     response_format={
                                                         "type": "json_object"},
                                                     temperature=temperature,
                                                     max_tokens=max_tokens)
    return res.choices[0].message.content
