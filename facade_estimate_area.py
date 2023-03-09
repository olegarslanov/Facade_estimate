
# Modulis "facade_estimate_area" 


class FigureArea:
    
    def __init__(self, facade_lenght:float) -> float:
        self.facade_lenght = facade_lenght
    
 
class Rectangle(FigureArea):

    def __init__(self, facade_lenght:float, facade_height_same:float) -> float:
        super().__init__(facade_lenght)
        self.facade_height_same = facade_height_same

    def calculate_area_rectangle(self) -> float:
        facade_area_rectangle = self.facade_lenght * self.facade_height_same
        return facade_area_rectangle


class Trapezoid(FigureArea):

    def __init__(self, facade_lenght:float, facade_height_left:float, facade_height_right:float) -> float:
        super().__init__(facade_lenght)
        self.facade_height_left = facade_height_left
        self.facade_height_right = facade_height_right

    def calculate_area_trapezoid(self) -> float:
        facade_average_height_trapezoid = (self.facade_height_right + self.facade_height_left)/2
        facade_area_trapezoid = facade_average_height_trapezoid * self.facade_lenght
        return facade_area_trapezoid


class DoubleTrapezoid(FigureArea):
  
    def __init__(self, facade_lenght:float, facade_height_left:float, facade_height_middle:float, facade_height_right:float) -> float:
        super().__init__(facade_lenght)
        self.facade_height_left = facade_height_left
        self.facade_height_middle = facade_height_middle
        self.facade_height_right = facade_height_right
    
    def calculate_area_double_trapezoid(self) -> float:
        facade_average_height_double_trapezoid = (self.facade_height_right + self.facade_height_left + self.facade_height_middle*2)/4
        facade_area_double_trapezoid = facade_average_height_double_trapezoid * self.facade_lenght
        return facade_area_double_trapezoid



# Each rectangular facade consists of a certain specific figure from which the total area of ​​the facade can be calculated. 
# These figures (rectangle, trapezoid and double Trapezoid) are described and calculated in this module.


