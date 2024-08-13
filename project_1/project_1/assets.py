import pandas as pd

from dagster import asset,AssetIn


@asset(group_name="iris")
def iris_dataset() -> pd.DataFrame:
    return pd.read_csv(
        "https://docs.dagster.io/assets/iris.csv",
        names=[
            "sepal_length_cm",
            "sepal_width_cm",
            "petal_length_cm",
            "petal_width_cm",
            "species",
        ],
    )

@asset(ins ={"upstream":AssetIn(key="iris_dataset")},group_name="iris")
def iris_cleaned(upstream: pd.DataFrame) -> pd.DataFrame:
    return upstream.dropna().drop_duplicates()