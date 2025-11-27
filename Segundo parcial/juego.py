import pygame
from Constantes import *
from Preguntas import *
from Funciones import *

pygame.init()

def mostrar_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    tiempo_inicio = datos_juego["tiempo_inicio_ticks"]
    tiempo_actual = pygame.time.get_ticks()
    datos_juego = actualizar_tiempo(tiempo_inicio, tiempo_actual, datos_juego)

    
    if datos_juego["game_over"]:
        return "terminado"
    
    tiempo_flotante = datos_juego["tiempo_restante"]
    tiempo_a_mostrar = int(tiempo_flotante) 
    
    texto_tiempo = f"Tiempo: {tiempo_a_mostrar}"

    mostrar_texto(pantalla, texto_tiempo, (50, 50), FUENTE_ARIAL_30, COLOR_NEGRO)

    ventana = "jugar"
    lista_preguntas = datos_juego.get("preguntas")
    pregunta_actual = obtener_pregunta_actual(datos_juego, lista_preguntas)
    
    if pregunta_actual is None:
        return "terminado"

    cuadro_pregunta = crear_elemento_juego("Segundo parcial\Texturas\Fondo_pregunta.webp", ANCHO_PREGUNTA, ALTO_PREGUNTA, 275, 100)
    lista_respuestas = crear_lista_respuestas("Segundo parcial/Texturas/Fondo_respuesta.jpg", 325 , 300, 4)
    pregunta_actual = obtener_pregunta_actual(datos_juego,lista_preguntas)
    
    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                datos_juego = responder_pregunta_pygame(lista_respuestas,evento.pos,SONIDO_CLICK,datos_juego,lista_preguntas,pregunta_actual)
                #responder_pregunta_pygame(lista_respuestas,evento.pos,SONIDO_CLICK,datos_juego,lista_preguntas,pregunta_actual)
                pregunta_actual = obtener_pregunta_actual(datos_juego,lista_preguntas)
                cuadro_pregunta = crear_elemento_juego("Segundo parcial/Texturas/Fondo_pregunta.webp",ANCHO_PREGUNTA,ALTO_PREGUNTA,150,125)
                lista_respuestas = crear_lista_respuestas("Segundo parcial/Texturas/Fondo_pregunta.webp",150 , 125, 4)
    
    if datos_juego.get("cantidad_vidas") == 0:
        ventana = "terminado"
    
    pantalla.fill(COLOR_GRIS_CLARO)
    mostrar_datos_juego_pygame(pantalla,datos_juego)
    mostrar_pregunta_pygame(pregunta_actual,pantalla,cuadro_pregunta,lista_respuestas)
    
    return ventana    
