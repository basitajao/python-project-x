#create the ayo board game
#starting with the system design and implementation
#make it a cli application that can be played by two players on the same machine
class AyoGame:
    def __init__(self):
        self.board = [4] * 12  # 12 pits with 4 seeds each
        self.scores = {1: 0, 2: 0}  # Player scores
        self.current_player = 1  # Player 1 starts
        self.is_active = True

    def _is_player_pit(self, pit_index):
        """Check if the pit belongs to the current player."""
        if self.current_player == 1:
            return 0 <= pit_index <= 5
        else:
            return 6 <= pit_index <= 11

    def _get_opposite(self, pit_index):
        """Get the opposite pit index."""
        return (11 - pit_index) % 12

    def play_turn(self, pit_index):
        """Process a player's turn based on the selected pit index."""
        if not self.is_active:
            print("Game over. Please start a new game.")
            return False

        # Validation
        if pit_index < 0 or pit_index > 11:
            print("Invalid pit index. Please select a pit between 0 and 11.")
            return False
        if not self._is_player_pit(pit_index):
            print("You can only play from your own pits.")
            return False
        if self.board[pit_index] == 0:
            print("Selected pit is empty. Please choose a different pit.")
            return False

        # Sowing process
        seeds = self.board[pit_index]
        self.board[pit_index] = 0
        current_idx = pit_index

        print(f"Player {self.current_player} picked up {seeds} seeds from pit {pit_index}.")

        while seeds > 0:
            current_idx = (current_idx + 1) % 12
            self.board[current_idx] += 1
            seeds -= 1

            if seeds == 0:
                # Check for relay condition
                if self.board[current_idx] > 1:
                    print(f"  -> Landed in pit {current_idx} (Total: {self.board[current_idx]}). Relay!")
                    seeds = self.board[current_idx]
                    self.board[current_idx] = 0

        # Check for capture condition
        opposite_idx = self._get_opposite(current_idx)
        if self.board[current_idx] == 1 and self.board[opposite_idx] > 0:
            captured_seeds = self.board[opposite_idx]
            self.scores[self.current_player] += captured_seeds + 1
            self.board[opposite_idx] = 0
            self.board[current_idx] = 0
            print(f"Player {self.current_player} captured {captured_seeds + 1} seeds!")

        # Check for game end condition
        if all(seeds == 0 for seeds in self.board[:6]) or all(seeds == 0 for seeds in self.board[6:]):
            self.is_active = False
            print("Game over!")
            print(f"Final Scores - Player 1: {self.scores[1]}, Player 2: {self.scores[2]}")

        # Switch player turn
        self.current_player = 2 if self.current_player == 1 else 1
        return True
