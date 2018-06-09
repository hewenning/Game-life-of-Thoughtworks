# 该类用来显示游戏信息
from pygame import font


class ShowMessages:
    def show_messages(window, info, messages):

        max_height = 30
        margin = 10

        f = font.SysFont(None, int(max_height))

        for index in range(len(messages)):
            surf = f.render(messages[index], 0, (255, 255, 255))

            y = (margin + max_height) * index + margin
            window.blit(surf, (margin, y))
