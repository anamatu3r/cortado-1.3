from time import sleep
from random import randint

class builtins:
    def flash():
        print("hit em with the chopper its the rat trap")

class engine:
    def __init__(self, program):
        self.program = program
        functions = builtins()
        
        self.simulated_memory = []
        self.simulated_memory_labels = []
        self.line = 0
        self.col = 0
        self.parameters = []
      
        self.paremeter_build_cache = []
        self.function_cache = [] 

        self.dispatch_table = {
            "flash": functions.flash
        }
      
        self.tokens = []
       

    
        
