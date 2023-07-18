def chocolates():
    choco = input("¿Cuántos chocolates quieres? ")
    cacao = 0
    print("RECORDATORIO: Por cada barra de chocolate se necesitan 6 granos de cacao")
    cacao = int(choco) * 6
    print("Debes ingresar ", cacao, " granos de cacao")
    cantCacao = input("¿Cuántos granos de cacao tienes? ")
    if int(cantCacao) >= cacao:
        print("¡Genial! Puedes hacer tus chocolates")
    else:
        print("Lo siento, no tienes suficientes granos de cacao :(")
        print("Te faltan ", cacao - int(cantCacao), " granos de cacao")
        print("De momento puedes hacer ", int(cantCacao) // 6, " chocolates")

chocolates()