def word_counter(text):
    if not text:
        return {}

    # Preprocess the text: convert to lowercase and remove punctuation
    text = text.lower().replace(",", "").replace("!", "").replace("?", "").replace(".", "")

    # Split the text into words
    words = text.split()

    # Initialize a dictionary to store word frequencies
    frequency = {}

    # Recursive helper function to process words
    def process_words(words, index):
        if index == len(words):
            return  # Base case: stop when all words are processed

        word = words[index]

        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

        # Recursive call for the next word
        process_words(words, index + 1)

    # Start processing words from index 0
    process_words(words, 0)

    return frequency

# Test the function
text = "This is a sample text. It contains some words. Some words are repeated, like 'is' and 'words'."
frequency_dict = word_counter(text)

# Print the word frequency dictionary
for word, count in frequency_dict.items():
    print(f"{word}: {count}")
