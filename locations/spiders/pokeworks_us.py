from typing import Iterable

from scrapy.http import TextResponse

from locations.categories import Categories, apply_category
from locations.items import Feature
from locations.storefinders.agile_store_locator import AgileStoreLocatorSpider


class PokeworksUSSpider(AgileStoreLocatorSpider):
    name = "pokeworks_us"
    item_attributes = {"brand": "Pokeworks", "brand_wikidata": "Q140690643"}
    allowed_domains = ["pokeworks.com"]

    def post_process_item(self, item: Feature, response: TextResponse, feature: dict) -> Iterable[Feature]:
        item["branch"] = item.pop("name", None)
        apply_category(Categories.FAST_FOOD, item)
        item["extras"]["cuisine"] = "poke"
        yield item
