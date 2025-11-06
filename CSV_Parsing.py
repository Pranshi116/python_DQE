import datetime
import os
import csv
import string
from collections import Counter
# Base class for records
class Record:
    """Base class for all record types."""
    def format_record(self) -> str:
        raise NotImplementedError("Subclasses must implement format_record()")
# Record type: News
class News(Record):
    def __init__(self, text: str, city: str):
        self.text = text
        self.city = city
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    def format_record(self) -> str:
        return (f"--- News ---\n"
                f"Text: {self.text}\n"
                f"City: {self.city}\n"
                f"Published at: {self.date}\n")
# Record type: Private Ad
class PrivateAd(Record):
    def __init__(self, text: str, expiration_date: str):
        self.text = text
        self.expiration_date = datetime.datetime.strptime(expiration_date, "%Y-%m-%d").date()
        self.days_left = (self.expiration_date - datetime.date.today()).days

    def format_record(self) -> str:
        return (f"--- Private Ad ---\n"
                f"Text: {self.text}\n"
                f"Expires on: {self.expiration_date} ({self.days_left} days left)\n")
# Record type: Motivational Quote
class MotivationalQuote(Record):
    def __init__(self, text: str, author: str):
        self.text = text
        self.author = author
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    def format_record(self) -> str:
        return (f"--- Motivational Quote ---\n"
                f"\"{self.text}\"\n"
                f"- Author: {self.author}\n"
                f"Published at: {self.date}\n")
# Case Normalization
def normalize_text_case(text: str) -> str:
    """Ensure each sentence starts with a capital letter and rest is lowercase."""
    sentences = [s.strip().capitalize() for s in text.split('.') if s.strip()]
    return '. '.join(sentences) + '.' if sentences else text
# Text Statistics: Word & Letter Count
def generate_statistics(file_path="news_feed.txt"):
    """Generate two CSVs: word_count.csv and letter_count.csv from the text file."""
    if not os.path.exists(file_path):
        print("⚠️ No news feed file found for statistics.")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # ---------------- WORD COUNT ----------------
    words = [
        word.strip(string.punctuation).lower()
        for word in content.split()
        if word.strip(string.punctuation)
    ]
    word_counter = Counter(words)

    with open("word_count.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["word", "count"])
        for word, count in sorted(word_counter.items()):
            writer.writerow([word, count])

    # ---------------- LETTER COUNT ----------------
    letters = [ch for ch in content if ch.isalpha()]
    total_letters = len(letters)
    counter_all = Counter(ch.lower() for ch in letters)
    counter_upper = Counter(ch for ch in content if ch.isupper())

    with open("letter_count.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["letter", "count_all", "count_uppercase", "percentage"])
        for letter in sorted(counter_all):
            count_all = counter_all[letter]
            count_upper = counter_upper.get(letter.upper(), 0)
            percentage = round((count_all / total_letters) * 100, 2) if total_letters else 0
            writer.writerow([letter, count_all, count_upper, percentage])

    print("📊 Statistics updated: 'word_count.csv' and 'letter_count.csv' recreated.\n")
# File publisher utility
def publish_record(record: Record, file_path="news_feed.txt"):
    """Append a record to the text file and regenerate statistics."""
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(record.format_record())
        f.write("\n")

    print("✅ Record published successfully!\n")
    generate_statistics(file_path)
# New Class: File Importer
class FileImporter:
    """
    Handles reading and processing records from a text file.

    Expected input format example:
    News | The sky is blue. | London
    Ad | Buy a car. | 2025-12-31
    Quote | Believe in yourself. | John Doe
    """

    def __init__(self, file_path=None):
        self.file_path = file_path or "input_records.txt"

    def process_file(self):
        if not os.path.exists(self.file_path):
            print(f"❌ File not found: {self.file_path}")
            return

        print(f"📂 Processing file: {self.file_path}\n")

        with open(self.file_path, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]

        for line in lines:
            try:
                parts = [p.strip() for p in line.split('|')]
                record_type = parts[0].lower()

                if record_type == "news" and len(parts) == 3:
                    text = normalize_text_case(parts[1])
                    city = parts[2]
                    record = News(text, city)

                elif record_type in ["ad", "privatead"] and len(parts) == 3:
                    text = normalize_text_case(parts[1])
                    expiration = parts[2]
                    record = PrivateAd(text, expiration)

                elif record_type in ["quote", "motivationalquote"] and len(parts) == 3:
                    text = normalize_text_case(parts[1])
                    author = parts[2]
                    record = MotivationalQuote(text, author)

                else:
                    print(f"⚠️ Skipping invalid line format: {line}")
                    continue

                publish_record(record)

            except Exception as e:
                print(f"❌ Error processing line: {line}\n   {e}")

        os.remove(self.file_path)
        print(f"🗑️ File '{self.file_path}' removed after successful processing.\n")
# Main menu logic 
def main():
    print("Welcome to the User News Feed Generator 🗞️")
    print("Choose record type:")
    print("1 – News")
    print("2 – Private Ad")
    print("3 – Motivational Quote (Unique Type)")
    print("4 – Import records from text file")

    choice = input("Enter your choice (1/2/3/4): ").strip()

    if choice == "1":
        text = normalize_text_case(input("Enter news text: "))
        city = input("Enter city: ")
        record = News(text, city)
        publish_record(record)

    elif choice == "2":
        text = normalize_text_case(input("Enter ad text: "))
        expiration = input("Enter expiration date (YYYY-MM-DD): ")
        record = PrivateAd(text, expiration)
        publish_record(record)

    elif choice == "3":
        text = normalize_text_case(input("Enter your motivational quote: "))
        author = input("Enter author name: ")
        record = MotivationalQuote(text, author)
        publish_record(record)

    elif choice == "4":
        file_path = input("Enter path to your input file (or press Enter for default 'input_records.txt'): ").strip()
        importer = FileImporter(file_path if file_path else None)
        importer.process_file()

    else:
        print("❌ Invalid choice.")
# Entry point
if __name__ == "__main__":
    main()
