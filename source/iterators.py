from utils import Answer, Question, exercise

@exercise
def iterators():

  Question(1, """
		Implement an iterator class to return the square of all numbers from “a” to “b”
 	""")
  
  class Square:

    def __init__(self, a, b):
      self.a = a
      self.b = b

    def __iter__(self):
      return self

    def __next__(self):
      if self.a < self.b:
        value = self.a
        self.a += 1
        return value**2
      else:
        raise StopIteration
        
  results = [x for x in Square(0, 10)]
  Answer(f"Square(0,10): {results}")
    
  #2 Implement an interator class to return all even numbers from 1 to (n)
  Question(2, """
		Implement an iterator class to return all the even numbers from 1 to (n).
 	""")

  class EvenIter:
    def __init__(self, n):
      self.i = 1
      self.n = n

    def __iter__(self):
      return self

    def __next__(self):
      while True:
        if self.i < self.n:
          if self.i % 2 == 0:
            value = self.i
            self.i += 1
            return value
        else:
          raise StopIteration
        self.i += 1
          
  results = [x for x in EvenIter(10)]
  Answer(f"EvenIter(10): {results}")
    
        
  #3 Implement an interator class to return all odd numbers from 1 to (n)
  Question(3, """
		Implement an iterator class to return all the odd numbers from 1 to (n).
 	""")
  
  class OddIter:
    def __init__(self, n):
      self.i = 1
      self.n = n

    def __iter__(self):
      return self

    def __next__(self):
      while True:
        if self.i < self.n:
          if self.i % 2 == 1:
            value = self.i
            self.i += 1
            return value
        else:
          raise StopIteration
        self.i += 1
          
  results = [x for x in OddIter(10)]
  Answer(f"OddIter(10): {results}")
  
  #4 Implement an interator class to return all numbers from (n) down to 0.
  Question(4, """
		Implement an iterator class to return all numbers from (n) down to 0.
 	""")
  
  class Descend:
    def __init__(self, n):
      self.n = n

    def __iter__(self):
      return self

    def __next__(self):
      if self.n >= 0:
        value = self.n
        self.n -= 1
        return value
      else:
        raise StopIteration

  results = [x for x in Descend(10)]
  Answer(f"Descend(10): {results}")
  
  #5 Implement an interator class to return the fibonnaci sequence from the first element up to (n).
  Question(5, """
		Implement an iterator class to return the fibonnaci sequence from the first element up to (n).
 	""")
 
  class Fibonacci:
    def __init__(self, n):
      self.n = n
      self.i = 0
      self.first = 0
      self.second = 1
    def __iter__(self):
      return self
  
    def __next__(self):
      if self.i < self.n:
        if self.i == 0 or self.i == 1:
          value = self.i
          self.i += 1
          return value
        else:
          value = self.first + self.second
          self.first = self.second
          self.second = value
          self.i += 1
          return value
      else:
        raise StopIteration
        
  results = [x for x in Fibonacci(12)]
  Answer(f"Fibonacci(12): {results}")
  
  #6 Implement an iterator class to return all consecutive pairs of numbers from 0 until (n), suc as (0,1), (1,2), (2,3)...
  Question(6, """
		Implement an iterator class to return all consecutive pairs of numbers from 0 until (n).
 	""")

  class Pairs:
    def __init__(self, n):
      self.n = n
      self.i = 0
    def __iter__(self):
      return self
    def __next__(self):
      if self.i < self.n:
        value = (self.i, self.i+1)
        self.i += 1
        return value
      else:
        raise StopIteration

  results = [x for x in Pairs(5)]
  Answer(f"Pairs(5): {results}")
