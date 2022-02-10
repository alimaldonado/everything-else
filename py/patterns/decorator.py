# this is the decorator
def capitalize_names(func):
    def func_wrapper(fname, lname):
        return func(fname, lname).upper()

    return func_wrapper


def get_fullname_v1(firstname, lastname):
    return "{}, {}".format(lastname, firstname)


# This ensures that the original function get_fullname
# becomes replaced by the modified (decorated) function
# returned by the capitalize_names decorator.
get_fullname_v1 = capitalize_names(get_fullname_v1)


@capitalize_names
# decorator syntactic sugar
def get_fullname(firstname, lastname):
    return "{}, {}".format(lastname, firstname)


# both work the same way
print(get_fullname_v1("ali", "maldonado"))
print(get_fullname("ali", "maldonado"))
