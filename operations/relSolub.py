from pydantic import BaseModel
import math
import math as ma

def rsStanding(Ygd,p,API,Tem):
  return ((Ygd)*(((p/18.2)+1.4)*(10**((0.0125*API)-(0.00091*Tem)))**1.2048))


class rsStanrequest(BaseModel):
  Ydg:float
  p:float
  API:float
  Tem:float


def rsVaz_Beg(Ygs,p,API,Tem):
  
  if(API<=30):
    return (((0.0362*Ygs)*(p**1.0937))*(ma.exp( 25.824*(API/(Tem+460)))))
  elif(API>30):
    return (((0.0178*Ygs)*(p**1.1870))*(ma.exp( 23.931*(API/(Tem+460)))))

class rsVazBegrequest(BaseModel):
  Ygs:float
  p:float
  API:float
  Tem:float


def rsGlaso(Ygd,API,Tem,p, A):
  F= (10**(2.8869-(14.1811-3.3093*(math.log(p)))**0.5))
  return Ygd*((F*(API**0.989)/(Tem**A))**1.2255)

class rsGlarequest(BaseModel):
  Ygd:float
  API:float
  Tem:float
  p:float
  A:float



