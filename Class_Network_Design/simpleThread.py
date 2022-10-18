import threading
from time import sleep


def thread(id):
    n = 0
    while n < 5:
        print("Thread " + str(id) + ": " + str(n) + "\n")
        n += 1
        sleep(1)


if __name__ == '__main__':
    id_1 = 1
    id_2 = 2
    task_1 = threading.Thread(target=thread, args=(id_1,))
    task_1.setDaemon(True)

    task_2 = threading.Thread(target=thread, args=(id_2,))
    task_2.setDaemon(True)

    task_1.start()
    task_2.start()

    task_1.join()
    task_2.join()

    print("Threads done.")
