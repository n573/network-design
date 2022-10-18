import threading
from time import sleep


def thread(name):
    print("Thread %s: starting" % name)
    sleep(5)
    print("Thread %sL finishing" % name)

if __name__ == '__main__':

    threads = list()

    N=3 # number of threads
    for index in range(N):
        x = threading.Thread(target=thread, args=(index,))
        threads.append(x)
        x.setDaemon(True)
        x.start()

    for index, thread in enumerate(threads):
        print("Main : before joining thread %d." % index)
        thread.join()
        print("Main : thread %s done" % index)