import numpy as np
import cv2 as cv
import random

#general parameters
width = 900
height = 600
n_trees = 30
ground_level = height-100

#colours
# green, light_green, brown = (40,185,40),(25,220,0),(30,65,155)

#blank image
bg = np.zeros((height, width, 3), dtype=np.uint8)

#draw background
cv.rectangle(bg,(width,0), (0, ground_level), (255,225,95), -1)

#***************

class Tree:
    def __init__(self,image):
        self.image = image
        self.loaction = int(np.random.choice(range(900),1).item())
        self.height =int(np.random.choice(range(200,350),1).item())
        self.radius= 50
        self.scale = np.random.choice(np.linspace(0.5,2.5,num=8),1).item()

    def Generate_color(self):
        green = (0,random.randint(130,200),0)
        light_green = (35,random.randint(200,250),35)
        brown = random.choice([(2,30,85),(5,55,129),(0,70,140)])
        return green,light_green,brown

    def Draw(self):
        green,light_green,brown = self.Generate_color()

        small_radius = int(self.radius*self.scale-int(20*self.scale))
        #tree
        cv.line(self.image,(self.loaction,ground_level),(self.loaction,ground_level-self.height),brown,int(10*self.scale))
        #branch
        cv.line(self.image,(self.loaction,ground_level-self.height+int(75*self.scale)),
                (self.loaction+int(45*self.scale),
                 ground_level-self.height+int(45*self.scale)),brown,int(5*self.scale))
        
        cv.line(self.image,(self.loaction,ground_level-self.height+int(75*self.scale)),
                (self.loaction-int(45*self.scale),
                 ground_level-self.height+int(45*self.scale)),brown,int(5*self.scale))


        #trunk
        cv.circle(self.image,(self.loaction,ground_level-self.height),(int(self.radius*self.scale)),green,-1)
        #leaf
        cv.circle(self.image,(self.loaction-int(45*self.scale),ground_level-self.height+int(45*self.scale)),small_radius,green,-1)
        cv.circle(self.image,(self.loaction+int(45*self.scale),ground_level-self.height+int(45*self.scale)),small_radius,green,-1)

        cv.circle(self.image,(self.loaction-int(45*self.scale),ground_level-self.height+int(45*self.scale)),small_radius,light_green,-1)
        cv.circle(self.image,(self.loaction+int(45*self.scale),ground_level-self.height+int(45*self.scale)),small_radius,light_green,-1)
        cv.rectangle(bg,(width, ground_level), (0, height), green, -1)

        return self.image

    
                
#***************

#display image
for i in range(n_trees):
    img = Tree(bg).Draw()
cv.imshow('forest of objects', img) 


cv.waitKey(000)
cv.destroyAllWindows()