import re

def tokenize(text):
    tokens = re.findall(r'\w+|[^\w\s]', text, re.UNICODE)

    print("\nTokenised ecodings:")
    for token in tokens:
        codepoints_str = "".join(f"{ord(char)}" for char in token)
        print(f" {token} : => {codepoints_str}")

    print("\nTokens:")
    print(tokens)

    print(f"\nTotal number of tokens: {len(tokens)}\n")

while True: 
    print("Press Ctrl+C to exit.")
    try:
        user_input = input("Enter text to tokenize: ")
        tokenize(user_input)
    except KeyboardInterrupt:
        print("\nExiting...")
        break

