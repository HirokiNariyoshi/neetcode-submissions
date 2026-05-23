class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_map = defaultdict(list)
        col_map = defaultdict(list)
        
        for i, row in enumerate(board):

            if i != 0 and (i % 3) == 0:
                col_map = defaultdict(list)

            seen_list = []

            for j, num in enumerate(row):
                box_row_index = j // 3

                if (num != '.'):

                    if num in seen_list:
                        return False

                    elif num in seen_map[j]:
                        return False

                    elif num in col_map[box_row_index]:
                        return False

                col_map[box_row_index].append(num)

                seen_list.append(num)
                seen_map[j].append(num)

        return True
