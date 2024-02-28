import asyncio
import csv
from telethon import TelegramClient

from tokens.tokens_telethon import API_ID, API_HASH

api_id, api_hash = API_ID, API_HASH


async def getIdCsv(client):
    try:
        with open("FilesWithUsers\\telegramUser.csv", encoding='cp1251', newline='') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row[0].isdigit():
                    print(f"int - {row[0]}")
                    try:
                        await client.send_message(int(row[0]), "Hi!")
                        print(f"Отправленно пользователю - {row[0]}")
                        await asyncio.sleep(3)
                    except ValueError:
                        print(f"Пользователь {row[0]} - отсутствует")

                else:
                    print(f"str - {row[0]}")
                    await client.send_message(row[0], "Hi!")
                    print(f"Отправленно пользователю - {row[0]}")
                    await asyncio.sleep(3)

    except FileNotFoundError:
        print("Не удалось открыть файл")


async def main():
    try:
        async with TelegramClient('anon', api_id, api_hash, system_version='4.16.30-vxCUSTOM') as client:

            await client.start()

            await getIdCsv(client)

    except:
        print("Что-то пошло не так")



if __name__ == "__main__":
    asyncio.run(main())
