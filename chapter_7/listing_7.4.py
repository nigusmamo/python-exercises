class Tv():
    def __init__(self):
        self.channel = 1
        self.volumeLevle = 1
        self.on = False
    def turnon(self):
        self.on = True
    def turnoff(self):
        self.on = False
    def get_channel(self):
        return self.channel
    def set_channel(self,channel):
        if self.on and 1 <= self.channel <= 150:
            self.channel = channel
    def get_volumeLevle(self):
        return self.volumeLevle
    def set_volumeLevle(self,volume):
        if self.on and 1 <= self.volumeLevle <= 10:
            self.volumeLevle = volume
    def channelUp(self):
        if self.on and self.channel < 150:
            self.channel += 1
    def channelDown(self):
        if self.on and self.channel < 150:
            self.channel -= 1
    def volumelUp(self):
        if self.on and self.volumeLevle < 10:
            self.volumeLevle += 1
    def volumelDown(self):
        if self.on and self.volumeLevle < 10:
            self.volumeLevle -= 1
def main():
    tv1 = Tv()
    tv1.turnon()
    tv1.get_channel()
    tv1.set_volumeLevle(7)
    print("tv1's channel is",tv1.get_channel(),"and volume level is",tv1.get_volumeLevle())
main()
    

