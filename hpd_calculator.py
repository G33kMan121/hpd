# HPD Cut Calculator

# Step 1: Gather inputs
donor_expected = int(input("Please input number of expected donors for the week:\n"))
hour_goal = float(input("Please input your center's HPD goal (e.g., 0.86):\n"))
emp_hours = float(input("Please input how many total employee hours are currently scheduled:\n"))

# Step 2: Calculate allowed hours based on donor target and goal
true_hours = donor_expected * hour_goal
hours_left = emp_hours - true_hours

# Step 3: If overstaffed, determine cuts
emp_count = int(input("Please input total number of non-exempt employees:\n"))
days_open = int(input("Please input how many days the center is open:\n"))

# Step 4: Decision logic
if hours_left <= 0:
    print("\nYou're already at or below your HPD goal. No cuts needed!")
else:
    cut_hours = hours_left / emp_count
    total_hours = cut_hours / days_open
    rounded_hours = round(total_hours * 4) / 4  # Round to nearest 15 minutes
    print(f"\nYou will need to cut approximately {rounded_hours:.2f} hours from every employee per day to meet goal.")
