class Animal():
    def __init__(self, weight, mood):
      self.weight = weight
      self.mood = mood
    def feed(self):
        pass
    def walk(self):
        pass
    def bath(self, n_bath):
        self.mood = self.mood -2*n_bath
    
class Dogs(Animal):
    def __init__(self, weight, mood):
        self.weight = weight
        self.mood = mood
    def feed(self, n_feed):
        self.weight = self.weight + n_feed*0.2
        self.mood = self.mood + n_feed*1
    def walk(self, n_walk):
        self.weight = self.weight - n_walk*0.2
        self.mood = self.mood + n_walk*2
    def bath(self, n_bath):
        super().bath(n_bath)
    def printf(self, n_feed, n_walk, n_bath):
        self.feed(n_feed)
        self.walk(n_walk)
        self.bath(n_bath)
        print("狗狗現在的體重=", self.weight, "kg", "心情=", self.mood) 


class Cats(Animal):
    def __init__(self, weight, mood):
      self.weight = weight
      self.mood = mood
    def feed(self,n_feed):
      self.weight = self.weight + n_feed*0.1
      self.mood = self.mood + n_feed*1
    def walk(self, n_walk):
      self.weight = self.weight - n_walk*0.1
      self.mood = self.mood - n_walk*1
    def bath(self, n_bath):
      super().bath(n_bath)
    def printf(self, n_feed, n_walk, n_bath):
      self.feed(n_feed)
      self.walk(n_walk)
      self.bath(n_bath)
      print("貓貓現在的體重=", self.weight, "kg", "心情=", self.mood) 

dog = Dogs(4.8, 65) 
dog.printf(18, 10, 4) 

cat = Cats(8.2, 60) 
cat.printf(40, 7, 1) 
