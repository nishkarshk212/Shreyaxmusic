import asyncio
from pyrogram import Client

async def generate_session():
    api_id = input("Enter API ID: ")
    api_hash = input("Enter API Hash: ")
    
    async with Client(":memory:", api_id=int(api_id), api_hash=api_hash) as app:
        session_string = await app.export_session_string()
        print("\nYour Session String:\n")
        print(session_string)
        print("\nCopy this string and put it in your .env file as SESSION.\n")

if __name__ == "__main__":
    asyncio.run(generate_session())
