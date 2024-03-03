[![](https://img.shields.io/github/release/mkanet/steam-wishlist-umc/all.svg?style=for-the-badge)](https://github.com/mkanet/steam-wishlist-umc/releases)
[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg?style=for-the-badge)](https://github.com/hacs/integration)
[![](https://img.shields.io/github/license/mkanet/steam-wishlist-umc?style=for-the-badge)](LICENSE)
[![](https://img.shields.io/github/actions/workflow/status/mkanet/steam-wishlist-umc/pythonpackage.yaml?branch=main&style=for-the-badge)](https://github.com/mkanet/steam-wishlist-umc/actions)

# Steam Wishlist UMC for Home Assistant

This custom component was originally adapted from https://github.com/boralyl/steam-wishlist to support [Upcoming Media Card's](https://github.com/custom-cards/upcoming-media-card) newer advanced features.

[![sensor.steam_wishlist](https://github.com/mkanet/steam-wishlist-umc/raw/main/assets/setup.png)](https://github.com/mkanet/steam-wishlist-umc/raw/main/assets/setup.png)

## Pre-Installation

Prior to installing this integration you must first ensure that your wishlist is publicly
viewable. To do this, login to you steam account and edit your profile. Under the
`Privacy Settings` tab, set `Game Details` to `Public`. Without this step, this integration
will not be able to parse your wishlist.

[![steam privacy settings](https://github.com/mkanet/steam-wishlist-umc/raw/main/assets/steam-profile.png)](https://github.com/mkanet/steam-wishlist-umc/raw/main/assets/steam-profile.png)

## HACS Installation

1. Search for `Steam Wishlist` under the `Integrations` tab on [HACS](https://hacs.xyz/).
2. Install the integration.
3. In the home assistant configuration screen click on `Integrations`.
4. Click on the `+` icon to add a new integration.
5. Search for `Steam Wishlist` and select it.
6. Enter your steam account name and click `Submit`.

## Manual Installation

1. Download the [latest release](https://github.com/mkanet/steam-wishlist-umc/releases).
2. Extract the files and move the `steam_wishlist` folder into the path to your
   `custom_components`. e.g. `/config/custom_components`.
3. In the home assistant configuration screen click on `Integrations`.
4. Click on the `+` icon to add a new integration.
5. Search for `Steam Wishlist` and select it.
6. Enter your steam account name and click `Submit`.

## Sensors

After you successfully setup the integration a number of sensors will be created.

### `sensor.steam_wishlist_umc_<your-profile-id>`

This sensor will report the number of games on sale from your wishlist.

[![sensor.steam_wishlist_umc](https://github.com/mkanet/steam-wishlist-umc/raw/main/assets/sensor.steam_wishlist.png)](https://github.com/mkanet/steam-wishlist-umc/raw/main/assets/sensor.steam_wishlist.png)

#### Attributes

The following state attributes are available for this sensor:

| attribute | description                                 |
| --------- | ------------------------------------------- |
| on_sale   | An array of [games on sale](#attributes-1). |

### `binary_sensor.steam_wishlist_<title>`

A binary sensor will be created for each game on your wishlist. It's state will
indicate if it is on sale or not.

[![sensor.steam_wishlist](https://github.com/mkanet/steam-wishlist-umc/raw/main/assets/binary_sensor.steam_wishlist_terraria.png)](https://github.com/mkanet/steam-wishlist-umc/raw/main/assets/binary_sensor.steam_wishlist_terraria.png)

#### Attributes

The following state attributes are available for this sensor:

| attribute       | description                                              |
| --------------- | -------------------------------------------------------- |
| title           | Title of the game                                        |
| fanart          | URL for the background image (fanart mode)               |
| poster          | URL for the background game  (poster mode)               |
| deep_link       | Direct url link to game on steam when clicked in UMC     |
| normal_price    | Price                                                    |
| percent_off     | Percentage off of the normal price.                      |
| sale_price      | Sale price of the game.                                  |
| steam_id        | Steam ID of the game.                                    |
| airdate         | Date game was released (Unix timestamp format)           |
| review_desc     | Review description _(value only)_|
| reviews_percent | Percentage of positive reviews _(value only)_            |
| reviews_total   | Total number of reviews _(value only)_                   |
| rating          | Reviews e.g. `Reviews: 92% (Very Positive)` _(formatted)_|
| price           | Price description of game                                |
| release         | Release date of game                                     |
| tags            | (Attributes)                                             |
| genres          | Genres of game e.g. `FPS, Action, First-Person, Shooter` |

## Displaying in Lovelace

You can use 
[upcoming-media-card](https://github.com/custom-cards/upcoming-media-card)
to display the games on sale from your Steam wish list.

```yaml
- type: custom:upcoming-media-card
  entity: sensor.steam_wishlist_umc_978793482343112
  title: Steam Wishlist
  image_style: backgroundart
  max: 10
```

[![wishlist in the nintendo card](https://github.com/mkanet/steam-wishlist-umc/raw/main/assets/custom-card.png)](https://github.com/mkanet/steam-wishlist-umc/raw/main/assets/custom-card.png)
