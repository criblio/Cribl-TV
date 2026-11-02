import random
import time

from prometheus_remote_writer import RemoteWriter

# Create a RemoteWriter instance
writer = RemoteWriter(
    url='http://CRIBL-URL-GOES-HERE:CRIBL-PORT-GOES-HERE/write'
)

# Send one random cpu_usage value every second until stopped (Ctrl+C)
while True:
    timestamp_ms = int(time.time() * 1000)
    data = [
        {
            'metric': {'__name__': 'cpu_usage', 'host': 'server1'},
            'values': [round(random.uniform(0, 100), 1)],
            'timestamps': [timestamp_ms]
        }
    ]

    print(f"data: {data}")
    writer.send(data)

    time.sleep(1)