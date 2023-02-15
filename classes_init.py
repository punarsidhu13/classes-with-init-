#first example

class Human:
    def __init__(self,eyes,arms):
        self.eyes=eyes
        self.arms=arms
    def speak(self):
        print("i can speak and i have", self.eyes, "eyes and", self.arms, "arms")


punar = Human(2,2)
punar.speak()



Human.speak(punar)
print("<<<--------------------->>>")
#Second Example

class Mountains:
    def __init__(self,peaks,trees):
        self.peaks=peaks
        self.trees=trees
    
    def scene(self):
        print("very scenic and has", self.peaks,"peaks and", self.trees, "trees")

everest = Mountains("highest","less")
mountk2 = Mountains(4,100)
everest.scene()
mountk2.scene()

print("<<<----------------------------------->>>")

# Third Example

class Building:
 
    def __init__(self,rooms,windows):
        self.rooms=rooms
        self.windows=windows
    def accomodate(self):
        print("place To-Let available with ",self.rooms ,"rooms and" ,self.windows, "windows" )

home = Building(4,10)
home1 = Building(8,20)
home.accomodate()
home1.accomodate()

print("<<<---------------------------------->>>")

# Fourth Example

class Football:
    def __init__(self,goals,assists,name):
        self.goals=goals
        self.assists=assists
        self.name=name

    def stats(self):
        print("GOAAALLLLL!!!! with", self.goals, "goals and", self.assists,"assists of" , self.name)

messi = Football(796,350,"MESSI")
ronaldo = Football(824,232,"RONALDO")
bani = Football(0,1,"BANI")

ronaldo.stats()
messi.stats()
bani.stats()

print("<<<----------------------------------->>>")

# Fifth Example'

class Planets:
    def __init__(self,name,planets,orbit,):
        self.planets=planets
        self.orbit=orbit
        self.name=name
    def solarsys(self):
        print("All planets revolve around the sun and", self.name, "is the",
         self.planets ,"planet in an",self.orbit, "orbit")
earth= Planets("earth","3rd","elliptical" )
mars= Planets("mars", "4th", "elliptical")
earth.solarsys()
mars.solarsys()

print("<<<-------------------------------->>>")

