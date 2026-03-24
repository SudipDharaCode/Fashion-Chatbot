from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",
                             google_api_key="api_key")

def selector_node(state: dict):

    user_input = state["user_input"].lower()

    if any(word in user_input for word in ["elegant", "modern", "stylish", "look"]):
        return {"final_response": state["llm_response"]}

    if state["tool_response"]:
        return {"final_response": state["tool_response"]}

    if state["rule_response"]:
        return {"final_response": state["rule_response"]}

    return {"final_response": state["llm_response"]}


