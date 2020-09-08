import asyncio
import itertools
import logging
from typing import List

import aiohttp
import async_timeout
from aiohttp import ClientSession

logger = logging.getLogger("main_logger")


class DataAPI:
    def __init__(self, host: str):
        self._loop = DataAPI._get_asyncio_loop()
        self._list_urls = DataAPI.get_urls(host)

    @staticmethod
    def get_urls(host: str) -> List[str]:
        return [f'http://{host}/data/{i}' for i in range(1, 4)]

    @staticmethod
    def _get_asyncio_loop():
        try:
            return asyncio.get_event_loop()
        except RuntimeError:
            return asyncio.new_event_loop()

    def get_data(self) -> list:
        """FIXME: тут запускаем луп, получаем данные и сортируем их перед тем как отдать"""
        data = self._loop.run_until_complete(self._get_data())
        res_list = list(itertools.chain(*data))
        res_list.sort(key=lambda item: item['id'])
        return res_list

    async def _get_data(self) -> dict:
        """FIXME: таймуат 2 сек
            если в _fetch поставить  sleep(2) то вернет {}
        """
        try:
            async with aiohttp.ClientSession() as session, async_timeout.timeout(2):
                tasks = [self._fetch(session, url) for url in self._list_urls]
                return await asyncio.gather(*tasks)
        except asyncio.TimeoutError as e:
            logger.error(f"{e}")
        return {}

    async def _fetch(self, session: ClientSession, url: str) -> dict:
        headers = {
            "content-type": "application/json",
        }
        async with session.get(url, headers=headers) as response:
            # sleep(2)
            return await response.json()
