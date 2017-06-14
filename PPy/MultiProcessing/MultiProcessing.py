import time, multiprocessing


class MultiProcessing(object):
	def deposit(self, balance, lock):
		print("Depositing amount, current balance is {}".format(balance.value))
		for i in range(1, 100):
			time.sleep(0.5)
			lock.acquire()
			balance.value = balance.value + i
			lock.release
		
	def withdrawal (self, balance, lock):
		print("Withdrawing amount, current balance is {}".format(balance.value))
		for i in range(1, 100):
			time.sleep(0.5)
			lock.acquire()
			balance.value = balance.value - i
			lock.release
	
MultiProcessing = MultiProcessing()
balance = multiprocessing.Value('i', 200)
lock = multiprocessing.Lock()
d = multiprocessing.Process(target=MultiProcessing.deposit, args=(balance, lock))
w = multiprocessing.Process(target=MultiProcessing.withdrawal, args=(balance, lock))
d.daemon = True
w.daemon = True
d.start()
w.start()
d.join()
w.join()
