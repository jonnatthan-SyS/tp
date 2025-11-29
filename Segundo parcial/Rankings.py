import pygame
from Constantes import *
from Funciones import *
from Manejo_de_archivos import *

pygame.init()

boton_volver = crear_elemento_juego("Segundo parcial\Texturas\Boton_volver_ajustes.webp",100,40,10,10)

def mostrar_rankings(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],lista_rankings:list) -> str:
    ventana = "rankings"
    
    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                SONIDO_CLICK.play()
                ventana = "menu"
    
    pantalla.fill(COLOR_BLANCO)

    #mostrar_texto(pantalla,f"ACA VA EL TOP 10",(150,200),FUENTE_ARIAL_50,COLOR_NEGRO)
    """mostrar_texto(pantalla,f"ACA VA EL TOP 10",(ANCHO // 2 -150, 50),FUENTE_ARIAL_50,COLOR_NEGRO)"""

    """mostrar_texto(pantalla, "RANK", (50, Y_INICIO), FUENTE_ARIAL_25, COLOR_AZUL_OSCURO)
    mostrar_texto(pantalla, "NOMBRE", (250, Y_INICIO), FUENTE_ARIAL_25, COLOR_AZUL_OSCURO)
    mostrar_texto(pantalla, "PUNTUACIÓN", (550, Y_INICIO), FUENTE_ARIAL_25, COLOR_AZUL_OSCURO)
"""

    mostrar_texto(pantalla,f" TOP 10 JUGADORES",(ANCHO // 2 - 250, 50),FUENTE_ARIAL_50,COLOR_NEGRO)

    # Encabezados de Columna: Usando el nuevo Y_INICIO_JUGADORES = 100
    mostrar_texto(pantalla, "RANK", (50, Y_INICIO_JUGADORES), FUENTE_ARIAL_25, COLOR_AZUL_OSCURO)
    mostrar_texto(pantalla, "NOMBRE", (250, Y_INICIO_JUGADORES), FUENTE_ARIAL_25, COLOR_AZUL_OSCURO)
    mostrar_texto(pantalla, "PUNTUACIÓN", (550, Y_INICIO_JUGADORES), FUENTE_ARIAL_25, COLOR_AZUL_OSCURO)

    if len(lista_rankings) > FILAS_A_MOSTRAR:
        filas_jugadores = FILAS_A_MOSTRAR
    else:
        filas_jugadores = len(lista_rankings)

    for i in range(filas_jugadores):
        partidas = lista_rankings[i]

        y_pos = Y_INICIO_JUGADORES + Y_OFFSET + (i * Y_OFFSET)

        rank = i + 1
        nombre = partidas.get("nombre", "N/A")
        puntuacion = partidas.get("puntuacion", 0)

        mostrar_texto(pantalla, f"{rank}.", (50, y_pos), FUENTE_ARIAL_20, COLOR_NEGRO)
        mostrar_texto(pantalla, nombre, (250, y_pos), FUENTE_ARIAL_20, COLOR_NEGRO)
        mostrar_texto(pantalla, f"{puntuacion}", (550, y_pos), FUENTE_ARIAL_20, COLOR_NEGRO)
    if filas_jugadores > 0:
        y_final_jugadores = Y_INICIO_JUGADORES + Y_OFFSET + ((filas_jugadores - 1) * Y_OFFSET) + Y_OFFSET
    else:
        y_final_jugadores = Y_INICIO_JUGADORES + (3 * Y_OFFSET)
    
    Y_INICIO_PREGUNTAS = y_final_jugadores + 30

    top_5_preguntas = []
    lista_preguntas = leer_csv_preguntas("PREGUNTAS.CSV") # Asumiendo CSV_PREGUNTAS existe

    if lista_preguntas is not None:
        top_5_preguntas = obtener_top_5_preguntas(lista_preguntas)[:FILAS_A_MOSTRAR]


    mostrar_texto(pantalla, "TOP 5 PREGUNTAS MÁS ACERTADAS", (ANCHO // 2 - 250, Y_INICIO_PREGUNTAS), FUENTE_ARIAL_25, COLOR_AZUL_OSCURO)

    mostrar_texto(pantalla, "RANK", (50, Y_INICIO_PREGUNTAS + Y_OFFSET), FUENTE_ARIAL_20_NEGRITA, COLOR_NEGRO)
    mostrar_texto(pantalla, "PREGUNTA", (250, Y_INICIO_PREGUNTAS + Y_OFFSET), FUENTE_ARIAL_20_NEGRITA, COLOR_NEGRO)
    mostrar_texto(pantalla, "ACIERTOS %", (650, Y_INICIO_PREGUNTAS + Y_OFFSET), FUENTE_ARIAL_20_NEGRITA, COLOR_NEGRO)

    if top_5_preguntas:
        for i, pregunta in enumerate(top_5_preguntas):

            y_pos = Y_INICIO_PREGUNTAS + Y_OFFSET_RANKING + (i * Y_OFFSET_RANKING)
            
            texto_pregunta_completo = pregunta.get('pregunta', 'N/A')
            
            texto_pregunta_truncado = f"{texto_pregunta_completo[:40]}..." if len(texto_pregunta_completo) > 43 else texto_pregunta_completo
            
            texto_porcentaje = f"{pregunta.get('porcentaje_aciertos', 0.0)}%"

            mostrar_texto(pantalla, f"{i+1}.", (50, y_pos), FUENTE_ARIAL_20, COLOR_NEGRO)
            mostrar_texto(pantalla, texto_pregunta_truncado, (250, y_pos), FUENTE_ARIAL_20, COLOR_NEGRO)
            mostrar_texto(pantalla, texto_porcentaje, (650, y_pos), FUENTE_ARIAL_20, COLOR_AZUL)
    else:
        
        y_pos_mensaje = Y_INICIO_PREGUNTAS + Y_OFFSET_RANKING + Y_OFFSET_RANKING
        mostrar_texto(pantalla, "No hay datos de preguntas usados o el archivo no existe.", (250, y_pos_mensaje), FUENTE_ARIAL_20, COLOR_ROJO)
        
    # ------------------- 5. BOTÓN VOLVER -------------------
    
    pantalla.blit(boton_volver["superficie"],boton_volver["rectangulo"])
    mostrar_texto(boton_volver["superficie"],"",(5,5),FUENTE_ARIAL_20,COLOR_BLANCO)

    return ventana
