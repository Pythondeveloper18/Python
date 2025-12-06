import threading
import time

def worker():
	print("threading execuation begin")
	time.sleep()
	print("threading execuation ends")


t1 = threading.Thread(target=worker)
t2 = threading.Thread(target=worker)

t1.start()
t2.start()
t1.join()
t2.join()
print("main thread execuation ends")
