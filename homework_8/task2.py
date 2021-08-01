# def num_sqr_decorator(function):
#     def inner():
#         generator = function()
#         while True:
#             try:
#                 print(next(generator))
#             except StopIteration:
#                 print("The last element is reached")
#                 break
#     return inner
#
#
# @num_sqr_decorator
# def num_sqr_gen():
#     num = 0
#     while num <= 1000000000:
#         yield num ** 2
#         num += 2
#
#
# if __name__ == "__main__":
#     next(num_sqr_gen())
# not bad. But this decorator brakes generator. In best scenario
# I will use this decorator to gen value. But decorator is blocking function
# in same time generator just sleep after yield. So this hum_sqr_gen start to
# be useless after wrapping in decorator.
# -5 points

#re-work:
def function_sqr_generator():
    num = 0
    while num <= 1000000000:
        yield num ** 2
        num += 2


if __name__ == "__main__":
    my_iter = function_sqr_generator()

    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))
# Good.
