import pygame
from Constantes import *
from Funciones import *

pygame.init()

fondo_categorias = pygame.transform.scale(pygame.image.load("Texturas/fondo_categorias.jpg"),PANTALLA)

botones = crear_lista_botones("Texturas/botones.png", 300, 120, 3)
texto_botones = ["HISTORIA", "FUTBOL", "JUEGOS"]

def mostrar_categorias(pantalla, cola_eventos, datos_juego):
    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            for i in range(len(botones)):
                if botones[i]["rectangulo"].collidepoint(evento.pos):
                    SONIDO_CLICK.play()
                    categoria = texto_botones[i].lower()

                    lista_filtrada = [
                        p for p in datos_juego["preguntas"]
                        if p.get("categoria") == categoria
                    ]
                    
                    datos_juego["preguntas_filtradas"] = lista_filtrada
                    datos_juego["indice_pregunta"] = 0

                    return "jugar"

    pantalla.blit(fondo_categorias, (0,0))

    for i in range(len(botones)):
        texto = texto_botones[i]
        ancho, alto = FUENTE_ARIAL_30.size(texto)
        pos_x = (ANCHO_BOTON // 2) - (ancho // 2)
        pos_y = (ALTO_BOTON // 2) - (alto // 2)

        mostrar_texto(botones[i]["superficie"], texto, (pos_x, pos_y),
                      FUENTE_ARIAL_30, COLOR_BLANCO)
        pantalla.blit(botones[i]["superficie"], botones[i]["rectangulo"])

    return "categorias"
