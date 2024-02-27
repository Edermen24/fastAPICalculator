from pydantic import BaseModel
import math
import math as ma


def viscVaz_Begg(Mob=float,p=float,pb=float):
  m=((2.6*(p**1.187))*(ma.exp(-11.513+((-8.98*(10**(-5)))*p))))
  return Mob*((p/pb)**m)

class viscVBrequest(BaseModel):
  Mob:float
  p:float
  pb:float

def viscKarto(Mob=float,p=float,pb=float):
  return ((1.0081*Mob)+(0.001127*(p-pb)))*((-0.006517*(Mob**1.8148))+((0.038*(Mob**1.59))))


def viscGuet(Mob=float,p=float,pb=float):
  return ((0.9886*Mob)+(0.002763*(p-pb)))*((-0.01153*(Mob**1.7933))+((0.0316*(Mob**1.5939))))


def viscPetro(Mob,p,pb):
  K= (-1.0146+(1.3322*(math.log(Mob))))- (0.4876*(math.log(Mob**2)))- (1.15036*(math.log(Mob**3)))
  return (Mob + (1.3449*(10**-3)))*((p-pb)*(10*K))