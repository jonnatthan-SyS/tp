import pygame
from Constantes import *
from Funciones import *
from Manejo_de_archivos import *

pygame.init()

def mostrar_game_over(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    datos_juego["bandera_texto"] = not datos_juego["bandera_texto"]
    ventana = "terminado"
    cuadro_texto = crear_elemento_juego("Texturas/textura.jpg",300,50,150,275)
    
    for evento in cola_eventos:
        if evento.type == pygame.TEXTINPUT:
            datos_juego["nombre"] += evento.text
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_BACKSPACE:
                datos_juego["nombre"] = datos_juego["nombre"][0:-1]
            elif evento.key == pygame.K_RETURN: 
                nombre = datos_juego.get("nombre", "")
                puntuacion = datos_juego.get("puntuacion", 0)
                nombre_limpio = nombre
                while len(nombre_limpio) > 0 and nombre_limpio[-1] == ' ':
                    nombre_limpio = nombre_limpio[:-1]
                if len(nombre_limpio) >= 3: 
                    guardar_partida(nombre_limpio, puntuacion)
                    SONIDO_CLICK.play()
                    return "menu"
                else:
                    SONIDO_ERROR.play()
    
    pantalla.fill(COLOR_GRIS_CLARO)
    mostrar_texto(pantalla,f"PERDISTE EL JUEGO: {datos_juego.get("puntuacion")}",(200,50),FUENTE_ARIAL_50,COLOR_NEGRO)
    
    #Estaria bueno que validen que texto tenga al menos 3 caracteres sino no puede seguir adelante
    #Estaria bueno que el nombre tenga limite de caracteres (por ejemplo 15/20)
    
    if len(datos_juego.get("nombre","")) > 0:
        
        if datos_juego["bandera_texto"]:
            mostrar_texto(cuadro_texto["superficie"],f"{datos_juego.get("nombre","")}|",(10,10),FUENTE_ARIAL_30,COLOR_BLANCO)
        else:
            mostrar_texto(cuadro_texto["superficie"],f"{datos_juego.get("nombre","")}",(10,10),FUENTE_ARIAL_30,COLOR_BLANCO)
    else:
        mostrar_texto(cuadro_texto["superficie"],f"Ingrese su nombre",(10,10),FUENTE_ARIAL_25,"#6F6B6B")
    
    pantalla.blit(cuadro_texto["superficie"],cuadro_texto["rectangulo"])
    
    return ventana
