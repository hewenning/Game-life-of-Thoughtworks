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

        if not change == None:
            pos = get_pos_on_game(info)

            # 判断这个细胞是否无效
            if pos[0] >= 0 and pos[1] >= 0 and pos[0] <= info['cell_size'] and pos[1] <= info['cell_size']:
                index = pos_to_index(info, pos)
                cell[index] = change

        return cell