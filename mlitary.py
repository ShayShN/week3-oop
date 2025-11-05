from tkinter import S


class Weapon:
    total_weapons = 0
    def __init__(self, name: str, ammo: int, ):
        self.name = name
        self.ammo = ammo
        Weapon.total_weapons +=1
        
    def __str__(self):
        return f' name: {self.name}, ammo: {self.ammo}'
    
    
class Soldier:
    def __init__(self, name: str, rank: str, weapon: Weapon):
        self.name = name
        self.rank = rank
        self.weapon = weapon
        
    def report(self):
        print(f' name: {self.name}\n rank: {self.rank}\n weapon >>> {self.weapon}')
            
            
class Unit:
    def __init__(self, unit_name: str, commander: Soldier, soldiers: list[Soldier], strike: list[StrikeOption]):
        self.unit_name = unit_name
        self.commander = commander
        self.soldiers = soldiers
        self.strike = strike
        
    def briefing(self):
        print(self.unit_name)
        self.commander.report()

weapon1 = Weapon("uzzi", 300)
weapon2 = Weapon("M4", 100)     
   
soldier1 = Soldier("shay", "ramatcal", weapon1)
soldier2 = Soldier("ossi", "turai", weapon2)
soldier3 = Soldier("chaim", "seren", weapon2)

# unit1 = Unit("givati",soldier1, [soldier1, soldier2, soldier3])
# unit2 = Unit("kodkod",soldier2, [soldier2, soldier3])

# soldier1.report()
# unit1.briefing()   
# unit2.briefing()     


class StrikeOption:
    def __init__(self, name: str, ammo: int):
        self.name = name
        self.ammo = ammo
        
    def strike(self):
        pass 
    
    def __str__(self):
        return f' name attack: {self.name}, ammo: {self.ammo}'
    
class Tank(StrikeOption):
    def __init__(self, name, ammo):
        super().__init__(name, ammo)
    
    def strike(self):
        print("attack Tank!")
    
class Drone(StrikeOption):
    def __init__(self, name, ammo):
        super().__init__(name, ammo)
        
    def strike(self):
        print("Hattack drone!")
        
        
strik1 = StrikeOption("robot", 5000)  
strik2 = StrikeOption("mag", 6000) 
strik3 = StrikeOption("tank", 4000)
     
unit1 = Unit("givati",soldier1, [soldier1, soldier2, soldier3], [strik1, strik2, strik3])

for i in unit1.strike:
    print(i)


class Agent:
    def __init__(self, codename: str, clearance_level: int):
        self.codename = codename
        self.clearance_level = clearance_level
        
 
class Mission:
    def __init__(self, mission_name: str, target: str, assigned_agent: Agent):
        self.mission_name = mission_name
        self.target = target
        self.assigned_agent = assigned_agent
        
    def briefing(self):
        print(f'mission: {self.mission_name}, target: {self.target}, assigned agent: {self.assigned_agent}')
    

class MissionManager:
    def __init__(self):
        self.list_mission = []
     
    def add(self, arr):
        self.list_mission.append(arr)
        
    def remove_mission(self, name_mission):
        for i in self.list_mission:
            if i.mission_name == name_mission:
                self.list_mission.remove(name_mission)
            
class Army:
    total_attacks =0
    def __init__(self, units: list[Unit]):
        self.units = units 
        Army.total_attacks +=1 
    
    def attack_all(self):
        pass
    
