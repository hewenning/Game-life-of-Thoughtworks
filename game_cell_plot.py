# -*- coding: utf-8 -*-
# 该类用于绘制细胞
class PlotCell():
    def plot_cell(size):
        cell = [False for i in range(size ** 2)]
        return cell

    def pos_to_index(info, pos):
        index = pos[0]
        index += pos[1] * info['cell_size']
        return index

    def index_to_index(info, index):
        y = (int(index / info['cell_size']))
        x = (index - (y * info['cell_size']))
        return x, y
