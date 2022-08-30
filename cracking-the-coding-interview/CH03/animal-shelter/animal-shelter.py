import sys
sys.path.append(sys.path[0] + '/../../../library/python')

from typing import Tuple
import unittest


from linear import Queue

class Animal(): 
    def __init__(self, name: str) -> None: 
        self.name = name
        self.order = 0
    
    def __str__(self) -> str: 
        return self.name

class Dog(Animal): 
    def __init__(self, name: str) -> None: 
        super().__init__(name)

class Cat(Animal):
    def __init__(self, name: str) -> None: 
        super().__init__(name)

class AnimalQueue(): 
    def __init__(self) -> None:
        self.dogs = Queue()
        self.cats = Queue()
        self._order = 0
    
    def enqueue(self, animal: Animal) -> None: 
        animal.order = self._order
        self._order += 1
        if isinstance(animal, Dog):
            self.dogs.enqueue(animal)
        elif isinstance(animal, Cat):
            self.cats.enqueue(animal)
        else: 
            raise TypeError('Animal must be a Dog or a Cat')
    
    def dequeue_any(self) -> Animal: 
        if self.dogs.peek().order < self.cats.peek().order: 
            return self.dequeue_dog()
        else: 
            return self.dequeue_cat()
    
    def dequeue_dog(self) -> Dog:
        return self.dogs.pop()
    
    def dequeue_cat(self) -> Cat:
        return self.cats.pop()


class SolutionTest(unittest.TestCase):
    def __init__(self, methodName: str, param: Tuple) -> None:
        super().__init__(methodName)
        self.input, self.output = param[0], param[1]
    def test_runs(self): 
        self.assertEqual(solution(*self.input), self.output)

if __name__ == '__main__': 
    # cases = [] # edit here
    # suite = unittest.TestSuite()
    # for i, o in cases: 
    #     suite.addTest(SolutionTest('test_runs', (i, o)))
    # unittest.TextTestRunner(verbosity=2).run(suite)
    cat = Cat('my cat')
    dog = Dog('my dog')
    animal = Animal('my animal')
    print(isinstance(cat, Cat), isinstance(cat, Animal), isinstance(dog, Dog), isinstance(dog, Animal), isinstance(cat, Dog), isinstance(dog, Cat))
    print(isinstance(animal, Animal), isinstance(animal, Cat), isinstance(animal, Dog))
