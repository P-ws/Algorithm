def run_cmd_with_queue(cmd, local_queue):
    cmd_type = cmd[0]

    if cmd_type == "push":
        _, num = cmd
        local_queue.append(int(num))
    elif cmd_type == "pop":
        if len(local_queue) > 0:
            print(local_queue.pop(0))
        else:
            print(-1)
    elif cmd_type == "size":
        print(len(local_queue))
    elif cmd_type == "empty":
        if len(local_queue) > 0:
            print(0)
        else:
            print(1)
    elif cmd_type == "front":
        if len(local_queue) > 0:
            print(local_queue[0])
        else:
            print(-1)
    elif cmd_type == "back":
        if len(local_queue) > 0:
            print(local_queue[-1])
        else:
            print(-1)

    return local_queue

n = int(input())
queue = []
cnt = 0

for _ in range(n):
    command = input().split()
    queue = run_cmd_with_queue(command, queue)