# 该类用于检测鼠标动作，计算细胞的改变
from pygame import mouse



class ChangeCell():
    def change_cell(cell, info):

        # 检测鼠标动作
        change = None
        if mouse.get_pressed()[0]:
            change = True
        if mouse.get_pressed()[2]:
            change = False

        if not change is None:
            pos = ChangeCell.get_pos_on_game(info)

            # 判断这个细胞是否无效
            if pos[0] >= 0 and pos[1] >= 0 and pos[0] <= info['cell_size'] and pos[1] <= info['cell_size']:
                index = PlotCell.pos_to_index(info, pos)
                cell[index] = change

        return cell

    def get_pos_on_game(info):

        pos = list(mouse.get_pos())
        game_scale = info['game_size'] / info['grid_size']

        pos[0] -= (info['window_size'][0] - info['game_size']) / 2
        pos[1] -= (info['window_size'][1] - info['game_size']) / 2

        pos[0] /= game_scale
        pos[1] /= game_scale

        pos[0] = int(pos[0])
        pos[1] = int(pos[1])

        return pos
