from Mistral_7b.static_query_handler import handle_static_query

# Test with a greeting
print("Greeting Test:")
print(handle_static_query("Hi there!"))

# Test with a timings question
print("\nTimings Test:")
print(handle_static_query("What are your restaurant timings?"))

# Test with an address question
print("\nAddress Test:")
print(handle_static_query("Where is your restaurant located?"))

# Test with a phone number question
print("\nPhone Number Test:")
print(handle_static_query("What is your phone number?"))