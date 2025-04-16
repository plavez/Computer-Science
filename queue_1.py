from collections import deque


def queue():
    a_queue = []
    b_queue = []
    temp = []
    for i in range(10):
        a_queue.append(i)
    temp = a_queue.copy()
    for i in range(len(a_queue)):
        b_queue.append(a_queue.pop(0))
    print(f"Порядок входа в очередь{temp} Порядок выхода из очереди {b_queue}")


queue()


def queue_2():
    a_list = deque()
    b_list = deque()
    temp = []
    for i in range(11):
        a_list.append(i)
        temp = a_list.copy()

    for i in range(len(a_list)):
        b_list.append(a_list.popleft())

    print(
        f"Порядок входа в очередь {list(temp)} Порядок выхода из очереди {list(b_list)}")


queue_2()
