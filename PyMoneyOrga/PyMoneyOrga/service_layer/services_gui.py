from ..database.database_interface import DatabaseInterface

def get_all_acc_names(database : DatabaseInterface):
    """
    returns a list with all acc names saved in the database
    """
    session = database.get_session()
    accs = database.get_all_acc(session)
    database.close(session)
    return [acc.acc_name for acc in accs]
