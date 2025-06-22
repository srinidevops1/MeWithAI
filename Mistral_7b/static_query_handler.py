from .llm_mistral_7b import generate_response

system_prompt = (
    "You are a friendly assistant for a restaurant called 'MeWithAI'.\n"
    "You MUST respond in the same language as the user's question.\n"
    "Here is information about the restaurant to use when answering:\n"
    "- Timings: 10 AM to 10 PM every day.\n"
    "- Address: 123 Main Street, Food City.\n"
    "- Phone Number: +1-234-567-8900.\n"
    "Keep your answers short and polite."
)

def handle_static_query(user_input):
    # Format the prompt for the Chat API
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input},
    ]
    return generate_response(messages) 