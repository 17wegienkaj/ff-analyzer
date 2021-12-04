from yfpy import data
from yfpy.models import Game, StatCategories, User, Scoreboard, Settings, Standings, League, Player, Team, \
    TeamPoints, TeamStandings, Roster
from yfpy.query import YahooFantasySportsQuery
from pathlib import Path
import os

authDir = Path(".")
season = "2021"
chosenWeek = 1
gameKey = "399" # NFL - 2020
gameCode = "nfl"
leagueID = "337476"

yahooQuery = YahooFantasySportsQuery(
    authDir,
    leagueID,
    game_id=gameKey,
    game_code=gameCode,
    offline=False,
    all_output_as_json=False,
    consumer_key=os.environ["CLIENT_ID"],
    consumer_secret=os.environ["CLIENT_SECRET"],
    browser_callback=True
)

results = yahooQuery.get_league_scoreboard_by_week(1)
print(results)