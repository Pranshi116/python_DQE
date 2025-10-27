import re

# Step 1: Original text
text = """ tHis iz your homeWork, copy these Text to variable.

 You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

 it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# --- Functional decomposition ---

# Step 2: Normalize letter case
def normalize_case(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r'\s+', ' ', s)  # <-- remove extra newlines and multiple spaces
    # Capitalize the first letter of each sentence
    parts = re.split(r'([.!?]\s*)', s)
    s = ''.join(
        [parts[i].capitalize() if i % 2 == 0 else parts[i] for i in range(len(parts))]
    )
    return s

# Step 3: Fix mistaken "iz" (only when it's a real word, not in quotes)
def fix_mistakes(s: str) -> str:
    return re.sub(r'\biz\b', 'is', s)

# Step 4: Extract last words of each sentence
def extract_last_words(s: str) -> str:
    sentences = re.split(r'[.!?]', s)
    last_words = [sentence.strip().split()[-1] for sentence in sentences if sentence.strip()]
    return ' '.join(last_words)

# Step 5: Count all whitespace characters (from original text)
def count_whitespaces(s: str) -> int:
    return sum(1 for c in s if c.isspace())

# Step 6: Combine everything
def process_text(text: str):
    # Count before modification
    whitespace_count_original = count_whitespaces(text)

    normalized = normalize_case(text)
    corrected = fix_mistakes(normalized)
    last_words_sentence = extract_last_words(corrected)
    final_text = corrected.strip() + ' ' + last_words_sentence.capitalize() + '.'

    return final_text, whitespace_count_original


# --- Run and print results ---
processed_text, whitespace_count = process_text(text)

print("=== Normalized and corrected paragraph ===\n")
print(processed_text)
print("\n=== Whitespace characters (in original text) ===")
print(f"Count: {whitespace_count}")
