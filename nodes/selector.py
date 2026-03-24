
def selector_node(state: dict):

    user_input = state["user_input"].lower()

    if any(word in user_input for word in ["elegant", "modern", "stylish", "look"]):
        return {"final_response": state["llm_response"]}

    if state["tool_response"]:
        return {"final_response": state["tool_response"]}

    if state["rule_response"]:
        return {"final_response": state["rule_response"]}

    return {"final_response": state["llm_response"]}


