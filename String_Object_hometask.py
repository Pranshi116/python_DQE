import re

# Step 1: Copy the given text into a variable (triple quotes preserve formatting)
text = """
  tHis iz your homeWork, copy these Text to variable.

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

# Step 2: Count all whitespace characters (spaces, newlines, tabs, etc.)
whitespace_count = len(re.findall(r'\s', text))

# Step 3: Replace incorrect "iz" → "is" but skip ones inside quotes
# We'll match "iz" as a whole word (\b) when not preceded/followed by quotes
fixed_text = re.sub(
    r'(?i)(?<![“"”])\biz\b(?![“"”])',  # skip if surrounded by quotes
    'is',
    text
)

# Step 4: Normalize capitalization properly (sentence case)
def sentence_case_paragraph(paragraph: str) -> str:
    # Split into sentences while keeping punctuation marks
    parts = re.split(r'([.!?])', paragraph)
    sentences = []

    for i in range(0, len(parts) - 1, 2):
        sentence = parts[i].strip()
        delimiter = parts[i + 1]

        if not sentence:
            continue

        # Lowercase the sentence, then capitalize first letter
        sentence = sentence.lower()
        first_alpha = re.search(r'[a-zA-ZÀ-ÖØ-öø-ÿ]', sentence)
        if first_alpha:
            idx = first_alpha.start()
            sentence = sentence[:idx] + sentence[idx].upper() + sentence[idx + 1:]

        # Fix standalone 'i' to uppercase 'I'
        sentence = re.sub(r'(?<=\s)i(?=\s|[,.!?;:\)\"]|$)', 'I', sentence)
        sentence = re.sub(r'^(i)(?=\s|$)', 'I', sentence)

        sentences.append(sentence + delimiter)

    # Rebuild text
    normalized = ' '.join(sentences)
    return normalized.strip()

normalized_text = sentence_case_paragraph(fixed_text)

# Step 5: Create a new sentence from last words of each existing sentence
sentences = [s.strip() for s in re.split(r'[.!?]\s*', normalized_text) if s.strip()]
last_words = [re.sub(r'[^\w\'-]+$', '', s.split()[-1]) for s in sentences]
extra_sentence = ' '.join(last_words).capitalize() + '.'

# Step 6: Add the new sentence to the paragraph
final_text = normalized_text
if not final_text.endswith(('.', '!', '?')):
    final_text += '.'
final_text += ' ' + extra_sentence

# Step 7: Output results
print("=== Normalized and corrected paragraph ===\n")
print(final_text)
print("\n=== Whitespace characters (in original text) ===")
print("Count:", whitespace_count)
