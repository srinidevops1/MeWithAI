from langchain.langchain_module import process_text

# Test with a greeting
result1 = process_text("హలో! మీరు ఎలా ఉన్నారు?")
print(result1)  # Should print: {'type': 'greeting', ...}

# Test with a query
result2 = process_text("What are your restaurant timings?")
print(result2)  # Should print: {'type': 'query', ...}