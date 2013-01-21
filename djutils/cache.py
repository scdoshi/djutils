"""
Cache: This module is for cache related utilites.

Module elements not in this file:
1. `clear_cache` management command in
    djutils.management.commands.clear_cache

"""

###############################################################################
## Constants
###############################################################################
HOUR_IN_SECONDS = 60 * 60
DAY_IN_SECONDS = 24 * HOUR_IN_SECONDS
MONTH_IN_SECONDS = 30 * DAY_IN_SECONDS
YEAR_IN_SECONDS = 365 * DAY_IN_SECONDS
