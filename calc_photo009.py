#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import ast
import os
import shutil
import sys
from typing import Any

import cv2
import numpy as np
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLineEdit
# from keyboard import add_hotkey
from pdf2image import convert_from_path

import calculon_photo_ui_1
from config import *

""" Calculon Now without keyboard shortcuts. Full functional. Translated as I could"""


def img_visual(self, g_ey_p, set_label_ok_p, img_path_p,
               spin_np):  # displays picture number gEyP in setLabelOkP from folder imgPathP
    is_spin = None
    width = None
    height = None
    img1 = None
    lis_files = os.listdir(img_path_p)  # View folder
    lis_files.sort()  # sort folders alphabetically
    try:  #
        is_spin = g_ey_p
    except IndexError:  #
        if is_spin is None:
            g_ey_p = 0
    num_files = len(lis_files)  # read number images
    while g_ey_p > (
            num_files - 1):  # check the exception - if the number of files in the directory
        # less than we spin it leads to an error
        g_ey_p -= 1
        self.lineEdit_134.setText(str(g_ey_p))
        self.label_46.setText('spinBox diapason over')
    img_file_name = lis_files[g_ey_p]  # take the file name by number from the list
    self.centralSpinPoint = g_ey_p  # set the spinBox pointer
    spin_np.blockSignals(True)
    spin_np.setProperty('value', self.centralSpinPoint)  # setting spinbox parameters
    spin_np.setMinimum(0)
    spin_np.setMaximum(num_files)
    spin_np.blockSignals(False)
    name_suffix = '.' + img_file_name.split('.')[
        -1]  # here I split by dot and select the file extension and correct the dot
    if (name_suffix == '.jpeg') or (name_suffix == '.pdf'):  #
        text_out = str('graphic file displayed =>' + img_file_name)
        self.label_46.setText(text_out)
        img_file_full = img_path_p + '/' + img_file_name  # full path and file name
        img_file_full2 = img_file_full
        if img_path_p != imageDir:  # Checking if input images are raw
            self.pixmap = QPixmap(img_file_full)  # Checking if input images are raw
            set_label_ok_p.setPixmap(self.pixmap)
        elif img_path_p == imageDir:  # Checking that the raw input images folder is visible
            # **************************Converting a picture for non-standard images
            lis_files = os.listdir(Temp)  # View folder
            len_temp = len(lis_files)
            if len_temp == 0:  #
                temp0 = 0
                temp_max = 0
            else:  #
                temp0 = 0
                i = 0
                temp_max = 0
                while i < len_temp:
                    if lis_files[i].split('.')[0][:-1] == 'temp':  #
                        temp0 = 1
                        temp_num = int(lis_files[i].split('.')[0][-1])
                        if temp_num > temp_max:  #
                            temp_max = temp_num
                    i += 1
            if (temp0 == 1) and not ((self.radioButton_19.isChecked()) and (
                    temp_max == 3)):  # in entering points area, but need select the second picture after the first
                img_file_temp = Temp + '/temp' + str(temp_max) + '.jpeg'
                self.pixmap = QPixmap(img_file_temp)  # image setup and output
                set_label_ok_p.setPixmap(self.pixmap)
            else:  #
                img_file_temp = Temp + '/temp.jpeg'
                if name_suffix == '.jpeg':  #
                    img1 = cv2.imread(img_file_full)
                    height, width, channel = img1.shape
                elif (name_suffix == '.pdf') and (self.checkBox_18.isChecked()):  #
                    img1pdf = convert_from_path(img_file_full)
                    img1pdf[0].save(img_file_temp, 'JPEG')
                    img1 = cv2.imread(img_file_temp)
                    height, width, channel = img1.shape
                elif self.checkBox_18.isChecked():  #
                    text_out = str('this file type will not be displayed =>' + img_file_name)
                    self.label_46.setText(text_out)
                    return ()
                if int(height / (width / Shir)) < Vys:  #
                    img1_s = cv2.resize(img1, (int(width / (width / Shir)), int(height / (width / Shir))),
                                        interpolation=cv2.INTER_CUBIC)  # Zoom to fit on screen
                else:  #
                    img1_s = cv2.resize(img1, (int(width / (height / Vys)), int(height / (height / Vys))),
                                        interpolation=cv2.INTER_CUBIC)  # Zoom to fit on screen
                cv2.imwrite(img_file_temp, img1_s)  # saved with a dot in a temporary folder
                self.pixmap = QPixmap(img_file_temp)  # image setup and output
                set_label_ok_p.setPixmap(self.pixmap)
    else:  #
        text_out = str('this file type will not be displayed  =>' + img_file_name)
        self.label_46.setText(text_out)
        return ()
    return ()


def txt_screen(self, addr_le):  # OK
    """A function that divides a list into groups of 10, giving these groups symbolic names to enable
    scrolling screens by 10. Group name from the first letter of the name of the first and last in ten.
    If the letters are the same, numbers are added"""
    i_count = 0  # The counters are set - this is the counter of the internal display loop. He = 10 or 20
    j_count = 0  # resetting the customer counter
    letter_1 = ' '  # the first letter in the first name of ten group
    letter_end = ' '  # the first letter in the last name of ten group
    k_count = 0  # Resetting the page counter with the same starting and ending letters
    l_count = 0  #
    i_var_count = 9
    data_order = {}  #
    report_o = addr_le[0].text()
    if report_o == '':  #
        report_order = []
    else:
        report_order = report_o.split(',')
    num_records = len(report_order)  # the number of persons is read
    if num_records == 0:  #
        data_order[0] = ['', '', '', '', '', '', '', '', '', '', '']
        return data_order  #
    while j_count < num_records:  # Counter of the total number of persons. Until it's all over
        str_output = list()  # The list is empty, but it will contain the names of the persons and the name of package.
        while i_count <= i_var_count:  # counter up to 10, according to the number of output lineEdit's
            name_surname = report_order[j_count]  # read the current name in the list of clients
            str_output.append(name_surname)  # add client name
            i_letter = str(name_surname)[0]  # read the first letter of the name
            if i_count == 0:  # If the beginning of a ten, remember the first letter as the first letter for scrolling
                letter_1 = i_letter
            if i_count == i_var_count:  # If the end is ten, remember it as the last letter
                letter_end = i_letter
            if j_count == (
                    num_records - 1):  # if reached name of last client, his letter is remembered
                # as the last letter in ten, albeit incomplete
                letter_end = i_letter
                data_order[l_count] = str_output  # add a list of names with an index and a key number to the dictionary
            if i_count == num_records:  # if the number of clients is less than ten and the counter in ten has reached
                # the end - exit
                break
            i_count += 1  # adding to counters
            j_count += 1
            if j_count == num_records:  # Exit when the list of clients is exhausted
                break
        if letter_1 != letter_end:  # if the letters of the beginning and end of the ten are different,
            # the Spinbox name is made up of two letters of the beginning and end
            name_spin_box = letter_1 + letter_end  #
            str_output.append(name_spin_box)  # Finally, add the index name
            k_count = 0  #
        if letter_1 == letter_end:  # if the letters of beginning and end of the ten are the same, another counter is ON
            k_count += 1  #
            if k_count == 1:  #
                name_spin_box = letter_1 + letter_end  # if it is only 1, then are still two letters, albeit identical
                str_output.append(name_spin_box)  # Finally, add the index name
            if k_count > 1:  # if more, then he begins to add numbers to the two-letter name, starting with 1
                name_spin_box = letter_1 + letter_end + str(k_count - 1)  #
                str_output.append(name_spin_box)  # Finally, add the index name
        if j_count <= (num_records - 1):  #
            i_count = 0
            data_order[l_count] = str_output  # add a list of names with an index and a key number to the dictionary
            l_count += 1
    self.lineEdit_102.setText(str(data_order))
    return data_order  #


def txt_screen_output(self, data_order, g_ex, list_ed, lab_x):  #
    """ A function that displays the names of 10 clients from the corresponding page in 10 screen lineEdit's.
        The page index is written, consisting of the first letters of the first and last in ten entry.
        If the first letters of the beginning and end are the same, numbers are added to the two letters index"""
    if g_ex != '':  # check - if the spinbox has been initialized
        g_ex = int(g_ex)
    else:  # or not
        g_ex = 0
    num_records = len(data_order)
    if g_ex >= len(data_order):  # check if there are more than files in
        for leI in [self.label_46]:
            leI.setText('spinBox diapason over')
        g_ex -= 1
    if lab_x == '':  #
        for leI in [self.label_46]:
            leI.setText('Visualisation Error,label numb leI empty')
        return
    if list_ed == '':  #
        for leI in [self.label_46]:
            leI.setText('Visualisation Error,lineEdit numb listEd empty')
        return
    i_count = 0  # lineEdit number counter
    str_output_vis = data_order[g_ex]  # list with ten data and index from the dictionary
    data_len = len(str_output_vis)  # number of entries in the list
    if data_len < 11:
        j_count = 11 - data_len
        while j_count != 0:
            str_output_vis.insert(-1, '')
            j_count -= 1
    elif data_len == 11:
        i_count = 0
    for le in list_ed:  #
        text_spin_str = str_output_vis[i_count]  #
        le.setText(str(text_spin_str))
        i_count += 1
    text_spin_str = str(g_ex + 1) + 'of' + str(num_records) + '@' + str_output_vis[i_count]  #
    lab_x[0].setText(str(text_spin_str))  # list of addresses to write in corresponded lineEdit
    return ()


def activation_graph(self):  # Buttons colors and txt at Graphics mode activation
    """ prepares the appearance of interface elements in accordance with the current task in Graphix mode"""
    self.pushButton_21.blockSignals(True)
    self.pushButton_19.blockSignals(True)
    self.pushButton_8.blockSignals(True)
    self.pushButton_9.blockSignals(True)
    self.pushButton_21.setChecked(False)
    self.pushButton_19.setChecked(False)
    self.pushButton_8.setChecked(False)
    self.pushButton_9.setChecked(False)
    self.pushButton_21.blockSignals(False)
    self.pushButton_19.blockSignals(False)
    self.pushButton_8.blockSignals(False)
    self.pushButton_9.blockSignals(False)
    self.pushButton_19.clearFocus()
    self.pushButton_21.clearFocus()
    self.checkBox_18.blockSignals(True)
    self.checkBox_18.setChecked(True)
    self.checkBox_18.blockSignals(False)
    self.buttonGroup_7.setExclusive(False)
    self.radioButton_19.blockSignals(True)
    self.radioButton_19.setChecked(True)
    self.radioButton_19.repaint()
    self.radioButton_19.blockSignals(False)
    self.radioButton_20.blockSignals(True)
    self.radioButton_20.setChecked(False)
    self.radioButton_20.repaint()
    self.radioButton_20.blockSignals(False)
    self.buttonGroup_7.setExclusive(True)
    self.lineEdit_22.setFocus()  #
    self.pushButton_18.setStyleSheet("background-color:rgb(200,255,200);")
    self.pushButton_19.setStyleSheet("background-color:rgb(242,238,235);")
    self.pushButton_19.setEnabled(False)
    self.pushButton_8.setStyleSheet("background-color:rgb(200,255,200);")
    self.pushButton_8.setText('compleTe')
    self.pushButton_8.setEnabled(True)
    self.pushButton_21.setStyleSheet("background-color:rgb(242,238,235);")
    self.pushButton_21.setText('')
    self.pushButton_21.setEnabled(False)
    self.pushButton_9.setStyleSheet("background-color:rgb(200,255,200);")
    self.pushButton_9.setText('Previous')
    self.pushButton_9.setEnabled(True)
    self.radioButton_19.setStyleSheet("background-color:rgb(200,255,200);")
    self.radioButton_19.setText('ID two images')
    self.radioButton_20.setStyleSheet("background-color:rgb(200,255,200);")
    self.radioButton_20.setText('passport one image')
    self.checkBox_18.setStyleSheet("background-color:rgb(200,255,200);")
    self.label_38.setStyleSheet("color:rgb(0, 70, 0);")
    self.label_38.setStyleSheet("background-color:rgb(200,255,200);")
    self.label_38.setText('Graphics Mode.Click 4 or 8 points one or two images to actual document corners')
    return


def activation_txt(self):  # Buttons colors and txt at TXT mode activation
    """ prepares the appearance of interface elements in accordance with the current task in TXT mode"""
    self.pushButton_21.blockSignals(True)
    self.pushButton_19.blockSignals(True)
    self.pushButton_8.blockSignals(True)
    self.pushButton_9.blockSignals(True)
    self.pushButton_21.setChecked(False)
    self.pushButton_19.setChecked(False)
    self.pushButton_8.setChecked(False)
    self.pushButton_9.setChecked(False)
    self.pushButton_21.blockSignals(False)
    self.pushButton_19.blockSignals(False)
    self.pushButton_8.blockSignals(False)
    self.pushButton_9.blockSignals(False)
    self.pushButton_19.clearFocus()
    self.pushButton_21.clearFocus()
    self.checkBox_18.blockSignals(True)
    self.checkBox_18.setChecked(False)
    self.checkBox_18.blockSignals(False)
    self.buttonGroup_7.setExclusive(False)
    self.radioButton_19.blockSignals(True)
    self.radioButton_19.setChecked(True)
    self.radioButton_19.repaint()
    self.radioButton_19.blockSignals(False)
    self.radioButton_20.blockSignals(True)
    self.radioButton_20.setChecked(False)
    self.radioButton_20.repaint()
    self.radioButton_20.blockSignals(False)
    self.buttonGroup_7.setExclusive(True)
    self.lineEdit_22.setFocus()  #
    self.pushButton_18.setStyleSheet("background-color:rgb(255,210,210);")
    self.pushButton_19.setStyleSheet("background-color:rgb(255,210,210);")
    self.pushButton_19.setEnabled(True)
    self.pushButton_8.setStyleSheet("background-color:rgb(242,238,235);")
    self.pushButton_8.setText('')
    self.pushButton_8.setEnabled(False)
    self.pushButton_21.setStyleSheet("background-color:rgb(255,210,210);")
    self.pushButton_21.setText('Go-->')
    self.pushButton_21.setEnabled(True)
    self.pushButton_9.setStyleSheet("background-color:rgb(242,238,235);")
    self.pushButton_9.setText('')
    self.pushButton_9.setEnabled(False)
    self.radioButton_19.setStyleSheet("background-color:rgb(242,238,235);")
    self.radioButton_19.setText('')
    self.radioButton_20.setStyleSheet("background-color:rgb(242,238,235);")
    self.radioButton_20.setText('')
    self.checkBox_18.setStyleSheet("background-color:rgb(255,210,210);")
    self.label_38.setStyleSheet("color:rgb(70, 0, 0);")
    self.label_38.setStyleSheet("background-color:rgb(255,210,210);")
    self.label_38.setText('Input New TXT. To save press Go-->')
    return


def name_capitalize_q(self, name_str):  #
    """ Begins the entered name with a capital letter. if separated by a space, the second name is also capitalized"""
    g_ez_c = None
    if name_str == '':
        self.label_46.setText('Enter your first name and middle name,separated by a space, possibly with a lowercase')
        name_str = ''
        g_ez_c = name_str
        return g_ez_c
    if len(name_str) == 1:  # Checking if it's not from space
        if name_str == ' ':
            self.label_46.setText('start from space')
            g_ez_c = ''
            return g_ez_c
        else:
            self.label_46.setText('')
            g_ez_c = name_str.capitalize()
    elif len(name_str) == 2:
        g_ez_c = name_str
    elif len(name_str) > 2:
        if name_str[-2] == ' ':
            name_str = name_str.split()  # if the name is entered, it is broken into pieces by spaces.
            name_first_c = name_str[0]  # the first value will be the name
            name_sec = name_str[1]
            name_sec_c = name_sec.capitalize()  #
            g_ez_c = name_first_c + ' ' + name_sec_c
        else:
            g_ez_c = name_str
    return g_ez_c


def list_dirs_method_1(self):  # outputs a list of full names of all clients
    list_dirs = os.listdir(infoPath)  # Indicating which folder to look in
    list_dirs.sort()  # sort directories alphabetically
    input_data = list_dirs
    self.lineEdit_108.setText(','.join(input_data))
    return ()


def name_capitalize_s(self, surname_str):  # Begins the input string with a capital letter for the Surname
    if surname_str == ' ':
        surname_str = ''
        self.label_46.setText('started with space')
        g_ez_c1 = surname_str
        return g_ez_c1
    if len(surname_str) == 1:
        surname_str_c = surname_str.capitalize()
        g_ez_c1 = surname_str_c
    else:
        g_ez_c1 = surname_str
    return g_ez_c1


class MyWindow(QtWidgets.QMainWindow, calculon_photo_ui_1.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.centralSpinPoint = None
        self.setupUi(self)  #
        dir_path = os.path.dirname(os.path.realpath(__file__))  # to get the file path
        '''Presets and Settings '''
        cwd = os.getcwd()  # to get the working directory
        self.lineEdit_133.setText('0')  # g_ex
        self.lineEdit_134.setText('0')  # g_ex +Ctrl
        self.wEv = 0  # mouse wheel spin counter
        self.ctrlEv = 0  # same with Ctrl
        list_dirs = os.listdir(infoPath)  # Indicating which folder to look in
        num_records4 = len(list_dirs)  # clients
        self.lineEdit_161.setText(str(len(list_dirs)))  # Setting the upper rotation limit
        '''Reaction to hot buttons '''
        # Without keyboard: add_hotkey('alt + x', QtWidgets.qApp.quit)
        self.pushButton_18.clicked.connect(QtWidgets.qApp.quit)  # Logout button event
        # Without keyboard: add_hotkey('alt + n', self.select_new)
        # Without keyboard: add_hotkey('alt + g', self.select_go)
        # Without keyboard: add_hotkey('alt + t', self.select_t)
        # Without keyboard: add_hotkey('alt + p', self.select_p)
        # self.tabWidget.currentChanged.connect(lambda x: self.select_tab(x))
        QtCore.QTimer.singleShot(0, self.pushButton_6.setFocus)
        '''Display '''
        self.label_40.setText('small company')
        self.label_41.setText("ID's and passport's processing helper")
        self.textEdit.setHtml('')
        my_file_name = Calculon + 'info.html'
        opened_file = open(my_file_name, 'r')
        txt_file = opened_file.read()
        self.textEdit.setHtml(txt_file)
        img_file_name = Calculon + 'gaviota.jpg'
        img_file_full = img_file_name  #
        self.pixmap = QPixmap(img_file_full)  #
        self.label_95.setPixmap(self.pixmap)
        self.pushButton_6.setFocus()
        self.pushButton_6.clicked[bool].connect(
            self.click_method_51)  # manual/about program selection
        activation_graph(self)  #
        self.label_46.setText('You can enter data for a new person')
        lis_files = os.listdir(Temp)  #
        len_temp = len(lis_files)
        i = 0
        while i < len_temp:  #
            img_temp_full = Temp + '/' + lis_files[i]
            os.remove(img_temp_full)  #
            i += 1
        '''Converting files to a standard '''
        lis_files = os.listdir(imageDir)  # View folder
        lis_files.sort()  # sort
        len_files = len(lis_files)
        i = 0
        while i < len_files:  #
            img_file_name = lis_files[i]  # take the file name by number
            name_suffix = '.' + img_file_name.split('.')[
                -1]  # divide by dot and select the file extension and correct the dot that disappeared in the process
            img_name = ','.join(img_file_name.split('.')[0:-1])  # file name without extension
            img_file_full = imageDir + '/' + img_file_name  # From Img file type .jpg, jpe, JPG
            if (name_suffix == '.jpg') or (name_suffix == '.jpe') or (name_suffix == '.JPG'):  #
                name_suffix = '.jpeg'
                img_file_dest = imageDir + '/' + img_name + '.jpeg'  # To Img moving in .jpeg format
                shutil.move(img_file_full, img_file_dest)  # Move
            elif (name_suffix == '.bmp') or (name_suffix == '.jp2') or (name_suffix == '.png') or (
                    name_suffix == '.webp') or (name_suffix == '.pgm'):  # from formats bmp, jp2, png, webp, pgm
                img1 = cv2.imread(img_file_full)
                img_file_dest = imageDir + '/' + img_name + '.jpeg'
                cv2.imwrite(img_file_dest, img1)  #
                os.remove(img_file_full)  # erased the file
            i += 1
        set_label_ok1 = self.label_42
        img_path1 = imageDir  # setup picture viewing
        spin_n1 = self.spinBox_4  # scrolling pictures
        g_ey1 = int(self.lineEdit_134.text())
        img_visual(self, g_ey1, set_label_ok1, img_path1, spin_n1)  # This draws the first picture
        list_dirs_method_1(self)  # List of full names
        addr_le1 = [self.lineEdit_108]
        data_order1 = txt_screen(self, addr_le1)  # prepare screen split
        g_ex = self.centralSpinPoint  # set to the beginning of the scroll
        self.spinBox_2.valueChanged.connect(self.spin_box_ch_1)  #
        global list_ed
        list_ed = [self.lineEdit_45, self.lineEdit_46, self.lineEdit_47, self.lineEdit_48, self.lineEdit_49,
                   self.lineEdit_50, self.lineEdit_51, self.lineEdit_52, self.lineEdit_53, self.lineEdit_54]
        lab_x1 = [self.label_37]
        g_ex1 = int(self.lineEdit_133.text())
        txt_screen_output(self, data_order1, g_ex1, list_ed, lab_x1)  # display
        self.spinBox_4.valueChanged.connect(lambda x: self.image_box_1(x))  # here is the display when scrolling
        self.lineEdit_22.setFocus()  # Focus is set to the first window - Name

        # ====================================Events e=1 Tabs=================================================
        self.checkBox_18.toggled.connect(self.ed_graph)
        self.lineEdit_22.textChanged.connect(lambda x: self.text_ch(x))
        self.lineEdit_22.returnPressed.connect(
            self.name_capitalize_1)  # when Enter is pressed, it is triggered to the input of a
        # middle name or first name, with capitalization of the first letters
        self.lineEdit_29.textChanged.connect(lambda x: self.text_ch_1(x))
        self.lineEdit_29.returnPressed.connect(self.click_method_33)  # it moves focus to the next input window
        self.lineEdit_33.textChanged.connect(lambda x: self.text_ch_3(x))
        self.lineEdit_33.returnPressed.connect(self.click_method_34)
        self.lineEdit_23.textChanged.connect(lambda x: self.text_ch_4(x))
        self.lineEdit_23.returnPressed.connect(self.click_method_35)
        self.lineEdit_18.returnPressed.connect(self.click_method_36)
        self.lineEdit_19.returnPressed.connect(self.click_method_37)
        self.lineEdit_28.textChanged.connect(lambda x: self.text_ch_4_v(x))
        self.lineEdit_28.returnPressed.connect(self.click_method_39)
        self.lineEdit_26.textChanged.connect(lambda x: self.text_ch_6(x))
        self.lineEdit_26.returnPressed.connect(self.click_method_40)  #
        self.lineEdit_27.textChanged.connect(lambda x: self.text_ch_5(x))
        self.lineEdit_27.returnPressed.connect(self.click_method_41)
        self.lineEdit_24.returnPressed.connect(self.click_method_42)
        self.lineEdit_25.returnPressed.connect(self.click_method_46)
        self.pushButton_21.clicked.connect(self.click_method_21)  # Go to txt and save data
        self.pushButton_8.clicked.connect(self.click_method_24)  # complete
        self.pushButton_9.clicked.connect(self.click_method_29)  # Previous
        self.pushButton_19.clicked.connect(self.click_method_19)  # Next client

    def select_new(self):  #
        self.pushButton_19.blockSignals(True)
        self.pushButton_19.setChecked(True)
        self.pushButton_19.blockSignals(False)
        self.click_method_19()
        return

    def select_go(self):  # alt+g
        self.pushButton_21.blockSignals(True)
        self.pushButton_21.setChecked(True)
        self.pushButton_21.blockSignals(False)
        self.click_method_21()
        return

    def select_t(self):  #
        self.pushButton_8.blockSignals(True)
        self.pushButton_8.setChecked(True)
        self.pushButton_8.blockSignals(False)
        self.click_method_24()
        return

    def select_p(self):  #
        self.pushButton_9.blockSignals(True)
        self.pushButton_9.setChecked(True)
        self.pushButton_9.blockSignals(False)
        self.click_method_29()
        return

    def mousePressEvent(self, e):  # mouse button pressed
        if (868 <= e.x() <= 1588) and (32 <= e.y() <= 932) and (self.checkBox_18.isChecked()):  #
            dict_points = {}
            mouse_x = e.x()
            mouse_y = e.y()
            edi_po_d = self.lineEdit_113.text()
            g_ey = self.spinBox_4.value()  # image number
            lis_files = os.listdir(imageDir)  # Viewing imageDir
            lis_files.sort()  # sort
            img_file_name = lis_files[g_ey]  # file name take by its number from list
            name_suffix = '.' + img_file_name.split('.')[
                -1]  # divide by dot and select the file extension and correct the dot that disappeared in the process
            if (name_suffix == '.jpeg') or (name_suffix == '.pdf'):  #
                img_file_full = imageDir + '/' + img_file_name  # full path and file name
                img_file_dest = Temp + '/' + img_file_name  #
                if not os.path.isfile(img_file_dest):  # Not that file in path
                    shutil.copyfile(img_file_full, img_file_dest)  # in folder tmpDir copy
                if edi_po_d == '':  #
                    edit_points_d = {}
                    d_key = 0
                else:  #
                    edit_points_d = ast.literal_eval(edi_po_d)
                    d_key = len(edit_points_d)
                if d_key < 4:  #
                    if d_key == 0:  #
                        img_temp = Temp + '/temp.jpeg'
                        img1 = cv2.imread(img_temp)
                        height, width, channel = img1.shape
                        xcv1 = int(mouse_x - ((
                                                      Shir - width) / 2) - 870)  # 870 Determined by window offset
                        # display in main window
                        ycv1 = int(mouse_y - ((
                                                      Vys - height) / 2) - 32)  # 32 Determined by window offset
                        # display in main window
                        edit_points_d[d_key] = [xcv1, ycv1]
                        self.lineEdit_113.setText(str(edit_points_d))
                        cv2.circle(img1, (xcv1, ycv1), radius=2, color=(0, 255, 255), thickness=2)  # paste a dot
                        self.label_46.setText(
                            'now have 1 point, continue clockwise')
                        img_file_temp = Temp + '/temp' + str(d_key) + '.jpeg'
                        cv2.imwrite(img_file_temp, img1)  #
                        self.pixmap = QPixmap(img_file_temp)  # image output
                        self.label_42.setPixmap(self.pixmap)
                    else:  #
                        d_points = self.lineEdit_113.text()
                        dict_points = ast.literal_eval(d_points)
                        xcv0 = dict_points[d_key - 1][0]
                        ycv0 = dict_points[d_key - 1][1]
                        img_file_temp = Temp + '/temp' + str(d_key - 1) + '.jpeg'  #
                        img1 = cv2.imread(img_file_temp)
                        height, width, channel = img1.shape
                        xcv1 = int(mouse_x - ((Shir - width) / 2) - 870)
                        ycv1 = int(mouse_y - ((Vys - height) / 2) - 32)
                        edit_points_d[d_key] = [xcv1, ycv1]
                        self.lineEdit_113.setText(str(edit_points_d))
                        cv2.circle(img1, (xcv1, ycv1), radius=2, color=(0, 255, 255), thickness=2)
                        cv2.line(img1, (xcv0, ycv0), (xcv1, ycv1), (0, 255, 255), 3)
                        if d_key == 3:  #
                            dict_points = ast.literal_eval(self.lineEdit_113.text())
                            xcv0 = dict_points[0][0]
                            ycv0 = dict_points[0][1]
                            cv2.line(img1, (xcv1, ycv1), (xcv0, ycv0), (0, 255, 255), 3)
                            self.label_46.setText(
                                'Now 4 corners, you can do other side or button "compleTe" process and save')
                        elif 0 < d_key < 3:
                            self.label_46.setText('now have ' + str(d_key + 1) + ' point, continue clockwise')
                        img_file_temp = Temp + '/temp' + str(d_key) + '.jpeg'
                        cv2.imwrite(img_file_temp, img1)  # save image to Temp named temp*.jpeg *=0..3
                        self.pixmap = QPixmap(img_file_temp)  # image output
                        self.label_42.setPixmap(self.pixmap)
                if (self.radioButton_19.isChecked()) and 3 < d_key < 8:  # ID
                    edi_po_d = self.lineEdit_113.text()
                    edit_points_d = ast.literal_eval(edi_po_d)
                    d_key = len(edit_points_d)
                    if d_key == 4:  #
                        img_temp = Temp + '/temp.jpeg'
                        img1 = cv2.imread(img_temp)
                        height, width, channel = img1.shape
                        xcv1 = int(mouse_x - ((Shir - width) / 2) - 870)
                        ycv1 = int(mouse_y - ((Vys - height) / 2) - 32)
                        edit_points_d[d_key] = [xcv1, ycv1]
                        self.lineEdit_113.setText(str(edit_points_d))
                        cv2.circle(img1, (xcv1, ycv1), radius=2, color=(0, 255, 255), thickness=2)  # paste a dot
                        self.label_46.setText('now have 5 point, continue clockwise')
                        img_file_temp = Temp + '/temp' + str(d_key) + '.jpeg'  #
                        cv2.imwrite(img_file_temp, img1)  # save with dot in Temp
                        self.pixmap = QPixmap(img_file_temp)  # image output
                        self.label_42.setPixmap(self.pixmap)
                    elif 3 < d_key < 8:  #
                        d_points = self.lineEdit_113.text()
                        dict_points = ast.literal_eval(d_points)
                        xcv0 = dict_points[d_key - 1][0]
                        ycv0 = dict_points[d_key - 1][1]
                        img_file_temp = Temp + '/temp' + str(d_key - 1) + '.jpeg'  #
                        img1 = cv2.imread(img_file_temp)
                        height, width, channel = img1.shape
                        xcv1 = int(mouse_x - ((Shir - width) / 2) - 870)
                        ycv1 = int(mouse_y - ((Vys - height) / 2) - 32)
                        edit_points_d[d_key] = [xcv1, ycv1]
                        self.lineEdit_113.setText(str(edit_points_d))
                        cv2.circle(img1, (xcv1, ycv1), radius=2, color=(0, 255, 255), thickness=2)
                        cv2.line(img1, (xcv0, ycv0), (xcv1, ycv1), (0, 255, 255), 3)
                        if 4 < d_key < 7:
                            self.label_46.setText('now have ' + str(d_key + 1) + ' point, continue clockwise')
                        elif d_key == 7:  #
                            dict_points = ast.literal_eval(self.lineEdit_113.text())
                            xcv0 = dict_points[4][0]
                            ycv0 = dict_points[4][1]
                            cv2.line(img1, (xcv1, ycv1), (xcv0, ycv0), (0, 255, 255), 3)
                            self.label_46.setText(
                                'Now are 8 corners, you can do other side or press button "compleTe" process and save')
                        img_file_temp = Temp + '/temp' + str(d_key) + '.jpeg'  #
                        cv2.imwrite(img_file_temp, img1)  # save to Temp image with name temp*,jpeg *- 0..7
                        self.pixmap = QPixmap(img_file_temp)  # image output
                        self.label_42.setPixmap(self.pixmap)

    def wheelEvent(self, event):  # mouse wheel rotation events
        step = event.angleDelta().y()  # -120 wheel towards you, 120 - away from you
        ier = int(step / (-120))
        if event.modifiers() == Qt.ControlModifier:  # Rotation + Ctrl
            self.ctrlEv = int(self.lineEdit_134.text())
            self.ctrlEv = self.ctrlEv + ier
            if self.ctrlEv < 0:  #
                self.ctrlEv = 0
            self.lineEdit_134.setText(str(self.ctrlEv))
            self.spinBox_4.setProperty('value', self.ctrlEv)
            return
        else:
            self.wEv = int(self.lineEdit_133.text())  # mouse wheel rotation
            limit_max = int(self.lineEdit_161.text())  # Setting the upper rotation limit
            self.wEv = self.wEv + ier
            if self.wEv < 0:  #
                self.wEv = 0
            elif self.wEv > limit_max:
                self.wEv = limit_max
            self.lineEdit_133.setText(str(self.wEv))  #
            self.spinBox_2.setProperty('value', self.wEv)

    def click_method_51(self, pressed):
        if pressed:
            my_file_name = Calculon + 'manual.html'
            opened_file = open(my_file_name, 'r')
            txt_file = opened_file.read()
            self.textEdit.setHtml(txt_file)
        else:  #
            my_file_name = Calculon + 'info.html'
            opened_file = open(my_file_name, 'r')
            txt_file = opened_file.read()
            self.textEdit.setHtml(txt_file)

    def image_box_1(self, ey1):  # scrolling pictures
        g_ey = ey1
        self.lineEdit_134.setText(str(g_ey))
        set_label_ok = self.label_42
        img_path = imageDir
        spin_n = self.spinBox_4
        img_visual(self, g_ey, set_label_ok, img_path, spin_n)
        return g_ey

    def spin_box_ch_1(self):  # Function that is work by scrolling the Scroll Wheel
        addr_le2 = [self.lineEdit_108]  # testing
        data_order2 = txt_screen(self, addr_le2)  #
        g_ex2 = int(self.lineEdit_133.text())
        lab_x2 = [self.label_37]
        txt_screen_output(self, data_order2, g_ex2, list_ed, lab_x2)
        return ()

    def text_ch(self,
                ez):  # A function that is triggered when the text in the first input window is changed
        g_ez = ez
        # ***************Checking the picture file ID is standard by resolution and type
        g_ey = int(self.lineEdit_134.text())
        lis_files = os.listdir(imageDir)  # imageDir which folder to look in
        lis_files.sort()  # sort directories alphabetically
        img_file_name = self.lineEdit_132.text()  #
        if img_file_name == '':  # check if images where normalized before
            img_file_name = lis_files[g_ey]  #
        img_file_full = imageDir + '/' + img_file_name  # imageDir
        img1 = cv2.imread(img_file_full)
        height, width, channel = img1.shape
        name_suffix = img_file_name.split('.')[-1]  # here I split by dot and select the file extension
        if (width <= 720) and (name_suffix == 'jpeg'):  #
            # We increase the first letter, split by first name and patronymic by a space and increase the first letter
            g_ez_c = name_capitalize_q(self, g_ez)  #
            self.lineEdit_22.blockSignals(True)
            self.lineEdit_22.setText(g_ez_c)
            self.lineEdit_22.blockSignals(False)
            self.list_iof_c(g_ez_c)  # Search for partially matching names
            addr_le3 = [self.lineEdit_125]
            data_order3 = txt_screen(self, addr_le3)
            g_ex3 = 0
            self.centralSpinPoint = g_ex3  #
            lab_x3 = [self.label_37]
            txt_screen_output(self, data_order3, g_ex3, list_ed, lab_x3)
        else:  #
            text2view = 'File- ' + img_file_full + ' is not standard. Standardize it with Graphic Editor'
            self.label_46.setText(text2view)
            return ()
        return ()

    def text_ch_1(self,
                  ez1):  # A function that is triggered when the text in the second input window is changed
        g_ez1 = ez1
        surname_str = g_ez1
        g_ez1 = name_capitalize_s(self, surname_str)  # surnames capitalization
        self.lineEdit_29.blockSignals(True)
        self.lineEdit_29.setText(g_ez1)
        self.lineEdit_29.blockSignals(False)
        ez = str(self.lineEdit_22.text()) + ' ' + g_ez1
        self.list_iof_c(ez)  # Search for partially matching names
        addr_le3 = [self.lineEdit_125]
        data_order3 = txt_screen(self, addr_le3)
        g_ex3 = 0
        self.centralSpinPoint = g_ex3  #
        lab_x3 = [self.label_37]
        txt_screen_output(self, data_order3, g_ex3, list_ed, lab_x3)
        return

    def text_ch_3(self, ez3):  # inserts the document type at the first letter entered, before its number
        g_ez3 = ez3
        if g_ez3 == ' ':
            g_ez3 = ''
        if len(g_ez3) == 1:
            if g_ez3 == 'i':
                put3 = 'ID '
                self.lineEdit_33.blockSignals(True)
                self.lineEdit_33.setText(put3)
                self.lineEdit_33.blockSignals(False)
            elif g_ez3 == 'p':
                put3 = 'pass '
                self.lineEdit_33.blockSignals(True)
                self.lineEdit_33.setText(put3)
                self.lineEdit_33.blockSignals(False)
            else:
                put3 = 'i=ID or p=passport, enter the numbers after '
                self.lineEdit_33.blockSignals(True)
                self.lineEdit_33.setText(put3)
                self.lineEdit_33.blockSignals(False)
        else:
            self.lineEdit_33.blockSignals(True)
            self.lineEdit_33.setText(g_ez3)
            self.lineEdit_33.blockSignals(False)
        return ()

    def text_ch_4(self, ez4):  # Document issue date
        g_ez4 = ez4
        g_ez02 = g_ez4
        line_edit_number2 = self.lineEdit_23
        self.auto_data(g_ez02, line_edit_number2)
        return ()

    def text_ch_4_v(self, ez4v):  # the document is valid until
        g_ez4_v = ez4v
        g_ez01 = g_ez4_v
        line_edit_number1 = self.lineEdit_28
        self.auto_data(g_ez01, line_edit_number1)
        return ()

    def auto_data(self, g_ez0, line_edit_number):  # this function assists by entering the date
        if g_ez0 == ' ':
            g_ez0 = ''
        if len(g_ez0) == 2:
            if not g_ez0.isdigit():
                line_edit_number.blockSignals(True)
                line_edit_number.setText('Must be a number')
                line_edit_number.blockSignals(False)
            put4 = g_ez0 + '-'
            line_edit_number.blockSignals(True)
            line_edit_number.setText(put4)
            line_edit_number.blockSignals(False)
        elif len(g_ez0) == 5:
            put4 = g_ez0 + '-20'
            line_edit_number.blockSignals(True)
            line_edit_number.setText(put4)
            line_edit_number.blockSignals(False)
        return ()

    def text_ch_5(self, ez5):  # Autocomplete country name
        g_ez5 = ez5
        countries = {('BG', 'Bulgaria'): ['b', 'B'], ('ES', 'Spain'): ['s', 'S', 'e', 'E'],
                     ('PL', 'Poland'): ['p', 'P'], ('IT', 'Italy'): ['i', 'I'], ('l', 'l'): ['l', 'L']}
        dict_keys = countries.keys()
        if (g_ez5 == ' ') or (g_ez5 == ''):
            g_ez5 = ''
            put5 = ''
            self.lineEdit_27.blockSignals(True)
            self.lineEdit_27.setText(put5)
            self.lineEdit_27.blockSignals(False)
            self.label_46.setText('input first letter country name ')
            return
        if (g_ez5 != 'l') and (len(g_ez5) == 1):
            for country_key in dict_keys:
                country_letters = countries[country_key]
                for one_letter in country_letters:
                    if (g_ez5 == one_letter) and (g_ez5 != 'l'):
                        put5 = country_key[0]
                        self.lineEdit_27.blockSignals(True)
                        self.lineEdit_27.setText(put5)
                        self.lineEdit_27.blockSignals(False)
                        self.label_46.setText(country_key[1])
                        return
                self.label_46.setText('undefined:  b,lv,lt,s,p,i Will be entered without auto-filling')
            return
        elif (g_ez5 == 'l') and (len(g_ez5) == 1):
            self.label_46.setText('letter "l", input second letter to determine country')
        if len(g_ez5) == 2:
            if (g_ez5 == 'lv') or (g_ez5 == 'Lv'):
                put5 = 'LV'
                self.lineEdit_27.blockSignals(True)
                self.lineEdit_27.setText(put5)
                self.lineEdit_27.blockSignals(False)
                self.label_46.setText('Latvia')
                return
            elif (g_ez5 == 'lt') or (g_ez5 == 'Lt'):
                put5 = 'LT'
                self.lineEdit_27.blockSignals(True)
                self.lineEdit_27.setText(put5)
                self.lineEdit_27.blockSignals(False)
                self.label_46.setText('Lithuania')
                return
        return

    def text_ch_6(self, ez6):  # address input in capital letters
        g_ez6 = ez6
        put6 = g_ez6.upper()
        self.lineEdit_26.blockSignals(True)
        self.lineEdit_26.setText(put6)
        self.lineEdit_26.blockSignals(False)
        return ()

    def name_capitalize_1(self):  #
        name_str = str(self.lineEdit_22.text())  #
        # name_first_c   first name and middle name ( if's need) corrected, starting with the first letter
        name_first_c = ''
        # name_sec_c surnames corrected, starting with a capital letter
        # name_c output variable for the name/patronymic name - or only the first name, if a not required
        name_sec_c = 'zzz'  # better so
        if not name_str:  # If Name field is empty
            self.label_46.setText('Empty name')  #
            name_str = 'Empty name'  #
        name_first_sec = name_str.split()  # if the name is entered, it is split into parts by spaces, if any
        name_first = name_first_sec[0]  # first is Name
        name_first_c = str(name_first.capitalize()).strip()  #
        name_sec_counter = 0
        try:  # if the middle name was not entered, the second word will not be in the list, this leads to an error
            name_sec = name_first_sec[1]
        except IndexError:  # we exclude it by assigning an empty space immediately for the capitalized patronymic
            name_sec_counter = 1
            name_sec_c = ' '  #
        if name_sec_counter != 1:  # if the middle name was not processed, then we process the middle name as usual
            name_sec = name_first_sec[1]  # second element - middle name
            name_sec_c = str(name_sec.capitalize()).strip()  #
        if name_sec_c == ' ':
            name_c = name_first_c
        else:
            name_c = name_first_c + ' ' + name_sec_c
        self.lineEdit_22.blockSignals(True)
        self.lineEdit_22.setText(name_c)
        self.lineEdit_22.blockSignals(False)
        self.lineEdit_29.setFocus()
        return ()

    def click_method_33(self):  # Starts with a capital letter Last name when entered by Enter
        surname = str(self.lineEdit_29.text())  #
        surname_c = str(surname.capitalize()).strip()  #
        self.lineEdit_29.blockSignals(True)
        self.lineEdit_29.setText(surname_c)
        self.lineEdit_22.blockSignals(False)
        self.lineEdit_33.setFocus()
        return

    def click_method_34(self):
        self.lineEdit_23.setFocus()

    def click_method_35(self):
        self.lineEdit_18.setFocus()

    def click_method_36(self):
        self.lineEdit_19.setFocus()

    def click_method_37(self):
        self.lineEdit_28.setFocus()

    def click_method_39(self):
        self.lineEdit_26.setFocus()

    def click_method_40(self):
        self.lineEdit_27.setFocus()

    def click_method_41(self):
        self.lineEdit_24.setFocus()

    def click_method_42(self):
        self.label_46.setText('Click the Go! button to save your data')
        self.lineEdit_25.setFocus()

    def click_method_46(self):
        self.pushButton_21.setDefault(True)
        QtCore.QTimer.singleShot(0, self.pushButton_21.setFocus)
        return ()

    def data_file_write_1(
            self):  # without the possibility of rewriting. Collects from all windows into a file with calculated names
        """The function of recording collected data into a file named in the format FirstNamePatronymicLastName.info in
            a directory/folder with a name in the format First Name, Patronymic Last Name, which he himself creates.
            only in Latin letters."""
        name_c = str(self.lineEdit_22.text())  #
        # name_first = name_c.split()[0]  #
        # name_first_c = str(name_first.capitalize()).strip()  #
        surname_c = str(self.lineEdit_29.text())  #
        # text_str_10 this string is collected from all data entered in the form
        text_str_10 = 'Name ' + str(name_c).strip() + '\n' + 'Surname ' + str(
            surname_c).strip() + '\n' + 'IdNumber ' + str(self.lineEdit_33.text()).strip() + '\n' + 'IdDate ' + str(
            self.lineEdit_23.text()).strip() + '\n' + 'IdAddress ' + str(
            self.lineEdit_18.text()).strip() + '\n' + 'personalCode ' + str(
            self.lineEdit_19.text()).strip() + '\n' + 'Valid ' + str(
            self.lineEdit_28.text()).strip() + '\n' + 'Address ' + str(
            self.lineEdit_26.text()).strip() + '\n' + 'Country ' + str(
            self.lineEdit_27.text()).strip() + '\n' + 'Prof ' + str(
            self.lineEdit_24.text()).strip() + '\n' + 'Phone ' + str(self.lineEdit_25.text()).strip()
        # data is separated by spaces and newlines
        text_str_12 = str(name_c) + ' ' + str(surname_c) + '.info'
        # this variable is a file name consisting of the Full Name with the addition of .info at the end
        text_str_13 = str(name_c) + ' ' + str(surname_c)  # the folder name
        mypath_10 = infoPath + '/' + text_str_13  # in which folder to create the directory
        if not os.path.exists(mypath_10):  # with checking not to overwrite the existing one
            os.makedirs(mypath_10, 0o777)
        my_file_name = infoPath + '/' + text_str_13 + '/' + text_str_12  # path and name of the file to be written
        if not os.path.isfile(my_file_name):
            fi_odata_10 = open(my_file_name, 'w')  # the file is opened, then the prepared data is entered into it
            fi_odata_10.write(text_str_10)  #
            self.label_46.setText('Person' + ' ' + str(name_c) + ' ' + str(surname_c) + ' ' + 'is added')
        else:
            self.label_46.setText('a .info file with this name already exists')
            return ()
        return ()

    def click_method_21(self):  # Go ->
        # data from lineEd is entered and written into a file with the name NameMediumSurname and extension .info.
        # Safe write that cannot overwrite an existing file
        self.data_file_write_1()  # the .info data file and the corresponding folder are written
        '''Here the image file is recorded, with name like NameMiddleSurname_ID.jpeg into a folder called same.'''
        g_ey = int(self.lineEdit_134.text())  # for variant with g_ey
        lis_files = os.listdir(imageDir)  #
        lis_files.sort()  # sort
        img_file_name = lis_files[g_ey]  # variant to find name must be good
        # img_file_name = self.lineEdit_132.text()  # variant
        img_file_full = imageDir + '/' + img_file_name
        suffix_id = str(self.lineEdit_33.text()).split()
        suffix = suffix_id[0]
        img_file_dest = infoPath + '/' + str(self.lineEdit_22.text()) + ' ' + str(
            self.lineEdit_29.text()) + '/' + str(self.lineEdit_22.text()) + ' ' + str(
            self.lineEdit_29.text()) + ' ' + str(suffix) + '.jpeg'
        if not os.path.isfile(img_file_dest):  # Not that file in path
            shutil.copyfile(img_file_full, img_file_dest)
            self.label_46.setText(
                'Image=' + ' ' + str(self.lineEdit_22.text()) + ' ' + str(self.lineEdit_29.text()) + ' ' + str(
                    suffix) + '.jpeg' + ' ' + 'was moved at ' + infoPath)
            img_file_dest = trashDir + '/' + str(img_file_name)
            shutil.move(img_file_full, img_file_dest)
            # os.remove(img_file_full)
            list_dirs = os.listdir(infoPath)  #
            self.lineEdit_161.setText(str(len(list_dirs)))  # top scrolling
        else:
            self.label_46.setText('a .jpeg file with this name already exists')
        self.label_46.setText('all client data and .jpeg file are saved, can press Next person or eXit ')
        return ()

    @staticmethod
    def data_inv(self, data_app):
        day, month, year = (int(x) for x in data_app.split('-'))
        yyyymmdd1 = str(year) + '-' + str(month) + '-' + str(day)
        return yyyymmdd1

    def click_method_24(self):  # compleTe
        if self.checkBox_18.isChecked():  #
            self.click_edi_ted()
            self.click_go_select()  #
            activation_txt(self)
        return ()

    def click_method_19(self):  # New Client
        l_ned: QLineEdit | Any
        for l_ned in [self.lineEdit_18, self.lineEdit_19, self.lineEdit_22, self.lineEdit_23, self.lineEdit_24,
                      self.lineEdit_25, self.lineEdit_26, self.lineEdit_27, self.lineEdit_28, self.lineEdit_29,
                      self.lineEdit_33]:  #
            l_ned.blockSignals(True)
            l_ned.setText('')
            l_ned.blockSignals(False)
        self.centralSpinPoint = int(0)
        self.spinBox_4.blockSignals(True)
        self.spinBox_4.setProperty('value', self.centralSpinPoint)  #
        self.spinBox_4.blockSignals(False)
        set_label_ok3 = self.label_42
        img_path3 = imageDir
        spin_n3 = self.spinBox_4
        g_ey3 = int(self.lineEdit_134.text())
        img_visual(self, g_ey3, set_label_ok3, img_path3,
                   spin_n3)  # view the first image from list, because you can reset the parameters for a new client,
        self.label_46.setText('is ready for new person')
        activation_graph(self)
        self.label_46.setText('You can enter new client data from the picture')
        self.lineEdit_113.setText('')
        # *********************************************a text display node
        list_dirs_method_1(self)  # List FullNames
        addr_le5 = [self.lineEdit_108]
        data_order5 = txt_screen(self, addr_le5)  # Prepare screen
        g_ex3 = self.centralSpinPoint  # set to the beginning of the scroll sheet
        self.spinBox_2.valueChanged.connect(self.spin_box_ch_1)  #
        lab_x5 = [self.label_37]
        g_ex5 = int(self.lineEdit_133.text())
        txt_screen_output(self, data_order5, g_ex5, list_ed, lab_x5)  # display
        return ()

    def click_method_29(self):  # Previous
        if self.checkBox_18.isChecked():  # If the graphic mode
            self.click_previous()
        return ()

    def ed_graph(self):  # Launch Graphix mode
        if self.checkBox_18.isChecked():  #
            activation_graph(self)
            self.label_46.setText(
                'Mark the ID corners in the picture for normalization and correction. From the top left clockwise ')
        else:  #
            activation_txt(self)
            lis_files = os.listdir(imageDir)  # start testing -is the image right type and size
            lis_image = sorted(lis_files)  # alphabetical order files in Img
            g_ey = int(self.lineEdit_134.text())
            img_file_name = lis_image[g_ey]
            img_file_full = imageDir + '/' + img_file_name  # imageDir
            img1 = cv2.imread(img_file_full)
            height, width, channel = img1.shape
            name_suffix = img_file_name.split('.')[-1]  # here I split by dot and select the file extension
            if not ((width <= 720) and (name_suffix == 'jpeg')):  #
                text2view = 'File- ' + img_file_full + ' is not standard. Standardize it with Graphic Editor'
                self.label_46.setText(text2view)
            else:
                self.label_46.setText('can enter new client data from the picture')
            lis_files = os.listdir(Temp)  #
            len_temp = len(lis_files)
            i = 0
            while i < len_temp:  #
                img_file_temp = Temp + '/' + lis_files[i]  #
                os.remove(img_file_temp)  # cleared Tmp file
                i += 1
            # testing g_ey4 = int(self.lineEdit_134.text())
            # set_label_ok4 = self.label_42
            # img_path4 = imageDir  # images from
            # spin_n4 = self.spinBox_4  # spin images
            # img_visual(self, g_ey4, set_label_ok4, img_path4, spin_n4)
            self.lineEdit_22.setFocus()  # Focus is set to the first window - Name
        return ()

    def click_edi_ted(self):  # view ediTed Graphic editor
        img1pdf = None
        img_file_name1 = None
        d_points = self.lineEdit_113.text()
        len_points = len(ast.literal_eval(d_points))
        if (len_points == 4) or (len_points == 8):  # Protection from starts until the points are completely filled
            lis_files = os.listdir(Temp)  #
            len_temp = len(lis_files)
            if len_temp > 7:  #
                i = 0
                while i < 8:  # If there are all 8 dots for ID, erase all 8 temp files
                    temp_name = Temp + '/temp' + str(i) + '.jpeg'
                    os.remove(temp_name)
                    i += 1
            else:  # For passport erase 4 temp files. The rollback becomes impossible
                i = 0
                while i < 4:  #
                    temp_name = Temp + '/temp' + str(i) + '.jpeg'
                    os.remove(temp_name)
                    i += 1
            img_file_temp = Temp + '/temp.jpeg'  #
            os.remove(img_file_temp)  # erase temp file
            if (self.checkBox_18.isChecked()) and (self.radioButton_19.isChecked()):  # ID execute
                # ***************************if ID edit - 2 images
                edi_po_d = self.lineEdit_113.text()
                edit_points_d = ast.literal_eval(edi_po_d)
                xy1 = edit_points_d[0]  # Point coordinates
                xy2 = edit_points_d[1]
                xy3 = edit_points_d[2]
                xy4 = edit_points_d[3]
                xy5 = edit_points_d[4]
                xy6 = edit_points_d[5]
                xy7 = edit_points_d[6]
                xy8 = edit_points_d[7]
                g_ey = self.spinBox_4.value()  #
                lis_files = os.listdir(imageDir)  #
                lis_files.sort()  # sort
                img_file_name2 = lis_files[g_ey]  # take the name of the second file by number spinBox_4 from the list
                lis_files_t = os.listdir(Temp)  #
                lis_files_t.sort()  # sort
                len_files_t = len(lis_files_t)
                if len_files_t == 1:
                    img_file_name1 = img_file_name2  # so we can use for passport two or one image
                elif (img_file_name2 == lis_files_t[0]) and (len_files_t == 2):  #
                    img_file_name1 = lis_files_t[1]
                elif (img_file_name2 != lis_files_t[0]) and (len_files_t == 2):  #
                    img_file_name2 = lis_files_t[1]
                    img_file_name1 = lis_files_t[0]  # because we knew img_file_name2, possible find name other in Temp
                img_file_temp1 = Temp + '/' + img_file_name1  #
                img_file_temp2 = Temp + '/' + img_file_name2  #
                # *****************work with pdf
                name_suffix1 = '.' + img_file_temp1.split('.')[
                    -1]  # split by dot and select name extensions. Then repair dot
                if name_suffix1 == '.pdf':  # convert pdf to jpeg file1
                    img1pdf = convert_from_path(img_file_temp1)
                    os.remove(img_file_temp1)  # erase tmp file pdf
                    img_file_temp1 = ','.join(img_file_temp1.split('.')[:-1]) + '.jpeg'  #
                    img1pdf[0].save(img_file_temp1, 'JPEG')
                name_suffix2 = '.' + img_file_temp2.split('.')[-1]  #
                if name_suffix2 == '.pdf':  #
                    if len_files_t > 1:  #
                        img2pdf = convert_from_path(img_file_temp2)
                        os.remove(img_file_temp2)  # erase tmp file pdf
                    else:  # if do from one image
                        img2pdf = img1pdf  #
                    img_file_temp2 = ','.join(img_file_temp2.split('.')[:-1]) + '.jpeg'  #
                    img2pdf[0].save(img_file_temp2, 'JPEG')
                # *******************First image
                # coefficient size correction  xy
                img_i1 = cv2.imread(img_file_temp1)
                height, width, channel = img_i1.shape
                if int(height / (width / Shir)) < Vys:  #
                    k_del = width / Shir
                else:  #
                    k_del = height / Vys
                list_xy2 = []
                list_xy = [xy1, xy2, xy3, xy4, xy5, xy6, xy7, xy8]
                for xy in list_xy:  #
                    if (xy == xy1) or (xy == xy2) or (xy == xy3) or (xy == xy4):  #
                        img_i1 = cv2.imread(img_file_temp1)
                        height, width, channel = img_i1.shape
                        if int(height / (width / Shir)) < Vys:  #
                            k_del = width / Shir
                        else:  #
                            k_del = height / Vys
                        xy = [xy[0] * k_del, xy[1] * k_del]
                        list_xy2.append(xy)
                    else:
                        img_i2 = cv2.imread(img_file_temp2)
                        height, width, channel = img_i2.shape
                        if int(height / (width / Shir)) < Vys:  #
                            k_del = width / Shir
                        else:  #
                            k_del = height / Vys
                        xy = [xy[0] * k_del, xy[1] * k_del]
                        list_xy2.append(xy)
                # *******************elimination of perspective distortions
                xy1 = list_xy2[0]  # Point coordinates
                xy2 = list_xy2[1]
                xy3 = list_xy2[2]
                xy4 = list_xy2[3]
                xy5 = list_xy2[4]
                xy6 = list_xy2[5]
                xy7 = list_xy2[6]
                xy8 = list_xy2[7]
                # first image *******************8
                img_i1 = cv2.imread(img_file_temp1)
                height, width, channel = img_i1.shape
                pts1 = np.float32([xy1, xy2, xy4, xy3])
                pts2 = np.float32([[0, 0], [width, 0], [0, int(height / 2)], [width, int(height / 2)]])
                m = cv2.getPerspectiveTransform(pts1, pts2)
                img_i1_t = cv2.warpPerspective(img_i1, m, (width, int(height / 2)))  # Image processing1
                # *****************normalisation of size*****************************
                img1_s = cv2.resize(img_i1_t, (Shir, int(Vys / 2)),
                                    interpolation=cv2.INTER_CUBIC)  # Zoom to fit on screen
                # *******************Second image
                img_i2 = cv2.imread(img_file_temp2)
                height, width, channel = img_i2.shape
                # *******************elimination of perspective distortions
                pts1 = np.float32([xy5, xy6, xy8, xy7])
                pts2 = np.float32([[0, 0], [width, 0], [0, int(height / 2)], [width, int(height / 2)]])
                m = cv2.getPerspectiveTransform(pts1, pts2)
                img_i2_t = cv2.warpPerspective(img_i2, m, (width, int(height / 2)))  # Image processing 2
                # *****************size normalization*****************************
                img2_s = cv2.resize(img_i2_t, (Shir, int(Vys / 2)),
                                    interpolation=cv2.INTER_CUBIC)  # Zoom to fit on screen
                img_st = np.concatenate((img1_s, img2_s), axis=0)  # combining two pictures
                # ********************output on display
                img_file_temp = Temp + '/temp.jpeg'  # image made from 2 images for pass
                cv2.imwrite(img_file_temp, img_st)  # write this file to Temp as temp.jpeg
                self.pixmap = QPixmap(img_file_temp)  # image output
                self.label_42.setPixmap(self.pixmap)
                self.label_46.setText('The picture temp.jpeg is prepared and displayed, save with the Go => button!')
            elif (self.checkBox_18.isChecked()) and (self.radioButton_20.isChecked()):  # passport
                # ******************if processing one picture - passport
                edi_po_d = self.lineEdit_113.text()
                edit_points_d = ast.literal_eval(edi_po_d)
                xy1 = edit_points_d[0]
                xy2 = edit_points_d[1]
                xy3 = edit_points_d[2]
                xy4 = edit_points_d[3]
                lis_files_t = os.listdir(Temp)  #
                img_file_name1 = lis_files_t[0]
                img_file_temp1 = Temp + '/' + img_file_name1
                name_suffix1 = '.' + img_file_temp1.split('.')[-1]  #
                if name_suffix1 == '.pdf':  #
                    img1pdf = convert_from_path(img_file_temp1)
                    os.remove(img_file_temp1)  # erase tmp
                    img_file_temp1 = ','.join(img_file_temp1.split('.')[:-1]) + '.jpeg'  #
                    img1pdf[0].save(img_file_temp1, 'JPEG')
                img_p = cv2.imread(img_file_temp1)
                height, width, channel = img_p.shape
                # calculation of the correction factor xy
                if int(height / (width / Shir)) < Vys:  #
                    k_del = width / Shir
                else:  #
                    k_del = height / Vys
                list_xy = [xy1, xy2, xy3, xy4]
                list_xy2 = []
                for xy in list_xy:  #
                    img_i1 = cv2.imread(img_file_temp1)
                    height, width, channel = img_i1.shape
                    if int(height / (width / Shir)) < Vys:  #
                        k_del = width / Shir
                    else:  #
                        k_del = height / Vys
                    xy = [xy[0] * k_del, xy[1] * k_del]
                    list_xy2.append(xy)
                # *******************elimination of perspective distortions
                xy1 = list_xy2[0]  # Point coordinates
                xy2 = list_xy2[1]
                xy3 = list_xy2[2]
                xy4 = list_xy2[3]
                pts1 = np.float32([xy1, xy2, xy4, xy3])
                pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
                m = cv2.getPerspectiveTransform(pts1, pts2)
                img_p_t = cv2.warpPerspective(img_p, m, (width, height))
                # *****************size normalization*****************************
                img_ps = cv2.resize(img_p_t, (Shir, Vys2),
                                    interpolation=cv2.INTER_CUBIC)  # Zoom to fit on screen
                # ********************display
                img_file_temp = Temp + '/temp.jpeg'
                cv2.imwrite(img_file_temp, img_ps)  # write corrected image to Temp as temp.jpeg
                self.pixmap = QPixmap(img_file_temp)  # image output
                self.label_42.setPixmap(self.pixmap)
                self.label_46.setText('picture temp.jpeg is prepared and displayed, save with the save and Go button!')
        else:  # If the input of picture points is not completed
            self.label_46.setText('The coordinates of the corners for transformation have not yet been entered!')
        return ()

    def click_previous(self):  #
        lis_files = os.listdir(Temp)  #
        len_temp = len(lis_files)
        temp0 = 0
        i = 0
        while i < len_temp:
            if lis_files[i] == 'temp0.jpeg':
                temp0 = 1
            i += 1
        if temp0 == 1:  # Rollback at the point entry area
            edi_po_d = self.lineEdit_113.text()
            if edi_po_d == '':  #
                self.label_46.setText('In this case, rollback is not possible')
                return ()
            edit_points_d = ast.literal_eval(edi_po_d)
            d_key = len(edit_points_d)
            del edit_points_d[d_key - 1]
            self.lineEdit_113.setText(str(edit_points_d))
            img_temp = Temp + '/temp' + str(d_key - 1) + '.jpeg'  #
            os.remove(img_temp)  # deleted the last tmp file
            self.label_46.setText('The corners input has been rolled back one position. Continue entering')
            if d_key == 1:  #
                img_temp = Temp + '/temp.jpeg'  #
            else:  #
                img_temp = Temp + '/temp' + str(d_key - 2) + '.jpeg'  #
            self.pixmap = QPixmap(img_temp)  # image setup and output
            self.label_42.setPixmap(self.pixmap)
        else:  #
            self.lineEdit_113.setText('')
            i = 0
            while i < len_temp:  #
                img_temp_full = Temp + '/' + lis_files[i]
                os.remove(img_temp_full)  # img_temp error?
                i += 1
            img_file_temp = Temp + '/' + 'temp.jpeg'
            self.pixmap = QPixmap(img_file_temp)  # image output
            self.label_42.setPixmap(self.pixmap)
            self.label_46.setText('rolled back from viewing processed images. Continue with entering angles')
        return ()

    def click_go_select(self):  # Go! on graphic editor
        lis_files = os.listdir(Temp)  #
        len_temp = len(lis_files)
        i = 0
        while i < len_temp:  # Has a correction been made?
            if lis_files[i] == 'temp0.jpeg':  #
                self.label_46.setText('corrections corners are not selected, You need select and make a "compleTe"')
                return ()
            i += 1
        if self.checkBox_18.isChecked():  #
            if lis_files[0] != 'temp.jpeg':  # name_file
                name_file = lis_files[0]
            else:
                name_file = lis_files[1]
            name_file_pdf = ','.join(name_file.split('.')[:-1]) + '.pdf'  #
            name_file_jpg = ','.join(name_file.split('.')[:-1]) + '.jpeg'  #
            img_file_full = imageDir + '/' + name_file_jpg  #
            if not os.path.isfile(img_file_full):  #
                img_file_full = imageDir + '/' + name_file_pdf  #
                img_file_dest = trashDir + '/' + name_file_pdf  #
            else:
                img_file_full = imageDir + '/' + name_file_jpg  #
                img_file_dest = trashDir + '/' + name_file_jpg  #
            name_file = name_file_jpg
            shutil.move(img_file_full, img_file_dest)  # Send to trash with the ability to rewrite
            # os.remove(img_file_full)  # erased file in imageDir
            img_file_full = Temp + '/' + name_file  #
            os.remove(img_file_full)  # erase same from Temp
            img_file_full = Temp + '/temp.jpeg'  # This file will replace the original one in the folder imageDir
            img_file_dest = imageDir + '/' + name_file  #
            self.lineEdit_132.setText(str(name_file))  # save conditioned file name
            prepared_file_name = name_file
            shutil.move(img_file_full, img_file_dest)  # From Temp/temp.jpeg to Img/name_file
            # os.remove(img_file_full)  # erase tmp file
            lis_files = os.listdir(Temp)  #
            if (self.radioButton_19.isChecked()) and (len(lis_files) > 0):  # If ID, then source files two
                name_file = lis_files[0]
                name_file_pdf = ','.join(name_file.split('.')[:-1]) + '.pdf'  #
                name_file_jpg = ','.join(name_file.split('.')[:-1]) + '.jpeg'  #
                img_file_full = imageDir + '/' + name_file_jpg  #
                if not os.path.isfile(img_file_full):  #
                    img_file_full = imageDir + '/' + name_file_pdf  #
                    img_file_dest = trashDir + '/' + name_file_pdf  #
                    name_file = name_file_pdf
                else:
                    img_file_full = imageDir + '/' + name_file_jpg  #
                    img_file_dest = trashDir + '/' + name_file_jpg  #
                    name_file = name_file_jpg
                shutil.move(img_file_full, img_file_dest)  # In Trash send
                img_file_full = Temp + '/' + name_file  #
                os.remove(img_file_full)  # erase same file at Temp
                # *********Resetting to new client
            self.pushButton_8.blockSignals(True)
            self.pushButton_8.setChecked(False)
            self.pushButton_8.blockSignals(False)
            self.pushButton_21.blockSignals(True)
            self.pushButton_21.setChecked(False)
            self.pushButton_21.blockSignals(False)
            self.lineEdit_113.setText('')
            self.label_46.setText(
                'The graphic file was successfully edited and replaced one or two (for ID) source files.'
                ' You can enter document data')
            self.checkBox_18.blockSignals(True)
            self.checkBox_18.setChecked(False)
            self.checkBox_18.blockSignals(False)
        return ()

    def list_iof_c(self, g_ez):  # function to compare the lineEdit with a list of Full names
        list_iof = os.listdir(infoPath)  # which folder to look in
        list_iof.sort()  # sort
        num_records = len(list_iof)  # number of clients
        len_gez = len(str(g_ez))  # length of the entered fragment
        i_list_iof = []  # Match list
        i_count = 0
        while i_count < num_records:  # loop iterate through all records
            i_count_iof = str(list_iof[i_count])
            if (str(g_ez)) == i_count_iof[0: len_gez]:  # Comparison of written with existing
                i_list_iof.append(i_count_iof)
            i_count += 1
        self.lineEdit_125.setText(','.join(i_list_iof))
        return i_list_iof


if __name__ == "__main__":
    #   import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
