# import asyncio

from characters.scraper import sync_characters_with_api
from asgiref.sync import async_to_sync

from celery import shared_task


@shared_task
def run_sync_with_api() -> None:
    async_to_sync(sync_characters_with_api)()
    # asyncio.run(sync_characters_with_api())
