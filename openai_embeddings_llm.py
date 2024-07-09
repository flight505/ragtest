# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""The EmbeddingsLLM class."""

from graphrag.llm.base import BaseLLM
from graphrag.llm.types import (
    EmbeddingInput,
    EmbeddingOutput,
    LLMInput,
)
from typing_extensions import Unpack

from .openai_configuration import OpenAIConfiguration
from .types import OpenAIClientTypes


class OpenAIEmbeddingsLLM(BaseLLM[EmbeddingInput, EmbeddingOutput]):
    """A text-embedding generator LLM."""

    _client: OpenAIClientTypes
    _configuration: OpenAIConfiguration

    def __init__(self, client: OpenAIClientTypes, configuration: OpenAIConfiguration):
        self._client = client
        self._configuration = configuration

    async def _execute_llm(
        self, input: EmbeddingInput, **kwargs: Unpack[LLMInput]
    ) -> EmbeddingOutput | None:
        args = {
            "model": self._configuration.model,  # Use the model from configuration
            **(kwargs.get("model_parameters") or {}),
        }
        embedding_list = []
        for inp in input:
            # Use the _client instance variable and pass args
            embedding = self._client.embeddings(model=args["model"], prompt=inp)
            embedding_list.append(embedding["embedding"])
        return embedding_list
