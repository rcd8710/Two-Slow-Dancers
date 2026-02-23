import pygame


class Dancer:
    def __init__(self, heart,head,body,larm,rarm,lleg,rleg):
        self.heart = heart
        self.head = head
        self.body = body
        self.larm = larm
        self.rarm = rarm
        self.lleg = lleg
        self.rleg = rleg
      
    def drawDancer(self, surface):
        self.head.draw(surface)
        self.body.draw(surface)
        self.heart.draw(surface)
        self.larm.draw(surface)
        self.rarm.draw(surface)
        self.lleg.draw(surface)
        self.rleg.draw(surface)

    def mirror(self):
        target = self.rarm.x

        if self.larm.x < target:
            self.larm.x += 1
        elif self.larm.x > target:
            self.larm.x -= 1
    
    def mirror(self):
        center = self.body.x

        self.larm.x = 2 * center - self.rarm.x
        self.lleg.x = 2 * center - self.rleg.x
            

        

class Circle:
    def __init__(self,x,y,radius,color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
    
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def drawmove(self,dx,dy):
        self.x += dx
        self.y += dy
    
    
    
    

dancer1head = Circle(125, 125, 10, "red")

dancer1body = Circle(125, 170, 10, "blue")

dancer1heart = Circle(125, 165, 10, "pink")

dancer1larm = Circle(95, 165, 10, "green")
dancer1rarm = Circle(155, 165, 10, "green")

dancer1lleg = Circle(110, 200, 10, "purple")
dancer1rleg = Circle(140, 200, 10, "purple")

dancer1 = Dancer(
    dancer1heart,
    dancer1head,
    dancer1body,
    dancer1larm,
    dancer1rarm,
    dancer1lleg,
    dancer1rleg
)
dancer2head = Circle(125 + 250, 125, 10, "red")
dancer2body = Circle(125 + 250, 170, 10, "blue")

dancer2heart = Circle(125 + 250, 165, 10, "pink")

dancer2larm = Circle(95 + 250, 165, 10, "green")
dancer2rarm = Circle(155 + 250, 165, 10, "green")

dancer2lleg = Circle(110 + 250, 200, 10, "purple")
dancer2rleg = Circle(140 + 250, 200, 10, "purple")
dancer2 = Dancer( 
    dancer2heart,
    dancer2head,
    dancer2body,
    dancer2larm,
    dancer2rarm,
    dancer2lleg,
    dancer2rleg
    )

