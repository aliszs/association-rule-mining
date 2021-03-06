# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'front.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QSize  

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QInputDialog
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
from mlxtend.frequent_patterns import fpgrowth
from mlxtend.frequent_patterns import association_rules
from datetime import datetime
import seaborn as sns
sns.set_theme()
#import savefig


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(545, 641)
        self.head_picture = QtWidgets.QLabel(Dialog)
        self.head_picture.setGeometry(QtCore.QRect(20, 20, 501, 321))
        self.head_picture.setText("")
        self.head_picture.setPixmap(QtGui.QPixmap(
            "C:/Users/alisz/Desktop/project/Screenshot (545).png"))
        self.head_picture.setScaledContents(True)
        self.head_picture.setObjectName("head_picture")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 367, 521, 271))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.algorithm_label = QtWidgets.QLabel(self.widget)
        self.algorithm_label.setObjectName("algorithm_label")
        self.horizontalLayout_2.addWidget(self.algorithm_label)
        self.algorithms = QtWidgets.QComboBox(self.widget)
        self.algorithms.setObjectName("algorithms")
        self.algorithms.addItem("")
        self.algorithms.addItem("")
        self.algorithms.addItem("")
        self.horizontalLayout_2.addWidget(self.algorithms)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.toolButton = QtWidgets.QToolButton(self.widget)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.min_sup = QtWidgets.QLabel(self.widget)
        self.min_sup.setObjectName("min_sup")
        self.horizontalLayout_3.addWidget(self.min_sup)
        self.sup_val = QtWidgets.QDoubleSpinBox(self.widget)
        self.sup_val.setObjectName("sup_val")
        self.horizontalLayout_3.addWidget(self.sup_val)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.min_conf = QtWidgets.QLabel(self.widget)
        self.min_conf.setObjectName("min_conf")
        self.horizontalLayout_4.addWidget(self.min_conf)
        self.conf_val = QtWidgets.QDoubleSpinBox(self.widget)
        self.conf_val.setObjectName("conf_val")
        self.horizontalLayout_4.addWidget(self.conf_val)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.chart_checkBox = QtWidgets.QCheckBox(self.widget)
        self.chart_checkBox.setObjectName("chart_checkBox")
        self.verticalLayout_3.addWidget(self.chart_checkBox)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.submit_button = QtWidgets.QPushButton(self.widget)
        self.submit_button.setObjectName("submit_button")
        self.horizontalLayout_5.addWidget(self.submit_button)
        self.close_button = QtWidgets.QPushButton(self.widget)
        self.close_button.setObjectName("close_button")
        self.horizontalLayout_5.addWidget(self.close_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.retranslateUi(Dialog)
        self.close_button.clicked.connect(Dialog.close)
        self.chart_checkBox.clicked['bool'].connect(Dialog.setEnabled)
        self.algorithms.objectNameChanged['QString'].connect(Dialog.update)
        self.sup_val.valueChanged['double'].connect(Dialog.update)
        self.conf_val.valueChanged['double'].connect(Dialog.update)
        self.submit_button.pressed.connect(Dialog.open)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Association-Rule-Mining"))
        self.algorithm_label.setText(_translate("Dialog", "Algorithm"))
        self.algorithms.setItemText(0, _translate("Dialog", "Apriori"))
        self.algorithms.setItemText(1, _translate("Dialog", "FP growth"))
        #self.algorithms.setItemText(2, _translate("Dialog", "Eclat"))
        self.label.setText(_translate("Dialog", "Browse dataset"))
        self.toolButton.setText(_translate("Dialog", "..."))
        self.toolButton.clicked.connect(self.browes_file)
        

        self.min_sup.setText(_translate("Dialog", "Support"))
        self.min_conf.setText(_translate("Dialog", "Confidence"))
        self.chart_checkBox.setText(_translate("Dialog", "View chart"))
        self.submit_button.setText(_translate("Dialog", "Submit"))
        self.submit_button.clicked.connect(self.submit_fuc)

        self.close_button.setText(_translate("Dialog", "Quit"))

    def submit_fuc(self):
        if(self.min_conf==0 or self.min_sup==0):
            self.QM()
            
        
        #QMessageBox::warning(self, "my title", "warning")    
        
        if (self.algorithms.setItemText == 0):
            self.apriori_func()
            self.chart()
        else :
            self.fpg_func()
            self.chart()

    def QM(self):
        QMessageBox.about(self, "Warning", "Please enter min_sup and min_conf")        

    def chart(self):
        chart_data = pd.read_excel(
            'Online_Retail_Results_FPGrowth.xlsx', usecols=['confidence'])
        chart_data.insert(0, 'ID', range(1, 1 + len(chart_data)))
        #chart_data = chart_data.pivot('lift', 'confidence')
        chart = sns.heatmap(chart_data)
        fig = chart.get_figure()
        fig.savefig('results.png', dpi=1200)

    def browes_file(self):
        print("pressed")
        self.open_file()

    def open_file(self):
        filename = QFileDialog.getOpenFileName()
        self.path = filename[0]
        print(self.path)

        # with open(self.path, 'r') as f:
          # print(f.readline())

    def apriori_func(self, min_conf, min_sup):
        store_data = pd.read_csv(self.path, header=None, sep=r',')
        store_data.columns = ((store_data.columns.str).replace(
            "^ ", "")).str.replace(" $", "")
        store_data.head()

        records = []
        for i in range(0, 7501):
            records.append([str(store_data.values[i, j])
                           for j in range(0, 20)])

        association_rules = apriori(
            records, min_support=self.min_sup, min_confidence=self.min_conf, min_lift=3, min_length=2)
        association_results = list(association_rules)

        print(len(association_results))

        print(association_results[0])

        f = open("demofile.txt", "w+")
        f.close()

        f = open("demofile.txt", "a")

        for item in association_results:

            # first index of the inner list
            # Contains base item and add item
            pair = item[0]
            items = [x for x in pair]
            f.write("Rule: " + items[0] + " -> " + items[1])
            f.write("\n")

            # second index of the inner list
            f.write("Support: " + str(item[1]))
            f.write("\n")

            # third index of the list located at 0th
            # of the third index of the inner list

            f.write("Confidence: " + str(item[2][0][2]))
            f.write("\n")
            f.write("Lift: " + str(item[2][0][3]))
            f.write("\n")
            f.write("=====================================")
            f.write("\n")

        f.close()

        f = open("demofile.txt", "r")
        print(f.read())

    def fpg_func(self):
        startTime = datetime.now()
        # ### Load and clean transactions data to be used in the analysis
        # read transactions data from csv file
        df = pd.read_excel(self.path)
        # clean the product names
        #df['Description'] = df['Description'].str.strip()
        #df['InvoiceNo'] = df['InvoiceNo'].astype('str')
        # ### Create basket datafarme from transactions data with each row representing one basket
        # create basket dataframe
        basket = df.groupby(['InvoiceNo', 'Description'])['Quantity'].sum(
        ).unstack().reset_index().fillna(0).set_index('InvoiceNo')
        basket.head()

        # one hot encode the basket

        def encode_units(x):
            if x <= 0:
                return 0
            if x >= 1:
                return 1

        basket_sets = basket.applymap(encode_units)
        basket_sets.head()
        # ### Run FP-growth algorithm on frequent item sets (items that frequently appear in the same basket)
        # create minTransactions variable to represent the minimum number of baskets for support parameter
        minTransaction = 300
        totalTransactions = len(basket_sets.index)
        min_support_calc = minTransaction/totalTransactions

        print('number of baskets for analysis is', totalTransactions)
        print('minimum support value is', round(min_support_calc*100, 4), '%')
        # create frequent items sets with clculated minimum support
        frequent_itemsets = fpgrowth(
            basket_sets, min_support=min_support_calc, use_colnames=True)
        frequent_itemsets.describe()

        rules = association_rules(
            frequent_itemsets, metric="lift", min_threshold=1)
        rules.sort_values('confidence', ascending=False, inplace=True)
        rules.head(10)

        # ### Save results to csv file based on desired association parameters

        rules[(rules['lift'] >= 1.4) & (rules['confidence'] >= 0.3)].sort_values(by=[
            'confidence', 'lift'], ascending=False).to_excel(r'Online_Retail_Results_FPGrowth.xlsx', index=False)

        print('It took ', datetime.now() - startTime, ' to run')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
