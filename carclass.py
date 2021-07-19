class Car (object):
    def __init__(self,model,color,company,top_speed):
        self.model=model
        self.color=color
        self.company=company
        self.top_speed=top_speed

    def start(self):
        print("started")
    
    def stop(self):
        print("stopped")
    
    def accelarate(self):
        print("moving...")

bugatti_Bolide= Car ("Bolide","black","Bugatti","349")
bugatti_Bolide.start()
bugatti_Bolide.accelarate()
bugatti_Bolide.stop()
