import requests
import os
from dotenv import load_dotenv
# import asyncio

#loads variables from .env
load_dotenv()

API_NEXT_URL = os.getenv("API_NEXT_URL")

async def get_next_puzzle():
    try:
        response = requests.get(API_NEXT_URL)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e :
        return  {"error": f"Failed to fetch puzzle: {str(e)}"}
    

# async def test():
#     puzzle = await get_next_puzzle()
#     print(puzzle)


# asyncio.run(get_next_puzzle())
