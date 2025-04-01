#Abstract class
from abc import ABC , abstractmethod

class Abclass(ABC):
    def print(self,x):
        print('Passed Value :',x)
    
    @abstractmethod
    def task(self):
        print('We are  inside the Abclass task')
        
class Test_Class(Abclass):
    def task(self):
        print('We are inside the Test_Class task')
        
test_obj = Test_Class()
test_obj.task()
test_obj.print(100)