# 该类用于将细胞计算结果显示出来
from pygame import draw


class ShowCells:
    def show_cells(window, cell, info):

        game_scale = info['game_size'] / info['grid_size']
        for value_index in range(len(cell)):

            # Change index to pos
            x, y = PlotCell.index_to_index(info, value_index)

            value = cell[value_index]
            if value: 
                draw.rect(window, info['live_colour'],
                          (x * game_scale, y * game_scale, int(game_scale), int(game_scale)))
