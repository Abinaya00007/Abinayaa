class Dog:
    def speak(self):
        return"woof"
class Cat:
    def speak(self):
        return"meow"
    
def makesound(animal):
    print(animal.speak())
    
dog=Dog()
cat=Cat()
makesound(dog)
makesound(cat)
