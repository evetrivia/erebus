

from thanatos.database.db_utils import update_sql_stored_procs, load_tables_from_files, get_connection

db_conn = get_connection()
update_sql_stored_procs(db_conn)
load_tables_from_files(db_conn)
