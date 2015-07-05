

from flask.ext.script  import Manager, Shell, Server, Command

from erebus.app import create_app
from erebus.settings import DevConfig
from erebus.extensions import mysql
from thanatos.database.db_utils import load_tables_from_files, update_sql_stored_procs


app = create_app(DevConfig)
server = Server()
    
manager = Manager(app)


def _make_context(Command):
    """ Return context dict for a shell session so you can access. """

    return {'app': app, 'db': mysql.connection}

class UpdateTables(Command):
    """ Runs the Thanatos database methods to update the database tables. """
    
    def run(self):
        load_tables_from_files(mysql.connection)

class UpdateProcs(Command):
    """ Runs the Thanatos database methods to update the database procedures. """

    def run(self):
        update_sql_stored_procs(mysql.connection)

manager.add_command('server', server)
manager.add_command('shell', Shell(make_context=_make_context))
manager.add_command('update_tables', UpdateTables())
manager.add_command('update_procs', UpdateProcs())

if __name__ == '__main__':
    manager.run()
