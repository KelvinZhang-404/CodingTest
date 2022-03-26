from datetime import datetime

timestamp = 1528797322
date_time = datetime.fromtimestamp(timestamp)

d = date_time.strftime("%d")
m = date_time.strftime("%b")
y = date_time.strftime("%Y")

print(d + " " + m + " " + y)

s = date_time.strftime("%d %b %Y")
print(s)