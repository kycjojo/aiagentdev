from typing import List
from pydantic import BaseModel, Field


class PlanStep(BaseModel):
    step_number: int
    description: str
    target_tool: str | None = None
    completed: bool = False
    result: str | None = None


class ExecutionPlan(BaseModel):
    goal: str
    steps: List[PlanStep] = Field(default_factory=list)
