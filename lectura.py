import xml.etree.ElementTree as ET

archivo_xml = "11o\pokemons.xml"

arbol = ET.parse(archivo_xml)

raiz = arbol.getroot()

for pokemon in raiz.findall("pokemon"):
    nombre = pokemon.find("nombre").text
    tipo = pokemon.find("tipo").text
    categoria = pokemon.find("categoria").text
    habilidad = pokemon.find("habilidad").text
    debilidad = pokemon.find("debilidad").text
    altura = pokemon.find("altura").text
    peso = pokemon.find("peso").text
    ps = pokemon.find("ps").text
    ataque = pokemon.find("ataque").text
    defensa = pokemon.find("defensa").text
    ataqueEsp = pokemon.find("ataqueEspecial").text
    defensaEsp = pokemon.find("defensaEspecial").text
    velocidad = pokemon.find("velocidad").text

    print("Nombre: ", nombre)
    print("Tipo: ", tipo)
    print("Categoria: ", categoria)
    print("Habilidad: ", habilidad)
    print("Debilidad: ", debilidad)
    print("Altura: ", altura)
    print("Peso: ", peso)
    print("PS: ", ps)
    print("Ataque: ", ataque)
    print("Defensa: ", defensa)
    print("Ataque Especial: ", ataqueEsp)
    print("Defensa Especial: ", defensaEsp)
    print("Velocidad: ", velocidad)
    print("")

