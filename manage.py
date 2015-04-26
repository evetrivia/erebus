

import os

from flask.ext.script  import Manager, Shell, Server

from erebus.app import create_app
from erebus.settings import C9Config

app     = create_app(C9Config)
server  = Server(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))
manager = Manager(app)


def _make_context():
    """ Return context dict for a shell session so you can access. """

    return {'app': app}


manager.add_command('server', server)
manager.add_command('shell',  Shell(make_context=_make_context))

if __name__ == '__main__':
    manager.run()