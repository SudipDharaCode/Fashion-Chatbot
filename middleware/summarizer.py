from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",
                             google_api_key="AIzaSyChqARrd2KT3_AUhJBhK_Kfg2PjdTL0K1o")

def summarize_history(history):

    prompt = f"""
            Summarize this conversation:

            {history}
            """

    res = llm.invoke(prompt)

    return res.content


def save_memory(state: dict):
    history = state.get("history", [])
    
    new_entry = f"User: {state['user_input']} | Bot: {state['final_response']}"
    history.append(new_entry)

    if len(history) > 10:
        summary = summarize_history("\n".join(history))
        history = [summary]

    return {
        "history": history
    }