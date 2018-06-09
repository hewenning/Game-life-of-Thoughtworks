# -*- coding: utf-8 -*-
# 更新细胞位置
from game_cell_plot import PlotCell


class UpdateCells:
    def update_cells(info, cell):
        copy = list(cell)

        # 存活的细胞放入一个数组
        live_cells = []
        for index in range(len(cell)):
            if cell[index]: live_cells.append(index)

        # 获得周围的细胞的信息
        neighbour_cells = []
        for cell_index in live_cells:
            pos = PlotCell.index_to_pos(info, cell_index)

            for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, 1), (1, -1), (-1, -1)]:
                new_pos = pos[0] + x, pos[1] + y

                # Is the new spot valid
                if new_pos[0] >= 0 and new_pos[1] >= 0 and new_pos[0] < info['cell_size'] and new_pos[1] < info[
                    'cell_size']:
                    new_index = PlotCell.pos_to_index(info, new_pos)

                    if not new_index in live_cells:
                        neighbour_cells.append(new_index)

        # 根据周围细胞的状态，判断此点细胞下一时刻状态
        for cell_type in range(0, 2):
            cells = [live_cells, neighbour_cells][cell_type]

            for index in cells:
                neighbours = 0
                pos = PlotCell.index_to_pos(info, index)

                for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, 1), (1, -1), (-1, -1)]:
                    new_pos = pos[0] + x, pos[1] + y

                    # 判断是不是一个新的细胞生成点
                    if new_pos[0] >= 0 and new_pos[1] >= 0 and new_pos[0] < info['cell_size'] and new_pos[1] < info[
                        'cell_size']:

                        new_index = PlotCell.pos_to_index(info, new_pos)
                        if copy[new_index]: neighbours += 1

                # If live\\
                if cell_type == 1:
                    if neighbours == 3:
                        cell[index] = True

                else:
                    if neighbours < 2:
                        cell[index] = False
                    elif neighbours <= 3:
                        pass
                    elif neighbours >= 4:
                        cell[index] = False

                    # If dead

        return cell