class area:
    def circle(self,r):
        self.r=r
        print("area=",(3.14*r**2))
class peri(area):
    def circle(self,r):
        self.r=r
        print("peri=",(3.14*r*2))
p=peri()
p.circle(10)
p.circle(10)
