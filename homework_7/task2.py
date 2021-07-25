from typing import Union


def custom_map(callback, sequence: Union[list, tuple, dict]) -> Union[list, tuple, dict]:
    result = []
    if type(sequence) == list:
        for item in sequence:
            result.append(callback(item))
        return result

    elif type(sequence) == tuple:
        for item in sequence:
            result.append(callback(item))
        return tuple(result)

    elif type(sequence) == dict:
        map_dict = {}
        for key, value in sequence.items():
            map_dict[key] = callback(value)
        return map_dict

    else:
        raise Exception("Unsupported type")


if __name__ == "__main__":
    my_list = [-1, -2, -2, 0, 0, 1, 2, 3, 3, 6]
    my_tuple = (1, 2, 3, 4, 5, 6, 7, 8)
    my_dict = {
        "john": {
            "age": 24,
            "name": "John"
        },
        "Bob": {
            "age": 33,
            "name": "Bob"
        }
    }

    print(custom_map(lambda x: x * 2, my_list))
    print(custom_map(lambda x: x * 5, my_tuple))
    print(custom_map(lambda item: item["age"] * 2, my_dict))
