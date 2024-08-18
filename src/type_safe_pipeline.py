from dagster import op, job, In, Out


@op(ins={"input1": In(int), "input2": In(int)}, out=Out(int))
def add_op(input1: int, input2: int) -> int:
    """
    2つの整数を受け取り、それらを加算した結果を返す関数です。

    Parameters:
        input1 (int): 加算する整数値
        input2 (int): 加算する整数値

    Returns:
        int: 加算結果の整数値
    """
    return input1 + input2


@op(ins={"value": In(int)}, out=Out(str))
def to_strings_op(value: int) -> str:
    """
    文字列に変換する関数です。

    Parameters:
        value (int): 変換する整数値

    Returns:
        str: 変換された文字列
    """
    return f"The result is {value}"


@job
def type_safe_pipeline(input1: int, input2: int):
    """
    これは型安全なパイプラインを表す関数で、2つの整数入力を受け取り、それらを加算します。

    Parameters:
    input1 (int): 最初の整数入力
    input2 (int): 2番目の整数入力

    Returns:
    None
    """
    to_strings_op(add_op(input1, input2))


if __name__ == "__main__":
    result = type_safe_pipeline.execute_in_process(
        run_config={
            "inputs": {
                "input1": {"value": 5},
                "input2": {"value": 10}
            }
        }
    )
