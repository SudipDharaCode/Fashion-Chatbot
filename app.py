from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Any

from langgraph.graph import StateGraph
from state import ChatState

from nodes.memory import load_memory
from nodes.intent import detect_intent
from nodes.rule_node import rule_node
from nodes.llm_node import llm_node
from nodes.tool_node import tool_node
from nodes.selector import selector_node
from middleware.summarizer import save_memory


# Build LangGraph

builder = StateGraph(ChatState)

builder.add_node("load_memory_node", load_memory)
builder.add_node("intent_node", detect_intent)
builder.add_node("rule_node", rule_node)
builder.add_node("llm_node", llm_node)
builder.add_node("tool_node", tool_node)
builder.add_node("selector_node", selector_node)
builder.add_node("save_memory_node", save_memory)

builder.set_entry_point("load_memory_node")

builder.add_edge("load_memory_node", "intent_node")

builder.add_edge("intent_node", "rule_node")
builder.add_edge("intent_node", "llm_node")
builder.add_edge("intent_node", "tool_node")

builder.add_edge("rule_node", "selector_node")
builder.add_edge("llm_node", "selector_node")
builder.add_edge("tool_node", "selector_node")

builder.add_edge("selector_node", "save_memory_node")

graph = builder.compile()


# FastAPI App

app = FastAPI(title="Fashion Chatbot")


sessions: Dict[str, Dict[str, Any]] = {}

class ChatRequest(BaseModel):
    session_id: str
    user_input: str


class ChatResponse(BaseModel):
    response: str
    history: List


# Endpoint

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):

    if req.session_id not in sessions:
        sessions[req.session_id] = {
            "user_input": "",
            "history": []
        }

    state = sessions[req.session_id]

    state["user_input"] = req.user_input


    result = graph.invoke(state)


    sessions[req.session_id]["history"] = result["history"]

    return ChatResponse(
        response=result["final_response"],
        history=result["history"]
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


