#建立Animal的class
class Animal():
    def __init__(self, weight, mood):
      self.weight = weight
      self.mood = mood
    def feed(self):
        #在子分類再做feed和walk的函式
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
        #因餵食改變體重和心情
        self.weight = self.weight + n_feed*0.2
        self.mood = self.mood + n_feed*1
    def walk(self, n_walk):
        #因散布改變體重和心情
        self.weight = self.weight - n_walk*0.2
        self.mood = self.mood + n_walk*2
    def bath(self, n_bath):
        #繼承父類別
        super().bath(n_bath)
    def printf(self, n_feed, n_walk, n_bath):
        self.feed(n_feed)
        self.walk(n_walk)
        self.bath(n_bath)
        print("狗狗現在的體重=", self.weight, "kg", "心情=", self.mood) 
              
class Shiba(Dogs):
    def __init__(self, weight, mood):
        self.weight = weight
        self.mood = mood
    def feed(self, n_feed):
        #覆寫原本的feed
        self.weight = self.weight + n_feed*0.3
        self.mood = self.mood + n_feed*5
    def printf(self, n_feed, n_walk, n_bath):
        self.feed(n_feed)
        #繼承父類別的walk和bath
        super().walk(n_walk)
        super().bath(n_bath)
        print("柴犬現在的體重=", self.weight, "kg", "心情=", self.mood) 
    def mood_constraint(self, constr):
        self.constr = constr
        #限制柴犬的心情上限
        if (self.mood > self.constr):
            self.mood = self.constr
            print("所以，柴犬現在的心情", self.mood)
        print("mood最高只能為=" ,self.constr )

shiba = Shiba(5, 70) 
shiba.printf(20, 10, 3) 
shiba.mood_constraint(90) 
shiba.mood_constraint(300) #請在這邊改變你的mood_constraint
