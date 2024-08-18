from dagster import asset, Definitions, define_asset_job


@asset
def raw_data() -> list:
    return [1, 2, 3]


@asset
def processed_data(raw_data: list) -> list:
    return [x * 2 for x in raw_data]


@asset
def summary(processed_data: list) -> int:
    return sum(processed_data)


defs = Definitions(assets=[raw_data, processed_data, summary])
run_job = define_asset_job("run_job", selection="*")
