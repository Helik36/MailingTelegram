import asyncio
from telethon import TelegramClient, functions
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon.tl.types import InputPhoneContact

from tokens.tokens_telethon import API_ID, API_HASH


api_id, api_hash = API_ID, API_HASH


async def test(client):
    guest_phone_number = "+79999999999"

    contact = InputPhoneContact(client_id=0, phone=guest_phone_number, first_name="custom_first_name",
                                last_name="custom_last_name")

    await client(ImportContactsRequest([contact]))

    contact_info = await client.get_entity(guest_phone_number)
    print(contact_info)
    print(contact_info.username)
    print(contact_info.phone)

    await client(functions.contacts.DeleteContactsRequest(id=[guest_phone_number]))

async def main():

    try:
        async with TelegramClient('anon', api_id, api_hash, system_version='4.16.30-vxCUSTOM') as client:

            await client.start()

            await test(client)

    except:
        print("Что-то пошло не так")


if __name__ == "__main__":
    asyncio.run(main())
