from dagster import Definitions, load_assets_from_modules, EnvVar,define_asset_job,AssetSelection,ScheduleDefinition
from dagster_snowflake_pandas import SnowflakePandasIOManager
from . import assets

# Load all assets from the assets module
all_assets = load_assets_from_modules([assets])

# Define the Definitions object
defs = Definitions(
    assets=all_assets,  # Unpack the list directly into the assets parameter
    resources={
        "io_manager": SnowflakePandasIOManager(
            account=EnvVar("SNOWFLAKE_ACCOUNT"),
            user=EnvVar("SNOWFLAKE_USER"),
            password=EnvVar("SNOWFLAKE_PASSWORD"),
            database=EnvVar("SNOWFLAKE_DATABASE"),
            role=EnvVar("SNOWFLAKE_ROLE"),
            warehouse=EnvVar("SNOWFLAKE_WAREHOUSE"),
            schema=EnvVar("SNOWFLAKE_SCHEMA"),
        )
    },
    jobs=[
        define_asset_job(
            name = "iris_job",
            selection=AssetSelection.groups("iris"),
        )
    ],
    schedules=[
        ScheduleDefinition(
        name= "iris_schedule",
        job_name="iris_job",
        cron_schedule="* * * * *"
        )
    ],
)
