def area_of_snowman(head,mid,bot):
    area=area_of_circle(head)+area_of_circle(mid)+area_of_circle(bot)
    return area

def area_of_circle(r):
    area=(pi*r**2)
    return area


pi=3.1415926
