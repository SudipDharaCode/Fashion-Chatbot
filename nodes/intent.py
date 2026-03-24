from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",
                             google_api_key="AIzaSyChqARrd2KT3_AUhJBhK_Kfg2PjdTL0K1o")

def detect_intent(state: dict):

    prompt = f"""
            You are an intent classification engine for a fashion-focused conversational AI chatbot.

            Your task is to analyze the user's query and classify it into exactly ONE of the following intent categories:

            1. wedding  → Queries related to weddings (bridal wear, wedding sarees, traditional outfits, ceremonies)
            2. party    → Queries related to parties, evening events, modern or stylish outfits
            3. blouse   → Queries specifically about blouse design, patterns, stitching, or styling
            4. color    → Queries focused on colors, color combinations, or preferences
            5. general  → Any query that does not clearly fit into the above categories (fallback category)

            ---------------------
            Instructions:
            - Carefully understand the user’s intent, not just keywords.
            - Use semantic meaning (context), not only exact word matches.
            - If multiple intents are present, choose the MOST dominant one.
            - If the query is vague, unclear, or does not strongly match any category, return "general".
            - Do NOT explain your answer.
            - Do NOT return anything except the intent label.

            ---------------------
            User Query:
            {state['user_input']}

            """

    response = llm.invoke(prompt)
    intent = response.content.strip().lower()
    return {
        "intent": intent
    }