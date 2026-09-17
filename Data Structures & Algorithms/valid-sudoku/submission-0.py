class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = defaultdict(set)
        row = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(0, 9):
            for j in range(0, 9):
                value = board[i][j]
                if value == '.':
                    continue
                if i in col[value] or j in row[value]:
                    return False
                box = (i // 3, j // 3)
                if box in boxes[value]:
                    return False
                boxes[value].add(box)
                col[value].add(i)
                row[value].add(j)

        return True
