import pygame
from Constantes import *
from Funciones import *

pygame.init()

# ============================================================
#  Funcionamiento de Barra / Volumen
# ============================================================



boton_resta = crear_elemento_juego("Segundo parcial\Texturas\Boton bajar volumen.png",ANCHO_BOTON_VOLUMEN, ALTO_BOTON_VOLUMEN, POS_X_RESTA, POS_Y_VOLUMEN)

boton_suma = crear_elemento_juego("Segundo parcial\Texturas\Boton subir volumen.png",ANCHO_BOTON_VOLUMEN, ALTO_BOTON_VOLUMEN, POS_X_SUMA, POS_Y_VOLUMEN)
boton_volver = crear_elemento_juego("Segundo parcial\Texturas\Boton_volver_ajustes.webp",50,50,10,10)



barra_vacia = pygame.image.load("Segundo parcial\Texturas\Barra_vacia.png")
barra_llena = pygame.image.load("Segundo parcial\Texturas\Barra_llena.png")

barra_vacia_escala = pygame.transform.scale(barra_vacia, (ANCHO_BARRA, ALTO_BARRA))

# ============================================================
#  
# ============================================================

fondo_ajustes = pygame.transform.scale(pygame.image.load("Segundo parcial/Texturas/Fondo_menu.jpg"),PANTALLA)

def administrar_botones(boton_suma:dict,boton_resta:dict,boton_volver:dict,datos_juego:dict,pos_mouse:tuple) -> str:
    ventana = "ajustes"
    vol_musica = datos_juego.get("volumen_musica",0)

    if boton_suma["rectangulo"].collidepoint(pos_mouse):
        if vol_musica <= 95:
            datos_juego["volumen_musica"] += 5
            SONIDO_CLICK.play()
            pygame.mixer.music.set_volume(datos_juego["volumen_musica"] / 100)
        else:
            SONIDO_ERROR.play()
    elif boton_resta["rectangulo"].collidepoint(pos_mouse):
        if vol_musica > 0:
            datos_juego["volumen_musica"] -= 5
            SONIDO_CLICK.play()
            pygame.mixer.music.set_volume(datos_juego["volumen_musica"] / 100)
        else:
            SONIDO_ERROR.play()
    elif boton_volver["rectangulo"].collidepoint(pos_mouse):
        SONIDO_CLICK.play()
        ventana = "menu"

    return ventana

def dibujar_elementos(pantalla:pygame.Surface,boton_suma:dict,boton_resta:dict,boton_volver:dict,datos_juego:dict) -> None:
    #pantalla.fill(COLOR_BLANCO)
    pantalla.blit(fondo_ajustes, (0,0))

    titulo_ajustes = FUENTE_ARIAL_50_NEGRITA.render("AJUSTES DE VOLUMEN", True, COLOR_NEGRO)
    titulo_rect = titulo_ajustes.get_rect(center=(ANCHO // 2, 80))
    pantalla.blit(titulo_ajustes, titulo_rect)

    vol_musica = datos_juego.get("volumen_musica", 0)

    barra = pygame.Rect(POS_X_BARRA,POS_Y_BARRA,ANCHO_BARRA,ALTO_BARRA)

    pantalla.blit(barra_vacia_escala, barra)

    ancho_relleno = int((vol_musica / 100) * ANCHO_BARRA)

    if ancho_relleno > 0:
        relleno = pygame.Rect(POS_X_BARRA, POS_Y_BARRA, ancho_relleno, ALTO_BARRA)

        textura_barra = pygame.transform.scale(barra_llena, (ancho_relleno, ALTO_BARRA))

        pantalla.blit(textura_barra, relleno)
    mostrar_texto(pantalla,f"{datos_juego.get("volumen_musica",0)} %",(ANCHO // 2 - 50, 320),FUENTE_ARIAL_50,COLOR_NEGRO)
    #mostrar_texto(boton_volver["superficie"]," ",(5,5),FUENTE_ARIAL_20,COLOR_BLANCO)


    pantalla.blit(boton_suma["superficie"],boton_suma["rectangulo"])
    pantalla.blit(boton_resta["superficie"],boton_resta["rectangulo"])
    pantalla.blit(boton_volver["superficie"],boton_volver["rectangulo"])


def mostrar_ajustes(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    ventana = "ajustes"
    
    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            ventana = administrar_botones(boton_suma,boton_resta,boton_volver,datos_juego,evento.pos)
    
    dibujar_elementos(pantalla,boton_suma,boton_resta,boton_volver,datos_juego)
    
    return ventana
