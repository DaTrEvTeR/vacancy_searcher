from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Site


# todo: redo when release parsers
async def get_sites_models(db: AsyncSession):
    sites_models: list[Site] = await Site.read_all(db)
    sites_references = dict()
    for site in sites_models:
        sites_references[site.site_name] = site
    return sites_references
