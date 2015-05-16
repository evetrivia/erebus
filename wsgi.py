

from erebus.app import create_app
from erebus.settings import ProdConfig
 
app = create_app(ProdConfig)
