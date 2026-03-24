from langchain_community.tools import DuckDuckGoSearchRun
from langchain_google_genai import ChatGoogleGenerativeAI


duck_search = DuckDuckGoSearchRun() 

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key="api_key",
    temperature=0.4
)

def tool_node(state: dict):
    """
    Tool-based information retrieval node that fetches real-time fashion trends 
    from external sources when relevant.

    Enhancements:
    - Uses stricter keyword filtering to avoid irrelevant searches
    - Cleans and summarizes raw search results using LLM
    - Prevents noisy or unrelated content from reaching the user
    """

    query = state["user_input"].lower()

    trend_keywords = ["latest", "trend", "trending", "new"]
    fashion_keywords = ["fashion", "outfit", "style", "wear", "clothing", "dress", "saree"]

    if not (
        any(word in query for word in trend_keywords) and
        any(word in query for word in fashion_keywords)
    ):
        return {"tool_response": ""}

    try:

        raw_results = duck_search.run(query)

        summary_prompt = f"""
        Extract ONLY fashion-related trends from the text below.
        Ignore news, politics, or unrelated topics.

        Provide 3-5 short bullet points.

        Text:
        {raw_results}
        """

        summary = llm.invoke(summary_prompt).content

        return {"tool_response": summary}

    except Exception as e:
        print("Tool Error:", e)
        return {"tool_response": ""}

