import copy
Example = [1, 2, -1, -2]


def update_inplace(data):
    data.append(0)
    data.sort()


def show(data=copy.deepcopy(Example)):
    print(data)


def show_updated(data=Example):
    data = copy.deepcopy(data)
    update_inplace(data)
    print(data)


def update_and_show(data=Example):
    if data is Example:
        data = copy.deepcopy(data)
    update_inplace(data)
    print(data)


update_and_show()
update_and_show()
UserData = [3, 1, 2]
update_and_show(UserData)
update_and_show(UserData)
