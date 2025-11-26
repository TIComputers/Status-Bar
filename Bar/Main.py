from threading import Thread as th
from time import time


class Bar:
    def __init__(self):
        self.block  = 30
        self.total  = 0.0
        self.filled = 0.0 
        
        self.times  = 0.0
        self.timef  = 0.0
        self.sumtime= 0.0
        self.checkt = False
        self.checkb = True
        self.text   = ""
        
        self.white  = "\033[97m"
        self.red    = "\033[91m"
        self.yellow = "\033[93m"
        self.green  = "\033[92m"
        self.gray   = "\033[90m"
        self.reset  = "\033[0m"
            
        self.shap1  = "▄"
        self.shap2  = "▓"
        self.shap3  = "█"
        self.shap4  = "▐"
    
    def color_bar(self, value=0):
        if value < 50:
            return self.white
        elif value < 85:
            return self.yellow
        elif value < 100:
            return self.red
        return self.green
        
    def calculate_block(self, precent=0):
        calculate = int((precent * self.block) / 100)
        remaining = self.block - calculate
        return [calculate, remaining]
        
    def display_bar(self, precentage=0):
        sumt  = self.sumtime
        color = self.color_bar(precentage)
        block = self.calculate_block(precentage)
        done  = block[1]
        ndone = block[0]
        reset = self.reset
        shap0 = self.shap4
        chline= ""

        if self.checkb == True:
            print(f"\r{color}{shap0*ndone}",end="")
            print(f"{self.gray}{shap0*done}   ",end="")
        else: chline = "\r"
        print(f"{chline}{reset}[{color}%{precentage:.2f}{reset}]  ",end="")
        if self.checkt == True:
            print(f"{color}{sumt:.2f}sec{self.reset}", end="")
        print(f"  {self.yellow}{self.text}{reset}", end="")
        if precentage >= 100:
            print("\n")


    def calculate_time(self):
        calculate    = (self.timef - self.times) / self.filled
        process      = self.total - self.filled
        self.sumtime = calculate * process
        
    def get_time(self):
        self.times  = float(time())
        self.checkt = True
        
    def update(self):
        self.calculate_time()
        precent = (self.filled * 100) / self.total
        self.display_bar(precent)  
    
    def get_process_processed(self, process=0, processd=0, text="", check_bar=True):
        self.timef = float(time())
        self.checkb= check_bar
        self.total = process
        self.filled= processd + 1
        self.text  = text
        self.update()
        
    def status(self, process, processd, text="", check_bar=True, count=1):
        p = th(target=self.get_process_processed, args=(process, processd, text, check_bar))
        p.start()
        p.join()
        
        
