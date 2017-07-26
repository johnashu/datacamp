def lists2dict(list1, list2):
    """Return a dictionary where list1 provides the keys nad list2 the values"""
    zipped_lists = zip(list1, list2)
    rs_dict = dict(zipped_lists)
    return rs_dict

rs_fxn = lists2dict(lista, listb)
print(rs_fxn)