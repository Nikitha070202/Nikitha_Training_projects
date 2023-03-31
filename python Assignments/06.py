#longest word from the list
def longest_word(words):
    max_length = 0
    longest = ''
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
            longest = word
    return longest

# Example usage
words = ['TamilNadu', 'Karnataka', 'Maharashtra', 'Rajasthan']
longest = longest_word(words)
print(longest)  # Output
