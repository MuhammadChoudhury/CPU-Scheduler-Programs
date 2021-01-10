'''

This program uses a two-dimmensional array to store date about the processes.
The first dimmension are the 8  processess indexed from 0-7

The second dimmnension have data relevant to that specific process
Here is what the indexes for the second dimmension means (this is for EACH process)
0: Time in which the process will end up back in ready queue from waiting queue
1: Waiting Time
2: Process Number
3: Which queue the process is in
4: Remaining Burst Time of current process
5: Index of the where the current CPU burst is
6: First CPU Burst
7: First I/O Burst
8: Second CPU Burst....
'''

print("Hello World. MultiLevel Feedback Queue scheduler created in Pycharm")

# Function finds Waiting, Turnaround, and Response Times
# of both individual process and averages. Also finds
# CPU utilization
def findTimes(processes, n, m, lot):
    io = [0] * n
    bt = [0] * n
    rt = [0] * n
    wt = [0] * n
    tat = [[0] * 2 for i in range(n)]
    totalWT = 0
    totalRT = 0
    totalTAT = 0


    t = 0
    r = 0
    f = 1
    b = 3
    d = 5
    m = 6
    l = 10
    z = 0
    h = 0
    tm = [0] * n
    rd = [0] * n
    io = [0] * n
    u = [0] * n
    last = 1
    tres = 0
    dos = 0

    c = [0] * 2
    c[0] = 10
    c[1] = 0
    tq1 = 5
    tq2 = 10
    p = 0
    cpu = 0
    progress = True
    response = False
    t = 0

    # Adds all CPU and I/O burst times to array
    # and sets up all other fields like position
    # of CPU burst time and if process is terminated
    for j in range(19):
        for i in range(n):
            lot[i][6 + j] = processes[i][j]
            if j == 0:
                lot[i][2] = i + 1
                lot[i][3] = 1
                lot[i][4] = lot[i][6]
                lot[i][5] = 6

    while (progress):
        # Will continue until every process is
        # finished with its burst times
        s = 9999
        g = 10
        x = 3

        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")


        for j in range(3):
            for i in range(n):
                # Determines which process should go next based on which queue
                # it is in and also and if has arrived yet
                if lot[i][3] == x and lot[i][0] < s and lot[i][0] <= t:
                    s = lot[i][0]
                    g = i
                    if lot[i][3] != 0 and lot[i][0] <= t:
                        # Places the processes who have arrived in the Ready Queue
                        rd[i] = 1
                        io[i] = 0
                    if lot[i][3] != 0 and lot[i][0] > t:
                        # Places the processes who havent arrived yet in the I/O Queue
                        io[i] = 1
                        rd[0] = 0
                    if lot[i][5] == 0:
                        # Puts terminated process in terminated queue
                        tm[i] = 1
            x -= 1  # Checks next, higher queue
            s = 9999

        if g == 10:
            # If no process is executing, will continue to next iteration in loop
            # Increases idle and time counters. Prints processes in  I/O Queue
            h += 1
            t += 1
            for i in range(n):
                if lot[i][0] > t and lot[i][3] != 0:
                    p = lot[i][5]
                    print("Process", lot[i][2], "is in the I/O queue with I/O burst of", lot[i][p - 1], "units")
            print("Idle. Total idle time (so far):", h, )
            print("Current Execution Time:", t)
            continue

        for i in range(n):
            # Prints out every process thats in the Ready Queue
            if lot[i][0] <= t and lot[i][3] != 0:
                print("Process", lot[i][2], " is in the Ready queue with CPU burst of ", lot[i][4], "units")

        for i in range(n):
            # Prints out every process thats in the I/O Queue
            if lot[i][0] > t and lot[i][3] != 0:
                p = lot[i][5]
                print("Process", lot[i][2], "is in the I/O queue with I/O burst of", lot[i][p - 1], "units")

        for i in range(n):
            # Prints out evey process that has been terminated so far
            if lot[i][3] == 0:
                print("Process", lot[i][2], "has already been terminated")

        if lot[g][1] == 0 and u[g] == 0:
            u[g] = 1
            response = True


        # If last process executed was in queue 3 and current process
        # is in queue 3, the last process will be executing now
        if last == 3 and lot[g][3] == 3:
            g = l

        # If last process executed was in queue 2 and current process
        # is in queue 2, the last process will be executing now
        if last == 2 and lot[g][3] == 2 and c[0] != 10:
            g = c[0]

        # If current process is in queue 3, the following will execute
        if lot[g][3] == 3:
            t += 1
            l = g
            c[0] = 10
            c[1] = 0

            # Adds waiting time to the process that will be executed
            r = t - lot[g][0]
            lot[g][1] += r

            # Updates arrival time and decreases remaining CPU burst time
            p = lot[g][5]
            lot[g][0] = t
            lot[g][4] -= 1

            if lot[g][4] == 0 and lot[g][p + 1] != 0:
                # Adds I/O burst time to the process that has executed
                # Positions process for next CPU burst time
                c[0] = 10
                c[1] = 0
                lot[g][0] += lot[g][p + 1]
                lot[g][5] += 2
                p += 2
                lot[g][4] = lot[g][p]

            if lot[g][4] == 0 and lot[g][p + 1] == 0:
                # Process will be terminated if no more bursts to run
                print("process", lot[g][2], " has ended")
                lot[g][3] = 0
                lot[g][4] = 0
            last = 3
            print("Process", g + 1, "is executing and is in Queue 3")
        # print("green")

        # If current process is in queue 2, the following will execute
        elif lot[g][3] == 2:
            # Counter for the amount of time units that
            # a process in queue 2 has been executing
            t += 1
            if c[0] == g:
                c[1] += 1
            else:
                c[0] = g
                c[1] = 1

            # Adds waiting time to the process that will be executed
            # Decreases remaining CPU burst time
            p = lot[g][5]
            if c[1] == 1:
                r = t - lot[g][0]
                lot[g][1] += r
            lot[g][4] -= 1

            if c[0] == g and c[1] == tq2 and lot[g][4] > 0:
                # If process still has CPU burst time after it reaches
                # time quantum of 10 units, process moved to Queue 3
                print("Process", g + 1, "will be moved to queue 3")
                lot[g][3] = 3
                c[0] = 10
                c[1] = 0

            lot[g][0] = t
            if lot[g][4] == 0 and lot[g][p + 1] != 0:
                # Adds I/O burst time to the process that has executed
                # Positions the process for next CPU burst time
                c[0] = 10
                c[1] = 0
                lot[g][0] += lot[g][p + 1]
                lot[g][5] += 2
                p += 2
                lot[g][4] = lot[g][p]

            if lot[g][4] == 0 and lot[g][p + 1] == 0:
                # If the process has no more burst times left, will terminate
                print("process has ended")
                lot[g][3] = 0
                lot[g][4] = 0
            l = 10
            last = 2
            print("Process", g + 1, "is executing and is in Queue 2")

        # If current process is in queue 1, the following will execute
        else:  # lot[g][3] == 1
            # Stops the counting for for a process was executing in queue 2
            l = 10
            last = 1
            c[0] = 10
            c[1] = 0

            # Adds waiting time to the process that will be executed
            # Also finds CPU burst time for current process
            r = t - lot[g][0]
            lot[g][1] += r
            p = lot[g][5]
            lot[g][0] = t


            if lot[g][4] > tq1:
                # If current burst is larger that time quantum (5 time units)
                # will be moved to Queue 2. Time updated
                print("Process",g+1,"will be moved to queue 2")
                lot[g][3] = 2
                lot[g][0] += tq1
                lot[g][4] -= tq1
                t += tq1

            else:
                # If current burst is not larger than time quantum, it
                # will execute fully the remaining current burst
                lot[g][0] += lot[g][4]
                t += lot[g][4]
                if lot[g][p + 1] == 0:
                    # Process will end if no more burst times remaining
                    print("Process",g+1," has ended")
                    lot[g][3] = 0
                    lot[g][4] = 0

                else:
                    # Adds I/O to the process so that it will come back
                    # after that I/O time has been fullfilled
                    lot[g][0] += lot[g][p + 1]
                    lot[g][5] += 2
                    p += 2
                    lot[g][4] = lot[g][p]
            print("Process", g + 1, "is executing and is in Queue 1")

        if response == True:
            rt[g] = lot[g][1]
            print("Process", g + 1, "has gone for the first time")
            print("Response time: ", rt[g])
        response = False

        print("Current Execution Time: ", t)

        # Checks to see if all processes are done executing
        e = 0
        for i in range(n):
            e += lot[i][4]
        # If all are done executing, loops will end
        if e == 0:
            progress = False

    lot.sort(key=lambda lot: lot[2])
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    cpu = 100 - (h / t * 100)
    print("Overall time spent being idle: ", h)
    print("The last process finished execution at time:", t)
    print("MLFQ CPU Utilization:", cpu, "%")

    # Finds turnaround times. Since the arrival time for all
    # processes are 0, the time in which the process ends
    # is in fact the turnaround time
    for j in range(n):
        tat[j][0] = lot[j][2]
        for i in range(6, 25):
            tat[j][1] += lot[j][i]
    tat.sort(key=lambda tat: tat[0])
    for i in range(n):
        tat[i][1] += lot[i][1]

    # Print process names
    print("Processes No. " +  "Response Time " +
          " Waiting time " + " Turn around time")


    for i in range(n):
        totalWT += lot[i][1]
        totalRT += rt[i]
        totalTAT += tat[i][1]
        print(" " + str(i + 1) + "\t\t" +
              str(rt[i]) + "\t\t " +
              str(lot[i][1]) + "\t\t " +
              str(tat[i][1]))

    print("Average waiting time = " + str(totalWT / n))
    print("Average response time = " + str(totalRT / n))
    print("Average turn around time = " + str(totalTAT / n))


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

    lot = [[0] * (m + 2) for i in range(n)]

    findTimes(processes, n, m, lot)



