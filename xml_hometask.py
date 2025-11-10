import datetime
import os
import csv
import string
import json
import xml.etree.ElementTree as ET
from collections import Counter

# ---------------- NEW CLASS: XMLImporter ----------------
class XMLImporter:

    def __init__(self, file_path=None):
        self.file_path = file_path or "input_records.xml"

    def process_file(self):
        if not os.path.exists(self.file_path):
            print(f"❌ File not found: {self.file_path}")
            return

        print(f"📂 Processing XML file: {self.file_path}\n")

        try:
            tree = ET.parse(self.file_path)
            root = tree.getroot()

            # Determine if root itself is <record> or <records>
            if root.tag.lower() == "record":
                records = [root]
            else:
                records = list(root.findall("record"))

            if not records:
                print("⚠️ No valid <record> elements found in XML.")
                return

            for elem in records:
                try:
                    record_type = elem.attrib.get("type", "").lower()
                    text = normalize_text_case(elem.findtext("text", default="").strip())

                    if record_type == "news":
                        city = elem.findtext("city", default="Unknown")
                        record = News(text, city)

                    elif record_type in ["ad", "privatead"]:
                        expiration = elem.findtext("expiration_date", default="")
                        if not expiration:
                            print("⚠️ Missing <expiration_date> in ad record.")
                            continue
                        record = PrivateAd(text, expiration)

                    elif record_type in ["quote", "motivationalquote"]:
                        author = elem.findtext("author", default="Unknown")
                        record = MotivationalQuote(text, author)

                    else:
                        print(f"⚠️ Unknown record type: {record_type}")
                        continue

                    publish_record(record)

                except Exception as e:
                    print(f"❌ Error processing record: {ET.tostring(elem, encoding='unicode')}\n   {e}")

            # Remove XML file after processing
            os.remove(self.file_path)
            print(f"🗑️ File '{self.file_path}' removed after successful processing.\n")

        except ET.ParseError as e:
            print(f"❌ Invalid XML format in file: {self.file_path}\n   {e}")
        except Exception as e:
            print(f"❌ Unexpected error while processing XML file: {e}")

# ---------------- MODIFY MAIN MENU ----------------
def main():
    print("Welcome to the User News Feed Generator 🗞️")
    print("Choose record type:")
    print("1 – News")
    print("2 – Private Ad")
    print("3 – Motivational Quote (Unique Type)")
    print("4 – Import records from text file")
    print("5 – Import records from JSON file")
    print("6 – Import records from XML file")  # 🆕 New option

    choice = input("Enter your choice (1/2/3/4/5/6): ").strip()

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

    elif choice == "6":
        file_path = input("Enter path to your XML file (or press Enter for default 'input_records.xml'): ").strip()
        importer = XMLImporter(file_path if file_path else None)
        importer.process_file()

    else:
        print("❌ Invalid choice.")

# ---------------- ENTRY POINT ----------------
if __name__ == "__main__":
    main()
