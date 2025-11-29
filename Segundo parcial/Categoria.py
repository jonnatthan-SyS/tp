import pygame
from Constantes import *
from Funciones import *

pygame.init()

fondo_categorias = pygame.transform.scale(pygame.image.load("Texturas/fondo_menu.jpg"), PANTALLA)
lista_botones = crear_lista_botones("Texturas/botones.png", 300, 120, 3)

lista_texto_botones = ["HISTORIA", "FUTBOL", "JUEGOS"]


def mostrar_categorias(pantalla, cola_eventos, datos_juego) -> str:
    ventana = "categorias"

    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            for i in range(len(lista_botones)):
                if lista_botones[i]["rectangulo"].collidepoint(evento.pos):

                    SONIDO_CLICK.play()

                    categoria = lista_texto_botones[i].lower()
                    lista_filtrada = [
                        p for p in datos_juego["preguntas"]
                        if p.get("categoria", "").lower() == categoria
                    ]

                    datos_juego["preguntas_filtradas"] = lista_filtrada
                    datos_juego["indice_pregunta"] = 0

                    return "jugar"

    pantalla.blit(fondo_categorias, (0, 0))

    for i in range(len(lista_botones)):
        texto = lista_texto_botones[i]
        ancho_texto, alto_texto = FUENTE_ARIAL_30.size(texto)

        pos_x = (ANCHO_BOTON // 2) - (ancho_texto // 2)
        pos_y = (ALTO_BOTON // 2) - (alto_texto // 2)

        mostrar_texto(lista_botones[i]["superficie"], texto, (pos_x, pos_y),
                      FUENTE_ARIAL_30, COLOR_BLANCO)

        pantalla.blit(lista_botones[i]["superficie"], lista_botones[i]["rectangulo"])

    return ventana
