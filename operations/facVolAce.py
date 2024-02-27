from pydantic import BaseModel
import math

#------------------------------------------------------------------------------------------------------
#METODO STANDING

def volStan(Rs, Ygd, Yo , Tem  ):

    return 0.9759 + (1.2)*(10**-4) * (((Rs*((Ygd/Yo)**0.5)) + (1.25 * Tem))** 1.2)

class   Stanrequest(BaseModel):
    Rs : float
    Ygd:  float
    Yo: float
    Tem: float


    
  
class Stanresponses(BaseModel):
    resultado: float


#------------------------------------------------------------------------------------------------------------
#METODO VAZQUEZ & BEGGS
def volVazBeg(Rs, Tem, API, Ygd):

    if(API<=30):
     return 1.0 + (((4.677)*(10**-4))*Rs) + (((1.751)*(10**-5))*(Tem-60)*(API/Ygd)) + ((((-1.811)*(10**-8))*Rs) *(Tem-60)*(API/Ygd))
    elif(API > 30):
     return 1.0 + (((4.67)*(10**-4))*Rs) + (((1.7)*(10**-5))*(Tem-60)*(API/Ygd)) + ((((-1.337)*(10**-9))*Rs) *(Tem-60)*(API/Ygd))
    

class   VazBegrequest(BaseModel):
    Rs: float
    Ygd:  float
    Tem: float
    API: float

 




#------------------------------------------------------------------------------------------------------------
#METODO GLASO
def volGlaso(Rs, Ygd, Yo , Tem):

    res = ( Rs * ((Ygd/Yo)**0.526)) + (0.968* Tem)

    return 1.0 + (10 **(((-6.58511 + 2.9139 )* (math.log(res))) - (((0.27683)*((math.log(res))**2)))))

    

    


#class   Glasogrequest(BaseModel):
    #Rs : float
    #Ygd:  float
    #Tem: float
    #Yo: float
   
