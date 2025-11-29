import pygame
from Constantes import *
from Preguntas import *
from Funciones import *

pygame.init()

lista_comodines = crear_comodines("Segundo parcial/Texturas/comodines.jpg",700,150,4)
lista_comodines_nombres = ["bomba","x2","doble chance","pasar"]

def mostrar_juego(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event], datos_juego: dict) -> str:
    ventana = "jugar"

    lista_preguntas = datos_juego.get("preguntas")
    pregunta_actual = obtener_pregunta_actual(datos_juego, lista_preguntas)

    if pregunta_actual is None:
        return "terminado"

    tiempo_actual = pygame.time.get_ticks()
    corriendo_tiempo(datos_juego, datos_juego["tiempo_inicio"], tiempo_actual)

    if datos_juego.get("tiempo_restante") <= 0:
        return "terminado"

    cuadro_pregunta = crear_elemento_juego("Segundo parcial/Texturas/fondo preguntas2.png",ANCHO_PREGUNTA, ALTO_PREGUNTA, 250, 50)
    lista_respuestas = crear_lista_respuestas("Segundo parcial/Texturas/fondo respuesta2.jpg",300, 250, 4)
    vincular_respuestas_a_botones(lista_respuestas, pregunta_actual)

    
    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            for comodin in lista_comodines:
                if comodin["rectangulo"].collidepoint(evento.pos):
                    activar_comodin(comodin["nombre"], datos_juego, pregunta_actual, lista_respuestas)
                    SONIDO_CLICK.play()
                    break
            responder_pregunta_pygame(lista_respuestas, evento.pos, SONIDO_CLICK, datos_juego, lista_preguntas, pregunta_actual)
            pregunta_actual = obtener_pregunta_actual(datos_juego, lista_preguntas)

    if datos_juego.get("cantidad_vidas") == 0:
        ventana = "terminado"

    pantalla.fill(COLOR_GRIS_CLARO)

    for j in range(len(lista_comodines)):
        texto = lista_comodines_nombres[j]
        pantalla.blit(lista_comodines[j]["superficie"], lista_comodines[j]["rectangulo"])
        mostrar_texto(lista_comodines[j]["superficie"],texto, (40,50), FUENTE_ARIAL_20_NEGRITA, COLOR_NEGRO)
        
    
    mostrar_datos_juego_pygame(pantalla, datos_juego)
    mostrar_pregunta_pygame(pregunta_actual, pantalla, cuadro_pregunta, lista_respuestas)
    return ventana
