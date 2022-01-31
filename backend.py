import pandas as pd
from sqlalchemy.dialects.mysql import pymysql
import pymysql

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt, QAbstractTableModel, QSize


# Set Data Frame ANd Make Qabstract Table Model
class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def size(self):
        return [self._data.shape[0], self._data.shape[1]]

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None
    #


class Backend:
    # From SQL server Get Data and make  Dictionaries
    """
    self.data_list = Dictionaries, there are all pandas data frame BY DB DATA
    self.lists = List, There are all DB Names
    self.key_data_dict = Dictionaries, There are all key columns name from DB and them Columns
    """

    def __init__(self):
        self.key_colum_parent = None
        self.shift_type_data = None
        self.shift_data = None
        self.staff_data = None
        self.key_data_dict = None
        self.lists = None
        self.service_data = None
        self.hospital_room_type_data = None
        self.hospital_room_data = None
        self.patient_history_data = None
        self.patient_data = None
        self.gender_data = None
        self.doctor_data = None
        self.department_type_data = None
        self.department_data = None
        self.data_list = None
        self.index = None
        self.line = None
        self.table = None
        self.list = None
        self.fream_1 = None
        self.answer_list = None
        self.id = None
        self.data_show = None
        self.columns_list = None
        self.error = None
        self.gridLayout_3 = None
        self.textBrowser = None
        self.check_box = None
        self.label = None
        self.frame = None
        self.gridLayout_2 = None
        self.frame_2 = None
        self.formLayout = None
        self.gridLayout = None
        self.nameLabel = None
        self.text = None
        self.page = None

    def update(self):
        self.data_list = {}
        connection = pymysql.connect(host="127.0.0.1", user="root", passwd="", db="hospital")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM Hospital_Department")
        self.department_data = pd.DataFrame(cursor.fetchall(), columns=["Department_Id", "Name", "Description", "Level",
                                                                        "Type_Number_Id", "Parent_Department"])

        cursor.execute("SELECT * FROM Hospital_Type_Department")
        self.department_type_data = pd.DataFrame(cursor.fetchall(), columns=["Type_Number_Id", "Name"])

        cursor.execute("SELECT Hospital_Doctor.Specalization,Hospital_Doctor.Biographical_Data, "
                       "Hospital_Doctor.Doctor_Id, Hospital_Doctor.Staf_Id, Hospital_Doctor.Type_Room, "
                       "Hospital_Staff.Name, Hospital_Staff.Lastname FROM Hospital_Staff RIGHT OUTER JOIN "
                       "Hospital_Doctor ON Hospital_Doctor.Staf_Id=Hospital_Staff.Staff_Id;")
        self.doctor_data = pd.DataFrame(cursor.fetchall(), columns=["Specialization", "Biographical_Data",
                                                                    "Doctor_Id", "Staff_Id", "Type_Room", "Name",
                                                                    "Lastname"])
        # self.doctor_data.inse

        cursor.execute("SELECT * FROM Hospital_Gender")
        self.gender_data = pd.DataFrame(cursor.fetchall(), columns=["Gender_Type", "Sex"])

        cursor.execute("SELECT * FROM Hospital_Patient")
        self.patient_data = pd.DataFrame(cursor.fetchall(), columns=["Patient_Id", "Patient_Name", "Patient_Lastname",
                                                                     "Birthdate", "Patient_Gender", "Address",
                                                                     "Blood_Type", "Patient_History_Id"])

        cursor.execute("SELECT * FROM Hospital_Patient_History")
        self.patient_history_data = pd.DataFrame(cursor.fetchall(), columns=["Patient_History_Id", "Date_Of_Application"
            , "Complains", "Admission_Doctor",
                                                                             "Services_Provided", "Date_Of_Discharge",
                                                                             "Sick", "Hospital_Room", "Department_Id"])

        cursor.execute("SELECT Hospital_Room.Hospital_Room_Id, Hospital_Room.Room_Name, Hospital_Room.Doctor_Assistant,"
                       "Hospital_Room.Department_Id, Hospital_Department.Name, Hospital_Room.Description FROM "
                       "Hospital_Department RIGHT OUTER JOIN Hospital_Room ON "
                       "Hospital_Room.Department_Id=Hospital_Department.Department_Id; ")
        self.hospital_room_data = pd.DataFrame(cursor.fetchall(), columns=["Hospital_Room_Id", "Room_Name",
                                                                           "Doctor_Assistant", "Department_Id", "Name",
                                                                           "Description"])

        cursor.execute("SELECT * FROM Hospital_Room_Type")
        self.hospital_room_type_data = pd.DataFrame(cursor.fetchall(), columns=["Room_Name", "Type_Room"])

        cursor.execute("SELECT Hospital_Service.Service_Id, Hospital_Service.Price, Hospital_Service.Name, "
                       "Hospital_Service.Department_Id, Hospital_Department.Name FROM Hospital_Department "
                       "RIGHT OUTER JOIN Hospital_Service ON "
                       "Hospital_Service.Department_Id=Hospital_Department.Department_Id; ")
        self.service_data = pd.DataFrame(cursor.fetchall(), columns=["Service_Id", "Price", "Name", "Department_Id",
                                                                     "Department_Name"])

        cursor.execute("SELECT * FROM Hospital_Shift")
        self.shift_data = pd.DataFrame(cursor.fetchall(), columns=["Shift_Id", "Department_Id", "Staff_Id",
                                                                   "Type_Of_Shift_Id", "Schedule"])

        cursor.execute("SELECT * FROM Hospital_Shift_Type")
        self.shift_type_data = pd.DataFrame(cursor.fetchall(), columns=["Type_Of_Shift_Id", "Shift_Name"])

        cursor.execute("SELECT Hospital_Staff.Staff_Id, Hospital_Staff.Name, Hospital_Staff.Lastname, "
                       "Hospital_Staff.Birthdate, Hospital_Staff.Address,Hospital_Staff.Position, "
                       "Hospital_Staff.Department_Id, Hospital_Department.Name, Hospital_Staff.Gender_Type "
                       "FROM Hospital_Department RIGHT OUTER JOIN Hospital_Staff ON "
                       "Hospital_Staff.Department_Id=Hospital_Department.Department_Id;")
        self.staff_data = pd.DataFrame(cursor.fetchall(), columns=["Staff_Id", "Name", "Lastname", "Birthdate",
                                                                   "Address", "Position", "Department_Id",
                                                                   "Department Name", "Gender_Type"])
        cursor.close()

        self.data_list["Hospital_Department"] = self.department_data
        self.data_list["Hospital_Service"] = self.service_data
        self.data_list["Hospital_Staff"] = self.staff_data
        self.data_list["Hospital_Patient"] = self.patient_data
        self.data_list["Hospital_Room"] = self.hospital_room_data
        self.data_list["Hospital_Shift"] = self.shift_data
        self.data_list["Hospital_Patient_History"] = self.patient_history_data
        self.data_list["Hospital_Doctor"] = self.doctor_data

        self.lists = ['Hospital_Department', 'Hospital_Service', 'Hospital_Staff', 'Hospital_Patient', 'Hospital_Room',
                      'Hospital_Shift', 'Hospital_Patient_History', 'Hospital_Doctor']

        self.key_data_dict = {"Department_Id": self.department_data["Department_Id"],
                              "Doctor_Id": self.doctor_data["Doctor_Id"],
                              "Gender_Type": self.gender_data["Gender_Type"],
                              "Patient_Id": self.patient_data["Patient_Id"],
                              "Patient_History_Id": self.patient_history_data["Patient_History_Id"],
                              "Hospital_Room_Id": self.hospital_room_data["Hospital_Room_Id"],
                              "Room_Name": self.hospital_room_type_data["Room_Name"],
                              "Service_Id": self.service_data["Service_Id"],
                              "Shift_Id": self.shift_data["Shift_Id"],
                              "Type_Of_Shift_Id": self.shift_type_data["Type_Of_Shift_Id"],
                              "Doctor_Assistant": self.staff_data["Staff_Id"],
                              "Staff_Id": self.staff_data["Staff_Id"],
                              "Type_Number_Id": self.department_type_data["Name"]}

        self.key_colum_parent = {"Department_Id": "Hospital_Department",
                                 "Doctor_Id": "Hospital_Doctor",
                                 "Gender_Type": "Hospital_Gender",
                                 "Patient_Id": "Hospital_Patient",
                                 "Patient_History_Id": "Hospital_Patient_History",
                                 "Hospital_Room_Id": "Hospital_Room",
                                 "Room_Name": "Hospital_Room_Type",
                                 "Service_Id": "Hospital_Service",
                                 "Shift_Id": "Hospital_Shift",
                                 "Type_Of_Shift_Id": "Hospital_Shift_Type",
                                 "Doctor_Assistant": "Hospital_Staff",
                                 "Staff_Id": "Hospital_Staff",
                                 "Type_Number_Id": "Hospital_Type_Department"}

    # =======================================================================
    #                   Show Data
    # =======================================================================
    # Set index of data and with that make QabstractItemModel
    def show_info(self, index):
        self.update()
        self.index = index
        data = pandasModel(self.data_list[self.lists[index]])

        self.show_data(data)

    # Set Model, with QtableView show that
    def show_data(self, data):
        # Create Widget
        self.page = QtWidgets.QWidget()
        self.page.setWindowTitle("Show")
        self.page.setStyleSheet("background:rgb(52, 101, 164)\nqlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,"
                                " stop:0 #2c5d87, stop:1 #83a3be);")
        self.nameLabel = QGridLayout(self.page)
        self.table = QTableView()
        self.table.setMinimumWidth(700)
        self.page.move(200, 200)
        # Read Data
        # Make Model
        self.table.setModel(data)
        size = data.size()
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        for i in range(1, size[0]):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)

        self.table.setHorizontalHeader(header)

        # ==========================================================================
        self.nameLabel.addWidget(self.table)
        # print(self.table.mouseDou)
        self.table.clicked.connect(lambda: self.set_ghost_text(self.table.selectedIndexes()))

        self.page.show()

    # Show Parent Data
    def set_ghost_text(self, item):
        global value1
        colum_index = 0

        for i in item:
            colum_index = i.column()
            value1 = i.data()

        ghost_data = self.data_list[self.lists[self.index]].columns[colum_index]

        if ghost_data in list(self.key_data_dict.keys()):
            connection = pymysql.connect(host="127.0.0.1", user="root", passwd="", db="hospital")
            cursor = connection.cursor()
            database = self.key_colum_parent[ghost_data]

            cursor.execute(f'SELECT * FROM {database}\n'
                           f'WHERE {ghost_data} LIKE "{value1}"')
            text = cursor.fetchall()
            # Set Ghost Text
            for i in text:
                self.table.setToolTip(str(i))
        else:
            self.table.setToolTip(value1)

            # ------------------------------------------------------------------------

    # ------------------------------------------------------------------------
    #                           Search
    # ------------------------------------------------------------------------

    def search_fnc(self):
        self.page = QtWidgets.QWidget()
        self.page.setWindowTitle("Search")
        self.page.setStyleSheet("background:rgb(52, 101, 164)\nqlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,"
                                " stop:0 #2c5d87, stop:1 #83a3be);")
        self.page.setFixedSize(350, 150)

        self.nameLabel = QLabel(self.page)
        self.nameLabel = QGridLayout(self.page)

        list_for_combobox = QtWidgets.QComboBox()
        self.text = QTextBrowser()
        self.text.setText("where to find?")
        self.text.setMaximumSize(170, 28)
        self.text.setStyleSheet("background-color: #B0B7B9")
        list_for_combobox.setStyleSheet("background-color: #35477d")
        for i in self.lists:
            list_for_combobox.addItem(i)

        self.nameLabel.addWidget(self.text, 0, 0, 1, 1)
        self.nameLabel.addWidget(list_for_combobox, 0, 1, 1, 1)
        button_search = QPushButton(self.page)
        button_search.setText("Search")
        button_search.setStyleSheet("background-color: #1a374d")
        self.nameLabel.addWidget(button_search, 1, 1, 1, 1)
        icon = QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        button_search.setIcon(icon)

        self.page.show()
        button_search.clicked.connect(lambda: self.search_word(list_for_combobox.currentText()))

        # self.data_fream()

    def search_word(self, index):
        self.page = QtWidgets.QWidget()
        self.page.setWindowTitle("Search")
        self.page.setStyleSheet("background:rgb(52, 101, 164)\nqlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,"
                                " stop:0 #2c5d87, stop:1 #83a3be);")
        # clear current selection.
        self.nameLabel = QGridLayout(self.page)
        data = self.data_list[index]
        self.table = QTableWidget()
        self.table.setMinimumWidth(700)
        self.page.move(200, 200)

        self.table.setRowCount(len(data))
        self.table.setColumnCount(len(data.columns))
        for i in range(0, len(data)):
            for j in range(0, len(data.columns)):
                item1 = str(data.iloc[i, j])
                self.table.setItem(i, j, QTableWidgetItem(item1))

        self.table.setHorizontalHeaderLabels(list(data.columns))
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        for i in range(1, len(data.columns)):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)

        self.table.setHorizontalHeader(header)

        # self.table.setHorizontalHeader(header)
        self.line = QLineEdit(self.page)
        # self.line.setEchoMode(QLineEdit.Password)
        self.line.setStyleSheet("background-color: #B0B7B9")
        self.line.setPlaceholderText("Word")
        self.nameLabel.addWidget(self.table, 0, 0, 1, 1)
        end_button = QPushButton("Finish")
        self.nameLabel.addWidget(end_button, 2, 0, 1, 1)
        self.line.textChanged.connect(self.search)
        self.nameLabel.addWidget(self.line, 1, 0, 1, 1)
        self.page.show()
        end_button.clicked.connect(lambda: self.page.close())

    def search(self, s):
        # self.table.setCurrentItem(None)
        print(s)
        print(self.table.keyboardSearch(s))

        if not s:
            # Empty string, don't search.
            return

        matching_items = self.table.findItems(s, Qt.MatchContains)

        if matching_items:
            # we have found something
            item = matching_items[0]  # take the first
            self.table.setCurrentItem(item)

    # ------------------------------------------------------------------------
    #                   INSERT
    # ------------------------------------------------------------------------

    def insert_data(self):
        self.page = QtWidgets.QWidget()
        self.page.setWindowTitle("Insert")
        self.page.setStyleSheet("background:rgb(52, 101, 164)\nqlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,"
                                " stop:0 #2c5d87, stop:1 #83a3be);")
        self.page.setFixedSize(350, 150)

        self.nameLabel = QLabel(self.page)
        self.nameLabel = QGridLayout(self.page)

        self.list = QtWidgets.QComboBox()
        self.text = QTextBrowser()
        self.text.setText("where to Insert?")
        self.text.setMaximumSize(170, 28)
        self.text.setStyleSheet("background-color: #B0B7B9")
        for i in self.lists:
            self.list.addItem(i)
        self.list.setStyleSheet("background-color: #35477d")
        button_search = QPushButton(self.page)
        button_search.setText("Insert")
        button_search.setStyleSheet("background-color: #6c5b7c")
        icon = QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/insert.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        button_search.setIcon(icon)

        self.nameLabel.addWidget(self.text, 0, 0, 1, 1)
        self.nameLabel.addWidget(button_search, 1, 1, 1, 1)
        self.nameLabel.addWidget(self.list, 0, 1, 1, 1)

        # self.nameLabel.addWidget(self.line, 0, 0, 1, 1)
        self.page.show()
        button_search.clicked.connect(lambda: self.insert_data_open(self.list.currentText()))

    def insert_data_open(self, where):
        count = len(self.data_list[where].columns)
        self.columns_list = self.data_list[where].columns
        self.answer_list = []

        self.page = QtWidgets.QWidget()
        self.page.setWindowTitle("Insert")
        self.page.setStyleSheet("background:rgb(52, 101, 164)\nqlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,"
                                " stop:0 #2c5d87, stop:1 #83a3be);")
        self.page.setFixedSize(350, 50)
        lop = True
        for i in range(count):
            if self.columns_list[i] in self.key_data_dict.keys() and i > 0:
                tuple_ = []
                for item in self.key_data_dict[self.columns_list[i]]:
                    tuple_.append(str(item))

                self.line, ok = QtWidgets.QInputDialog.getItem(self.page, "Insert", "Insert " +
                                                               str(self.columns_list[i]), tuple(tuple_), 0, False)

            else:
                if self.columns_list[i] == "Schedule":
                    self.line, ok = QtWidgets.QInputDialog.getText(self.page, "Insert", "Insert " +
                                                                   str(self.columns_list[i]) + "\nFormat is YYYY-MM-DD")
                else:
                    self.line, ok = QtWidgets.QInputDialog.getText(self.page, "Insert", "Insert " +
                                                                   str(self.columns_list[i]))
            if ok:
                self.answer_list.append(self.line)
            else:
                lop = False
                break
        if lop:
            self.insert(self.answer_list, where, self.columns_list)
        # print(self.answer_list, self.columns_list, sep="\n")

    def insert(self, answer_list, where, columns):
        value = []
        for i in answer_list:
            try:
                value.append(int(i))
            except:
                value.append(i)

        colum = []
        for i in columns:
            colum.append(i)

        value = tuple(value)
        test = "%s, " * len(colum)
        test = test[:-2]

        connection = pymysql.connect(host="127.0.0.1", user="root", passwd="", db="hospital")
        cursor = connection.cursor()

        try:

            key = f'''INSERT INTO {where} 
                      VALUES ({test})'''
            cursor.execute(key, value)
            connection.commit()
            self.page.close()
        except connection.Error as error:

            self.error = QErrorMessage()
            self.error.setWindowTitle("Insert Error")
            self.error.showMessage("Failed to insert into MySQL table {}".format(error))
            self.error.show()
        cursor.close()

    # =======================================================================
    #                   Update Functions
    # =======================================================================
    def update_start(self):
        self.page = QtWidgets.QWidget()
        self.page.setWindowTitle("Update Date")
        self.page.setStyleSheet("background:rgb(52, 101, 164)\nqlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,"
                                " stop:0 #2c5d87, stop:1 #83a3be);")
        self.page.setFixedSize(400, 150)

        self.nameLabel = QLabel(self.page)
        self.nameLabel = QGridLayout(self.page)

        self.list = QtWidgets.QComboBox()
        self.text = QTextBrowser()
        self.text.setText("where to Update?")
        self.text.setMaximumSize(250, 28)
        self.text.setStyleSheet("background-color: #B0B7B9")
        for i in self.lists:
            self.list.addItem(i)
        self.list.setStyleSheet("background-color: #35477d")
        button_search = QPushButton(self.page)
        button_search.setText(" Open")
        icon = QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/new_updates.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        button_search.setIcon(icon)

        self.nameLabel.addWidget(self.text, 0, 0, 1, 1)
        self.nameLabel.addWidget(button_search, 1, 1, 1, 1)
        self.nameLabel.addWidget(self.list, 0, 1, 1, 1)

        # self.nameLabel.addWidget(self.line, 0, 0, 1, 1)
        self.page.show()
        button_search.clicked.connect(lambda: self.update_start_up(self.list.currentText()))

    def update_start_up(self, where):

        count = len(self.data_list[where].columns)
        self.columns_list = self.data_list[where].columns
        # print(count)
        self.answer_list = []

        self.page = QtWidgets.QWidget()
        self.page.setWindowTitle("Update")
        self.page.setStyleSheet("background:rgb(52, 101, 164)\nqlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,"
                                " stop:0 #2c5d87, stop:1 #83a3be);")
        self.page.setMinimumWidth(700)
        self.data_show = QTableView()

        layout = QGridLayout(self.page)
        data = pandasModel(self.data_list[where])
        self.data_show.setModel(data)
        self.data_show.setMinimumWidth(700)
        size = data.size()
        header = self.data_show.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        self.new_data_lines = []  # new data list
        self.id = QComboBox(self.page)
        self.id.setFixedSize(170, 35)
        self.id.setStyleSheet("background-color: #35477d")
        for item in self.key_data_dict[self.columns_list[0]]:
            self.id.addItem(str(item))
        self.id.itemText(1)
        text = QTextBrowser(self.page)
        text.setText("Select ID what yo wont change:")
        text.setFixedSize(240, 35)
        button = QPushButton(self.page)
        button.setText("Finish")
        button.setFixedSize(100, 35)
        button.setStyleSheet("QPushButton{\n"
                             "background-color: #afc6d9;\n"
                             "border-radius:30px;\n"
                             "border:14px;\n"
                             "width:10;\n"
                             "font: 15pt;\n"
                             "border-bottom: 1px solid rgb(40, 44, 84);\n"
                             "}\n"
                             "QPushButton::hover{\n"
                             "background-color: rgb(40, 44, 84);\n"
                             "}\n"
                             "QPushButton::pressed{\n"
                             "background-color: #191c22;\n"
                             "}\n")

        layout.addWidget(button, count - 1, 1, 1, 1)
        layout.addWidget(text, 1, 1, 1, 1)
        layout.addWidget(self.id, 2, 1, 1, 1)
        for j in range(1, count):
            if self.columns_list[j] in self.key_data_dict.keys():
                text_line = QComboBox(self.page)
                text_line.setFixedSize(170, 35)
                text_line.setStyleSheet("background-color: #35477d")
                for item in self.key_data_dict[self.columns_list[j]]:
                    text_line.addItem(str(item))
            else:

                text_line = QLineEdit(self.page)
                text_line.setFixedSize(170, 35)
                text_line.setPlaceholderText(self.columns_list[j])

                print(text_line.text())
            self.new_data_lines.append(text_line)
            layout.addWidget(text_line, j, 0, 1, 1)

        for i in range(1, size[0]):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)

        self.data_show.setHorizontalHeader(header)
        layout.addWidget(self.data_show, 0, 0, 1, 1)
        # gif for update

        self.fream_1 = QtWidgets.QFrame(self.page)

        self.fream_1.setStyleSheet("border:0px;\n"
                                   "background-color: rgb(240, 44, 54);\n"
                                   "iconify:{icon: dash:admin-generic; color: white; size: 32;"
                                   "animation: breathe; animateOn: hover}\n")
        self.fream_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fream_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fream_1.setObjectName("frame_1")

        gif_label = QtWidgets.QLabel(self.fream_1)
        gif_label.setFixedSize(240, 200)
        gif = QtGui.QMovie("./icons/update2.gif")
        gif_label.setMovie(gif)
        gif.start()

        self.page.show()
        layout.addWidget(self.fream_1, 0, 1)
        self.id.currentIndexChanged.connect(lambda: self.set_auto_text(self.id.currentText(), where))

        button.clicked.connect(lambda: self.read_data(self.new_data_lines, self.id.currentText(), where,
                                                      self.columns_list))

    def set_auto_text(self, event, where):
        event = int(event)
        colum = self.data_list[where].columns[0]
        data = self.data_list[where]
        data = data.loc[data[colum] == event].values[0][1:]
        oop = QLineEdit()
        for i in range(len(data)):
            if type(self.new_data_lines[i]) == type(oop):
                self.new_data_lines[i].setText(str(data[i]))
            else:
                self.new_data_lines[i].setCurrentIndex(i - 1)

    def read_data(self, new_data_lines, id, where, colum):
        value = []
        columns = colum[1:]
        for i in new_data_lines:
            try:
                value.append(int(i.currentIndex()) + 1)
            except AttributeError:
                value.append(i.text())

        for i in range(len(value)):
            try:
                value[i] = int(value[i])
            except ValueError:
                pass

        value = tuple(value)

        connection = pymysql.connect(host="127.0.0.1", user="root", passwd="", db="hospital")
        cursor = connection.cursor()

        for count in range(len(columns)):

            if type(value[count]) == int:
                code_sql = f"""UPDATE {where} 
                               SET {columns[count]}={value[count]}
                               WHERE {colum[0]} = {id}"""
            else:
                code_sql = f"""UPDATE {where} 
                               SET {columns[count]}='{value[count]}'
                               WHERE {colum[0]} = {id}"""
            try:

                cursor.execute(code_sql)

                connection.commit()

            except connection.Error as error:
                self.error = QErrorMessage()
                self.error.setWindowTitle("Insert Error")
                self.error.showMessage("Failed to Update into MySQL table {}".format(error))
                self.error.show()

        cursor.close()
        self.page.close()

        #

    # =======================================================================
    #                               Calculate
    # =======================================================================
    def calculate(self):
        self.page = QtWidgets.QWidget()
        self.page.setWindowTitle("Calculate Mode")
        self.page.setStyleSheet("background:rgb(52, 101, 164)\nqlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,"
                                " stop:0 #2c5d87, stop:1 #83a3be);")
        self.gridLayout = QtWidgets.QGridLayout(self.page)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_2 = QtWidgets.QFrame(self.page)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.page)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_3.addWidget(self.textBrowser, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)

        self.check_box = []
        data = list(self.service_data["Name"])
        price = list(self.service_data["Price"])
        for i in range(len(data)):
            check_box = QtWidgets.QCheckBox()
            check_box.setText(data[i] + "  " + str(price[i]))
            check_box.setStyleSheet("background-color: rgb(150, 150, 150)")
            self.check_box.append(check_box)
            self.gridLayout_2.addWidget(check_box, i, 0, 1, 1)

        self.page.show()
        for i in self.check_box:
            i.toggled.connect(lambda: self.checked(price))

    def checked(self, price):
        a = 0
        pric = 0
        activ_index = []
        for i in range(len(self.check_box)):
            if self.check_box[i].isChecked():
                a += 1
                activ_index.append(self.check_box[i].text())
                # self.textBrowser.setText(z)
                pric += price[i]

        if a == 0:
            self.textBrowser.setText("No Services")
            self.label.setText("0")
        else:
            z = ""
            for i in activ_index:
                z += "\n" + i
            self.textBrowser.setText(z)
            self.label.setText("All Sum:\t" + str(pric))

    # =======================================================================
    #                               Show All Functions
    # =======================================================================
    def all(self):
        self.page = QtWidgets.QWidget()
        self.page.setWindowTitle("Show")
        self.page.setStyleSheet("background:rgb(52, 101, 164)\nqlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,"
                                " stop:0 #2c5d87, stop:1 #83a3be);")
        self.page.setFixedSize(350, 150)

        self.nameLabel = QLabel(self.page)
        self.nameLabel = QGridLayout(self.page)

        list = QtWidgets.QComboBox()
        self.text = QTextBrowser()
        self.text.setText("What to show?")
        self.text.setMaximumSize(170, 28)
        self.text.setStyleSheet("background-color: #B0B7B9")
        list.setStyleSheet("background-color: #35477d")
        for i in self.lists:
            list.addItem(i)

        self.nameLabel.addWidget(self.text, 0, 0, 1, 1)
        self.nameLabel.addWidget(list, 0, 1, 1, 1)
        button_search = QPushButton(self.page)
        button_search.setText("Show")
        button_search.setStyleSheet("background-color: #1a374d")
        self.nameLabel.addWidget(button_search, 1, 1, 1, 1)
        icon = QIcon()
        icon.addPixmap(QtGui.QPixmap(".icons/all2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        button_search.setIconSize(QSize(40, 40))
        button_search.setIcon(icon)
        self.page.show()
        button_search.clicked.connect(lambda: self.show_info(list.currentIndex()))

    def setting(self):
        self.page = QMessageBox.information(None, "Authors", "On this project working`\n"
                                                             "\tArsen Margaryan\n\tColak Musikyan\n"
                                                             "\tNver Postolakyan")
