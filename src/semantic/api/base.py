from abc import ABC, abstractmethod


class EmbeddingAPI(ABC):
    @abstractmethod
    def encode(self, text: str) -> list[float]:
        pass


class LLMAPI(ABC):
    @abstractmethod
    def generate(self, prompt: str, **kwargs) -> str:
        pass