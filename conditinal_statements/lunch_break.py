series_name = input()
episode_duration = int(input())
break_duration = int(input())

lunch_time = break_duration * (1/8)  # 1/8 of break time
rest_time = break_duration * (1/4)    # 1/4 of break time

remaining_time = break_duration - lunch_time - rest_time

import math

if remaining_time >= episode_duration:
    free_time = remaining_time - episode_duration
    print(f"You have enough time to watch {series_name} and left with {math.ceil(free_time)} minutes free time.")
else:
    needed_time = episode_duration - remaining_time
    print(f"You don't have enough time to watch {series_name}, you need {math.ceil(needed_time)} more minutes.")
