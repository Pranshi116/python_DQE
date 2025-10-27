import datetime

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

# Unique record: Motivational Quote

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

# Utility: File handler

def publish_record(record: Record, file_path="news_feed.txt"):
    """Append a record to the text file."""
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(record.format_record())
        f.write("\n")  # blank line between records
    print("✅ Record published successfully!\n")

# Main menu logic

def main():
    print("Welcome to the User News Feed Generator 🗞️")
    print("Choose record type:")
    print("1 – News")
    print("2 – Private Ad")
    print("3 – Motivational Quote (Unique Type)")

    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        text = input("Enter news text: ")
        city = input("Enter city: ")
        record = News(text, city)

    elif choice == "2":
        text = input("Enter ad text: ")
        expiration = input("Enter expiration date (YYYY-MM-DD): ")
        record = PrivateAd(text, expiration)

    elif choice == "3":
        text = input("Enter your motivational quote: ")
        author = input("Enter author name: ")
        record = MotivationalQuote(text, author)

    else:
        print("❌ Invalid choice.")
        return

    publish_record(record)

# Entry point

if __name__ == "__main__":
    main()
