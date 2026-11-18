#1. Add Process: Insert a process with Process ID, Process Name and Priority (enqueue)

queue = []

def enqueue(pid, name, priority):
    queue.append((priority, pid, name))
    queue.sort()
    print("Process added successfully")

enqueue(101, "System", 1)
enqueue(102, "Browser", 2)
enqueue(103, "Music", 3)

print(queue)


#2. Execute Process: Remove the process with the highest priority (dequeue)

def dequeue():
    if not queue:
        print("Queue is empty")
    else:
        p = queue.pop(0)
        print("Executed Process:", p[2])

dequeue()

print("Remaining Queue:", queue)       


# 3. View Next Process: Display the next process to be executed (display_next)

def display_next():
    if not queue:
        print("Queue is empty")
    else:
        print("Next Process:", queue[0][2])

display_next()

# 4. Display Processes: Display all pending processes in priority order (display_all)

def display_all():
    if not queue:
        print("Queue is empty")
    else:
        for p in queue:
            print(p)

display_all()

# 5. Count Processes: Display the total number of pending processes (count)

def count():
    print("Total Processes:", len(queue))

count()