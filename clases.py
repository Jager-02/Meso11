import xml.etree.ElementTree as ET

ruta = "11o\clases.xml"

arbol = ET.parse(ruta)

raiz = arbol.getroot()

for clase in raiz.findall("clase"):
    identi = clase.find("id").text
    nombre = clase.find("nombre").text
    catedratico = clase.find("catedratico").text
    creditos = clase.find("creditos").text
    punteo = clase.find("punteo").text
    laboratorio = clase.find("laboratorio").text

    print(f"id : {identi} - Clase: {nombre} - Catedratico: {catedratico} - Creditos: {creditos} - Punteo: {punteo} - Laboratorio: {laboratorio}")
