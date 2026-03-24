from langgraph.graph import StateGraph
from state import ChatState

from nodes.memory import load_memory
from nodes.intent import detect_intent
from nodes.rule_node import rule_node
from nodes.llm_node import llm_node
from nodes.tool_node import tool_node
from nodes.selector import selector_node
from middleware.summarizer import save_memory

builder = StateGraph(ChatState)

# nodes 
builder.add_node("load_memory_node", load_memory)
builder.add_node("intent_node", detect_intent)
builder.add_node("rule_node", rule_node)
builder.add_node("llm_node", llm_node)
builder.add_node("tool_node", tool_node)
builder.add_node("selector_node", selector_node)
builder.add_node("save_memory_node", save_memory)

# Entry
builder.set_entry_point("load_memory_node")

# Flow
builder.add_edge("load_memory_node", "intent_node")

builder.add_edge("intent_node", "rule_node")
builder.add_edge("intent_node", "llm_node")
builder.add_edge("intent_node", "tool_node")

builder.add_edge("rule_node", "selector_node")
builder.add_edge("llm_node", "selector_node")
builder.add_edge("tool_node", "selector_node")

builder.add_edge("selector_node", "save_memory_node")

# Compile
graph = builder.compile()



if __name__ == "__main__":
    
    state = {
        "user_input": "",
        "history": []
    }

    print("Fashion Chatbot Started (type 'exit' to stop)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        state["user_input"] = user_input

        result = graph.invoke(state)

        print("Bot:", result["final_response"])

        state["history"] = result["history"]

        