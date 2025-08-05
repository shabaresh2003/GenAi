import re

def classify_with_regex(log_message):
    regex_patterns = {
        # Existing Patterns
        r"User User\d+ logged (in|out).": "User Action",
        r"Backup (started|ended) at .*": "System Notification",
        r"Backup completed successfully.": "System Notification",
        r"System updated to version .*": "System Notification",
        r"File .* uploaded successfully by user .*": "System Notification",
        r"Disk cleanup completed successfully.": "System Notification",
        r"System reboot initiated by user .*": "System Notification",
        r"Account with ID .* created by .*": "User Action",

        r"Failed login attempt by user .*": "Security Alert",
        r"Unauthorized access attempt detected.": "Security Alert",
        r"User .* changed password successfully.": "User Action",
        r"Application .* crashed at .*": "Application Error",
        r"Database connection lost at .*": "System Notification",
        r"Network latency exceeds threshold.*": "Performance Alert",
        r"Service .* restarted by user .*": "System Notification",
        r"License for .* expired on .*": "System Notification",
        r"Scheduled maintenance started at .*": "System Notification",
        r"Scheduled maintenance completed at .*": "System Notification",
        r"Low disk space on drive .*": "Performance Alert",
        r"Printer .* is out of paper.": "System Notification",
        r"Email notification failed to send to .*": "Application Error",
        r"System scan completed with .* threats found.": "Security Alert",
        r"Configuration file .* modified by .*": "User Action"
    }

    for pattern, label in regex_patterns.items():
        if re.search(pattern, log_message):
            return label
    return None

if __name__ == "__main__":
    print(classify_with_regex("Backup completed successfully."))
    print(classify_with_regex("Account with ID 1234 created by User1."))
    print(classify_with_regex("Hey Bro, chill ya!"))  # Returns: None
    print(classify_with_regex("Failed login attempt by user root"))
    print(classify_with_regex("System scan completed with 5 threats found."))
