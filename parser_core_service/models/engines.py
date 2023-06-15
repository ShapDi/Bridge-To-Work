from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://doom:15426378@localhost/link_manager_service", isolation_level="REPEATABLE READ")