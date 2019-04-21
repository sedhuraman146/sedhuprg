def volumecuboid(l,h,w):
return(l*h*w)
def surfaceareacuboid(l,h,w):
return(2*1*w+2*w*h+2*1+h)
l=1
h=5
w=7
print("volume=",volumecuboid(l,h,w))
print("total surface area=",surfaceareacuboid(l,h,w))
