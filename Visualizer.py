import time
import datetime
import pygetwindow as gw
import matplotlib.pyplot as plt
from Collector import *
from App import *

def modify_name(name, MAX_L=15):
    if len(name) > MAX_L:
        return name[:MAX_L] + "..."
    else:
        return name 

app_total_time = {}
for app_name, timestamps in app_usage.items():
    total_seconds = sum(ts.minute * 60 for ts in timestamps)
    app_total_time[app_name] = total_seconds / 60 


names = [modify_name(name) for name in app_total_time.keys()]
app_times = list(app_total_time.values())

plt.bar(names, app_times, width=.3, color = "red")
plt.xlabel('Apps')
plt.ylabel('Total Usage Time (s)')
plt.title('Total App Usage Time')
plt.tight_layout()

plt.show()
