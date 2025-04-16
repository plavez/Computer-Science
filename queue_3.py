from queue import Queue

my_queue = Queue()
my_list = []
for i in range(1, 11):
    my_queue.put(i)
    my_list.append(my_queue.get())
print(my_list)
