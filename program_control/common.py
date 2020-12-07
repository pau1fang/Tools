def get_next_voltage(voltage_current, phase_init, phase_current, k):
    """
    牛顿迭代法对当前控制相位电压进行补偿
    :param voltage_current: 当前电压值
    :param phase_init: 初始相位
    :param phase_current: 当前相位
    :param k: 斜率
    :return:
    """
    return voltage_current + (phase_init-phase_current)/k


def get_next_voltage_ampl(voltage_current, ampl_init, ampl_current, k):
    """
    牛顿迭代法对当前控制振幅电压进行补偿
    """
    return voltage_current + (ampl_init-ampl_current)/k


def get_current_value(filename, row, n):
    """
    从数据文件指定行中读取相位值
    :param filename: 文件名称
    :param row: 指定行
    :param n: 1取振幅，2取相位
    :return: 返回相位值
    """
    with open(filename, "r") as f:
        data = f.readlines()[row]
    data = data.strip()
    current_phase = data.split(",")[n]
    return float(current_phase)  # 获取当前电压下的相位值


def get_freq(array, value, start, end):
    """
    二分法获取待测频率在数据文件中的大概位置
    :param array: s2p文件中的频率组成的数组
    :param value: 待测频率
    :param start:
    :param end:
    :return:
    """
    if end - start > 1:
        mid = (start + end) // 2
        if array[mid] == value:
            return mid
        if array[mid] < value:
            return get_freq(array, value, mid + 1, end)
        else:
            return get_freq(array, value, start, mid - 1)
    else:
        return start


def get_row(freq, filename):
    """
    精确获取待测频率所在行
    :param freq: 待测频率
    :param filename: s2p文件名
    :return:
    """
    with open(filename, "r") as f:
        data = f.readlines()[3:]
        data = list(map(lambda x: x.strip(), data))
        arr = list(map(lambda x: float(x.split(',')[0]), data))
        row = get_freq(arr, freq, 0, len(arr) - 1)
        res = row
        if freq != arr[row]:
            if row > 0 and abs(arr[row - 1] - freq) < abs(arr[res] - freq):
                res = row - 1
            if row < len(arr) and abs(arr[row + 1] - freq) < abs(arr[res] - freq):
                res = row + 1
    res = res + 3
    return res


def package_voltage_message(ampl_route, ampl_v, phase_v):
    """
    打包电压源设置信息
    :param ampl_route 振幅电压路
    :param ampl_v: 控制振幅路电压
    :param phase_v: 控制相位路电压
    :return:
    """
    res = "<M_"
    for _ in range(ampl_route-1):
        res += "{:0>5}_".format(str("%.2f" % phase_v))
    res += "{:0>5}_".format(str("%.2f" % ampl_v))
    res += "_".join(map(lambda x: "{:0>5}".format(str("%.2f" % x)), [phase_v for _ in range(32-ampl_route)]))
    res += "\r\n"
    return res


def package_ampl_voltage_message(ampl_route, ampl_voltage):
    """
    命令：<Smm_nn.nnCR
    mm:通道号01-32
    nn.nn:电压值
    """
    message = "<S{:0>2}_{:0>5}\r\n".format(str(ampl_route), str("%.2f" % ampl_voltage))
    return message
