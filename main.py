from PIL import Image
import numpy as np

# Mapeamento de cores
color_map = {
    (0, 0, 0, 0): '.',       # Transparente
    (255, 255, 255): '1',    # Branco
    (255, 32, 33): '2',      # #ff2021
    (255, 147, 196): '3',    # #ff93c4
    (255, 129, 52): '4',     # #ff8134
    (119, 220, 82): '7',     # #77dc52
    (1, 64, 173): '8',       # #0140ad
    (134, 242, 255): '9',    # #86f2ff
    (140, 46, 198): 'a',     # #8c2ec6
    (164, 131, 159): 'b',    # #a4839f
    (91, 64, 107): 'c',      # #5b406b
    (229, 205, 195): 'd',    # #e5cdc3
    (144, 70, 61): 'e',      # #90463d
    (0, 0, 0): 'f'           # Preto
}

def closest_color(rgb):
    r, g, b = rgb
    min_dist = float('inf')
    closest_key = None
    for key in color_map:
        if key == (0, 0, 0, 0):  # Ignore transparent key
            continue
        kr, kg, kb = key
        dist = (r - kr)**2 + (g - kg)**2 + (b - kb)**2
        if dist < min_dist:
            min_dist = dist
            closest_key = key
    return color_map[closest_key]

def convert_image_to_code(image_path):
    # Abrir a imagem
    img = Image.open(image_path).convert('RGBA')
    width, height = img.size

    # string reslt
    result = []

    for y in range(height):
        row = []
        for x in range(width):
            pixel = img.getpixel((x, y))

            # Verificar se é um pixel transparente
            if pixel[3] == 0:
                row.append('.')
            else:
                # Ignorar o componente alpha para o mapeamento
                rgb = pixel[:3]
                row.append(closest_color(rgb))  # Adicionar o código correspondente à cor mais próxima
        result.append(' '.join(row))

    # Unir todas as linhas em uma única string com quebras de linha
    return '\n'.join(result)

# Caminho para a imagem
image_path = 'assets/knight_f_idle_anim_f0.png'

code = convert_image_to_code(image_path)

print(code)