from abc import ABC, abstractmethod
from typing import Any, Dict
from pydantic import BaseModel, Field


class ToolResult(BaseModel):
    success: bool
    output: Any
    error: str | None = None


class BaseTool(ABC):
    """Abstract Base Class untuk setiap tool yang dapat dipanggil oleh AI Agent."""

    name: str
    description: str

    @abstractmethod
    def run(self, **kwargs: Any) -> ToolResult:
        """Eksekusi aksi tool dengan argumen yang diberikan."""
        pass

    def get_schema(self) -> Dict[str, Any]:
        """Mengembalikan metadata schema tool untuk integrasi function calling."""
        return {
            "name": self.name,
            "description": self.description,
        }
