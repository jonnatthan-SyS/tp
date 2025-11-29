import pygame
from Constantes import *
from Funciones import *

pygame.init()

def mostrar_dificultad(pantalla, cola_eventos):
    ventana = "dificultad"

    # Botones de dificultad
    btn_facil = pygame.Rect(300, 250, 300, 80)
    btn_normal = pygame.Rect(300, 360, 300, 80)
    btn_dificil = pygame.Rect(300, 470, 300, 80)

    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if btn_facil.collidepoint(evento.pos):
                SONIDO_CLICK.play()
                return "jugar_facil"

            if btn_normal.collidepoint(evento.pos):
                SONIDO_CLICK.play()
                return "jugar_media"

            if btn_dificil.collidepoint(evento.pos):
                SONIDO_CLICK.play()
                return "jugar_dificil"

    # Fondo gris
    pantalla.fill((230, 230, 230))

    fuente = pygame.font.SysFont("Arial", 45, True)
    titulo = fuente.render("Seleccioná dificultad", True, (0,0,0))
    pantalla.blit(titulo, (250, 150))

    # Dibujar botones
    pygame.draw.rect(pantalla, (200,255,200), btn_facil, border_radius=20)
    pygame.draw.rect(pantalla, (255,255,200), btn_normal, border_radius=20)
    pygame.draw.rect(pantalla, (255,200,200), btn_dificil, border_radius=20)

    pant = pantalla.blit
    pant(fuente.render("FÁCIL", True, (0,0,0)), (btn_facil.x+90, btn_facil.y+20))
    pant(fuente.render("NORMAL", True, (0,0,0)), (btn_normal.x+55, btn_normal.y+20))
    pant(fuente.render("DIFÍCIL", True, (0,0,0)), (btn_dificil.x+60, btn_dificil.y+20))

    return ventana
