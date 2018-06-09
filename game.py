# 导入所需要的包
import pygame
clock = time.Clock()

def game(info):
    import time, pygame

    # 在info中添加游戏区域的大小（而不是窗口大小）
    info['game_size'] = int(min(info['window_size']))
    grid = PlotCell.plot_cell(info['cell_size'])

    global clock
    pygame.init()

    # 设置窗口大小
    main_window = pygame.display.set_mode(info['window_size'], RESIZABLE)
    game_window = pygame.Surface((info['game_size'],) * 2)

    running = 0
    t = 0
    last_time = time.time()

    speed = 1

    while True:

        # Resize loop
        for e in pygame.event.get():
            if e.type == pygame.VIDEORESIZE:
                # Set sizes
                info['window_size'] = e.w, e.h
                info['game_size'] = int(min(info['window_size']))

                # Set Surfaces
                main_window = pygame.display.set_mode(info['window_size'], pygame.RESIZABLE)
                game_window = pygame.Surface((info['game_size'],) * 2)

            if e.type == pygame.QUIT: quit()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    running = abs(running - 1)

                if e.key == pygame.K_SPACE:
                    grid = UpdateCells.update_cells(info, grid)
                    last_time = time.time()

                if e.key == pygame.K_c:
                    grid = PlotCell.plot_cell(info['grid_size'])

        game_window.fill(info['background'])

        cell = ChangeCell.change_cells(grid, info)
        ShowCells.show_cells(game_window, grid, info)

        pygame.display.set_caption(str(t))
        dt = clock.tick() / 1000

        if running:
            t += dt * speed * 10
            if t > 1:
                grid = UpdateCells.update_cells(info, grid)
                t -= 1
                last_time = time.time()

        messages = ['Time since last: ' + str(round(time.time() - last_time, 5)),
                    'Speed: ' + str(round(speed, 5)),
                    'Running: ' + str(bool(running)),
                    ]

        k = pygame.key.get_pressed()
        if k[pygame.K_UP]: speed += dt
        if k[pygame.K_DOWN]: speed -= dt
        speed = max(speed, 0)

        # Add the game window to the main and show
        main_window.fill((10, 10, 10))
        main_window.blit(game_window, (
        (info['window_size'][0] - info['game_size']) / 2, (info['window_size'][1] - info['game_size']) / 2))
        # show_messages(main_window, info, messages)
        pygame.display.update()


game(info)