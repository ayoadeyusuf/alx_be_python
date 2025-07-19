task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
  case "high":
    if time_bound == "yes":
      print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    else:
      print(f"Reminder: '{task}' is a high priority task that requires immediate when urgent tasks are completed!")
  case "medium":
    if time_bound == "yes":
      print(f"Reminder: '{task}' is a medium priority task that needs immediate attention after the urgent high priority tasks.")
    else:
      print(f"Reminder: '{task}' is a medium priority task that is not urgent. Consider completing it 
      when you are done with all urgent and high priority tasks")
  case "low":
    if time_bound == "yes":
      print(f"Reminder: '{task}' is a low priority task that needs to be carried out after the urgent medium priority tasks.")
    else:
      print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time.")
      
