import requests
import os
from dotenv import load_dotenv
import chess.pgn
import io
# import asyncio

#loads variables from .env
load_dotenv()

API_NEXT_URL = os.getenv("API_NEXT_URL")

#ply is half move, 1 move = a turn from both players
def pgn_to_fen(pgn, ply): 
    #convert it to file-like object with io.StringIO
    pgn_file = io.StringIO(pgn)
    #read_game take file like object
    game = chess.pgn.read_game(pgn_file)
    board = game.board()

    #play the moves up to the specific puzzle position
    for p, move in enumerate(game.mainline_moves(), start =1):
        board.push(move)
        if p == ply:
            break
    return board.fen()


async def get_next_puzzle():
    try:
        response = requests.get(API_NEXT_URL)
        response.raise_for_status()

        data = response.json()
        pgn = data["game"]["pgn"]
        initial_ply = data["puzzle"]["initialPly"]
        data["fen"] = pgn_to_fen(pgn, initial_ply)
        return data

    except requests.RequestException as e :
        return  {"error": f"Failed to fetch puzzle: {str(e)}"}
    





# async def test():
#     puzzle = await get_next_puzzle()
#     print(puzzle)


# asyncio.run(get_next_puzzle())
