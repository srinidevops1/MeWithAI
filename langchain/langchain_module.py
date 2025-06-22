import re

greeting_patterns = [
    r'\bhello\b', r'\bhi\b', r'\bhey\b', r'\bnamaste\b', r'\bహలో\b', r'\bనమస్తే\b', r'\bహాయ్\b',
    r'\bgood morning\b', r'\bgood afternoon\b', r'\bgood evening\b', r'\bgood night\b',
    r'\bwelcome\b', r'\bbye\b', r'\bgoodbye\b', r'\bsee you\b', r'\bthank you\b', r'\bthanks\b',
    r'\bధన్యవాదాలు\b', r'\bస్వాగతం\b', r'\bశుభోదయం\b', r'\bశుభ సాయంత్రం\b', r'\bశుభ రాత్రి\b', r'\bవీడ్కోలు\b', r'\bమళ్ళీ కలుద్దాం\b'
]

def process_text(text):
    text_lower = text.lower()
    for pattern in greeting_patterns:
        if re.search(pattern, text_lower):
            return {'type': 'greeting', 'text': text}
    # Add more rules for other intents here
    return {'type': 'query', 'text': text} 