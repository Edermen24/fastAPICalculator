from pydantic import BaseModel
import math


def pbStan(Rs, Ygd,API, Tem):

  Cpb = ((Rs/Ygd)**0.83) * (10**((0.00091*Tem)-(0.0125*API)))
  return 18.2 *(Cpb - 1.4)
#




def pbLasater(Ygd , Yo, Rs,Tem, API):

    if(15<=API<=40):
     Mo= (63.506 - API)/(0.0996)
     Yg= (Rs/379.3) / ((Rs/379.3)+(350*(Yo)/Mo))
     Pf=(5.043*((Yg)**3))+ (3.10526*((Yg)**2))+(1.36226*Yg)+(0.119118)
     return ((Pf*(Tem+460))/Ygd)
    elif(40< API <= 55):
     Mo= (1048.33/API)**1.6736
     Yg= (Rs/379.3) / ((Rs/379.3)+(350*(Yo)/Mo))
     Pf=(5.043*((Yg)**3))+ (3.10526*((Yg)**2))+(1.36226*Yg)+(0.119118)
    return ((Pf*(Tem+460))/Ygd)
   
class Lasarequest(BaseModel):
    Ygd:float
    Yo: float
    Rs:float
    Tem:float
    API:float
  
   

def pbVazBeg(Yg, API,Tem,Psep,Tsep,Rs):
   

  if(API <=30):
   Ygs = (Yg)*(((1+(5.912*(10**-5))))*(API*Tsep)*((math.log(Psep/114.7))))
   return ((27.624*Rs)/Ygs) *(10**(((-11.172*API)/(Tem+460))**0.914328))   
  elif(API>30):
    Ygs = (Yg)*(((1+(5.912*(10**-5))))*(API*Tsep)*((math.log(Psep/114.7))))
    return (( 58.18*Rs)/Ygs) *(10**(((10.393*API)/(Tem+460))**0.84246))  
  

class Vazbeggrequest(BaseModel):
  API: float
  Tem:float
  Psep:float
  Tsep:float
  Rs:float
  Yg:float


def pbGlaso(Rs,Ygd,Tem, API):
  F=(((Rs/Ygd)**0.816) * ((Tem**0.172)/(API**0.989)))
  return 10**((1.7669+1.7447*(math.log(F)))-(0.30218*((math.log(F))**2)))
  

