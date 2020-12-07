import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from assistant_ui import Ui_Form
from RsInstrument import *
import serial
import serial.tools.list_ports
import time
import os
from common import *


class Assistant(QtWidgets.QWidget, Ui_Form):
    stop_phase_signal = pyqtSignal()
    stop_ampl_signal = pyqtSignal()
    stop_all_signal = pyqtSignal()

    def __init__(self):
        super(Assistant, self).__init__()
        self.setupUi(self)
        self.init()
        self.setWindowTitle("assistant")
        self.setMaximumSize(850, 490)
        self.setMinimumSize(850, 490)
        self.ser = serial.Serial()
        self.port_check()
        self.loop_state_phase = 0
        self.loop_state_ampl = 0
        self.loop_state_all = 0
        self.ampl_route = 1

    def init(self):
        self.data_clear_button.clicked.connect(self.data_clear)
        self.start_all_button.clicked.connect(self.start_all)
        self.stop_all_button.clicked.connect(self.stop_all)

        self.start_phase.clicked.connect(self.start_phase_loop)
        self.stop_phase.clicked.connect(self.stop_phase_loop)

        self.start_ampl.clicked.connect(self.start_ampl_loop)
        self.stop_ampl.clicked.connect(self.stop_ampl_loop)

        self.voltage_source_input.currentTextChanged.connect(self.port_imf)
        self.voltage_button.clicked.connect(self.port_open)
        self.voltage_close_button.clicked.connect(self.port_close)
        if not os.path.exists("data_files"):
            os.mkdir("data_files")

    def port_check(self):
        # 检测所有存在的串口，将信息存储在字典中
        self.com_dict = {}
        port_list = list(serial.tools.list_ports.comports())
        for port in port_list:
            self.com_dict["%s" % port[0]] = "%s" % port[1]
            self.voltage_source_input.addItem(port[0])
        if len(self.com_dict) == 0:
            self.state_label.setText(" 无串口")

    def port_imf(self):
        """
        显示选定的串口的详细信息
        """
        imf_s = self.voltage_source_input.currentText()
        if imf_s != "":
            self.state_label.setText(self.com_dict[self.voltage_source_input.currentText()])

    def port_open(self):
        """
        打开电源串口
        :return:
        """
        self.ser.port = self.voltage_source_input.currentText()
        try:
            self.ser.open()
        except:
            QtWidgets.QMessageBox.critical(self, "Port Error", "此串口不能被打开！")
            return None
        if self.ser.isOpen():
            self.voltage_button.setEnabled(False)
            self.voltage_close_button.setEnabled(True)
            self.formGroupBoxState.setTitle("电压源串口状态（已开启）")

    def port_close(self):
        """
        关闭电源串口
        :return:
        """
        try:
            self.ser.close()
        except Exception:
            pass
        self.voltage_button.setEnabled(True)
        self.voltage_close_button.setEnabled(False)
        self.formGroupBoxState.setTitle("电压源串口状态（已关闭）")

    def data_clear(self):
        self.voltage_text.clear()

    def start_phase_loop(self):
        """
        开始循环，使用牛顿迭代法逐步逼近初始相位
        不会停止，直到点击停止键
        :return:
        """
        params = self.get_params_phase()

        self._thread_1 = Thread_1(**params)
        self.stop_phase_signal.connect(self._thread_1.stop)
        self._thread_1.start()
        self._thread_1.trigger_current_data.connect(self.show_current_data_phase)
        self._thread_1.trigger_na_connect.connect(self.na_except_connect)
        self._thread_1.trigger_set_voltage.connect(self.set_voltage_phase)
        self.loop_state_phase = 1
        if self.loop_state_phase:
            self.start_phase.setEnabled(False)
            self.stop_phase.setEnabled(True)

    def start_ampl_loop(self):
        """
        开始循环，使用牛顿迭代法逐步逼近初始振幅
        不会停止，直到点击停止键
        :return:
        """
        params = self.get_params_ampl()
        self._thread_2 = Thread_2(**params)
        self.stop_ampl_signal.connect(self._thread_2.stop)
        self._thread_2.start()
        self._thread_2.trigger_current_data.connect(self.show_current_data_ampl)
        self._thread_2.trigger_na_connect.connect(self.na_except_connect)
        self._thread_2.trigger_set_voltage.connect(self.set_voltage_ampl)
        self.loop_state_ampl = 1
        if self.loop_state_ampl:
            self.start_ampl.setEnabled(False)
            self.stop_ampl.setEnabled(True)

    def start_all(self):
        """
        开始循环，使用牛顿迭代法同时回调相位和振幅
        不会停止，直到点击停止键
        :return:
        """
        params = self.get_params_ampl()
        params.update(self.get_params_phase())
        self._thread_3 = Thread_3(**params)
        self.stop_all_signal.connect(self._thread_3.stop)
        self._thread_3.start()
        self._thread_3.trigger_current_data.connect(self.show_current_data_all)
        self._thread_3.trigger_na_connect.connect(self.na_except_connect)
        self._thread_3.trigger_set_voltage.connect(self.set_voltage_all)
        self.loop_state_all = 1
        if self.loop_state_ampl:
            self.start_all_button.setEnabled(False)
            self.stop_all_button.setEnabled(True)

    def get_common_params(self):
        """
        收集通用参数
        """
        params = {"na": self.network_address_input.text()}

        freq = self.freq_setter_input.text() or 16
        freq = float(freq)

        unit = self.freq_setter_unit.currentText()

        exponent = 0
        if unit == "GHz":
            exponent = 9
        elif unit == "MHz":
            exponent = 6
        elif unit == "KHz":
            exponent = 3

        freq = freq * pow(10, exponent)
        params["freq"] = freq

        time_space = self.interval_input.text() or 1
        time_space = int(time_space)
        params["time_interval"] = time_space
        self.ampl_route = int(self.ampl_control_route.currentText())
        return params

    def get_params_ampl(self):
        """
        收集用于调节振幅的参数
        """
        params = self.get_common_params()
        phase_control_voltage_init = self.phase_voltage_init_input.text() or 10
        phase_control_voltage_init = float(phase_control_voltage_init)
        params["phase_voltage_init"] = phase_control_voltage_init

        ampl_control_voltage_min = self.ampl_voltage_min_input.text() or 0
        ampl_control_voltage_min = float(ampl_control_voltage_min)
        params["ampl_voltage_min"] = ampl_control_voltage_min

        ampl_control_voltage_max = self.ampl_voltage_max_input.text() or 3
        ampl_control_voltage_max = float(ampl_control_voltage_max)
        params["ampl_voltage_max"] = ampl_control_voltage_min

        ampl_control_voltage_init = self.ampl_voltage_init_input.text() or 1.5
        ampl_control_voltage_init = float(ampl_control_voltage_init)

        if ampl_control_voltage_init > ampl_control_voltage_max:
            ampl_control_voltage_init = ampl_control_voltage_max
        if ampl_control_voltage_init < ampl_control_voltage_min:
            ampl_control_voltage_init = ampl_control_voltage_min
        params["ampl_voltage_init"] = ampl_control_voltage_init

        slope = self.slope_ampl_input.text() or 20
        slope = float(slope)
        params["slope_ampl"] = slope

        target_ampl = self.ampl_init_input.text() or 50
        target_ampl = float(target_ampl)
        params["target_ampl"] = target_ampl
        return params

    def get_params_phase(self):
        """
        收集用于调节相位的参数
        """
        params = self.get_common_params()
        ampl_control_voltage_init = self.ampl_voltage_init_input.text() or 1.5
        ampl_control_voltage_init = float(ampl_control_voltage_init)
        params["ampl_voltage_init"] = ampl_control_voltage_init

        phase_control_voltage_min = self.phase_voltage_min_input.text() or 0
        phase_control_voltage_min = float(phase_control_voltage_min)
        params["phase_voltage_min"] = phase_control_voltage_min

        phase_control_voltage_max = self.phase_voltage_max_input.text() or 20
        phase_control_voltage_max = float(phase_control_voltage_max)
        params["phase_voltage_max"] = phase_control_voltage_max

        phase_control_voltage_init = self.phase_voltage_init_input.text() or 10
        phase_control_voltage_init = float(phase_control_voltage_init)

        if phase_control_voltage_init > phase_control_voltage_max:
            phase_control_voltage_init = phase_control_voltage_max
        if phase_control_voltage_init < phase_control_voltage_min:
            phase_control_voltage_init = phase_control_voltage_min
        params["phase_voltage_init"] = phase_control_voltage_init

        slope = self.slope_phase_input.text() or 20
        slope = float(slope)
        params["slope_phase"] = slope

        target_phase = self.ampl_init_input.text() or 50
        target_phase = float(target_phase)
        params["target_phase"] = target_phase
        return params

    def show_current_data_phase(self, value):
        """
        将当前的电压和相位显示在面板上
        :param value:
        :return:
        """
        params = value.split("_")
        self.voltage_text.insertPlainText(
            "电压: {:0>5}  相位：{}\n".format(
                str("%.2f" % float(params[0])),
                float(params[1]),
            )
        )

    def show_current_data_ampl(self, value):
        """
        将当前的电压和振幅显示在面板上
        :param value:
        :return:
        """
        params = value.split("_")
        self.voltage_text.insertPlainText(
            "电压: {:0>5}  振幅：{}\n".format(
                str("%.2f" % float(params[0])),
                float(params[1])
            )
        )

    def show_current_data_all(self, value):
        """
        将当前的电压、相位以及振幅显示在面板上
        :param value:
        :return:
        """
        params = value.split("_")
        self.voltage_text.insertPlainText(
            "振幅电压:{:0>5} 振幅:{:0>6}  相位电压:{:0>5} 相位:{:0>6}\n".format(
                str("%.2f" % float(params[0])),
                str("%.2f" % float(params[1])),
                str("%.2f" % float(params[2])),
                str("%.2f" % float(params[3]))
            )
        )

    def set_voltage_phase(self, value):
        """
        设置电压源电压
        :param value:
        :return:
        """
        v1, v2 = value.split("_")[0], value.split("_")[1]
        message = package_voltage_message(self.ampl_route, float(v1), float(v2))
        try:
            self.ser.write(f"{message}\n".encode())
        except Exception as e:
            self.stop_phase_signal.emit()
            self.start_phase.setEnabled(True)
            self.stop_phase.setEnabled(False)
            if not self.ser.isOpen():
                QtWidgets.QMessageBox.critical(self, "port error", "电源串口未打开！")
            else:
                QtWidgets.QMessageBox.critical(self, "port error", str(e))

    def set_voltage_all(self, value):
        """
        设置电压源电压
        :param value:
        :return:
        """
        v1, v2 = value.split("_")[0], value.split("_")[1]
        message = package_voltage_message(self.ampl_route, float(v1), float(v2))
        try:
            self.ser.write(f"{message}\n".encode())
        except Exception as e:
            self.stop_all_signal.emit()
            self.start_all_button.setEnabled(True)
            self.stop_all_button.setEnabled(False)
            if not self.ser.isOpen():
                QtWidgets.QMessageBox.critical(self, "port error", "电源串口未打开！")
            else:
                QtWidgets.QMessageBox.critical(self, "port error", str(e))

    def set_voltage_ampl(self, value):
        """
        设置电压源电压
        :param value:
        :return:
        """
        v1, v2 = value.split("_")[0], value.split("_")[1]
        message = package_voltage_message(self.ampl_route, float(v1), float(v2))
        try:
            self.ser.write(f"{message}\n".encode())
        except Exception as e:
            self.stop_ampl_signal.emit()
            self.start_ampl.setEnabled(True)
            self.stop_ampl.setEnabled(False)
            if not self.ser.isOpen():
                QtWidgets.QMessageBox.critical(self, "port error", "电源串口未打开！")
            else:
                QtWidgets.QMessageBox.critical(self, "port error", str(e))

    def na_except_connect(self, value):
        """
        接受矢网连接异常信息，
        如果出现异常，则弹窗提示
        :param value:
        :return:
        """
        QtWidgets.QMessageBox.critical(self, "connect error", "网分连接有误，请确认IP地址正确！")
        if self.loop_state_ampl:
            self.loop_state_ampl = 0
            self.start_ampl.setEnabled(True)
            self.stop_ampl.setEnabled(False)
        if self.loop_state_phase:
            self.loop_state_phase = 0
            self.start_phase.setEnabled(True)
            self.stop_phase.setEnabled(False)
        if self.loop_state_all:
            self.loop_state_all = 0
            self.start_all_button.setEnabled(True)
            self.stop_all_button.setEnabled(False)

    def stop_phase_loop(self):
        """
        点击停止键，停止循环
        :return:
        """
        try:
            self.stop_phase_signal.emit()
        except Exception as e:
            pass
        self.start_phase.setEnabled(True)
        self.stop_phase.setEnabled(False)

    def stop_ampl_loop(self):
        """
        点击停止键，停止循环
        :return:
        """
        try:
            self.stop_ampl_signal.emit()
        except Exception as e:
            pass
        self.start_ampl.setEnabled(True)
        self.stop_ampl.setEnabled(False)

    def stop_all(self):
        """
        点击停止键，停止循环
        :return:
        """
        try:
            self.stop_all_signal.emit()
        except Exception as e:
            pass
        self.start_all_button.setEnabled(True)
        self.stop_all_button.setEnabled(False)


class Thread_1(QThread):  # 子线程
    """
    相位
    """
    trigger_current_data = pyqtSignal(str)
    trigger_set_voltage = pyqtSignal(str)
    trigger_na_connect = pyqtSignal(str)
    trigger_stop_flag = 1

    def __init__(self, **kwargs):
        """
        :param na: 矢网地址
        :param freq: 待测频率
        :param time_interval:每次测试时间间隔
        :param ampl_voltage_init: 振幅初始值
        :param phase_voltage_min: 相位电压最小值
        :param phase_voltage_max: 相位电压最大值
        :param phase_voltage_init: 相位电压初始值
        :param slope: 电压和相位线性关系斜率
        :param target_phase: 初始相位
        """
        super().__init__()
        for key, value in kwargs.items():
            setattr(self, key, value)

    def run(self):
        # 相位控制电压的初始值
        voltage = self.phase_voltage_init
        # 控制振幅电压初始值
        ampl_voltage = self.ampl_voltage_init

        # 将电压输出到电压源上
        self.trigger_set_voltage.emit("_".join([str(ampl_voltage), str(voltage)]))

        # 数据保存路径
        local_file = os.path.join(os.path.curdir, "data_files")
        file_name = os.path.join(local_file, "temp_phase.s2p")
        time.sleep(self.time_interval)
        try:
            # 连接矢网
            # 此处可修改矢网IP地址
            instrument = RsInstrument('TCPIP::{}::INSTR'.format(self.na), True, False)
        except Exception as e:
            self.trigger_na_connect.emit(str(e))
            return

        instrument.write_str(
            "MMEM:STOR:TRAC:CHAN 1,'RSC_interims.dat',UNF,LOGP,POIN,SEM")  # create data file in ZNB
        instrument.query_opc()
        instrument.read_file_from_instrument_to_pc('RSC_interims.dat', file_name)  # 从失网将数据复制到电脑

        # 获取待测频率在数据文件中的哪一行
        row = get_row(self.freq, file_name)

        # 取出对应行的相位
        phase_current = get_current_value(file_name, row, 2)
        # 将当前电压和相位发送给主线程，用于实时显示
        self.trigger_current_data.emit("_".join([str(voltage), str(phase_current)]))

        while True:
            if not self.trigger_stop_flag:  # 判断停止按钮
                return
            # 求下一个电压值
            voltage = get_next_voltage(voltage, self.target_phase, phase_current, self.slope_phase)
            # 如果电压大于最大值，则从最小值开始
            if voltage > self.phase_voltage_max:
                voltage = self.phase_voltage_min

            # 如果电压小于最小值，则从最大值开始
            if voltage < self.phase_voltage_min:
                voltage = self.phase_voltage_max

            # 将下一个电压发送给主线程，让主线程设置电源
            self.trigger_set_voltage.emit("_".join([str(ampl_voltage), str(voltage)]))
            # 等待
            time.sleep(self.time_interval)

            # 从矢网获取数据
            instrument.write_str(
                "MMEM:STOR:TRAC:CHAN 1,'RSC_interims.dat',UNF,LOGP,POIN,SEM")  # create data file in ZNB
            instrument.query_opc()
            instrument.read_file_from_instrument_to_pc('RSC_interims.dat', file_name)  # 从失网将数据复制到电脑

            # 从数据文件中读取相位值
            phase_current = get_current_value(file_name, row, 2)
            self.trigger_current_data.emit("_".join([str(voltage), str(phase_current)]))

    def stop(self):
        """
        停止信号
        :return:
        """
        self.trigger_stop_flag = 0


class Thread_2(QThread):  # 子线程
    """
    振幅
    """
    trigger_current_data = pyqtSignal(str)
    trigger_set_voltage = pyqtSignal(str)
    trigger_na_connect = pyqtSignal(str)
    trigger_stop_flag = 1

    def __init__(self, **kwargs):
        """
        :param freq: 待测频率
        :param time_interval:每次测试时间间隔
        :param target_ampl: 初始振幅，最终要达到的值
        :param ampl_voltage_max: 振幅电压最大值
        :param phase_voltage_init: 相位电压设置
        :param ampl_voltage_init: 振幅电压初始值
        :param ampl_voltage_min: 振幅电压最小值
        :param slope: 电压和振幅线性关系斜率
        """
        super().__init__()
        for key, value in kwargs.items():
            setattr(self, key, value)

    def run(self):

        # 控制振幅的电压初始值
        voltage_ampl = self.ampl_voltage_init
        # 控制相位的电压初始值
        voltage_phase = self.phase_voltage_init

        # 将电压输出到电压源上
        self.trigger_set_voltage.emit("_".join([str(voltage_ampl), str(voltage_phase)]))

        # 数据保存路径
        local_file = os.path.join(os.path.curdir, "data_files")
        file_name = os.path.join(local_file, "temp_ampl.s2p")
        time.sleep(self.time_interval)
        try:
            # 连接矢网
            # 此处可修改矢网IP地址
            instrument = RsInstrument('TCPIP::{}::INSTR'.format(self.na), True, False)
        except Exception as e:
            self.trigger_na_connect.emit(str(e))
            return

        instrument.write_str(
            "MMEM:STOR:TRAC:CHAN 1,'RSC_interims.dat',UNF,LOGP,POIN,SEM")
        instrument.query_opc()
        instrument.read_file_from_instrument_to_pc('RSC_interims.dat', file_name)  # 从失网将数据复制到电脑

        # 获取待测频率在数据文件中的哪一行
        row = get_row(self.freq, file_name)

        # 取出对应行的振幅
        ampl_current = get_current_value(file_name, row, 1)
        # 将当前电压和振幅发送给主线程，用于实时显示
        self.trigger_current_data.emit("_".join([str(voltage_ampl), str(ampl_current)]))

        while True:
            if not self.trigger_stop_flag:  # 判断停止按钮
                return
            # 求下一个电压值
            voltage_ampl = get_next_voltage_ampl(voltage_ampl, self.target_ampl, ampl_current, self.slope_ampl)
            # 如果电压大于最大值，则从最小值开始
            if voltage_ampl > self.ampl_voltage_max:
                voltage_ampl = self.ampl_voltage_min

            # 如果电压小于最小值，则从最大值开始
            if voltage_ampl < self.ampl_voltage_min:
                voltage_ampl = self.ampl_voltage_max

            # 将下一个电压发送给主线程，让主线程设置电源
            self.trigger_set_voltage.emit("_".join([str(voltage_ampl), str(voltage_phase)]))
            # 等待
            time.sleep(self.time_interval)

            # 从矢网获取数据
            instrument.write_str(
                "MMEM:STOR:TRAC:CHAN 1,'RSC_interims.dat',UNF,LOGP,POIN,SEM")  # create data file in ZNB
            instrument.query_opc()
            instrument.read_file_from_instrument_to_pc('RSC_interims.dat', file_name)  # 从失网将数据复制到电脑

            # 从数据文件中读取相位值
            ampl_current = get_current_value(file_name, row, 1)
            self.trigger_current_data.emit("_".join([str(voltage_ampl), str(ampl_current)]))

    def stop(self):
        """
        停止信号
        :return:
        """
        self.trigger_stop_flag = 0


class Thread_3(QThread):  # 子线程
    """
    振幅
    """
    trigger_current_data = pyqtSignal(str)
    trigger_set_voltage = pyqtSignal(str)
    trigger_na_connect = pyqtSignal(str)
    trigger_stop_flag = 1

    def __init__(self, **kwargs):
        """
        :param freq: 待测频率
        :param time_interval:每次测试时间间隔
        :param target_ampl: 初始振幅，
        :param target_phase:初始相位，
        :param ampl_voltage_max: 振幅电压最大值
        :param phase_voltage_max: 相位电压最大值
        :param phase_voltage_init: 相位电压设置
        :param ampl_voltage_init: 振幅电压设置
        :param ampl_voltage_init: 振幅电压初始值
        :param phase_voltage_init: 相位电压初始值
        :param ampl_voltage_min: 振幅电压最小值
        :param phase_voltage_min: 相位电压最小值
        :param slope_ampl: 电压和振幅线性关系斜率
        :param slope_phase: 电压和相位线性关系斜率
        """
        super().__init__()
        for key, value in kwargs.items():
            setattr(self, key, value)

    def run(self):

        # 控制振幅的电压初始值
        voltage_ampl = self.ampl_voltage_init
        # 控制相位的电压初始值
        voltage_phase = self.phase_voltage_init

        # 将电压输出到电压源上
        self.trigger_set_voltage.emit("_".join([str(voltage_ampl), str(voltage_phase)]))

        # 数据保存路径
        local_file = os.path.join(os.path.curdir, "data_files")
        file_name = os.path.join(local_file, "temp_all.s2p")
        time.sleep(self.time_interval)
        try:
            # 连接矢网
            # 此处可修改矢网IP地址
            instrument = RsInstrument('TCPIP::{}::INSTR'.format(self.na), True, False)
        except Exception as e:
            self.trigger_na_connect.emit(str(e))
            return

        instrument.write_str(
            "MMEM:STOR:TRAC:CHAN 1,'RSC_interims.dat',UNF,LOGP,POIN,SEM")
        instrument.query_opc()
        instrument.read_file_from_instrument_to_pc('RSC_interims.dat', file_name)  # 从失网将数据复制到电脑
        instrument.query_opc()

        # 获取待测频率在数据文件中的哪一行
        row = get_row(self.freq, file_name)

        # 取出对应行的振幅
        ampl_current = get_current_value(file_name, row, 1)
        phase_current = get_current_value(file_name, row, 2)
        # 将当前电压和振幅发送给主线程，用于实时显示
        self.trigger_current_data.emit("_".join([str(voltage_ampl),
                                                 str(ampl_current),
                                                 str(voltage_phase),
                                                 str(phase_current)]))

        while True:
            if not self.trigger_stop_flag:  # 判断停止按钮
                return
            # 求下一个电压值
            voltage_ampl = get_next_voltage_ampl(voltage_ampl, self.target_ampl, ampl_current, self.slope_ampl)
            voltage_phase = get_next_voltage(voltage_phase, self.target_phase, phase_current, self.slope_phase)
            # 振幅电压大于最大值，则从最小值开始
            if voltage_ampl > self.ampl_voltage_max:
                voltage_ampl = self.ampl_voltage_min

            # 振幅电压小于最小值，则从最大值开始
            if voltage_ampl < self.ampl_voltage_min:
                voltage_ampl = self.ampl_voltage_max

            # 相位电压大于最大值，则变为最小值
            if voltage_phase > self.phase_voltage_max:
                voltage_phase = self.phase_voltage_min

            # 相位电压小于最小值，则变为最大值
            if voltage_phase < self.phase_voltage_min:
                voltage_phase = self.phase_voltage_max

            # 将下一个电压发送给主线程，让主线程设置电源
            self.trigger_set_voltage.emit("_".join([str(voltage_ampl), str(voltage_phase)]))
            # 等待
            time.sleep(self.time_interval)

            # 从矢网获取数据
            instrument.write_str(
                "MMEM:STOR:TRAC:CHAN 1,'RSC_interims.dat',UNF,LOGP,POIN,SEM")  # create data file in ZNB
            instrument.query_opc()
            instrument.read_file_from_instrument_to_pc('RSC_interims.dat', file_name)  # 从失网将数据复制到电脑
            instrument.query_opc()

            # 从数据文件中读取振幅相位
            ampl_current = get_current_value(file_name, row, 1)
            phase_current = get_current_value(file_name, row, 2)
            # 将当前电压和振幅发送给主线程，用于实时显示
            self.trigger_current_data.emit("_".join([str(voltage_ampl),
                                                     str(ampl_current),
                                                     str(voltage_phase),
                                                     str(phase_current)]))

    def stop(self):
        """
        停止信号
        :return:
        """
        self.trigger_stop_flag = 0


if __name__ == '__main__':
    if hasattr(Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

    if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    app = QtWidgets.QApplication(sys.argv)
    myshow = Assistant()
    myshow.show()
    sys.exit(app.exec_())
