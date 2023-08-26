import time
import datetime
import pygetwindow as gw
import matplotlib.pyplot as plt

from App import *

app_usage = {}

print("loop 1 start")
while START <= END:
    active_window = gw.getActiveWindow()
    if active_window is not None:

        app_name = active_window.title
        print(f"Running APP : {app_name}")
        current_time = datetime.datetime.now().time()
        print(f"Caught Time :{current_time}")

        app_usage.setdefault(app_name, []).append(current_time)

    if datetime.datetime.now().second == 30:
        with open('app_usage_data.txt', 'w') as f:
            for app_name, timestamps in app_usage.items():
                f.write(f"{app_name}: {', '.join(str(ts) for ts in timestamps)}\n")

    time.sleep(60)
    START += 1
    print(f"finish {START}")  # check if running well
