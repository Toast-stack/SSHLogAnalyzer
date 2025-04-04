import re
from collections import Counter

def analyze_auth_log(file_path):
    # Dictionary to stored failed login attempts

    failed_attempts = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Search for "Failed password" log entries

                if "Failed password" in line:
                    # Extract IP address using regex
                    match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
                    if match:
                        failed_attempts.append(match.group(1))

        # Count occurrences of each IP address
        ip_counter = Counter(failed_attempts)

        print("Failed Login Attempts by IP Address:")
        for ip, count in ip_counter.items():
            print(f"{ip}: {count} times")

        # Highlight suspicious activity
        print("\nSuspicious IPs (5+ failed attempts):")
        for ip,count in ip_counter.items():
            if count >= 5:
                print(f"{ip} - Potential brute force attacker")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.") 
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
log_file_path = "/var/log/auth.log" # Replace with a different path if needed

analyze_auth_log(log_file_path)
