import pygame
from Constantes import *
from Funciones import *

pygame.init()

fondo_menu = pygame.transform.scale(pygame.image.load("Segundo parcial/Texturas/Fondo_menu.jpg"),PANTALLA)

lista_botones = crear_lista_botones("Segundo parcial/Texturas/botones.png",300,120,4)

lista_texto_botones = ["JUGAR","AJUSTES","RANKINGS","SALIR "]

def mostrar_menu(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event]) -> str:
    ventana = "menu"
    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            for i in range(len(lista_botones)):
                if lista_botones[i]["rectangulo"].collidepoint(evento.pos):
                    ventana = lista_texto_botones[i].lower()
        
    pantalla.blit(fondo_menu,(0,0))
    for i in range(len(lista_botones)):
        mostrar_texto(lista_botones[i]["superficie"],lista_texto_botones[i],(100,20),FUENTE_ARIAL_30,COLOR_BLANCO)
        pantalla.blit(lista_botones[i]["superficie"],lista_botones[i]["rectangulo"])
    return ventana


