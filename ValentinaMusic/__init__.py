from ValentinaMusic.core.bot import Valentina
from ValentinaMusic.core.dir import dirr
from ValentinaMusic.core.git import git
from ValentinaMusic.core.userbot import Userbot
from ValentinaMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Valentina()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
