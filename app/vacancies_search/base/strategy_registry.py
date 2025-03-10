from typing import Dict, Type, List

from app.vacancies_search.base.abc.strategy_abc import Strategy


class StrategyRegistry:
    _registry: Dict[str, Type["Strategy"]] = {}

    @classmethod
    def register(cls, strategy_class: Type["Strategy"]) -> None:
        if not issubclass(strategy_class, Strategy):
            raise ValueError(f"{strategy_class} is not a subclass of Strategy")
        if (not strategy_class.__site_name__) or (not isinstance(strategy_class.__site_name__, str)):
            raise ValueError("Strategy classes must have `__site_name__`: str attr")
        if strategy_class.__site_name__ in cls._registry:
            raise ValueError(
                f"Site name {strategy_class.__site_name__} already registered by {cls._registry[strategy_class.__site_name__]}"
            )
        cls._registry[strategy_class.__site_name__] = strategy_class

    @classmethod
    def get_strategy(cls, site_name: str) -> type["Strategy"]:
        try:
            return cls._registry[site_name]
        except KeyError:
            raise ValueError(f"No strategy found for site: {site_name}")

    @classmethod
    def get_all_sites(cls) -> List[str]:
        return list(cls._registry.keys())
