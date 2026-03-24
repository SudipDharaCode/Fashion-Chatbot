# state.py
from typing import TypedDict, List

class ChatState(TypedDict):
    user_input: str
    intent: str
    memory: str
    rule_response: str
    llm_response: str
    tool_response: str
    final_response: str
    history: List[str]