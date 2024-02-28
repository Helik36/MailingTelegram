import asyncio
import csv

from tokens.tokens_telethon import API_ID, API_HASH
from IDUsers.IDusers import Id_users_telega
import openpyxl

api_id, api_hash = API_ID, API_HASH

async def main():
    with open("..\\FilesWithUsers\\telegaUsers.csv", "r", encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)


if __name__ == "__main__":
    asyncio.run(main())
