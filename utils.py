import re

def truncate_to_complete_sentence(text, max_length):
    """Truncates text to the last complete sentence within the max length."""
    if len(text) <= max_length:
        return text

    truncated_text = text[:max_length]
    match = re.search(r'([.!?])[^.!?]*$', truncated_text)

    if match:
        return truncated_text[:match.end()].strip()
    
    return truncated_text.strip()
