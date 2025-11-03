from random import randint


class Agent:
    total_agents = 0
    def __init__(self,code_name: str):
        self.code_name = code_name
        self._clearance_level = 0
        Agent.total_agents += 1
    
    def get_clearance_level(self):
        return self._clearance_level
    
    def set_clearance_level(self, value):
        if 1 <= value <= 10:
            self._clearance_level = value
    
    def report(self):
        print(f'Agent: {self.code_name} , reporting. ,Clearance Level: {self.get_clearance_level()}')
        
    @staticmethod
    def get_total_agents():
        print(Agent.total_agents)
    
class Mission:
    def __init__(self, mission_name: str, target_location: str, assigned_agent: Agent):
        self. mission_name =mission_name
        self.target_location = target_location
        self.assigned_agent = assigned_agent
            
    def brief(self):
        print(f'Mission: {self.mission_name}, Target: {self.target_location}, Agent: {self.assigned_agent.code_name    }')
    
class FieldAgent(Agent):
    def __init__(self, code_name, region: str):
        super().__init__(code_name, )       
        self.region = region
    
    def report(self):
        super().report()
        print(self.region)
    
# f = FieldAgent("shay", "open", "israel")
# f.report()


class CyberAgent(Agent):
    specialty = None
    def __init__(self, code_name ):
        super().__init__(code_name)
        CyberAgent.specialty = "Hack"
        
    def report(self):
        super().report()
        return self.specialty
    
agent = [FieldAgent("Haim", "Gaza"), CyberAgent("shay"), CyberAgent("David") ]
for i in agent:
    i.set_clearance_level(randint(1, 10))
    print(i.report())

Agent.get_total_agents()

# class AgencyDirector:
    