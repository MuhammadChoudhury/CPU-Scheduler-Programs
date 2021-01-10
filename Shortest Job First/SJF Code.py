'''

This program uses a two-dimmensional array to store date about the processes.
The first dimmension are the 8  processess indexed from 0-7

The second dimmnension have data relevant to that specific process
Here is what the indexes for the second dimmension means (this is for EACH process)
0: Time in which the process will end up back in ready queue from waiting queue
1: Waiting Time
2: Process Number
3: Index of the where the current CPU burst is
4: Current CPU Burst
5: Indicator for when process is finished
6: First CPU Burst
7: First I/O Burst
8: Second CPU Burst....
'''

print("Hello World. SJF scheduler created in Pycharm")

# Function finds Waiting, Turnaround, and Response Times
# of both individual process and averages. Also finds
# CPU utilization
def findTimes(processes, n, m, lot):
    io = [0] * n
    bt = [0] * n
    rt = [0] * n
    wt = [0] * n
    tat = [[0] * 2 for i in range(8)]
    total_wt = 0
    total_rt = 0
    total_tat = 0

    t = 0
    r = 0
    f = 1
    b = 3
    d = 5
    m = 6
    tm = [0] * n
    rd = [0] * n
    io = [0] * n
    c = [0] * n
    z = 0
    h = 0
    v = 8
    response = False
    progress = True
    cpu = 0

    # Adds all CPU and I/O burst times to array
    # and sets up all other fields like position
    # of CPU burst time and if process is terminated
    for j in range(20):
        for i in range(n):
            lot[i][6 + j] = processes[i][j]
            if j == 0:
                lot[i][2] = i + 1
                lot[i][3] = 6
                lot[i][4] = lot[i][6]
                lot[i][5] = 1

    while (progress):
        # Will continue until every process is
        # finished with its burst times
        s = 9999
        g = 10
        e = 0

        for i in range(n):
            # Determines which process will execute next depending on which
            # process has the shortest CPU burst time
            if lot[i][5] == 1 and lot[i][4] < s and lot[i][0] <= t:
                s = lot[i][4]
                g = i
                if lot[i][5] == 1 and lot[i][0] <= t:
                    # Places the processes who have arrived in the Ready Queue
                    rd[i] = 1
                    io[i] = 0
                if lot[i][5] == 1 and lot[i][0] > t:
                    # Places the processes who havent arrived yet in the I/O Queue
                    io[i] = 1
                    rd[i] = 0
                if lot[i][5] == 0:
                    # Puts terminated process in terminated queue
                    tm[i] = 1

        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

        if g == 10:
            # If no process is executing, will continue to next iteration in loop
            # Increases idle and time counters. Prints processes in  I/O Queue
            h += 1
            t += 1
            for i in range(n):
                if lot[i][0] > t and lot[i][5] == 1:
                    p = lot[i][3]
                    print("Process", lot[i][2], "is in the I/O queue with I/O burst of", lot[i][p - 1], "units")
            print("Idle. Total idle time (so far):", h, )
            print("Current Execution Time:", t)
            continue

        for i in range(n):
            # Prints out every process thats in the Ready Queue
            if lot[i][0] <= t and lot[i][5] == 1:
                print("Process", lot[i][2], " is in the Ready queue with CPU burst of ", lot[i][4], "units")

        for i in range(n):
            # Prints out every process thats in the I/O Queue
            if lot[i][0] > t and lot[i][5] == 1:
                p = lot[i][3]
                print("Process", lot[i][2], "is in the I/O queue with I/O burst of", lot[i][p - 1], "units")

        for i in range(n):
            # Prints out evey process that has been terminated so far
            if lot[i][5] == 0:
                print("Process", lot[i][2], "has already been terminated")

        if lot[g][1] == 0 and c[g] == 0:
            # Records if a process has executed for the first time
            c[g] = 1
            response = True

        print("Process", g + 1, "is currently executing")

        # Adds waiting time to the process that will be executed
        r = t - lot[g][0]
        lot[g][1] += r

        # Process executes. CPU burst time gets added to the
        # updated arrival time and also the time counter
        lot[g][0] = t
        lot[g][0] += lot[g][4]
        t += lot[g][4]

        # Finds CPU burst position and also checks to see
        # if this is the last CPU or I/O burst or not
        p = lot[g][3]
        if lot[g][p + 1] == 0:
            # Process has no more CPU or I/O bursts. Terminates process
            lot[g][5] = 0
            rd[g] = 0
            io[g] = 0
            print("Process", lot[g][2], "has finished total execution.")
            print("Total Turnaround Time: ", lot[g][0])
        else:
            # Adds the I/O burst time so it can go to I/O Also adjusts array
            # so that the next CPU burst is available when it next executes
            lot[g][0] += lot[g][p + 1]
            lot[g][3] += 2
            lot[g][4] = lot[g][p + 2]

        if response == True:
            # Records and prints the response time of the process
            rt[g] = lot[g][1]
            print("Process", g + 1, "has gone first execution. Response Time: ", rt[g])
        response = False

        print("Current Execution Time:", t)  # Prints out current execution time

        # Checks to see if all processes are done executing
        for i in range(n):
            e += lot[i][5]
        # If all are done executing, loops will end
        if e == 0:
            progress = False

    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    cpu = 100 - (h / t * 100)
    print("Overall time spent being idle: ", h)
    print("The last process finished execution at time:", t)
    print("SJF CPU Utilization:", cpu, "%")

    # Finds turnaround times. Since the arrival time for all
    # processes are 0, the time in which the process ends
    # is in fact the turnaround time
    for i in range(n):
        tat[i][0] = lot[i][2]
        tat[i][1] = lot[i][0]
    tat.sort(key=lambda tat: tat[0])


    print("Processes No. " +  "Response Time " +
          " Waiting time " + " Turn around time")


    for i in range(n):
        total_wt += lot[i][1]
        total_rt += rt[i]
        total_tat += tat[i][1]
        print(" " + str(i + 1) + "\t\t" +
              str(rt[i]) + "\t\t " +
              str(lot[i][1]) + "\t\t " +
              str(tat[i][1]))


    print("Average waiting time = " + str(total_wt / n))
    print("Average response time = " + str(total_rt / n))
    print("Average turn around time = " + str(total_tat / n))


# Driver code
if __name__ == "__main__":
    # process id's
    processes = [[5, 27, 3, 31, 5, 43, 4, 18, 6, 22, 4, 26, 3, 24, 4, 0, 0, 0, 0, 0],
                 [4, 48, 5, 44, 7, 42, 12, 37, 9, 76, 4, 41, 9, 31, 7, 43, 8, 0, 0, 0],
                 [8, 33, 12, 41, 18, 65, 14, 21, 4, 61, 15, 18, 14, 26, 5, 31, 6, 0, 0, 0],
                 [3, 35, 4, 41, 5, 45, 3, 51, 4, 61, 5, 54, 6, 82, 5, 77, 3, 0, 0, 0],
                 [16, 24, 17, 21, 5, 36, 16, 26, 7, 31, 13, 28, 11, 21, 6, 13, 3, 11, 4, 0],
                 [11, 22, 4, 8, 5, 10, 6, 12, 7, 14, 9, 18, 12, 24, 15, 30, 8, 0, 0, 0],
                 [14, 46, 17, 41, 11, 42, 15, 21, 4, 32, 7, 19, 16, 33, 10, 0, 0, 0, 0, 0],
                 [4, 14, 5, 33, 6, 51, 14, 73, 16, 87, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    m = 24
    n = len(processes)

    # Burst time of all processes
    lot = [[0] * (m + 2) for i in range(n)]
    print("1 lot =", lot)

    findTimes(processes, n, m, lot)
