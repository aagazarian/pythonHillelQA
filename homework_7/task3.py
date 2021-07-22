from typing import Union


def custom_reduce(callback, sequence: Union[list, tuple, dict]) -> int:
    if type(sequence) in [list, tuple]:
        result = sequence[0]
        for i in range(1, len(sequence)):
            result = callback(result, sequence[i])
            i += 1
        return result
    # elif type(sequence) == dict:
    #     reduced_dict = {}
    #     values = list(sequence.values())
    #     for i in range(0, len(values)):
    #         reduced_dict = callback(values[i - 1], values[i])
    #     return reduced_dict
    else:
        raise Exception("Unsupported type of sequence")


if __name__ == "__main__":
    my_dict_list = [{
            "age": 24,
            "name": "John"
        },
        {
            "age": 33,
            "name": "Bob"
        },
        {
            "age": 28,
            "name": "Kevin"
        }
    ]

    my_list = [-1, -2, -2, 1, 2, 3, 3, 6]
    my_list_float = [-1.3, -2.2, -2.9, 1.7, 2.9, 3.6, 3.5, 6.8]
    my_list_str = ["a", "b", "c", "d"]

    my_tuple = (1, 2, 3, 4, 5, 6, 7, 8)
    my_tuple_float = (1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8)
    my_tuple_str = ("1", "2", "3", "4", "5")

    print("Reduce for dict:")
    print(custom_reduce(lambda man1, man2: man1 if man1["age"] > man2["age"] else man2, my_dict_list))
    print("\nReduce for list:")
    print(custom_reduce(lambda el1, el2: el1 * el2, my_list))
    print(custom_reduce(lambda el1, el2: el1 * el2, my_list_float))
    print(custom_reduce(lambda el1, el2: f"{el1} {el2}", my_list_str))

    print("\nReduce for tuple:")
    print(custom_reduce(lambda el1, el2: el1 * el2, my_tuple))
    print(custom_reduce(lambda el1, el2: el1 * el2, my_tuple_float))
    print(custom_reduce(lambda el1, el2: f"{el1} {el2}", my_tuple_str))