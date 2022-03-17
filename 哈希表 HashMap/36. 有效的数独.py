# https://leetcode-cn.com/problems/valid-sudoku/solution/gong-shui-san-xie-yi-ti-san-jie-ha-xi-bi-ssxp/
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 创建数组
        # 注意！！！ 因为有 0 - 9 十个数字，所以这里的数组的size是 10 乘 10 ！！！
        row = [[False] * 10 for _ in range(10)]
        col = [[False] * 10 for _ in range(10)]
        # 将 每个宫格 也设一个数组
        box = [[False] * 10 for _ in range(10)]
        for i in range(9):
            for j in range(9):
                # 空格就不填
                if board[i][j] == '.':
                    continue
                # 数字
                u = int(board[i][j])
                # 在哪个小格子里
                index = (i//3) * 3 + j//3
                # 如果已经出现过了 返回无效
                if row[i][u] or col[j][u] or box[index][u]:
                    return False
                # 填表
                row[i][u] = col[j][u] = box[index][u] = True
        return True