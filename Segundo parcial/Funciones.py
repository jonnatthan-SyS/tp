import random
import os
import time
import datetime
import pygame

from Constantes import *

# ============================================================
#  UTILS
# ============================================================

def mostrar_texto(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]   
    space = font.size(' ')[0]  
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  
                y += word_height  
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  
        y += word_height  

# ============================================================
#  DATOS DEL JUEGO
# ============================================================

def crear_datos_juego() -> dict:
    datos_juego = {
        "nombre": "",
        "tiempo_restante": TIEMPO_PARTIDA,
        "puntuacion": 0,
        "cantidad_vidas": CANTIDAD_VIDAS,
        "indice": 0,
        "volumen_musica": 100,
        "bandera_texto": False,
        "tiempo_inicio_ticks":0,
        "game_over":False,
    }
    return datos_juego

def obtener_pregunta_actual(datos_juego:dict,lista_preguntas:list) -> dict | None:
    
    if type(datos_juego) == dict and type(lista_preguntas) == list and len(lista_preguntas) > 0 and type(datos_juego.get("indice")) == int:
        
        indice = datos_juego.get("indice")
        
        if 0 <= indice < len(lista_preguntas):
            return lista_preguntas[indice]
        else:
            return None
        
    return None   

# ============================================================
#  PUNTOS - VIDAS - RESPUESTAS
# ============================================================

def modificar_vida(datos_juego: dict, incremento: int) -> dict:
    if type(datos_juego) == dict and datos_juego.get("cantidad_vidas") != None:
        nuevo_estado = datos_juego.copy() # Copia
        nuevo_estado["cantidad_vidas"] += incremento
        
        return nuevo_estado # Retorna la copia modificada
    
    return datos_juego

def modificar_puntuacion(datos_juego: dict, incremento: int) -> dict:
    if type(datos_juego) == dict and datos_juego.get("puntuacion") != None:
        nuevo_estado = datos_juego.copy() # Copia
        nuevo_estado["puntuacion"] += incremento
        
        return nuevo_estado # Retorna la copia modificada
    
    return datos_juego

#def verificar_respuesta(pregunta_actual: dict, datos_juego: dict, respuesta: int) -> dict:
 #   if type(pregunta_actual) == dict and pregunta_actual.get("respuesta_correcta") != None:
  #      retorno = True
   #     if respuesta == pregunta_actual.get("respuesta_correcta"):
    #        modificar_puntuacion(datos_juego, 100)
     #   else:
      #      modificar_puntuacion(datos_juego, -25)
       #     modificar_vida(datos_juego, -1)
    #else:
     #   retorno = False
        
    #return retorno

def verificar_respuesta(pregunta_actual: dict, datos_juego: dict, respuesta: int) -> dict:
    
    if type(pregunta_actual) == dict and pregunta_actual.get("respuesta_correcta") != None:
        
        if respuesta == pregunta_actual.get("respuesta_correcta"):
           
            return modificar_puntuacion(datos_juego, 100)
        else:
            
            estado_despues_puntuacion = modificar_puntuacion(datos_juego, -25)
            
            return modificar_vida(estado_despues_puntuacion, -1)
            
    
    return datos_juego

# ============================================================
#  MANEJO DE LISTA DE PREGUNTAS
# ============================================================
    
def pasar_pregunta(datos_juego: dict, lista_preguntas: list) -> bool:
    if type(datos_juego) == dict and datos_juego.get("indice") != None:
        retorno = True
        datos_juego["indice"] += 1
        verificar_indice(datos_juego,lista_preguntas)
    else:
        retorno = False 
        
    return retorno

def verificar_indice(datos_juego: dict, lista_preguntas: list) -> None:
    if datos_juego["indice"] == len(lista_preguntas):
        datos_juego["indice"] = 0
        mezclar_lista(lista_preguntas)
        
def mezclar_lista(lista_preguntas: list) -> bool:
    if type(lista_preguntas) == list and len(lista_preguntas) > 0:
        retorno = True
        random.shuffle(lista_preguntas)
    else:
        retorno = False
    
    return retorno

# ============================================================
#  REINICIO / FINAL DE PARTIDA
# ============================================================

def reiniciar_estadisticas(datos_juego: dict) -> dict:
        datos_juego.update({
            "tiempo_total": TIEMPO_PARTIDA,
            "puntuacion": 0,
            "cantidad_vidas": CANTIDAD_VIDAS,
        })
        return datos_juego

def actualizar_tiempo(tiempo_inicio: float, tiempo_actual: float, datos_juego: dict) -> dict:
    #if type(datos_juego) == dict:
        #retorno = True
    tiempo_transcurrido_s = (tiempo_actual - tiempo_inicio) / 1000
        #datos_juego["tiempo_restante"] = TIEMPO_PARTIDA - tiempo_transcurrido
    #else:
        #retorno = False
        
    #return retorno
    tiempo_restante = TIEMPO_PARTIDA - tiempo_transcurrido_s

    if tiempo_restante <= 0:
        datos_juego["tiempo_restante"] = 0
        datos_juego["game_over"] = True
    else:
        datos_juego["tiempo_restante"] = int(tiempo_restante)

    return datos_juego 
# ============================================================
#  FUNCIONES PYGAME (GRÁFICAS)
# ============================================================
    
def mostrar_presentacion(pantalla, cola_eventos):
    ventana = "presentacion"

    # Fondo estilo preguntados
    fondo = pygame.image.load("Segundo parcial/Texturas/menu_inicio.png")
    fondo = pygame.transform.scale(fondo, PANTALLA)
    pantalla.blit(fondo, (0,0))

    # Botón jugar
    boton = pygame.Rect(X_CENTRO_BOTON, Y_POSICION_FIJA, ANCHO_BOTON, ALTO_BOTON)
    pygame.draw.rect(pantalla, (255,165,0), boton)

    fuente = pygame.font.SysFont("Arial", 45, True)
    texto = fuente.render("JUGAR", True, (255,255,255))
    texto_rect = texto.get_rect()
    texto_rect.center = boton.center
    pantalla.blit(texto, texto_rect)

    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if boton.collidepoint(evento.pos):
                return "menu"   # ← va al menú real

    return ventana


def crear_elemento_juego(textura: str, ancho_elemento: int, alto_elemento: int, x: int, y: int) -> dict | None:
    
    if (type(textura) == str and type(ancho_elemento) == int and type(alto_elemento) == int and type(x) == int and type(y) == int and os.path.exists(textura)):
        elemento_juego = {}
        elemento_juego["superficie"] = pygame.image.load(textura)
        elemento_juego["superficie"] = pygame.transform.scale(elemento_juego["superficie"],(ancho_elemento, alto_elemento))
        elemento_juego["rectangulo"] = pygame.rect.Rect(x,y,ancho_elemento,alto_elemento)
    else:
        elemento_juego = None
    
    return elemento_juego

def crear_lista_respuestas(textura: str, x: int, y: int, cantidad_respuestas: int) -> list:
    lista_respuestas = []

    for i in range(cantidad_respuestas):
        cuadro_respuesta = crear_elemento_juego(textura ,ANCHO_RESPUESTA ,ALTO_RESPUESTA ,x ,y)
        lista_respuestas.append(cuadro_respuesta)
        y += 70
    
    return lista_respuestas

def mostrar_datos_juego_pygame(pantalla: pygame.Surface, datos_juego: dict):
    mostrar_texto(pantalla,f"Tiempo restante: {datos_juego.get('tiempo_restante')} s",(10,10),FUENTE_ARIAL_20)
    mostrar_texto(pantalla,f"Puntuacion: {datos_juego.get('puntuacion')}",(10,35),FUENTE_ARIAL_20)
    mostrar_texto(pantalla,f"Vidas: {datos_juego.get('cantidad_vidas')}",(10,60),FUENTE_ARIAL_20)
    
#def responder_pregunta_pygame(lista_respuestas: list, pos_click: tuple, sonido: pygame.mixer.Sound, datos_juego: dict,lista_preguntas: list, pregunta_actual: dict) -> bool:
    #if (type(lista_respuestas) == list and type(pos_click) == tuple and type(datos_juego) == dict and type(lista_preguntas) == list and type(pregunta_actual) == dict and len(lista_respuestas) > 0):
        
    #    for i in range(len(lista_respuestas)):
     #       if lista_respuestas[i]["rectangulo"].collidepoint(pos_click):
      #          sonido.play()
       #         respuesta = i + 1
        #        verificar_respuesta(pregunta_actual,datos_juego,respuesta)
         #       pasar_pregunta(datos_juego,lista_preguntas)
          #      return True
    
    #return False       
def responder_pregunta_pygame(lista_respuestas: list, pos_click: tuple, sonido: pygame.mixer.Sound, datos_juego: dict,lista_preguntas: list, pregunta_actual: dict) -> dict: # Cambio a dict
    
    if (type(lista_respuestas) == list and type(pos_click) == tuple and type(datos_juego) == dict and type(lista_preguntas) == list and type(pregunta_actual) == dict and len(lista_respuestas) > 0):
        
        for i in range(len(lista_respuestas)):
            if lista_respuestas[i]["rectangulo"].collidepoint(pos_click):
                sonido.play()
                respuesta = i + 1
                
                # 1. ESTADO 1: Actualiza puntos/vidas
                estado_despues_respuesta = verificar_respuesta(pregunta_actual, datos_juego, respuesta) 
                
                # 2. Pasa a la siguiente pregunta (debe retornar el nuevo dict)
                nuevo_estado = pasar_pregunta(estado_despues_respuesta, lista_preguntas)
                
                return nuevo_estado # Retorna el diccionario de estado FINAL
    
    return datos_juego

def mostrar_pregunta_pygame(pregunta_actual: dict, pantalla: pygame.Surface, cuadro_pregunta: dict,lista_respuestas: list) -> bool:
    if type(pregunta_actual) == dict:
        retorno = True
        
        mostrar_texto(cuadro_pregunta["superficie"],pregunta_actual.get("pregunta"),(10,10),FUENTE_ARIAL_30)
        pantalla.blit(cuadro_pregunta["superficie"],cuadro_pregunta["rectangulo"])
        
        mostrar_texto(lista_respuestas[0]["superficie"],pregunta_actual.get("respuesta_1"),(20,20),FUENTE_ARIAL_20,COLOR_GRIS_CLARO)
        mostrar_texto(lista_respuestas[1]["superficie"],pregunta_actual.get("respuesta_2"),(20,20),FUENTE_ARIAL_20,COLOR_GRIS_CLARO)
        mostrar_texto(lista_respuestas[2]["superficie"],pregunta_actual.get("respuesta_3"),(20,20),FUENTE_ARIAL_20,COLOR_GRIS_CLARO)
        mostrar_texto(lista_respuestas[3]["superficie"],pregunta_actual.get("respuesta_4"),(20,20),FUENTE_ARIAL_20,COLOR_GRIS_CLARO)     
        
        for i in range(len(lista_respuestas)):
            pantalla.blit(lista_respuestas[i]["superficie"],lista_respuestas[i]["rectangulo"]) 
    else:
        retorno = False
        
    return retorno

def crear_lista_botones(textura: str, x: int, y: int, cantidad_botones: int) -> list:
    lista_botones = []

    for i in range(cantidad_botones):
        boton = crear_elemento_juego(textura,ANCHO_BOTON,ALTO_BOTON,x,y)
        lista_botones.append(boton)
        y += 85
    
    return lista_botones

def cambiar_musica_fondo(musica: str, datos_juego: dict) -> bool:
    if os.path.exists(musica):
        retorno = True
        pygame.mixer.init()
        pygame.mixer.music.stop()
        pygame.mixer.music.load(musica)
        volumen = datos_juego.get("volumen_musica",100)            
        pygame.mixer.music.set_volume(volumen / 100)
        pygame.mixer.music.play(-1)
    else:
        retorno = False
        
    return retorno
