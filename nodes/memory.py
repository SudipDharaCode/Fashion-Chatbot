def load_memory(state: dict):
    history = state.get("history", [])

    context = "\n".join(history[-5:])  

    return {
        "memory": context
    }


