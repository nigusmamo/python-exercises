class BMI:
    def __init__(self,name,weight,height):
        self.N = name
        self.W = weight
        self.H = height
    def get_BMI(self):
        return self.W / (self.H ** 2)
    def get_status(self):
        bmi = self.get_BMI()
        if bmi > 30 :
            return "obes"
        elif bmi > 24 :
            return "over weight"
        elif bmi > 18 :
            return "normal"
        else:
            return "under weight"
