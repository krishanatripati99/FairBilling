# Import necessary libraries
from datetime import datetime, timedelta

# Function to process the log file and print the report
def process_log_file(file_path):
    # Step 1: Read the Log File
    with open(file_path, 'r') as file:
        # Step 2: Process Valid Log Entries
        user_sessions = {}  # Step 3: Track User Sessions
        earliest_time = None
        latest_time = None

        # Loop through each line in the log file
        for line in file:
            parts = line.strip().split()
            
            # Check if the line is a valid log entry
            if len(parts) == 4 and parts[1].isalnum() and (parts[3] == "Start" or parts[3] == "End"):
                timestamp = datetime.strptime(parts[0], '%H:%M:%S')
                username = parts[1]
                event = parts[3]

                # Step 4: Find Earliest and Latest Times
                if earliest_time is None or timestamp < earliest_time:
                    earliest_time = timestamp

                if latest_time is None or timestamp > latest_time:
                    latest_time = timestamp

                # Update user_sessions dictionary
                if username not in user_sessions:
                    user_sessions[username] = []

                user_sessions[username].append((timestamp, event))

        # Step 5: Sort and Calculate Session Durations
        for username, sessions in user_sessions.items():
            sessions.sort()  # Sort sessions by timestamp

            total_duration = 0
            current_start = earliest_time

            # Iterate through sessions to calculate duration
            for session in sessions:
                timestamp, event = session
                if event == "Start":
                    current_start = timestamp
                elif event == "End":
                    total_duration += max((timestamp - current_start).total_seconds(), 0)

            # Handle ongoing sessions after the log file ends
            total_duration += max((latest_time - current_start).total_seconds(), 0)

            # Step 6: Print the Report
            print(f"{username} {len(sessions)} {int(total_duration)}")


# Step 7: Handle Command Line Parameters
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_log_file>")
    else:
        # Step 8: Run the Script
        log_file_path = sys.argv[1]
        process_log_file(log_file_path)
