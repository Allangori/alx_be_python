task = input ( "Enter your task: " )
priority = input ( "Priority (high/medium/low): " )
time_bound = input ( "Is it time-bound? (yes/no): " )



# Process task based on priority
match priority:
    case "high":
        Reminder = f" '{task}' is a high priority task"
    case "medium":
        Reminder = f" '{task}' is a medium priority task"
    case "low":
        Reminder = f" '{task}' is a low priority task"
    case _:
        Reminder = f" '{task}' has an unknown priority"

# Modify the Reminder if the task is time-sensitive
if time_bound == "yes":
    Reminder += " that requires immediate attention today!"
elif time_bound == "no":
    Reminder += ". Consider completing it when you have free time."

# Print the customized Reminder
print ( f"{Reminder: }" )
