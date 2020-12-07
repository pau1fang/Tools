from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(850, 490)

        self.formGroupBox = QtWidgets.QGroupBox(Form)
        self.formGroupBox.setGeometry(QtCore.QRect(20, 180, 171, 150))
        self.formGroupBox.setObjectName("formGroupBox")
        self.formLayout = QtWidgets.QFormLayout(self.formGroupBox)

        self.formGroupBoxState = QtWidgets.QGroupBox(Form)
        self.formGroupBoxState.setGeometry(QtCore.QRect(20, 20, 171, 155))
        self.formGroupBoxState.setObjectName("formGroupBoxState")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formGroupBoxState)

        self.formGroupBoxAll = QtWidgets.QGroupBox(Form)
        self.formGroupBoxAll.setGeometry(QtCore.QRect(20, 335, 171, 120))
        self.formGroupBoxAll.setObjectName("formGroupBoxAll")
        self.formLayout_all = QtWidgets.QFormLayout(self.formGroupBoxAll)

        self.formGroupBoxPhase = QtWidgets.QGroupBox(Form)
        self.formGroupBoxPhase.setGeometry(QtCore.QRect(660, 240, 171, 215))
        self.formGroupBoxPhase.setObjectName("formGroupBoxPhase")
        self.formLayout_phase = QtWidgets.QFormLayout(self.formGroupBoxPhase)

        self.formGroupBoxAmpl = QtWidgets.QGroupBox(Form)
        self.formGroupBoxAmpl.setGeometry(QtCore.QRect(660, 20, 171, 215))
        self.formGroupBoxAmpl.setObjectName("formGroupBoxAmpl")
        self.formLayout_ampl = QtWidgets.QFormLayout(self.formGroupBoxAmpl)

        self.verticalGroupBox = QtWidgets.QGroupBox(Form)
        self.verticalGroupBox.setGeometry(QtCore.QRect(200, 20, 451, 435))
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")

        self.network_address = QtWidgets.QLabel(self.formGroupBoxState)
        self.network_address.setObjectName("network_address")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.network_address)

        self.network_address_input = QtWidgets.QLineEdit(self.formGroupBoxState)
        self.network_address_input.setObjectName("network_address_input")
        self.network_address_input.setInputMask('999.999.9.999')
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.network_address_input)

        self.voltage_source = QtWidgets.QLabel(self.formGroupBoxState)
        self.voltage_source.setObjectName("voltage_source")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.voltage_source)

        self.voltage_source_input = QtWidgets.QComboBox(self.formGroupBoxState)
        self.voltage_source_input.setObjectName("voltage_source_input")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.voltage_source_input)

        self.state_label = QtWidgets.QLabel(self.formGroupBoxState)
        self.state_label.setText("")
        self.state_label.setTextFormat(QtCore.Qt.AutoText)
        self.state_label.setScaledContents(True)
        self.state_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.state_label.setObjectName("state_label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.state_label)

        self.voltage_button = QtWidgets.QPushButton(self.formGroupBoxState)
        self.voltage_button.setObjectName("voltage_button")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.voltage_button)

        self.voltage_close_button = QtWidgets.QPushButton(self.formGroupBoxState)
        self.voltage_close_button.setObjectName("voltage_close_button")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.voltage_close_button)

        self.freq_setter = QtWidgets.QLabel(self.formGroupBox)
        self.freq_setter.setObjectName("freq_setter")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.freq_setter)

        self.freq_setter_input = QtWidgets.QLineEdit(self.formGroupBox)
        self.freq_setter_input.setObjectName("freq_setter_input")
        self.freq_setter_input.setValidator(QtGui.QDoubleValidator())
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.freq_setter_input)

        self.freq_setter_unit = QtWidgets.QComboBox(self.formGroupBox)
        self.freq_setter_unit.setObjectName("freq_setter_unit")
        self.freq_setter_unit.addItem("")
        self.freq_setter_unit.addItem("")
        self.freq_setter_unit.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.freq_setter_unit)

        # 导入txt文件时间间隔
        self.interval = QtWidgets.QLabel(self.formGroupBox)
        self.interval.setObjectName("interval")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.interval)

        self.interval_input = QtWidgets.QLineEdit(self.formGroupBox)
        self.interval_input.setObjectName("interval_input")
        self.interval_input.setValidator(QtGui.QIntValidator())
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.interval_input)

        # 振幅控制选择
        self.ampl_control = QtWidgets.QLabel(self.formGroupBox)
        self.ampl_control.setObjectName("ampl_control")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.ampl_control)

        self.ampl_control_route = QtWidgets.QComboBox(self.formGroupBox)
        self.ampl_control_route.setObjectName("ampl_control_route")
        self.ampl_control_route.addItem("")
        self.ampl_control_route.addItem("")
        self.ampl_control_route.addItem("")
        self.ampl_control_route.addItem("")
        self.ampl_control_route.addItem("")
        self.ampl_control_route.addItem("")
        self.ampl_control_route.addItem("")
        self.ampl_control_route.addItem("")
        self.ampl_control_route.addItem("")
        self.ampl_control_route.addItem("")
        self.ampl_control_route.addItem("")
        self.ampl_control_route.addItem("")
        self.ampl_control_route.addItem("")
        self.ampl_control_route.addItem("")
        self.ampl_control_route.addItem("")
        self.ampl_control_route.addItem("")
        self.ampl_control_route.addItem("")
        self.ampl_control_route.addItem("")
        self.ampl_control_route.addItem("")
        self.ampl_control_route.addItem("")
        self.ampl_control_route.addItem("")
        self.ampl_control_route.addItem("")
        self.ampl_control_route.addItem("")
        self.ampl_control_route.addItem("")
        self.ampl_control_route.addItem("")
        self.ampl_control_route.addItem("")
        self.ampl_control_route.addItem("")
        self.ampl_control_route.addItem("")
        self.ampl_control_route.addItem("")
        self.ampl_control_route.addItem("")
        self.ampl_control_route.addItem("")
        self.ampl_control_route.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.ampl_control_route)

        self.data_clear_button = QtWidgets.QPushButton(self.formGroupBoxAll)
        self.data_clear_button.setObjectName("data_clear_button")
        self.formLayout_all.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.data_clear_button)

        # 开始按钮(相位和振幅)
        self.start_all_button = QtWidgets.QPushButton(self.formGroupBoxAll)
        self.start_all_button.setObjectName("start_all_button")
        self.formLayout_all.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.start_all_button)

        # 停止按钮(相位和振幅)
        self.stop_all_button = QtWidgets.QPushButton(self.formGroupBoxAll)
        self.stop_all_button.setObjectName("stop_all_button")
        self.formLayout_all.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.stop_all_button)

        self.phase_voltage_min = QtWidgets.QLabel(self.formGroupBox)
        self.phase_voltage_min.setObjectName("phase_voltage_min")
        self.formLayout_phase.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.phase_voltage_min)

        self.phase_voltage_min_input = QtWidgets.QLineEdit(self.formGroupBox)
        self.phase_voltage_min_input.setObjectName("phase_voltage_min_input")
        self.phase_voltage_min_input.setValidator(QtGui.QDoubleValidator())
        self.formLayout_phase.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.phase_voltage_min_input)

        self.phase_voltage_max = QtWidgets.QLabel(self.formGroupBox)
        self.phase_voltage_max.setObjectName("phase_voltage_max")
        self.formLayout_phase.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.phase_voltage_max)

        self.phase_voltage_max_input = QtWidgets.QLineEdit(self.formGroupBox)
        self.phase_voltage_max_input.setObjectName("phase_voltage_max_input")
        self.phase_voltage_max_input.setValidator(QtGui.QDoubleValidator())
        self.formLayout_phase.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.phase_voltage_max_input)

        # 控制相位初始电压
        self.phase_voltage_init = QtWidgets.QLabel(self.formGroupBox)
        self.phase_voltage_init.setObjectName("phase_voltage_init")
        self.formLayout_phase.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.phase_voltage_init)

        self.phase_voltage_init_input = QtWidgets.QLineEdit(self.formGroupBox)
        self.phase_voltage_init_input.setObjectName("phase_voltage_init_input")
        self.phase_voltage_init_input.setValidator(QtGui.QDoubleValidator())
        self.formLayout_phase.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.phase_voltage_init_input)

        # 斜率设置_相位
        self.slope_phase = QtWidgets.QLabel(self.formGroupBoxAmpl)
        self.slope_phase.setObjectName("slope_phase")
        self.formLayout_phase.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.slope_phase)

        self.slope_phase_input = QtWidgets.QLineEdit(self.formGroupBoxAmpl)
        self.slope_phase_input.setObjectName("slope_phase_input")
        self.slope_phase_input.setValidator(QtGui.QDoubleValidator())
        self.formLayout_phase.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.slope_phase_input)

        # 初始相位
        self.phase_init = QtWidgets.QLabel(self.formGroupBoxAmpl)
        self.phase_init.setObjectName("phase_init")
        self.formLayout_phase.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.phase_init)

        self.phase_init_input = QtWidgets.QLineEdit(self.formGroupBoxAmpl)
        self.phase_init_input.setObjectName("phase_init_input")
        self.phase_init_input.setValidator(QtGui.QDoubleValidator())
        self.formLayout_phase.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.phase_init_input)

        # 开始按钮(相位)
        self.start_phase = QtWidgets.QPushButton(self.formGroupBoxAmpl)
        self.start_phase.setObjectName("start_phase")
        self.formLayout_phase.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.start_phase)

        # 停止按钮(相位)
        self.stop_phase = QtWidgets.QPushButton(self.formGroupBoxAmpl)
        self.stop_phase.setObjectName("stop_button")
        self.formLayout_phase.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.stop_phase)

        self.ampl_voltage_min = QtWidgets.QLabel(self.formGroupBox)
        self.ampl_voltage_min.setObjectName("ampl_voltage_min")
        self.formLayout_ampl.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ampl_voltage_min)

        self.ampl_voltage_min_input = QtWidgets.QLineEdit(self.formGroupBox)
        self.ampl_voltage_min_input.setObjectName("ampl_voltage_min_input")
        self.ampl_voltage_min_input.setValidator(QtGui.QDoubleValidator())
        self.formLayout_ampl.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ampl_voltage_min_input)

        self.ampl_voltage_max = QtWidgets.QLabel(self.formGroupBox)
        self.ampl_voltage_max.setObjectName("ampl_voltage_max")
        self.formLayout_ampl.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.ampl_voltage_max)

        self.ampl_voltage_max_input = QtWidgets.QLineEdit(self.formGroupBox)
        self.ampl_voltage_max_input.setObjectName("ampl_voltage_max_input")
        self.ampl_voltage_max_input.setValidator(QtGui.QDoubleValidator())
        self.formLayout_ampl.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ampl_voltage_max_input)

        # 控制振幅初始电压
        self.ampl_voltage_init = QtWidgets.QLabel(self.formGroupBox)
        self.ampl_voltage_init.setObjectName("ampl_voltage_init")
        self.formLayout_ampl.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.ampl_voltage_init)

        self.ampl_voltage_init_input = QtWidgets.QLineEdit(self.formGroupBox)
        self.ampl_voltage_init_input.setObjectName("ampl_voltage_init_input")
        self.ampl_voltage_init_input.setValidator(QtGui.QDoubleValidator())
        self.formLayout_ampl.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ampl_voltage_init_input)

        # 斜率设置_相位
        self.slope_ampl = QtWidgets.QLabel(self.formGroupBoxAmpl)
        self.slope_ampl.setObjectName("slope_ampl")
        self.formLayout_ampl.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.slope_ampl)

        self.slope_ampl_input = QtWidgets.QLineEdit(self.formGroupBoxAmpl)
        self.slope_ampl_input.setObjectName("slope_ampl_input")
        self.slope_ampl_input.setValidator(QtGui.QDoubleValidator())
        self.formLayout_ampl.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.slope_ampl_input)

        # 初始相位
        self.ampl_init = QtWidgets.QLabel(self.formGroupBoxAmpl)
        self.ampl_init.setObjectName("ampl_init")
        self.formLayout_ampl.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.ampl_init)

        self.ampl_init_input = QtWidgets.QLineEdit(self.formGroupBoxAmpl)
        self.ampl_init_input.setObjectName("ampl_init_input")
        self.ampl_init_input.setValidator(QtGui.QDoubleValidator())
        self.formLayout_ampl.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.ampl_init_input)

        # 开始按钮(相位)
        self.start_ampl = QtWidgets.QPushButton(self.formGroupBoxAmpl)
        self.start_ampl.setObjectName("start_ampl")
        self.formLayout_ampl.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.start_ampl)

        # 停止按钮(相位)
        self.stop_ampl = QtWidgets.QPushButton(self.formGroupBoxAmpl)
        self.stop_ampl.setObjectName("stop_ampl")
        self.formLayout_ampl.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.stop_ampl)

        # 电压输出
        self.voltage_text = QtWidgets.QTextBrowser(self.verticalGroupBox)
        self.voltage_text.setObjectName("voltage_text")
        self.verticalLayout.addWidget(self.voltage_text)

        # self.label_1 = QtWidgets.QLabel(self.formGroupBoxAmpl)
        # self.label_1.setObjectName("label_1")
        # self.formLayout.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.label_1)

        self.formGroupBox_1 = QtWidgets.QGroupBox(Form)
        self.formGroupBox_1.setGeometry(QtCore.QRect(190, 460, 561, 30))
        self.formGroupBox_1.setContentsMargins(0,0,0,0)
        self.formGroupBox_1.setStyleSheet("border:0px")
        self.formGroupBox_1.setObjectName("formGroupBox_1")
        self.formLayout_ampl = QtWidgets.QFormLayout(self.formGroupBox_1)

        self.designer_lb = QtWidgets.QLabel(self.formGroupBox_1)
        self.designer_lb.setObjectName("designer_lb")
        self.designer_lb.setAlignment(QtCore.Qt.AlignVCenter)
        self.formLayout_ampl.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.designer_lb)

        self.verticalGroupBox.raise_()
        self.formGroupBox.raise_()
        self.formGroupBoxState.raise_()
        self.formGroupBox_1.raise_()
        self.formGroupBoxPhase.raise_()
        self.formGroupBoxAll.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

        self.formGroupBoxState.setTitle(_translate("Form", "仪器连接设置"))
        self.network_address.setText(_translate("Form", "矢网地址:"))
        self.network_address_input.setText(_translate("Form", "192.168.1.49"))
        self.voltage_source.setText(_translate("Form", "电源串口:"))
        self.voltage_button.setText(_translate("Form", "打开电压源串口"))
        self.voltage_close_button.setText(_translate("Form", "关闭电压源串口"))

        self.formGroupBox.setTitle(_translate("Form", "参数设置"))
        self.freq_setter.setText(_translate("Form", "待测频率:"))
        self.freq_setter_input.setText(_translate("Form", "16"))
        self.freq_setter_unit.setItemText(0, _translate("Form", "GHz"))
        self.freq_setter_unit.setItemText(1, _translate("Form", "MHz"))
        self.freq_setter_unit.setItemText(2, _translate("Form", "KHz"))
        self.interval.setText(_translate("Form", "时间间隔(s):"))
        self.interval_input.setText(_translate("Form", "2"))
        self.ampl_control.setText(_translate("Form", "振幅控制路:"))
        self.ampl_control_route.setItemText(0, _translate("Form", "1"))
        self.ampl_control_route.setItemText(1, _translate("Form", "2"))
        self.ampl_control_route.setItemText(2, _translate("Form", "3"))
        self.ampl_control_route.setItemText(3, _translate("Form", "4"))
        self.ampl_control_route.setItemText(4, _translate("Form", "5"))
        self.ampl_control_route.setItemText(5, _translate("Form", "6"))
        self.ampl_control_route.setItemText(6, _translate("Form", "7"))
        self.ampl_control_route.setItemText(7, _translate("Form", "8"))
        self.ampl_control_route.setItemText(8, _translate("Form", "9"))
        self.ampl_control_route.setItemText(9, _translate("Form", "10"))
        self.ampl_control_route.setItemText(10, _translate("Form", "11"))
        self.ampl_control_route.setItemText(11, _translate("Form", "12"))
        self.ampl_control_route.setItemText(12, _translate("Form", "13"))
        self.ampl_control_route.setItemText(13, _translate("Form", "14"))
        self.ampl_control_route.setItemText(14, _translate("Form", "15"))
        self.ampl_control_route.setItemText(15, _translate("Form", "16"))
        self.ampl_control_route.setItemText(16, _translate("Form", "17"))
        self.ampl_control_route.setItemText(17, _translate("Form", "18"))
        self.ampl_control_route.setItemText(18, _translate("Form", "19"))
        self.ampl_control_route.setItemText(19, _translate("Form", "20"))
        self.ampl_control_route.setItemText(20, _translate("Form", "21"))
        self.ampl_control_route.setItemText(21, _translate("Form", "22"))
        self.ampl_control_route.setItemText(22, _translate("Form", "23"))
        self.ampl_control_route.setItemText(23, _translate("Form", "24"))
        self.ampl_control_route.setItemText(24, _translate("Form", "25"))
        self.ampl_control_route.setItemText(25, _translate("Form", "26"))
        self.ampl_control_route.setItemText(26, _translate("Form", "27"))
        self.ampl_control_route.setItemText(27, _translate("Form", "28"))
        self.ampl_control_route.setItemText(28, _translate("Form", "29"))
        self.ampl_control_route.setItemText(29, _translate("Form", "30"))
        self.ampl_control_route.setItemText(30, _translate("Form", "31"))
        self.ampl_control_route.setItemText(31, _translate("Form", "32"))
        # self.label_1.setText(_translate("Form", "指导说明：\n"
        #                                         "1.请设置正确的矢网IP地址；\n"
        #                                         "2.请确保电源驱动正常使用；\n"
        #                                         "3.在实验中请输入合适的斜\n"
        #                                         "  率, 太小电压不会收敛，\n"
        #                                         "  太大电压收敛的速度变慢\n"
        #                                         "4.点击开始后，程序不会自\n"
        #                                         "  动停止，需在电压趋于稳\n"
        #                                         "  定后点击停止按钮。\n"))

        self.formGroupBoxAll.setTitle(_translate("Form", "相位和振幅同时回调"))
        self.data_clear_button.setText(_translate("Form", "清除数据"))
        self.start_all_button.setText(_translate("Form", "开始"))
        self.stop_all_button.setText(_translate("Form", "停止"))

        self.verticalGroupBox.setTitle(_translate("Form", "实时数据显示"))

        self.formGroupBoxAmpl.setTitle(_translate("Form", "振幅"))
        self.ampl_voltage_min.setText(_translate("Form", "最小值:"))
        self.ampl_voltage_min_input.setText(_translate("Form", "0"))
        self.ampl_voltage_max.setText(_translate("Form", "最大值:"))
        self.ampl_voltage_max_input.setText(_translate("Form", "3"))
        self.ampl_voltage_init.setText(_translate("Form", "初始值:"))
        self.ampl_voltage_init_input.setText(_translate("Form", "1.5"))
        self.slope_ampl.setText(_translate("Form", "斜率设置:"))
        self.slope_ampl_input.setText(_translate("Form", "20"))
        self.ampl_init.setText(_translate("Form", "初始振幅:"))
        self.ampl_init_input.setText(_translate("Form", "10"))
        self.start_ampl.setText(_translate("Form", "开始"))
        self.stop_ampl.setText(_translate("Form", "停止"))

        self.formGroupBoxPhase.setTitle(_translate("Form", "相位"))
        self.phase_voltage_min.setText(_translate("Form", "最小值:"))
        self.phase_voltage_min_input.setText(_translate("Form", "0"))
        self.phase_voltage_max.setText(_translate("Form", "最大值:"))
        self.phase_voltage_max_input.setText(_translate("Form", "20"))
        self.phase_voltage_init.setText(_translate("Form", "初始值:"))
        self.phase_voltage_init_input.setText(_translate("Form", "10"))
        self.slope_phase.setText(_translate("Form", "斜率设置:"))
        self.slope_phase_input.setText(_translate("Form", "20"))
        self.phase_init.setText(_translate("Form", "初始相位:"))
        self.phase_init_input.setText(_translate("Form", "50"))
        self.start_phase.setText(_translate("Form", "开始"))
        self.stop_phase.setText(_translate("Form", "停止"))

        self.designer_lb.setText(_translate("Form", "©2021 paulfang"))
