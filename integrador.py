preguntas = {
    "horarios": {"caja":"los horarios de atencion son de 8:am a 4:00pm"},
    "precios": {
        "inscripcionTSU":"el precio de la inscripcion y de re-inscripcion de TSU es de $372",
        "admision":"el examen de admision TSU tiene un precio de $275",
        "colegiaturaTSU":"$712",
        "inscripcionING":"la incripcion de la ingenieria es de $482",
        "colegiaturaING":"el precio de la colegiatura de ingenieria es de $942"
    }
}

usuario= input("Pregunta: ").lower()

for categoria in preguntas:
    if categoria in usuario:
        print(f"Seleccionaste la categoría {categoria}. Opciones disponibles:")
        for key in preguntas[categoria]:
            print(key,": ")
        opcion = input("Elige una opción: ")
        print(preguntas[categoria].get(opcion, "No tengo información sobre eso"))
        break
else:
    print("No entiendo la pregunta, intenta con otra palabra clave")
