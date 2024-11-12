steps_goal = 10000
total_steps = 0
end_of_day = True

while end_of_day:
    steps_made = input("Steps or command (or 'Going Home' to stop): ")

    if steps_made == "Going Home":
        go_home = int(input("Steps to home: "))
        total_steps += go_home
        end_of_day = False

    else:
        steps_made = int(steps_made)
        total_steps += steps_made

    if total_steps >= steps_goal:
        print("Goal reached! Good job!")
        print(f"{total_steps - steps_goal} steps over the goal!")
        break

if total_steps < steps_goal:
    print(f"{steps_goal - total_steps} more steps to reach the goal.")

