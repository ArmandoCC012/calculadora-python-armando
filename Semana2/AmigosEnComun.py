MisAmigosArmando={"Jana","Tiara","Jonas","Ulrich","Kevin"}
AmigosDeJonas={"Arnold","Armando","Jonas","Erica","Marta"}
ListaComunes=[]
ListaComunes.append(MisAmigosArmando & AmigosDeJonas)
print("Nuestros amigos en comun son/es:",ListaComunes)
ListaAmigos=[]
ListaAmigos.append(MisAmigosArmando | AmigosDeJonas)
print("Mis amigos y de el son:",ListaAmigos)
ListaDeMisAmigos=[]
ListaDeMisAmigos.append(MisAmigosArmando - AmigosDeJonas)
print("Mis amigos son",ListaDeMisAmigos)