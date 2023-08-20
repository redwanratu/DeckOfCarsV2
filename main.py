from typing import List
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from players import Player
from pydantic import BaseModel
from dealer import Dealer
from server_game_interface import ServerGame

app = FastAPI()

class User(BaseModel):
    username: str

username_database: List[Player] = []

dealer = Dealer()
game = ServerGame(dealer)

html = ""

@app.get("/")
async def get():
    return HTMLResponse(html)

@app.post("/username")
def register(user: User):
        player = Player(**user.model_dump())
        username_database.append(player)
        return {"username": player.username}


@app.websocket("/ws/game")
async def websocket_endpoint(websocket: WebSocket):
    connection = await websocket.accept()
    await websocket.send_text("Enter your Username: ")

    username = await websocket.receive_text()
    player_list = [player.username for player in username_database]
    
    while username not in player_list:
        await websocket.send_text("Please give valid username")
        username = await websocket.receive_text()
    
    player = Player(username=username)
    game.set_players(player)

    while True:
        card_list = game.get_card_on_hands(player)
        cards_on_board = game.get_card_on_boards()
        player_to_play = game.get_player_to_play()

        payload = {
             "cards": [card.card_face() for card in card_list],
             "cards_on_board": [card.card_face() for card in cards_on_board],
             "player_to_play": player_to_play.get_player_name()
             }
        
        await websocket.send_json(payload)
        data = await websocket.receive_text()

        if game.has_turn(player):
            game.play(card = card_list[int(data)-1],player =player)
        else:
            await websocket.send_json({"message" : "Not your Turn"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app=app)