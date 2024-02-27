
from pydantic import BaseModel

import math
import math as ma


def compVaz(Rs,Ygs,API,pb,Tem):

  return (((-1433-5)*Rs) + (17.2*Tem) + (-1180*Ygs)+ (12.61*API)) / ((10**5)*pb)
 
    

class compVazrequest(BaseModel):

  Rs:float
  Ygs:float
  API:float
  pb:float
  Tem:float

