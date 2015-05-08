

import os

from flask.ext.script  import Manager, Shell, Server, Command

from erebus.app import create_app
from erebus.settings import C9Config, ProdConfig, DevConfig
from erebus.extensions import mysql
from thanatos.database.db_utils import download_tables, load_tables_from_files, update_sql_stored_procs


if os.environ.get('PRODUCTION') is not None:
    app = create_app(ProdConfig)
    server = Server()

elif os.environ.get('C9_PROJECT') is not None:
    app = create_app(C9Config)
    server = Server(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))

else:
    app = create_app(DevConfig)
    server = Server()
    
manager = Manager(app)


def _make_context(Command):
    """ Return context dict for a shell session so you can access. """

    return {'app': app, 'db': mysql.connection}

class UpdateDatabase(Command):
    """ Runs the Thanatos database methods to update the databae tables. """
    
    def run(self):
        download_tables()
        load_tables_from_files(mysql.connection)
        update_sql_stored_procs(mysql.connection)

manager.add_command('server', server)
manager.add_command('shell', Shell(make_context=_make_context))
manager.add_command('update_db', UpdateDatabase())

if __name__ == '__main__':
    manager.run()