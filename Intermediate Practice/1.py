words = ["apple", "bat", "cherry", "dog", "elderberry"]

Output = []
for word in words:
    if len(word) >= 4:
        Output.append(word.upper())

print(Output)

# words = ["apple", "bat", "cherry", "dog", "elderberry"]

# # Single line transformation and filtering
# filtered_words = [w.upper() for w in words if len(w) >= 4]

# print(f"Original: {words}")
# print(f"Result:   {filtered_words}")