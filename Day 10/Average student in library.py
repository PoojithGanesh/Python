#Find the average no. of students present inside the library in the given time
entry_time= [40, 20, 10, 30, 20]
exit_time= [20, 10, 20, 10, 15]
def avg(entry_time, exit_time):
    cs = 0
    ts = 0
    for e, l in zip(entry_time, exit_time):
        cs += e - l
        ts += cs
    return ts / len(entry_time)
print("Average number of students in the library:", avg(entry_time, exit_time))
