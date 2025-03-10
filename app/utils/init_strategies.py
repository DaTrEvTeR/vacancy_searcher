import logging

from app.vacancies_search.concrete_strategies.work_ua_strategy import WorkUaStrategy  # noqa: F401

from app.db.db import session_maker
from app.db.models import Site
from app.vacancies_search.base.strategy_registry import StrategyRegistry


async def init_sites_in_db() -> None:
    """Removes unregistered sites from the database and adds new registered ones"""
    sites_in_code = StrategyRegistry.get_all_sites()

    async with session_maker() as db:
        sites_in_db: list[Site] = await Site.read_all(db)

        for db_site in sites_in_db:
            if db_site.site_name not in sites_in_code:
                logging.info(f"Deleting {db_site.site_name} from DB")
                await db_site.delete(db)

        sites_in_db_names = [site.site_name for site in sites_in_db]
        for parser_site in sites_in_code:
            if parser_site not in sites_in_db_names:
                logging.info(f"Add {parser_site} to DB")
                await Site(site_name=parser_site).create(db)
