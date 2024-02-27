from fastapi import FastAPI, Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer 
from operations.comprenVaz import compVaz,compVazrequest
from operations.facVolAce import volStan, Stanrequest, Stanresponses, volVazBeg, VazBegrequest, volGlaso
from operations.presBurb import pbStan,  pbLasater, Lasarequest, pbVazBeg, Vazbeggrequest, pbGlaso
from operations.relSolub import rsStanding,rsStanrequest,rsVaz_Beg, rsVazBegrequest, rsGlaso, rsGlarequest
from operations.viscAceite import viscVaz_Begg, viscVBrequest, viscKarto, viscGuet, viscPetro
from operations.viscAcemue import aceMuertorequest, acmuGlas,acmuBeg_Rob,acmuKarto,acmuPerto
from operations.viscAcesatu import acSaturequest, acsaBeg_Rob,acsaGuet,acsaKarto
from tags import tags_tittle
from db.securit import  users_db, sec_app, oauth2_scheme




app = FastAPI()




app.include_router(sec_app)





#---------------------------------------------------------------------------------------------------------------------
#POST Para calcular la Comprensibilidad 
@app.post("/Vazquez Com",tags=["Comprensibilidad"])

async def Vazquezcom( formula: compVazrequest, token:str= Depends(oauth2_scheme)):
   resultado = compVaz (formula.Rs, formula.Ygs,formula.API,formula.pb,formula.Tem)

   return Stanresponses(resultado= resultado)


#---------------------------------------------------------------------------------------------------------------------
#POST Para calcular el factor del aceite mediante Standing 
@app.post("/Standing Fv",tags=["Factor Volumen del Aceite"])

async def StandingFv( formula: Stanrequest ):
   resultado = volStan(formula.Rs, formula.Ygd, formula.Yo,formula.Tem )

   return Stanresponses(resultado= resultado)

#---------------------------------------------------------------------------------------------------------------------
#POST Para calcular el factor del aceite mediante el metodo Vazquez y Beggs
@app.post("/Vazquez & Beggs Fv",tags=["Factor Volumen del Aceite"])

async def Vazquez_BeggsFv(formula: VazBegrequest  ):
   resultado = volVazBeg(formula.Rs, formula.API, formula.Ygd,formula.Tem )

   return Stanresponses(resultado= resultado)


#---------------------------------------------------------------------------------------------------------------------
#POST Para cañcular el factor del aceite mediante el metodo Glaso

@app.post("/Glaso Fv",tags=["Factor Volumen del Aceite"])

async def GlasoFv(formula:  Stanrequest  ):
   resultado = volGlaso(formula.Rs, formula.Ygd, formula.Yo,formula.Tem )
  
   return Stanresponses(resultado= resultado)



#---------------------------------------------------------------------------------------------------------------------
#POST Para calcular la Presion Burbuja mediante el metodo Standing
@app.post("/Standing Pb", tags=["Presion Burbuja"])

async def StandingPb(formula: VazBegrequest):
   resultado = pbStan(formula.Rs, formula.Ygd, formula.API,formula.Tem)

   return Stanresponses(resultado=resultado)

#---------------------------------------------------------------------------------------------------------------------
#POST Para calcular la Presion Burbuja mediante el metodo Lasater
@app.post("/Lasater Pb",tags=["Presion Burbuja"])
async def LasaterPb(formula: Lasarequest):
   resultado = pbLasater(formula.Ygd , formula.Yo, formula.Rs,formula.Tem, formula.API)
   return Stanresponses(resultado=resultado)


#---------------------------------------------------------------------------------------------------------------------
#POST Para calcular la Presion Burbuja mediante el metodo Vasquez Y Beggs
@app.post("/Vazquez & Beggs Pb",tags=["Presion Burbuja"])
async def Vazquez_BeggsPb(formula: Vazbeggrequest):
   resultado = pbVazBeg(formula.Yg,formula.API,formula.Tem,formula.Psep,formula.Tsep,formula.Rs)
   return Stanresponses(resultado=resultado)


#---------------------------------------------------------------------------------------------------------------------
#POST Para calcular la Presion Burbuja mediante el metodo Glaso
@app.post("/Glaso Pb",tags=["Presion Burbuja"])
async def Glasopb(formula: VazBegrequest):
   resultado= pbGlaso(formula.Rs, formula.Ygd, formula.Tem,formula.API)
   return Stanresponses(resultado=resultado)




#---------------------------------------------------------------------------------------------------------------------
#POST Para calcular Relación de solubilidad mediante el metodo Standing
@app.post("/Standing Rs",tags=["Relacion de solubilidad"])
async def StandingRs(formula: rsStanrequest):
   resultado= rsStanding(formula.Ydg,formula.p,formula.API,formula.Tem)
   return Stanresponses(resultado=resultado)


#---------------------------------------------------------------------------------------------------------------------
#POST Para calcular Relación de solubilidad mediante el metodo Vazquez & Beggs
@app.post("/Vazquez & Beggs Rs",tags=["Relacion de solubilidad"])
async def Vazquez_BeggsRs(formula: rsVazBegrequest):
   resultado= rsVaz_Beg(formula.Ygs,formula.p,formula.API,formula.Tem)
   return Stanresponses(resultado=resultado)


#---------------------------------------------------------------------------------------------------------------------
#POST Para calcular Relación de solubilidad mediante el metodo Glaso
@app.post ("/Glaso Rs / A=0.130 Aceites volatiles / A= 0.172 Aceites negros",tags=["Relacion de solubilidad"])
async def GlasoRs(formula: rsGlarequest):
   resultado= rsGlaso(formula.Ygd,formula.API,formula.Tem,formula.p,formula.A)
   return Stanresponses(resultado=resultado)




#---------------------------------------------------------------------------------------------------------------------
#POST Para calcular Viscosidad del aceite bajosaturado mediante el metodo Vazquez & Beggs
@app.post("/Vasquez & Beggs Ab", tags=["Viscosidad del aceite bajosaturado"])
async def Vasquez_Beggsmo(formula: viscVBrequest):
   resultado= viscVaz_Begg(formula.Mob,formula.p,formula.pb)
   return Stanresponses(resultado=resultado)


#---------------------------------------------------------------------------------------------------------------------
#POST Para calcular Viscosidad del aceite bajosaturado mediante el metodo Kartoadmojo
@app.post("/Kartoadmojo Ab", tags=["Viscosidad del aceite bajosaturado"])
async def KartoadmojoMob(formula: viscVBrequest):
   resultado= viscKarto(formula.Mob,formula.p,formula.pb)
   return Stanresponses(resultado=resultado)

#---------------------------------------------------------------------------------------------------------------------
#POST Para calcular Viscosidad del aceite bajosaturado mediante el metodo Guetto
@app.post("/Guetto Ab", tags=["Viscosidad del aceite bajosaturado"])
async def GuettoMob(formula: viscVBrequest):
   resultado= viscGuet(formula.Mob,formula.p,formula.pb)
   return Stanresponses(resultado=resultado)

#---------------------------------------------------------------------------------------------------------------------
#POST Para calcular Viscosidad del aceite bajosaturado mediante el metodo Petrosky
@app.post("/Petrosky Ab", tags=["Viscosidad del aceite bajosaturado"])
async def PetroskyMob(formula: viscVBrequest):
   resultado= viscPetro(formula.Mob,formula.p,formula.pb)
   return Stanresponses(resultado=resultado)


#---------------------------------------------------------------------------------------------------------------------
#POST Para calcular Viscosidad del aceite muerto mediante el metodo  Beggs y Robinson
@app.post("Beggs y Robinson Am", tags=["Viscosidad del aceite muerto"])
async def Beg_RobMod(formula: aceMuertorequest):
   resultado = acmuBeg_Rob(formula.API,formula.Tem)
   return Stanresponses(resultado=resultado)


#---------------------------------------------------------------------------------------------------------------------
#POST Para calcular Viscosidad del aceite muerto mediante el metodo Glaso
@app.post("Glaso Am", tags=["Viscosidad del aceite muerto"])
async def GlasMod(formula: aceMuertorequest):
   resultado = acmuGlas(formula.API,formula.Tem)
   return Stanresponses(resultado=resultado)


#---------------------------------------------------------------------------------------------------------------------
#POST Para calcular Viscosidad del aceite muerto mediante el metodo Kartoatmodjo
@app.post("Kartoatmodjo Am", tags=["Viscosidad del aceite muerto"])
async def KartoMod(formula: aceMuertorequest):
   resultado = acmuKarto(formula.API,formula.Tem)
   return Stanresponses(resultado=resultado)


#---------------------------------------------------------------------------------------------------------------------
#POST Para calcular Viscosidad del aceite muerto mediante el metodo  Petrosky
@app.post(" Petrosky Am", tags=["Viscosidad del aceite muerto"])
async def PetroMod(formula: aceMuertorequest):
   resultado = acmuPerto (formula.API, formula.Tem)
   return Stanresponses (resultado = resultado)


#---------------------------------------------------------------------------------------------------------------------
#POST Para calcular Viscosidad del aceite Saturado
@app.post(" Beggs y Robinson As", tags=["Viscosidad del aceite saturado"])
async def Beg_RobMob(formula: acSaturequest):
   resultado = acsaBeg_Rob (formula.Rs, formula.Mod)
   return Stanresponses (resultado = resultado)

#---------------------------------------------------------------------------------------------------------------------
#POST Para calcular Viscosidad del aceite Saturado
@app.post(" Kartoadmojo As", tags=["Viscosidad del aceite saturado"])
async def KartoMob(formula: acSaturequest):
   resultado = acsaKarto (formula.Rs, formula.Mod)
   return Stanresponses (resultado = resultado)


#---------------------------------------------------------------------------------------------------------------------
#POST Para calcular Viscosidad del aceite Saturado
@app.post(" De Guetto As", tags=["Viscosidad del aceite saturado"])
async def GuettMob(formula: acSaturequest):
   resultado = acsaGuet (formula.Rs, formula.Mod)
   return Stanresponses (resultado = resultado)