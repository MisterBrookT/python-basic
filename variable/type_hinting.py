from typing import Union, cast

def process_data(data: Union[int, str]):
    if isinstance(data, int):
        result = data + 1
    else:
        # Cast is used to let type checker know `data` is `str` here,
        # can help clarifying the ambiguities.
        result = cast(str, data).upper()
    print(result)

process_data(42)      # Output: 43
process_data("hello")  # Output: HELLO