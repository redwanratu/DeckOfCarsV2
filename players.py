class Player:
    def __init__(self, username: str = "Player 1") -> None:
        self.username = username

    def get_player_name(self) -> str:
        return f"{self.username.capitalize()}"
    
    def set_username_from_user_input(self) -> str:
        self.username = input("Enter your Username: ")


    def __str__(self) -> str:
        return f"{self.username.capitalize()}"
    