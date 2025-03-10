from aiohttp import ClientError
from app.utils.custom_session import CustomSession
from app.vacancies_search.base.abc.scraper_abc import Scraper
from app.db.models import Filter


class WorkUaScraper(Scraper):
    BASE_URL = "https://www.work.ua/jobs"

    async def get_data(self, filt_obj: Filter, page: int = 1) -> str:
        url = self.get_url(filt_obj, page)

        async with CustomSession() as session:
            async with session.get(url) as response:
                if not response.ok:
                    raise ClientError(f"get_data: {response.status}: {response.reason}")
                res = await response.text()
            return res

    def get_url(self, filt_obj, page):
        url = self.BASE_URL
        if filt_obj.only_remote:
            url += "-remote"
        jt = "+".join(filt_obj.title.strip().split())
        url += "-" + jt + f"/?page={page}"
        return url
