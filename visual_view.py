import pygame
import games
import heuristic

game = games.ConnectFour()
state = game.initial

player = 'X'

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
width = 20
height = 20
margin = 5

grid = []
for x in range(7):
    grid.append([])
    for y in range(6):
        grid[x].append(0)

pygame.init()

pantalla = pygame.display.set_mode([700, 500])

pygame.display.set_caption("Connect 4")

done = False

reloj = pygame.time.Clock()

mode = 1
difficult = 1
fuente = pygame.font.Font(None, 36)

show_intro = True
intro_page = 1

while not done and show_intro:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            done = True
        if evento.type == pygame.MOUSEBUTTONDOWN:
            intro_page += 1
            if intro_page == 3:
                show_intro = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_m:
                mode += 1
                if mode == 5:
                    mode = 1

    pantalla.fill(black)

    if intro_page == 1:
        texto = fuente.render("4 en raya", True, white)
        pantalla.blit(texto, [10, 10])

        texto = fuente.render("Realizado por:", True, red)
        pantalla.blit(texto, [500, 400])

        texto = fuente.render("Alvaro Falcon Morales", True, white)
        pantalla.blit(texto, [400, 445])
        texto = fuente.render("Stefan Hautz", True, white)
        pantalla.blit(texto, [400, 470])

    if intro_page == 2:
        texto = fuente.render("Pulse m para cambiar la modalidad", True, white)
        pantalla.blit(texto, [10, 10])
        texto = fuente.render("Y de click para empezar!", True, white)
        pantalla.blit(texto, [10, 35])
        if mode == 1:
            texto = fuente.render("Modo: Multiplayer", True, white)
            pantalla.blit(texto, [10, 90])
        if mode == 2:
            texto = fuente.render("Modo: vs CPU", True, white)
            pantalla.blit(texto, [10, 90])
            texto = fuente.render("Dificultad: Facil", True, white)
            difficult = 1
            pantalla.blit(texto, [10, 120])
        if mode == 3:
            texto = fuente.render("Modo: vs CPU", True, white)
            pantalla.blit(texto, [10, 90])
            texto = fuente.render("Dificultad: Medio", True, white)
            difficult = 5
            pantalla.blit(texto, [10, 120])
        if mode == 4:
            texto = fuente.render("Modo: vs CPU", True, white)
            pantalla.blit(texto, [10, 90])
            texto = fuente.render("Dificultad: Dificil", True, white)
            difficult = 10
            pantalla.blit(texto, [10, 120])

    reloj.tick(20)

    pygame.display.flip()

while not done:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if mode == 1:
                pos = pygame.mouse.get_pos()
                y = pos[0] // (width + margin)
                x = pos[1] // (height + margin)
                if grid[x][y] == 0 and (x, y) in state.moves:
                    state = game.make_move((x, y), state)
                    if player == 'X':
                        grid[x][y] = 1
                        player = 'O'
                    else:
                        grid[x][y] = 2
                        player = 'X'
            elif mode == 2:
                if player == 'X':
                    pos = pygame.mouse.get_pos()
                    y = pos[0] // (width + margin)
                    x = pos[1] // (height + margin)
                    if grid[x][y] == 0 and (x, y) in state.moves:
                        state = game.make_move((x, y), state)
                        grid[x][y] = 1
                        player = 'O'
    pantalla.fill(black)
    if mode != 1 and player == 'O':
        print("holita")
        move = games.alphabeta_search(state, game, d=10, cutoff_test=None, eval_fn=heuristic.compute_utility(state))
        state = game.make_move(move, state)
        grid[move[0]][move[1]] = 2
        player = 'X'
    for x in range(7):
        for y in range(6):
            color = white
            if grid[x][y] == 1:
                color = blue
            elif grid[x][y] == 2:
                color = red
            pygame.draw.rect(pantalla,
                             color,
                             [(margin + width) * y + margin,
                              (margin + height) * x + margin,
                              width,
                              height])
    if game.terminal_test(state):
        print "Final de la partida"
        break

    reloj.tick(20)

    pygame.display.flip()

pygame.quit()
