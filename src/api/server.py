from fastapi import FastAPI
from pydantic import BaseModel
from src.agent.core import EnterpriseAgent

app = FastAPI(
    title="GTNIC 2026 AI Agent API",
    description="Enterprise Productivity Autonomous Agent Server",
    version="0.1.0",
)

agent = EnterpriseAgent()


class TaskRequest(BaseModel):
    task: str


@app.get("/")
def health_check():
    return {
        "status": "online",
        "competition": "GTNIC 2026",
        "category": "AI Agent Development",
    }


@app.post("/api/agent/run")
def run_agent_task(payload: TaskRequest):
    result = agent.execute_task(payload.task)
    return result
