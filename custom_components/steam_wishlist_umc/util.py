import logging
import datetime
from typing import Any, Dict, Optional

from .types import SteamGame

_LOGGER = logging.getLogger(__name__)


def get_steam_game(game_id: int, game: Dict[str, Any], config_entry) -> SteamGame:
    """Get a SteamGame from a game dict."""
    pricing: Optional[Dict[str, Any]] = None
    try:
        pricing: Dict[str, Any] = game["subs"][0]
        discount_pct = pricing["discount_pct"] or 0
    except IndexError:
        # This typically means this game is not yet released so pricing is not known.
        pricing = None
        discount_pct = 0

    normal_price: Optional[float] = None
    if pricing:
        price = int(pricing["price"])
        if discount_pct == 100:
            normal_price = price
        else:
            normal_price = round(price / (100 - discount_pct), 2)

    sale_price: Optional[float] = None
    if pricing and discount_pct:
        # Price is an integer so $6.00 is 600.
        sale_price = round(int(pricing["price"]) * 0.01, 2)

    reviews_percent = game.get('reviews_percent', 'N/A')
    review_desc = game.get('review_desc', 'No reviews')
    rating_info = f"Reviews: {reviews_percent}% &#40;{review_desc}&#41;"

    tags = game.get("tags", [])
    tags_string = ", ".join(tags)

    try:
        original_price = float(normal_price if normal_price is not None else 0)
        sale_price_val = float(sale_price if sale_price is not None else original_price)
        discount_percentage = int(discount_pct)
        original_price_formatted = f"{original_price:.2f}"
        if sale_price is not None:
            strikethrough_price = ''.join(ch + "\u0336" for ch in original_price_formatted[:-1]) + original_price_formatted[-1]
            price_info = f"{strikethrough_price} ${sale_price_val:.2f} &#40;{discount_percentage}% off&#41; 🎫"
        else:
            price_info = f"Price: ${original_price:.2f}"
    except (ValueError, TypeError):
        price_info = "Price information unavailable"


    release_date = "Released: " + datetime.datetime.utcfromtimestamp(int(game.get("release_date", "0"))).strftime("%b %d, %Y") if str(game.get("release_date", "0")).isdigit() else "Unknown"

    return {
        "title": game["name"],
        "fanart": game.get("capsule"),
        "poster": game.get("capsule"),
        "deep_link": f"https://store.steampowered.com/app/{game_id}",
        "normal_price": str(normal_price),
        "percent_off": str(discount_pct),
        "sale_price": sale_price if not config_entry.options.get("show_all_wishlist_items", True) else str(sale_price),
        "steam_id": str(game_id),
        "airdate": game.get("release_date", ""),
        "rating": rating_info,
        "price": price_info,
        "release": release_date,
        "tags": tags,
	    "genres": ", ".join(game.get("tags", [])),
    }
