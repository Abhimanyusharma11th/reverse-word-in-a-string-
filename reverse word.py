s = "the sky is blue"

def reverseWords(s: str) -> str:
    words = s.split()
    words.reverse()
    return " ".join(words)

print(reverseWords(s))
