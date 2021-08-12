from typing import Union


class CustomIterator:
    def __init__(self, sequence: Union[list, tuple], start_index: int, end_index: int):
        self.__sequence = sequence
        self.__set_current(start_index)
        self.__end_index = end_index
        print(f"Try to iterate sequence: {sequence}, from index: {start_index}, to index: {end_index}")

    def __set_current(self, start_index):
        if start_index >= 0:
            self.__current = start_index
        else:
            self.__current = 0
            print("start_index can't by less than '0'. start_index set to '0")

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.__sequence) > self.__current <= self.__end_index:
            element = self.__sequence[self.__current]
            self.__current += 1
            return element
        else:
            print("End of sequence was reached")
            raise StopIteration


if __name__ == '__main__':
    in_list = [1, 2, 3, 4, 5, 6]
    custom_iterator_more_length = CustomIterator(in_list, 0, 9)
    iterator1 = iter(custom_iterator_more_length)
    for item in iterator1:
        print(item)

    in_tuple = [-2, -1, 0, 1, 2, 3, 4]
    custom_iterator_less0 = CustomIterator(in_tuple, -2, 2)
    iterator2 = iter(custom_iterator_less0)
    for item in iterator2:
        print(item)
