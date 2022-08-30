import sys
sys.path.append(sys.path[0] + '/../../../library/python')


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
