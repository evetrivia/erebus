

from erebus import mysql
from thanatos.database.db_utils import update_sql_stored_procs, load_tables_from_files

update_sql_stored_procs(mysql.connection)
load_tables_from_files(mysql.connection)
