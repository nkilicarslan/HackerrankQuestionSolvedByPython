import pandas as pd

from warp.core.logger import LoggerMixin


from acme.acme.utility import

def get_database_from_cotton():
    db_credentials = {
        "username": "necat.kilicarslan",
        "password": "",
        "host": "koton.db.inventanalytics.com",
        "port": "1433",
        "database": "KotonTest",
        "engine": "sqlserver"
    }
    db_credentials["system"] = "mssql"
    table_to_send_to_api = get_data_executions(db_credentials)


def get_data_executions(db_credentials: dict):
    query = """
        SELECT TOP(10) * from markdown.DailyNewItemsInformation
    """
    return Utility.get_database(db_credentials).read_from_db(sql_query=query)
if __name__ == "__main__":
    get_database_from_cotton()
