from Model.SudokuAppModel.ISudokuAppModel import ISudokuAppModel
from Model.SudokuGameGridFactory.ISudokuGameGridFactory import ISudokuGameGridFactory
from Model.SudokuGameGridFactory.sudokuGameGridFactory import SudokuGameGridFactory
from Model.SudokuGridFactory.gridFactory import GridFactory
from Model.cell import Cell
from Model.SudokuGridFactory.ISudokuGridFactory import ISudokuGridFactory


class SudokuAppModel(ISudokuAppModel):
    solved_grid: list[list[int]] = None
    game_grid: list[list[Cell]] = None
    solved_grid_factory: ISudokuGridFactory = GridFactory()
    game_grid_factory: ISudokuGameGridFactory = SudokuGameGridFactory(30)

    def __init__(self) -> None:
        self.new_game()

    def new_game(self) -> None:
        self.solved_grid = self.solved_grid_factory.create_new_grid()
        self.game_grid = self.game_grid_factory.create_game_grid(self.solved_grid)

    def is_player_win(self) -> bool:
        for i in range(9):
            for j in range(9):
                if self.solved_grid[i][j] != self.game_grid[i][j].num:
                    return False
        return True

    def get_game_grid_cell_num(self, row, col) -> int:
        return self.game_grid[row][col].num

    def get_game_grid_cell_is_const(self, row, col) -> bool:
        return self.game_grid[row][col].isActive is False

    def get_solved_grid_cell(self, row, col) -> int:
        return self.solved_grid[row][col]

    def set_cell_num(self, row, col, num) -> None:
        self.game_grid[row][col].num = num

    def is_game_grid_filled(self) -> bool:
        for i in range(9):
            for j in range(9):
                if self.game_grid[i][j].num == 0:
                    return False
        return True

    def set_difficulty(self, difficulty: int) -> None:
        self.game_grid_factory.difficulty = difficulty
