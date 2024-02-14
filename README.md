# Fair Billing

You're part of a company that charges users for using its app based on session duration. 
The app logs start and end times, along with user names. Your task is to create a report showing the total number of sessions and the shortest possible total duration for each user. 
However, the log file might lack clear pairings for start and end entries, and sessions might overlap or extend beyond the log file's timeframe. 
Your program, which takes a file path as input, needs to handle these scenarios and ignore irrelevant lines in the log file. Just assume the data is in chronological order and covers a single day.

## Solution
Read the Log File:

Open the log file.
Look at each line.
Process Valid Log Entries:

Check if a line has a valid time, a username, and specifies the start or end of a session.
Ignore lines that don't have this information.
Track User Sessions:

Keep track of each user's sessions in a list.
Find Earliest and Latest Times:

Remember the earliest and latest times in the log.
Sort and Calculate Session Durations:

For each user, organize their sessions by time.
Calculate how long each session lasted.
Print the Report:

Share the user's name, how many sessions they had, and the total time they used the application.
Handle Command Line Parameters:

Check if the script is used correctly.
Show a message if it's not.
Run the Script:

Use the script by providing the log file path.

### code flow

Function Definition:

The script defines a function process_log_file to handle the processing of the log file and printing the report.
Open the Log File:

The function starts by opening the specified log file using open(file_path, 'r').
Process Valid Log Entries:

It then loops through each line in the log file.
For each line, it checks if it contains valid information (timestamp, username, and "Start" or "End" marker).
Invalid lines are ignored.
Track User Sessions:

A dictionary (user_sessions) is used to track user sessions. Each user has a list of tuples containing timestamps and events ("Start" or "End").
Find Earliest and Latest Times:

The function keeps track of the earliest and latest timestamps encountered in the log file.
Sort and Calculate Session Durations:

For each user, the sessions are sorted based on timestamps.
It iterates through the sorted sessions to calculate the duration for each session.
Special handling is included for ongoing sessions that extend beyond the log file boundaries.
Print the Report:

The function prints a report for each user, including their name, the number of sessions, and the total duration of their sessions.
Command Line Parameter Handling:

The script checks if it's run with the correct number of command line parameters.
If not, it prints a usage message.
Run the Script:

If the script is executed correctly with a log file path as a command line parameter, it calls the process_log_file function with the specified log file.

## Prerequisite
Valid Log File
Datetime Module

### How to Run
git clone https://github.com/krishanatripati99/FairBilling.git
cd your_repository
python fair_billing.py samplelog.txt

### Input Example 
sample input log_text file

14:02:03 ALICE99 Start
14:02:05 CHARLIE End
14:02:34 ALICE99 End
14:02:58 ALICE99 Start
14:03:02 CHARLIE Start
14:03:33 ALICE99 Start
14:03:35 ALICE99 End
14:03:37 CHARLIE End
14:04:05 ALICE99 End
14:04:23 ALICE99 End
14:04:41 CHARLIE Start

### Output Example(terminal)
Expected Output:

ALICE99 4 240
CHARLIE 3 37

