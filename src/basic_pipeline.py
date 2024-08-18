from dagster import op, job


@op
def load_data() -> list:
    """
    データをロードする関数です。

    Returns:
        list: ロードされたデータのリスト
    """
    # ここではダミーデータを返しますが、実際のデータソースからデータを取得することができます。
    return [1, 2, 3]


@op
def process_data(data: list) -> list:
    """
    データを処理して結果を返す関数です。

    Parameters:
        data (list): 処理するデータのリスト

    Returns:
        list: 処理されたデータのリスト
    """
    # ここではダミーデータを返しますが、実際のデータ処理を行うことができます。
    return [x * 2 for x in data]


@op
def save_data(data: list):
    """
    データを保存します。

    Args:
        data (list): 保存するデータのリスト

    Returns:
        None
    """
    # ここではデータを印刷しますが、実際のデータ保存処理を行うことができます。
    print(data)


@job
def basic_pipeline():
    """
    基本パイプラインを定義します。

    このパイプラインは、データをロードし、処理し、保存する基本的な手順を実行します。

    Args:
        None

    Returns:
        None
    """
    data = load_data()
    processed_data = process_data(data)
    save_data(processed_data)


# ここでパイプラインを実行する
if __name__ == "__main__":
    result = basic_pipeline.execute_in_process()
