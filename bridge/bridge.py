# circle square
# vector raster
# 2 x 2 matrix

# VectorCircle, VectorSquare, RasterCircle, RasterSquare -> leads to Cartesian complexity explosion
# cartesian product (set of all ordered possible pairs)
from abc import ABC


# renderer for particular shape (grows with addition of new shapes)
class Renderer(ABC):
    def render_circle(self, radius):
        pass


# Vector class (grows with addition of new shapes)
class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing vectors for a circle of radius {radius}.')


# Raster class (grows with addition of new shapes)
class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing pixels for a circle of radius {radius}.')
        

# bridge
class Shape:
    def __init__(self, renderer):
        self.renderer = renderer
        
    def draw(self):
        pass
    
    def resize(self, factor):
        pass
    

# concrete shape
class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):  # using bridge
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor


if __name__ == "__main__":
    raster = RasterRenderer()
    vector = VectorRenderer()

    circle = Circle(vector, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()
    print('-----')

    circle = Circle(raster, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()

# violates open-close principle but it's better than create separate solution for each pair
# e.g., if need to add Triangle -> update Renderer, VectorRenderer, RasterRenderer
