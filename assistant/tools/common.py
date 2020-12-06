import os
import re


def get_filenames(filepath="", file_ext="all"):
    # 遍历filepath下的文件
    file_list = []
    for filename in os.listdir(filepath):
        fi_d = os.path.join(filepath, filename)
        if file_ext == ".doc":
            if os.path.splitext(fi_d)[1] in [".doc", "docx"]:
                file_list.append(fi_d)
        else:
            if file_ext == "all":
                file_list.append(fi_d)
            elif os.path.splitext(fi_d)[1] == file_ext:
                file_list.append(fi_d)
            else:
                pass
    file_list.sort(key=index_sort)
    return file_list


def index_sort(elem):
    a = re.findall(r"第\d*章", elem)
    if not a:
        return float("inf")
    else:
        return int(a[0][1:-1])
