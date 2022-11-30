class area:
    def shape(self,a=None,b=None):
        if a!=None and b!=None:
            print("rectangle=",(a*b))
        elif a!=None:
            print("square=",(a*a))
        else:
            print("no area")
a=area()
a.shape(10,5)
a.shape(10)
a.shape()
