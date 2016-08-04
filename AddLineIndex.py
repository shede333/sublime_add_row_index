import sublime, sublime_plugin
import re


class AddLineIndexCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        row_num_arr = []
        for sel in self.view.sel():
            row_begin = self.view.rowcol(sel.begin())[0]
            row_end = self.view.rowcol(sel.end())[0]
            row_num_arr.extend(range(row_begin, row_end+1))
        # only one line, no handle
        if len(row_num_arr) <= 1:
            return

        first_number = 0
        first_line = self.view.substr(self.view.line(self.view.text_point(row_num_arr[0], 0)))
        first_line = first_line.strip()
        result = re.search("^\d+", first_line)
        # if first line has numbers, first_number use this number
        if result:
            first_number = int(result.group(0))+1
            row_num_arr.pop(0)
        # insert number in beginning of line
        for tmp_row in row_num_arr:
            self.view.insert(edit, self.view.text_point(tmp_row, 0), str(first_number))
            first_number += 1
