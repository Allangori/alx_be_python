
task = input ( "Enter your task: " )
time_bound = input ( "Is it time-bound? (yes or no): " )
priority = input ( "Priority (high, medium, low): " )


# Process task based on priority
match priority:
    case "high":
        reminder = f"Task '{task}' is a HIGH priority."
    case "medium":
        reminder = f"Task '{task}' is a MEDIUM priority."
    case "low":
        reminder = f"Task '{task}' is a LOW priority."
    case _:
        reminder = f"Task '{task}' has an UNKNOWN priority."

# Modify the reminder if the task is time-sensitive
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

# Print the customized reminder
print(reminder)
