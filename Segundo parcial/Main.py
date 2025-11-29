import pygame

from Constantes import *
from Funciones import *

from Menu import *
from juego import *
from ajustes import *
from Rankings import *
from Termiado import *
from Dificultad import *
from Categoria import *
from Manejo_de_archivos import leer_csv_preguntas

lista_preguntas = leer_csv_preguntas("PREGUNTAS.CSV")

pygame.init()
pygame.display.set_caption("TRIVIAL")
pygame.display.set_icon(pygame.image.load("Texturas/icono.png"))

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
    
    elif ventana_actual == "dificultad":
        ventana_actual = mostrar_dificultad(pantalla, cola_eventos)
    
    elif ventana_actual == "jugar_facil":
        datos_juego["dificultad"] = "facil"
        datos_juego["tiempo_limite"] = 60
        ventana_actual = "categorias"
    
    elif ventana_actual == "jugar_media":
        datos_juego["dificultad"] = "media"
        datos_juego["tiempo_limite"] = 40
        ventana_actual = "categorias"
    
    elif ventana_actual == "jugar_dificil":
        datos_juego["dificultad"] = "dificil"
        datos_juego["tiempo_limite"] = 25
        ventana_actual = "categorias"
    
    elif ventana_actual == "categorias":
        ventana_actual = mostrar_categorias(pantalla, cola_eventos, datos_juego)

    elif ventana_actual == "jugar":
        if bandera_juego == False:
            random.shuffle(datos_juego["preguntas"])
            reiniciar_estadisticas(datos_juego)
            
            datos_juego["tiempo_inicio"] = pygame.time.get_ticks()
            bandera_juego = True
        ventana_actual = mostrar_juego(pantalla, cola_eventos, datos_juego)
    
    elif ventana_actual == "ajustes":
        ventana_actual = mostrar_ajustes(pantalla, cola_eventos, datos_juego)
    
    elif ventana_actual == "rankings":
        top_10_mejores = obtener_top_10()
        ventana_actual = mostrar_rankings(pantalla, cola_eventos, top_10_mejores)
    
    elif ventana_actual == "terminado":
        ventana_actual = mostrar_game_over(pantalla, cola_eventos, datos_juego)
    
    pygame.display.flip()

pygame.quit()