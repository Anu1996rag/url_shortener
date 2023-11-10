import settings

secrets = settings.get_settings()

DATABASE_URL = f"postgresql://{secrets.database_username}:{secrets.database_password}@" \
                          f"{secrets.database_hostname}/{secrets.database_name}"
