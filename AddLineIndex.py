import sublime, sublime_plugin
import re
import os


g_view = None
g_edit = None

def test(*result):
    print("done:", result)


def get_selected_rows(view=None):
    view = g_view if view == None else view
    row_num_arr = []
    for sel in view.sel():
        row_begin = view.rowcol(sel.begin())[0]
        row_end = view.rowcol(sel.end())[0]
        row_num_arr.extend(range(row_begin, row_end+1))
    return row_num_arr


def insert_digit_index(view=None, edit=None, row_num_list=[], first_number=0, index_step=1):
    # start insert number in beginning of line
    view = g_view if view == None else view
    edit = g_edit if edit == None else edit
    for tmp_row in row_num_list:
        view.insert(edit, view.text_point(tmp_row, 0), str(first_number))
        first_number += index_step


def insert_letter_index(row_num_list, first_letter, max_letter):
    # start insert letter in beginning of line
    for tmp_row in row_num_list:
        g_view.insert(g_edit, g_view.text_point(tmp_row, 0), first_letter)
        if first_letter < max_letter:
            first_letter = chr(ord(first_letter) + 1)
        else:
            break


def handle_user_popup_select(selected_index):
    first_number = 0
    if selected_index == -1:
        # 取消选择
        return
    elif selected_index <= 1:
        # 出入数字
        first_number = selected_index
        settings = sublime.load_settings("AddLineIndex.sublime-settings")
        index_step = settings.get("add_line_index_step", 1)
        insert_digit_index(row_num_list=get_selected_rows(), first_number=first_number, index_step=index_step)
    elif selected_index == 2:
        # 插入小写字母
        insert_letter_index(get_selected_rows(), "a", "z")
    elif selected_index == 3:
        # 插入大写字母
        insert_letter_index(get_selected_rows(), "A", "Z")
    
    
class AddLineIndex(sublime_plugin.TextCommand):
    def is_enabled(self):
        line_num = len(get_selected_rows(self.view))
        if line_num <= 1:
            print("Notice:Only when selected line num >= 2, AddLineIndex is enable!")
        return line_num > 1


class AddLineIndexCommand(AddLineIndex):
    def run(self, edit, first_number=-1):
        view = self.view
        # get local setting
        settings = sublime.load_settings("AddLineIndex.sublime-settings")
        index_start_num = settings.get("add_line_index_start_num", 0)
        index_step = settings.get("add_line_index_step", 1)
        index_is_check_first_num = settings.get("add_line_index_is_check_first_num", True)
        # get all selected row
        row_num_arr = get_selected_rows(view)
        # check setting: is need check first line number params
        if first_number == -1:
            # if command has params, not user setting params of first_number
            first_number = index_start_num
        if index_is_check_first_num:
            first_line = view.substr(view.line(view.text_point(row_num_arr[0], 0)))
            first_line = first_line.strip()
            result = re.search("^\d+", first_line)
            # if first line has numbers, first_number use this number
            if result:
                first_number = int(result.group(0))+1
                row_num_arr.pop(0)
        insert_digit_index(view, edit, row_num_arr, first_number, index_step)
        

class AddLineIndexWithPopupCommand(AddLineIndex):
    def run(self, edit):
        global g_edit
        global g_view
        g_edit = edit
        g_view = self.view

        selected_list = []
        selected_list.append("click select: 0,1,2,3...")
        selected_list.append("click select: 1,2,3,4...")
        selected_list.append("click select: a,b,c,d...")
        selected_list.append("click select: A,B,C,D...")
        self.view.show_popup_menu(selected_list, handle_user_popup_select)

