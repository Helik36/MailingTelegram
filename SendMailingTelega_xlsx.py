import asyncio
from telethon import TelegramClient

from tokens.tokens_telethon import API_ID, API_HASH
import openpyxl  # import


api_id, api_hash = API_ID, API_HASH


async def getIdxlsx(client):

    # Скрипт для открытия файла в формате .xlsx (excel)
    try:
        workbook = openpyxl.load_workbook('FilesWithUsers\\telegaUsers.xlsx')
        sheet = workbook.active

        for row in sheet.iter_rows(values_only=True):

            # Можно отправить сообщение по телефону - "+79999999999" (В кавычках)
            await client.send_message(row[0], "Hi!")
            print(f"Отправленно пользователю - {row[0]}")
            await asyncio.sleep(3)

    except FileNotFoundError:
        print("Не удалось открыть файл")

    await client

async def main():

    try:
        async with TelegramClient('anon', api_id, api_hash, system_version='4.16.30-vxCUSTOM') as client:

            await client.start()

            await getIdxlsx(client)

    except:
        print("Что-то пошло не так")


if __name__ == "__main__":
    asyncio.run(main())
