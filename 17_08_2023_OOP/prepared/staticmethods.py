import math

class AreaUtils:
    _calculations = 0
    
    @staticmethod
    def circle_area(radius):
        AreaUtils._calculations += 1
        return math.pi * (radius ** 2)
    
    @staticmethod
    def rectangle_area(width, length):
        AreaUtils._calculations += 1
        return width * length
    
    @staticmethod
    def get_calculations():
        return AreaUtils._calculations
        


print(AreaUtils.circle_area(25))
print(AreaUtils.circle_area(10))
    
print(AreaUtils.get_calculations())
    
    
    
    
    