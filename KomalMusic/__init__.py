from KomalMusic.core.bot import Komal
from KomalMusic.core.dir import dirr
from KomalMusic.core.git import git
from KomalMusic.core.userbot import Userbot
from KomalMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Komal()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
