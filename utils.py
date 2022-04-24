import pygame

putih = ((200, 200, 200))
hitam = ((0, 0, 0))
merah = ((255, 0, 0))
hijau = ((0, 255, 0))
biru = ((0, 0, 255))


def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


def blit_rotate_center(win, image, top_left, angel):
    rotated_image = pygame.transform.rotate(image, angel)
    new_rect = rotated_image.get_rect(
        center=image.get_rect(topleft=top_left).center)
    win.blit(rotated_image, new_rect.topleft)


def blit_text_center(win, font, text):
    render = font.render(text, 1, putih)
    win.blit(render, (win.get_width()/2 - render.get_width() /
             2, win.get_height()/2 - render.get_height()/2))
