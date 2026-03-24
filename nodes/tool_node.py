from langchain_community.tools import DuckDuckGoSearchRun

duck_search = DuckDuckGoSearchRun()

def tool_node(state: dict):

    """
    Tool-based information retrieval node that fetches real-time fashion trends 
    from external sources when relevant.

    This node analyzes the user's query to detect keywords such as 
    "latest", "trend", "new", or "fashion". If such keywords are present, 
    it triggers a web search using DuckDuckGo to retrieve up-to-date information.

    If no relevant keywords are found, the node skips tool usage and returns 
    an empty response to avoid unnecessary API calls.

    The retrieved results provide dynamic, real-world insights that can 
    complement rule-based and LLM-generated responses, ensuring the system 
    stays current with evolving fashion trends.
    """


    query = state["user_input"]

    if not any(word in query.lower() for word in ["latest", "trend", "new", "fashion"]):
        return {"tool_response": ""}

    ddg_results = duck_search.run(query)

    return {
        "tool_response": ddg_results
    }

