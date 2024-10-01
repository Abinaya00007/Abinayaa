class animal:  #overridding
    def speak(self):
        return"hi"
    
class dog(animal):
    def speak(self):
        return "bark"
    
d=dog()
print(d.speak())
