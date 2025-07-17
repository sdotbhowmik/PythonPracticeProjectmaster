import random
import datetime

LOG_FILE = "logs.txt"
LOG_LEVELS = ["INFO", "WARNING", "ERROR"]
MESSAGES = [
    "Application started",
    "Low memory warning",
    "Database connection failed",
    "User logged in",
    "File not found",
    "Network timeout",
    "Disk space running low",
    "Unauthorized access attempt"
]


# Function to generate a log entry
def generate_log():
    """Generate a random log entry and write it to the file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    level = random.choice(LOG_LEVELS)
    message = random.choice(MESSAGES)
    log_entry = f"{timestamp} [{level}] {message}"

    with open(LOG_FILE, "a") as f:
        f.write(log_entry + "\n")

    print("New log entry added!")


def view_logs():
    """Display all log entries."""
    with open(LOG_FILE, "r") as f:
        logs = f.readlines()

    if logs:
        print("\n--- Log Entries ---")
        for log in logs:
            print(log.strip())
    else:
        print("No logs found.")


# Function to filter logs by level
def filter_logs_by_level():
    """Filter logs based on the log level."""

    level = input("Enter log level (INFO, WARNING, ERROR): ").strip().upper()

    if level not in LOG_LEVELS:
        print("Invalid log level!")
        return

    filtered_logs = []
    with open(LOG_FILE, "r") as file:
        # Read all lines from the file
        all_logs = file.readlines()

        # Process each log entry
        for log in all_logs:
            # Clean up the log entry by removing whitespace
            cleaned_log = log.strip()

            # Check if the log contains our desired level tag
            if f"[{level}]" in cleaned_log:
                # Add matching logs to our filtered list
                filtered_logs.append(cleaned_log)

    if filtered_logs:
        print(f"\n--- {level} Logs ---")
        for log in filtered_logs:
            print(log)
    else:
        print(f"No {level} logs found.")


# Function to search logs by keyword
def search_logs():
    """Search logs containing a specific keyword."""
    keyword = input("Enter keyword to search in logs: ").strip()

    # Open the log file in read mode
    with open(LOG_FILE, "r") as f:
        # Read all lines from the file
        all_logs = f.readlines()

    # Initialize an empty list to store filtered logs
    filtered_logs = []

    # Convert the keyword to lowercase for case-insensitive search
    keyword_lower = keyword.lower()

    # Iterate through each log entry
    for log in all_logs:
        # Remove any leading/trailing whitespace from the log entry
        cleaned_log = log.strip()

        # Check if the keyword is present in the log (case-insensitive)
        if keyword_lower in cleaned_log.lower():
            # Add the matching log to the filtered list
            filtered_logs.append(cleaned_log)

    if filtered_logs:
        print(f"\n--- Logs containing '{keyword}' ---")
        for log in filtered_logs:
            print(log)
    else:
        print(f"No logs found containing '{keyword}'.")


# Function to display log statistics
def log_statistics():
    """Show log statistics including total logs and count per level."""
    with open(LOG_FILE, "r") as f:
        logs = f.readlines()

    if not logs:
        print("No logs found to analyze.")
        return

    total_logs = len(logs)
    level_counts = {level: 0 for level in LOG_LEVELS}

    for log in logs:
        for level in LOG_LEVELS:
            if f"[{level}]" in log:
                level_counts[level] += 1

    most_recent_log = logs[-1].strip()

    print("\n--- Log Statistics ---")
    print(f"Total logs: {total_logs}")
    for level, count in level_counts.items():
        print(f"{level} logs: {count}")
    print(f"Most recent log: {most_recent_log}")


# Function to handle user choices
def user_choice(choice):
    if choice == "1":
        generate_log()
    elif choice == "2":
        view_logs()
    elif choice == "3":
        filter_logs_by_level()
    elif choice == "4":
        search_logs()
    elif choice == "5":
        log_statistics()
    elif choice == "6":
        print("Exiting... Goodbye!")
        return
    else:
        print("Invalid choice! Try again.")


# Main  Menu
if __name__ == "__main__":
    while True:
        print("\nLog File Parser")
        print("1. Generate a new log entry")
        print("2. View all logs")
        print("3. Filter logs by level")
        print("4. Search logs by keyword")
        print("5. View Log Statistics")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()
        user_choice(choice)

        if choice == "6":
            break
