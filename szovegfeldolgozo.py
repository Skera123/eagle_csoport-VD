"""
PUSKA

A szöveg hossza: len(szoveg)
A szöveg utolsó karater: szoveg[len(szoveg)-1]
Csere a szövegben : szoveg.replace("H", "J") // a nagy "H"-kat nagy "J"-re cserélem
A szöveg tartalmazza az alma karaktereket?: logikaiValtozo = "alma" in szoveg // not in - nem tartalmazza

Ciklus:
ujSzoveg=""
for x in range(0,len(szoveg)-1,2):
	ujSzoveg=ujSzoveg+szoveg[x] 

Eljáras:
def szovegFordit(szöveg):
	...
	return vissza
"""
# Az eljárást készítette:
def szovegFordit(szoveg):
<<<<<<< HEAD
fordSzoveg=""
for x in range(len(szoveg)-1,-1,-1):
fordSzoveg+=szoveg[x]
	# Ide írd meg az eljárást!
=======
	fordSzoveg=""
	for x in range(0,len(szoveg)-1,-1,-1):
		fordSzoveg+=szoveg[X]
>>>>>>> e4bd6ac5bf64a21b03dbb2936cf6ebc4198b2d5f
	return fordSzoveg
	return	fordSzoveg
	
# Az eljárást készítette:	
def szovegCsere(szoveg):
<<<<<<< HEAD

	# Ide írd meg az eljárást!
	return ""
=======
	maganHango="aáéoóöőuúüű"
	for x in range(0, len(magánHango)):
	szoveg=szoveg.replace(maganHango)[x],"e");
	return szoveg
>>>>>>> a747155e084889737f92f63bf623b51ce949608d
	
# Az eljárást készítette:	
def szovegParos(szoveg):

parosSzoveg = ""
for x in range (0,len(szoveg)2):
parosSzoveg += szoveg [x]

	# Ide írd meg az eljárást!
	return parosSzoveg
	
# Az eljárást készítette:	
def szovegParatlan(szoveg):

	# Ide írd meg az eljárást!
	return ""
	
# Itt kezdődik a főprogram
szoveg=input("Valamit írjááááá be:")
print(szovegFordit(szoveg))
