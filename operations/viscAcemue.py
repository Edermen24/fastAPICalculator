from pydantic import BaseModel
import math
import math as ma

class aceMuertorequest(BaseModel):
  API:float
  Tem:float

def acmuBeg_Rob(API,Tem):
  A=(10**((3.0324-0.02023)*(API*(Tem**-1.163))))

  return (10**A) -1

def acmuGlas(API,Tem):

  return (3.141 *((10**10)*(Tem**-3.444)))*((math.log(API))**(((5.7525*(math.log(Tem)))-26.9718)))

def acmuKarto ( API,Tem):

  return ((10.0*(10**8))*(Tem**-2.5177)*((math.log(API))**(5.7526*(math.log(Tem))*-26.9718)))

def acmuPerto(API,Tem):
  J= (4.59388*(math.log(Tem)))-22.82792
  return (2.3511*(10**7)) * (Tem**-2.10255) *(math.log((API)**J))



