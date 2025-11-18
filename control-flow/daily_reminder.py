task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes or no): ")
priority = input("what is your task priority (high, medium, low): ")


match priority :
    case  "high":
        if time_bound == "yes":
            print(f"{task} is a time-senstive high Priority task that requires immediate attention today")
        else:
            print(f"{task} is a high priority but can be dealt in your convinience")
    case "medium":
        if time_bound == "yes":
            print(f"{task} is a time-senstive medium Priority task that requires immediate attention today")
        else: 
            print(f"{task} is a medium priority but can be dealt in your convinience")
    case "low":
        if time_bound == "yes":
            print(f"{task} is a time-senstive low Priority task that requires immediate attention today")
        else: 
            print(f"{task} is a low priority but can be dealt in your convenience")
    case _:
        print(f"please enter a valid task-priority")