class AyoGame:
    """
    Implementation of the Ayo game - a traditional African mancala-style board game.
    """
    
    def __init__(self):
        """Initialize the game with 12 pits and 4 seeds per pit."""
        # Board configuration: pits 0-5 for Player 1, pits 6-11 for Player 2
        self.board = [4] * 12
        self.player1_score = 0
        self.player2_score = 0
        self.current_player = 1
        self.PITS_PER_PLAYER = 6
        self.INITIAL_SEEDS = 4
    
    def display_board(self):
        """Display the current state of the board."""
        print("\n" + "=" * 50)
        print("         AYO GAME BOARD".center(50))
        print("=" * 50)
        
        # Player 2's side (top row) - displayed in reverse
        player2_pits = "  ".join([f"[{self.board[i]}]" for i in range(11, 5, -1)])
        print(f"Player 2:  {player2_pits}  Score: {self.player2_score}")
        
        pit_indices_top = "   ".join([f" {i} " for i in range(11, 5, -1)])
        print(f"Pit Index: {pit_indices_top}")
        
        print("-" * 50)
        
        pit_indices_bottom = "   ".join([f" {i} " for i in range(6)])
        print(f"Pit Index: {pit_indices_bottom}")
        
        # Player 1's side (bottom row)
        player1_pits = "  ".join([f"[{self.board[i]}]" for i in range(6)])
        print(f"Player 1:  {player1_pits}  Score: {self.player1_score}")
        
        print("=" * 50 + "\n")
    
    def is_valid_move(self, pit_index):
        """
        Validate if a move is legal.
        
        Args:
            pit_index: The pit selected by the player
            
        Returns:
            bool: True if move is valid, False otherwise
        """
        # Check if pit index is within valid range
        if pit_index < 0 or pit_index >= 12:
            print("Invalid pit index. Choose between 0-11.")
            return False
        
        # Check if pit belongs to current player
        if self.current_player == 1 and not (0 <= pit_index <= 5):
            print("Invalid move. Player 1 must choose pits 0-5.")
            return False
        
        if self.current_player == 2 and not (6 <= pit_index <= 11):
            print("Invalid move. Player 2 must choose pits 6-11.")
            return False
        
        # Check if pit has seeds
        if self.board[pit_index] == 0:
            print("Invalid move. Selected pit is empty.")
            return False
        
        return True
    
    def make_move(self, pit_index):
        """
        Execute a move by sowing seeds and checking for captures.
        
        Args:
            pit_index: The pit selected by the player
        """
        if not self.is_valid_move(pit_index):
            return
        
        # Pick up all seeds from selected pit
        seeds = self.board[pit_index]
        self.board[pit_index] = 0
        print(f"Player {self.current_player} picked up {seeds} seeds from pit {pit_index}")
        
        # Sow seeds counter-clockwise
        current_pit = pit_index
        while seeds > 0:
            current_pit = (current_pit + 1) % 12
            
            # Skip the original pit if we cycle back
            if current_pit == pit_index:
                current_pit = (current_pit + 1) % 12
            
            self.board[current_pit] += 1
            seeds -= 1
            print(f"  Dropped seed in pit {current_pit} (now has {self.board[current_pit]} seeds)")
        
        # Check for captures
        self.perform_capture(current_pit)
        
        # Switch player
        self.current_player = 2 if self.current_player == 1 else 1
    
    def perform_capture(self, last_pit):
        """
        Handle capture logic after a move.
        
        Args:
            last_pit: The pit where the last seed was dropped
        """
        # Can only capture from opponent's side
        is_opponent_side = False
        if self.current_player == 1 and 6 <= last_pit <= 11:
            is_opponent_side = True
        elif self.current_player == 2 and 0 <= last_pit <= 5:
            is_opponent_side = True
        
        if not is_opponent_side:
            print("  Last seed landed on own side - no capture possible.")
            return
        
        # Capture if landing pit has 2 or 3 seeds
        captured_total = 0
        capture_pit = last_pit
        
        while 0 <= capture_pit < 12 and self.board[capture_pit] in [2, 3]:
            # Verify still on opponent's side
            if self.current_player == 1 and not (6 <= capture_pit <= 11):
                break
            if self.current_player == 2 and not (0 <= capture_pit <= 5):
                break
            
            captured_total += self.board[capture_pit]
            print(f"  Captured {self.board[capture_pit]} seeds from pit {capture_pit}")
            self.board[capture_pit] = 0
            
            # Move backwards to check for chain captures
            capture_pit -= 1
            if capture_pit < 0:
                capture_pit = 11
        
        if captured_total > 0:
            if self.current_player == 1:
                self.player1_score += captured_total
            else:
                self.player2_score += captured_total
            print(f"  Total captured: {captured_total} seeds")
        else:
            print(f"  No capture - landing pit had {self.board[last_pit]} seeds.")
    
    def is_game_over(self):
        """
        Check if the game has ended.
        
        Returns:
            bool: True if game is over, False otherwise
        """
        # Check if Player 1 has no seeds
        player1_seeds = sum(self.board[0:6])
        
        # Check if Player 2 has no seeds
        player2_seeds = sum(self.board[6:12])
        
        return player1_seeds == 0 or player2_seeds == 0
    
    def announce_winner(self):
        """Determine and display the winner."""
        print("\n" + "=" * 50)
        print("          GAME OVER!".center(50))
        print("=" * 50)
        print(f"Player 1 Final Score: {self.player1_score}")
        print(f"Player 2 Final Score: {self.player2_score}")
        print("-" * 50)
        
        if self.player1_score > self.player2_score:
            print("     PLAYER 1 WINS! 🎉".center(50))
        elif self.player2_score > self.player1_score:
            print("     PLAYER 2 WINS! 🎉".center(50))
        else:
            print("     IT'S A TIE! 🤝".center(50))
        
        print("=" * 50 + "\n")
    
    def play(self):
        """Main game loop."""
        print("*" * 50)
        print("*   WELCOME TO AYO GAME (AYOAYO)   *".center(50))
        print("*" * 50)
        print("\nRules:")
        print("1. Players take turns picking a pit and sowing seeds counter-clockwise")
        print("2. Capture occurs when last seed lands in opponent's pit with 2 or 3 seeds")
        print("3. Game ends when one player has no seeds left")
        print("4. Player with most captured seeds wins!\n")
        
        while not self.is_game_over():
            self.display_board()
            print(f"Player {self.current_player}'s turn")
            
            try:
                pit_index = int(input("Enter pit index to play: "))
                self.make_move(pit_index)
            except ValueError:
                print("Invalid input. Please enter a number.")
            except KeyboardInterrupt:
                print("\n\nGame interrupted by user.")
                return
        
        self.display_board()
        self.announce_winner()


def main():
    """Entry point for the Ayo game."""
    game = AyoGame()
    game.play()


if __name__ == "__main__":
    main()