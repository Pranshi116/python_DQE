import datetime
import os
import csv
import string
import json
from collections import Counter
# ---------------- NEW CLASS: JSONImporter ----------------
class JSONImporter:
    def __init__(self, file_path=None):
        self.file_path = file_path or "input_records.json"

    def process_file(self):
        if not os.path.exists(self.file_path):
            print(f"❌ File not found: {self.file_path}")
            return

        print(f"📂 Processing JSON file: {self.file_path}\n")

        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Support both single record and list of records
            records = data if isinstance(data, list) else [data]

            for entry in records:
                try:
                    record_type = entry.get("type", "").lower()
                    text = normalize_text_case(entry.get("text", ""))

                    if record_type == "news":
                        city = entry.get("city", "Unknown")
                        record = News(text, city)

                    elif record_type in ["ad", "privatead"]:
                        expiration = entry.get("expiration_date")
                        if not expiration:
                            print("⚠️ Missing expiration_date in ad record.")
                            continue
                        record = PrivateAd(text, expiration)

                    elif record_type in ["quote", "motivationalquote"]:
                        author = entry.get("author", "Unknown")
                        record = MotivationalQuote(text, author)

                    else:
                        print(f"⚠️ Unknown record type: {record_type}")
                        continue

                    publish_record(record)

                except Exception as e:
                    print(f"❌ Error processing record: {entry}\n   {e}")

            # Remove JSON file after processing
            os.remove(self.file_path)
            print(f"🗑️ File '{self.file_path}' removed after successful processing.\n")

        except json.JSONDecodeError as e:
            print(f"❌ Invalid JSON format in file: {self.file_path}\n   {e}")
        except Exception as e:
            print(f"❌ Unexpected error while processing JSON file: {e}")

# ---------------- MODIFY MAIN MENU ----------------
def main():
    print("Welcome to the User News Feed Generator 🗞️")
    print("Choose record type:")
    print("1 – News")
    print("2 – Private Ad")
    print("3 – Motivational Quote (Unique Type)")
    print("4 – Import records from text file")
    print("5 – Import records from JSON file")  # 🆕 new option

    choice = input("Enter your choice (1/2/3/4/5): ").strip()

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

    elif choice == "5":
        file_path = input("Enter path to your JSON file (or press Enter for default 'input_records.json'): ").strip()
        importer = JSONImporter(file_path if file_path else None)
        importer.process_file()

    else:
        print("❌ Invalid choice.")

# ---------------- ENTRY POINT ----------------
if __name__ == "__main__":
    main()
