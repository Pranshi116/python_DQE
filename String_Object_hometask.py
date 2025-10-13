import re  # Regular expressions for pattern replacements

# Step 1: Copy the given text into a variable (use triple quotes to preserve formatting)
text = """
  tHis iz your homeWork, copy these Text to variable.

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

# Step 2: Normalize letter cases (make proper capitalization)
normalized_text = text.lower().capitalize()

# Step 3: Fix "iz" → "is", but only when it is a mistake
# The rule: replace " iz " with " is " (surrounded by spaces)
normalized_text = re.sub(r'\biz\b', 'is', normalized_text)

# Step 4: Create one more sentence from the last words of each sentence
# Split sentences by period
sentences = [s.strip() for s in normalized_text.split('.') if s.strip()]

# Extract last word from each sentence
last_words = [s.split()[-1] for s in sentences]

# Join them into a new sentence
extra_sentence = ' '.join(last_words).capitalize() + '.'

# Add this new sentence to the paragraph
final_text = '. '.join(sentences) + '. ' + extra_sentence

# Step 5: Count all whitespace characters (spaces, newlines, tabs, etc.)
whitespace_count = len(re.findall(r'\s', text))

# Step 6: Print the results
print("Normalized and corrected text:\n")
print(final_text)
print("\nNumber of whitespace characters:", whitespace_count)
