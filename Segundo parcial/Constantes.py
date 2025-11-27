import pygame

pygame.init()

# PANTALLA
ANCHO = 900
ALTO = 600
PANTALLA = (ANCHO, ALTO)
FPS = 30

# COLORES
COLOR_BLANCO = (255,255,255)
COLOR_AZUL = (18,73,224)
COLOR_AZUL_OSCURO = (0,0,128)
COLOR_NEGRO = (0,0,0)

# LOGICA DEL JUEGO
CANTIDAD_VIDAS = 3
TIEMPO_PARTIDA = 30


# ELEMENTOS DEL  JUEGO
ANCHO_PREGUNTA = 350
ALTO_PREGUNTA = 150

ANCHO_RESPUESTA = 250
ALTO_RESPUESTA = 60

ANCHO_BOTON = 300
ALTO_BOTON = 80

# FUENTES (se inicializan luego)
FUENTE_ARIAL_20 = pygame.font.SysFont("Arial",20,False)
FUENTE_ARIAL_25 = pygame.font.SysFont("Arial",25,False)
FUENTE_ARIAL_30 = pygame.font.SysFont("Arial",30,True)
FUENTE_ARIAL_50 = pygame.font.SysFont("Arial",50,False)
FUENTE_ARIAL_50_NEGRITA = pygame.font.SysFont("Arial",50,True)

# SONIDOS
SONIDO_CLICK = pygame.mixer.Sound("Segundo parcial\Sonidos\click.mp3")
SONIDO_ERROR = pygame.mixer.Sound("Segundo parcial\Sonidos\error.mp3")