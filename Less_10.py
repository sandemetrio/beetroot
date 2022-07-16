# def oops():
#     raise KeyError
#
# try:
#     oops()
# except KeyError:
#     print("Oppppssss")
#
# try:
#     oops()
# except IndexError:
#     print("Opps")
#


def some_funck():
    a = input("First arg: ")
    b = input("Second arg: ")
    try:
        c = int(a) ** 2 / int(b)
    except ValueError:
        print("Use numbers, pls")
        some_funck()
    except ZeroDivisionError:
        print("Second arg can't be 0, try again,pls")
        some_funck()
    else:
        print(c)


some_funck()

