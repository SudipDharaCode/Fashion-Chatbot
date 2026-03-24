def rule_node(state: dict):

    """
    Rule-based fashion recommendation node that generates outfit suggestions 
    based on user intent, input keywords, and optional attributes like color.

    Supported intents include:
    - wedding: Recommends traditional sarees like Banarasi or Kanjeevaram with optional color enhancement.
    - party: Suggests modern sarees such as sequin or georgette, with styling tips for trendy looks.
    - blouse: Provides blouse style recommendations based on current trends and user preference (modern/traditional).
    - casual: Recommends comfortable cotton sarees suitable for everyday wear with optional pastel color suggestions.

    The function returns a structured response indicating whether the suggestion 
    was generated using predefined rules or should fall back to an LLM.
    """

    intent = state["intent"]
    user_input = state.get("user_input", "").lower()
    color = state.get("color", None)

    response = ""

    if intent == "wedding":
        response = "Try a rich Banarasi or Kanjeevaram saree for a royal look."
        if color:
            response += f" A {color} shade would enhance the traditional vibe."

    elif intent == "party":
        response = "Go for a sequin or georgette saree for a modern party look."
        if "modern" in user_input or "trendy" in user_input:
            response += " You can pair it with a sleek sleeveless blouse."

    elif intent == "blouse":
        response = "Boat neck and backless blouses are trending right now."
        if "traditional" in user_input:
            response += " You can also try elbow-length sleeves with embroidery."

    elif intent == "casual":
        response = "Opt for a light cotton saree for a comfortable casual look."
        if color:
            response += f" A {color} pastel shade would be perfect for daytime."

    
    if response:
        return {
            "rule_response": response,
            "source": "rule_based"
        }

    return {
        "rule_response": None,
        "source": "llm"
    }



