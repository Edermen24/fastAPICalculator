from pydantic import BaseModel
import math
import math as ma

class acSaturequest(BaseModel):
  Rs:float
  Mod:float

def acsaBeg_Rob(Rs,Mod):
  B= (0.43 + (0.57*(10**(-0.00072*Rs))))
  A= (0.20 + (0.80*(10**(-0.00072*Rs))))

  return A * (Mod*B)


def acsaKarto(Rs,Mod):
  B= 10**(-0.00081*Rs)
  A=((0.2001 + 0.8428)*(10**(-0.000845*Rs)))*(Mod**(0.43+0.5165*B))
  return -0.06821+(0.9824*A) + (0.0004034*(A**2))

def acsaGuet(Rs,Mod):
  B=(0.4731+0.5158) * (10**(-0.00081*Rs))
  A=((0.2478+0.6114) *(10**(-0.000845*Rs)))*(Mod**B)
  
  return (-0.6311+1.078) * ((A-0.003653)*(A**2))

#def acsaPetros()
