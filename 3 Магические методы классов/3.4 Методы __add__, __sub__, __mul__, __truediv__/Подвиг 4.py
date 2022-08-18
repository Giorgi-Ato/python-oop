class NewList:
    def __init__(self, ls=[]):
        self.ls = ls

    def get_list(self):
        return self.ls

    def __sub__(self, other):
        s = other
        copy_list = self.ls[:]
        if isinstance(other, NewList):
            s = other.ls
        for i in range(len(s)):
            for j in range(len(copy_list)):
                if s[i] is copy_list[j]:
                    copy_list.pop(j)
                    break
        return NewList(copy_list)

    def __isub__(self, other):
        return NewList((self - other).ls)

    def __rsub__(self, other):
        copy_list = self.ls[:]
        for i in range(len(copy_list)):
            for j in range(len(other)):
                if copy_list[i] is other[j]:
                    other.pop(j)
                    break
        return NewList(other)


lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2  # NewList: [-4, 6, 10, 11, 15, False]
print(res_1.ls)
lst1 -= lst2  # NewList: [-4, 6, 10, 11, 15, False]
print(lst1.ls)
res_2 = lst2 - [0, True]  # NewList: [1, 2, 3]
print(res_2.ls)
res_3 = [1, 2, 3, 4.5] - res_2  # NewList: [4.5]
print(res_3.ls)
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a  # NewList: [1, 2]
print(res_4.ls)
lst = res_2.get_list()  # [1, 2, 3]
print(lst)
