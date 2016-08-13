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


def get_plugin_setting():
    return sublime.load_settings("AddRowIndex.sublime-settings")


def insert_digit_index(view=None, edit=None, is_skip_first_row=False, row_num_list=[], first_number=0, index_step=1):
    # start insert number in beginning of line
    view = g_view if view == None else view
    edit = g_edit if edit == None else edit
    new_regions = []
    if is_skip_first_row:
        # skip first row
        first_line = view.substr(view.line(view.text_point(row_num_list[0], 0)))
        result = re.search("\d+", first_line)
        if result:
            text_point = view.text_point(row_num_list[0], result.end())
            new_regions.append(sublime.Region(text_point, text_point))
        row_num_list = row_num_list[1:]
        first_number += index_step
        
    for tmp_row in row_num_list:
        number_str = str(first_number)
        view.insert(edit, view.text_point(tmp_row, 0), number_str)
        text_point = view.text_point(tmp_row, len(number_str))
        new_regions.append(sublime.Region(text_point, text_point))
        first_number += index_step
    # change cursor location
    settings = get_plugin_setting()
    if settings.get("change_cursor_location_after_insert_index", True):
        regions = view.sel()
        regions.clear()
        regions.add_all(new_regions)



def insert_letter_index(view=None, edit=None, row_num_list=[], first_letter="a", max_letter="z"):
    # start insert letter in beginning of line
    view = g_view if view == None else view
    edit = g_edit if edit == None else edit
    new_regions = []
    inserted_letter = first_letter
    for tmp_row in row_num_list:
        view.insert(edit, view.text_point(tmp_row, 0), inserted_letter)
        text_point = view.text_point(tmp_row, len(inserted_letter))
        new_regions.append(sublime.Region(text_point, text_point))
        if inserted_letter < max_letter:
            inserted_letter = chr(ord(inserted_letter) + 1)
        else:
            break
    # change cursor location
    settings = get_plugin_setting()
    if settings.get("change_cursor_location_after_insert_index", True):
        regions = view.sel()
        regions.clear()
        regions.add_all(new_regions)


def handle_user_popup_select(selected_index):
    first_number = 0
    if selected_index == -1:
        # cancel select
        return
    elif selected_index <= 1:
        # insert digit
        first_number = selected_index
        # settings = get_plugin_setting()
        # index_step = settings.get("add_digit_index_step", 1)
        index_step = 1
        insert_digit_index(row_num_list=get_selected_rows(), first_number=first_number, index_step=index_step)
    elif selected_index == 2:
        # inset lower letter
        insert_letter_index(row_num_list=get_selected_rows(), first_letter="a", max_letter="z")
    elif selected_index == 3:
        # insert upper letter
        insert_letter_index(row_num_list=get_selected_rows(), first_letter="A", max_letter="Z")
    
    
class AddRowIndex(sublime_plugin.TextCommand):
    def is_enabled(self):
        row_num = len(get_selected_rows(self.view))
        if row_num <= 1:
            print("Notice:Only when selected row num >= 2, AddRowIndex is enable!")
        return row_num > 1


class AddRowIndexCommand(AddRowIndex):
    def run(self, edit, first_number=0, use_plugin_setting=True):
        view = self.view
        # get all selected row
        row_num_arr = get_selected_rows(view)
        is_skip_first_row = False
        index_step = 1
        if use_plugin_setting:
            # use plugin setting
            settings = get_plugin_setting()
            first_number = settings.get("add_digit_index_start_number", 0)
            index_step = settings.get("add_digit_index_step", 1)
            index_is_check_first_num = settings.get("add_digit_index_is_parse_first_row", True)

            if index_is_check_first_num:
                # search digit in beginning of first line
                first_line = view.substr(view.line(view.text_point(row_num_arr[0], 0)))
                first_line = first_line.strip()
                result = re.search("^\d+", first_line)
                # if first line has digit, first_number use this digit
                if result:
                    is_skip_first_row = True
                    first_number = int(result.group(0))
        insert_digit_index(view, edit, is_skip_first_row, row_num_arr, first_number, index_step)


class AddRowIndexWithLetterCommand(AddRowIndex):
    def run(self, edit, first_letter="a", max_letter="z"):
        insert_letter_index(self.view, edit, get_selected_rows(self.view), first_letter, max_letter)
      

class AddRowIndexWithPopupCommand(AddRowIndex):
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

