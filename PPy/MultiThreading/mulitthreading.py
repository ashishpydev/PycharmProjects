import threading
import time


class CreateThreads(object):
	
	def find_square(self, lst):
		print("Square of Numbers.")
		for n in lst:
			time.sleep(0.5)
			print("Square of {} is {}".format(n, n*n))

	def find_cube(self, lst):
		print("Cube of Numbers.")
		for n in lst:
			time.sleep(0.5)
			print("Cube of {} is {}".format(n, n*n*n))

create_threads = CreateThreads()
start_time = time.time()
lst = [2, 3, 4, 5]
t1 = threading.Thread(target=create_threads.find_square, args=(lst,))
t2 = threading.Thread(target=create_threads.find_cube, args=(lst,))
t1.daemon = True
t2.daemon = True
t1.start()
t2.start()
t1.join()
t2.join()
print("Completed in {}".format(time.time() - start_time))