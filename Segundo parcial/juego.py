import pygame
from Constantes import *
from Preguntas import *
from Funciones import *

pygame.init()

def mostrar_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    ventana = "jugar"
    lista_preguntas = datos_juego.get("preguntas")
    pregunta_actual = obtener_pregunta_actual(datos_juego, lista_preguntas)

    if pregunta_actual is None:
        return "terminado"
    
    tiempo_actual = pygame.time.get_ticks()
    corriendo_tiempo(datos_juego, datos_juego["tiempo_inicio"], tiempo_actual)
    
    if datos_juego.get("tiempo_restante") <= 0:
        return "terminado"
    

    cuadro_pregunta = crear_elemento_juego("Segundo parcial/Texturas/fondo preguntas2.png", ANCHO_PREGUNTA, ALTO_PREGUNTA, 250, 50)
    lista_respuestas = crear_lista_respuestas("Segundo parcial/Texturas/fondo respuesta2.jpg", 300 , 250, 4)

    
    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                #respuesta_elegida = responder_pregunta_pygame(lista_respuestas,evento.pos,SONIDO_CLICK,datos_juego,lista_preguntas,pregunta_actual)
                respuesta_elegida = responder_pregunta_pygame(lista_respuestas, evento.pos, SONIDO_CLICK, datos_juego,lista_preguntas,pregunta_actual)

                if respuesta_elegida is not None:
                    respuesta_correcta = pregunta_actual.get("respuesta_correcta")
                    fue_correcta = (respuesta_elegida == respuesta_correcta)
                    
                    if fue_correcta:
                        datos_juego["puntuacion"] += 10
                    else:
                        datos_juego["cantidad_vidas"] -= 1
                    
                    datos_juego["indice"] += 1
                    
                    if datos_juego.get("cantidad_vidas") <= 0 or datos_juego.get("indice") >= len(lista_preguntas):
                        return "terminado"

                pregunta_actual = obtener_pregunta_actual(datos_juego,lista_preguntas)
                cuadro_pregunta = crear_elemento_juego("Segundo parcial/Texturas/fondo preguntas2.png",ANCHO_PREGUNTA,ALTO_PREGUNTA,250,50)
                lista_respuestas = crear_lista_respuestas("Segundo parcial/Texturas/fondo respuesta2.jpg",300 , 250, 4)
    
    if datos_juego.get("cantidad_vidas") == 0:
        ventana = "terminado"
    
    pantalla.fill(COLOR_GRIS_CLARO)
    mostrar_datos_juego_pygame(pantalla,datos_juego)
    mostrar_pregunta_pygame(pregunta_actual,pantalla,cuadro_pregunta,lista_respuestas)
    
    return ventana

