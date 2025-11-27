import pygame

from Constantes import *
from Funciones import *

from Menu import *
from juego import *
from ajustes import *
from Rankings import *
from Termiado import *

from Manejo_de_archivos import leer_csv_preguntas

lista_preguntas = leer_csv_preguntas("PREGUNTAS.CSV")

pygame.init()
pygame.display.set_caption("TRIVIAL")
pygame.display.set_icon(pygame.image.load("Segundo parcial/Texturas/icono.png"))

pantalla = pygame.display.set_mode(PANTALLA)
ejecutando = True

reloj = pygame.time.Clock()

datos_juego = crear_datos_juego()
datos_juego["preguntas"] = lista_preguntas
bandera_juego = False

cambiar_musica_fondo(MUSICA_FONDO, datos_juego)

ventana_actual = "presentacion"

while ejecutando:
    reloj.tick(FPS)
    cola_eventos = pygame.event.get()

    for event in cola_eventos:
        if event.type == pygame.QUIT:
            ejecutando = False
    
    if ventana_actual == "presentacion":
        ventana_actual = mostrar_presentacion(pantalla, cola_eventos)

    elif ventana_actual == "menu":
        ventana_actual = mostrar_menu(pantalla, cola_eventos)
    
    elif ventana_actual == "jugar":
        if bandera_juego == False:
            random.shuffle(lista_preguntas)
            reiniciar_estadisticas(datos_juego)
            datos_juego["tiempo_inicio"] = pygame.time.get_ticks()
            bandera_juego = True
        ventana_actual = mostrar_juego(pantalla, cola_eventos, datos_juego)
    
    elif ventana_actual == "ajustes":
        ventana_actual = mostrar_ajustes(pantalla, cola_eventos, datos_juego)
    
    elif ventana_actual == "rankings":
        ventana_actual = mostrar_rankings(pantalla, cola_eventos, datos_juego)
    
    elif ventana_actual == "terminado":
        ventana_actual = mostrar_game_over(pantalla, cola_eventos, datos_juego)
    
    pygame.display.flip()

pygame.quit()
