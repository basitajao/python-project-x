class AyoGameSystem:
    def __init__(self):
        # System State Initialization
        self.board = [4] * 12  # 12 pits, 4 seeds each
        self.scores = {1: 0, 2: 0} # Score tracking
        self.current_player = 1
        self.is_active = True

    # --- Helper Functions (System Analysis Support) ---
    def _is_player_pit(self, index):
        """Validates if index belongs to current player."""
        if self.current_player == 1:
            return 0 <= index <= 5
        return 6 <= index <= 11

    def _get_opposite(self, index):
        """Maps pit index to opponent's corresponding pit."""
        return 11 - index

    # --- Core Processes ---
    def play_turn(self, pit_index):
        """
        The main driver for the IPO Process.
        Input: pit_index (int)
        Output: Boolean (success/fail)
        """
        if not self.is_active:
            print("System Message: Game is over.")
            return False

        # 1. Validation Process
        if not (0 <= pit_index <= 11):
            print("Error: Index out of bounds.")
            return False
        if not self._is_player_pit(pit_index):
            print("Error: You can only play from your own pits.")
            return False
        if self.board[pit_index] == 0:
            print("Error: Cannot play from an empty pit.")
            return False

        # 2. Sowing Process (The Algorithm)
        seeds = self.board[pit_index]
        self.board[pit_index] = 0
        current_idx = pit_index
        
        print(f"Player {self.current_player} picked up {seeds} seeds from pit {pit_index}.")

        while True: # Continuous Relay Loop
            # Sow one seed
            current_idx = (current_idx + 1) % 12
            self.board[current_idx] += 1
            seeds -= 1

            if seeds == 0:
                # RELAY CONDITION: Landed in non-empty pit
                if self.board[current_idx] > 1:
                    print(f"  -> Landed in pit {current_idx} (Total: {self.board[current_idx]}). Relay!")
                    seeds = self.board[current_idx]
                    self.board[current_idx] = 0
                    continue # Continue sowing
                
                # STOP CONDITION: Landed in empty pit (value is now 1)
                elif self.board[current_idx] == 1:
                    print(f"  -> Landed in empty pit {current_idx}. Stop.")
                    self._check_capture(current_idx)
                    break 

        # 3. Finalize State
        self._check_game_over()
        if self.is_active:
            self.current_player = 2 if self.current_player == 1 else 1
        return True

    def _check_capture(self, landing_index):
        """Process for checking capture rules."""
        if self._is_player_pit(landing_index):
            opp_idx = self._get_opposite(landing_index)
            if self.board[opp_idx] > 0:
                captured = self.board[opp_idx]
                self.board[opp_idx] = 0
                self.scores[self.current_player] += captured
                print(f"  *** CAPTURE! Player {self.current_player} captured {captured} seeds! ***")

    def _check_game_over(self):
        """Process to check system termination condition."""
        p1_seeds = sum(self.board[0:6])
        p2_seeds = sum(self.board[6:12])
        
        if p1_seeds  == 0 or p2_seeds == 0:
            self.is_active = False
            # Remaining seeds ownership logic (simplified)
            self.scores[1] += p1_seeds
            self.scores[2] += p2_seeds
            print("\n--- GAME OVER ---")
            print(f"Final Score -> P1: {self.scores[1]} | P2: {self.scores[2]}")

    # --- Output Generation ---
    def display_board(self):
        """Generates the visual output of the system."""
        # P2 is top row (reversed for visual alignment)
        p2_row = self.board[6:12][::-1] 
        p1_row = self.board[0:6]
        
        print("\n" + "="*30)
        print(f"Player 2 (Top) [Score: {self.scores[2]}]")
        print(f"Pits [11-6]: {p2_row}")
        print(f"Pits [ 0-5]: {p1_row}")
        print(f"Player 1 (Bot) [Score: {self.scores[1]}]")
        print("="*30 + "\n")

# --- Driver Code (User Interface Simulation) ---
if __name__ == "__main__":
    game = AyoGameSystem()
    game.display_board()
    
    
    # Example sequence to demonstrate flow
    # Player 1 moves pit 0
    game.play_turn(0) 
    game.display_board()


def start_terminal_game():
    game = AyoGameSystem()
    print("Welcome to Ayo (Terminal Edition)!")
    
    while game.is_active:
        game.display_board()
        print(f"Current Player: {game.current_player}")
        
        try:
            # Get input from the terminal
            choice = int(input("Select a pit index to play (0-5 for P1, 6-11 for P2): "))
            
            # Execute the move logic
            success = game.play_turn(choice)
            
            if not success:
                print("Invalid move, try again.")
                
        except ValueError:
            print("Please enter a valid number between 0 and 11.")

    print("Thanks for playing!")

if __name__ == "__main__":
    start_terminal_game()