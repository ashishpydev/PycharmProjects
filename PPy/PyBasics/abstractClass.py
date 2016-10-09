from abc import ABCMeta, abstractmethod


class AbstractClass(object):
	__metaclass__ = ABCMeta
	
	@abstractmethod
	def display(self):
		pass


class ImplementAbsMethod(AbstractClass):
	def display(self):
		print("Implemented the Abstract Class")


aclass = ImplementAbsMethod()
aclass.display()
