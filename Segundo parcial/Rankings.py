import pygame
from Constantes import *
from Funciones import *

pygame.init()

boton_volver = crear_elemento_juego("Segundo parcial\Texturas\textura.jpg",100,40,10,10)

def mostrar_rankings(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],lista_rankings:list) -> str:
    ventana = "rankings"
    
    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                SONIDO_CLICK.play()
                ventana = "menu"
    
    pantalla.fill(COLOR_BLANCO)

    #mostrar_texto(pantalla,f"ACA VA EL TOP 10",(150,200),FUENTE_ARIAL_50,COLOR_NEGRO)
    mostrar_texto(pantalla,f"ACA VA EL TOP 10",(ANCHO // 2 -150, 50),FUENTE_ARIAL_50,COLOR_NEGRO)

    mostrar_texto(pantalla, "RANK", (50, Y_INICIO), FUENTE_ARIAL_25, COLOR_AZUL_OSCURO)
    mostrar_texto(pantalla, "NOMBRE", (250, Y_INICIO), FUENTE_ARIAL_25, COLOR_AZUL_OSCURO)
    mostrar_texto(pantalla, "PUNTUACIÓN", (550, Y_INICIO), FUENTE_ARIAL_25, COLOR_AZUL_OSCURO)

    for i in range(len(lista_rankings)):
        partidas = lista_rankings[i]

        y_pos = Y_INICIO + Y_OFFSET + (i * Y_OFFSET)

        rank = i + 1
        nombre = partidas.get("nombre", "N/A")
        puntuacion = partidas.get("puntuacion", 0)

        mostrar_texto(pantalla, f"{rank}.", (50, y_pos), FUENTE_ARIAL_20, COLOR_NEGRO)
        mostrar_texto(pantalla, nombre, (250, y_pos), FUENTE_ARIAL_20, COLOR_NEGRO)
        mostrar_texto(pantalla, f"{puntuacion}", (550, y_pos), FUENTE_ARIAL_20, COLOR_NEGRO)
    
    
        pantalla.blit(boton_volver["superficie"],boton_volver["rectangulo"])
        mostrar_texto(boton_volver["superficie"],"VOLVER",(5,5),FUENTE_ARIAL_20,COLOR_BLANCO)

    return ventana
