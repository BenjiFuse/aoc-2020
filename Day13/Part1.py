from math import floor

with open('input.txt') as f:
    lines = f.read().split('\n')
    earliest_departure = int(lines[0])
    bus_intervals = [int(i) for i in lines[1].split(',') if i != 'x']

    wait_times = {(floor(earliest_departure/n)*n+n)-earliest_departure :n for n in bus_intervals}
    lowest = min(wait_times)
    bus_id = wait_times[lowest]

    print(bus_id, lowest, (lowest)*bus_id)