import pygame
from Constantes import *
from Funciones import *

pygame.init()

fondo_menu = pygame.transform.scale(pygame.image.load("Segundo parcial/Texturas/Fondo_menu.jpg"),PANTALLA)

lista_botones = crear_lista_botones("Segundo parcial/Texturas/Fondo_boton.jpeg",150,125,4)

lista_texto_botones = ["JUGAR","AJUSTES","RANKINGS","SALIR "]

# Menu.py (Línea 15 - CORREGIDO)
def mostrar_menu(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event], datos_juego:dict) -> tuple[str, dict]:
#def mostrar_menu(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event], datos_juego: dict) -> str:
    ventana = "menu"
    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            for i in range(len(lista_botones)):
                if lista_botones[i]["rectangulo"].collidepoint(evento.pos):
                    ventana_siguiente = lista_texto_botones[i].lower()
                    if ventana_siguiente == "jugar":
                        # 1. CAPTURA el nuevo estado reiniciado (DICT)
                        datos_juego = reiniciar_estadisticas(datos_juego) 
                        
                        # 2. Ahora que datos_juego es un diccionario, puedes asignarle el tiempo
                        datos_juego["tiempo_inicio_ticks"] = pygame.time.get_ticks() 
                    
                    ventana = ventana_siguiente
        
    pantalla.blit(fondo_menu,(0,0))
    
    for i in range(len(lista_botones)):
        mostrar_texto(lista_botones[i]["superficie"],lista_texto_botones[i],(100,20),FUENTE_ARIAL_30,COLOR_GRIS_CLARO)
        pantalla.blit(lista_botones[i]["superficie"],lista_botones[i]["rectangulo"])
    
    return ventana, datos_juego



