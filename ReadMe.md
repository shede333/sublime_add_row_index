
[中文说明，点这](#中文ReadMe)


# English

sublime text 3 plugin，add digit and letter index in the beginning of every row

**notice：**

This Plugin (include `the shortcut key` and `command palette`) is invalid when the number of selected row <= 1.

---
## Usage


### Method 1: Shortcut key

shortcut key **default** setting：**sublime text** -> **Preferences** -> **Package Settings** -> **AddRowIndex** -> **Key Bindings – Default**   

shortcut key **custom** setting：**sublime text** -> **Preferences** -> **Package Settings** -> **AddRowIndex** -> **Key Bindings – User**   

#### Shortcut key 1：

- OS X: <kbd>cmd+ctrl+x</kbd>
- Linux: <kbd>ctrl+alt+x</kbd>
- Windows: <kbd>ctrl+alt+x</kbd>

example image：

![image](https://raw.githubusercontent.com/shede333/image-link/master/addRowIndex/gif_insert_char_after_cursor_and_esc.gif)

####  Shortcut key 2：

- OS X: <kbd>cmd+ctrl+**shift**+x</kbd>
- Linux: <kbd>ctrl+alt+**shift**+x</kbd>
- Windows: <kbd>ctrl+alt+**shift**+x</kbd>

show popup menu, then use **<kbd>arrow-key(up/down)</kbd>** to select，  
example image：

![image](https://raw.githubusercontent.com/shede333/image-link/master/addRowIndex/gif_kbd_show_select.gif)

### Method 2：use Command Palette

**menu** -> **Tool** -> **Command Palette**，(or use shortcut-key open `Command Palette`)

input `add row index` in `Command Palette` , rather `enter`

![image](https://raw.githubusercontent.com/shede333/image-link/master/addRowIndex/gif_show_command_palette.gif)

1. **command-1** `AddRowIndex: add row index` : According to `Plugin Params Of Setting` ,insert digit in  the beginning of every row
2. **command-2** `AddRowIndex: add row index, 0,1,2,3...` : insert：0,1,2,3...
3. **command-3** `AddRowIndex: add row index, 1,2,3,4...` : insert：1,2,3,4...
4. **command-4** `AddRowIndex: add row index, a,b,c,d...` : insert：a,b,c,d...z，When > z, don`t insetrt letter
5. **command-5** `AddRowIndex: add row index, A,B,C,D...` : insert：A,B,C,D...Z，When > Z, don`t insetrt letter
6. **command-6** `AddRowIndexWithPopup: add row index with popup menu` : show popup menu, is equal to `Shortcut key 2`(show popup menu)

---
## Setting

Default Setting：**sublime text** -> **Preferences** -> **Package Settings** -> **AddRowIndex** -> **Settings – Default**  

Custom setting：**sublime text** -> **Preferences** -> **Package Settings** -> **AddRowIndex** -> **Settings – User**

**setting option：**

original text of test case, all texts is selected：

```
first row
second row
third row

```

#### add_digit_index_start_number

default value: 0

`start number` of inserted digit

when `add_digit_index_start_number` is 0, after insert digit index::


```
0first row
1second row
2third row

```

when `add_digit_index_start_number` is 1, after insert digit index::


```
1first row
2second row
3third row

```

	
#### add_digit_index_step

default value: 1

digit step

when `add_digit_index_step` is 1, after insert digit index::


```
0first row
1second row
2third row

```

when `add_digit_index_step` is 2, after insert digit index::


```
0first row
2second row
4third row

```

	
#### add_digit_index_is_parse_first_row

default value: true

search digit in beginning of first row, if have digit, use this digit as `add_digit_index_start_number`

original text of test case, all texts is selected：

```
  2 first row
second row
third row

```

when `add_digit_index_is_parse_first_row` is true, after insert digit index:

`2` is detected in beginning of the firt row, `add_digit_index_start_number` is set to `2`

```
  2 first row
3second row
4third row

```

when `add_digit_index_is_parse_first_row` is false, after insert digit index:

ignore didit `2` in beginning of the firt row, `add_digit_index_start_number` is default value (`2`)

```
0  2 first row
1second row
2third row

```

#### change_cursor_location_after_insert_index

default value: true
    
insert the cursor at the back of the index number

![image](https://raw.githubusercontent.com/shede333/image-link/master/addRowIndex/gif_insert_char_after_cursor_and_esc.gif)

---
## Notice：

This Plugin (include `the shortcut key` and `command palette`) is valid when the number of selected row > 1.


![image](https://raw.githubusercontent.com/shede333/image-link/master/addRowIndex/gif_select_much_row.gif)

In addition, multiple rows with the cursor, this plugin is also valid :

![image](https://raw.githubusercontent.com/shede333/image-link/master/addRowIndex/gif_select_much_cursor.gif)





---







<h1 id="中文ReadMe">中文</h1>

sublime text 3 插件，给选中的每一行的行首增加数字索引，而且数字是递增的

**注意：**

当前选中的行数只有1行时，下面的方法1快捷键**不会生效**，方法2的**command Command Palette**里面也**不会**出现对应的选项

**选中的行数必须 >= 2**

---
## 使用

### 方法1：快捷键

快捷键 默认设置：**sublime text** -> **Preferences** -> **Package Settings** -> **AddRowIndex** -> **Key Bindings – Default**   

快捷键 自定义设置：**sublime text** -> **Preferences** -> **Package Settings** -> **AddRowIndex** -> **Key Bindings – User**   


#### 快捷键1：

- OS X: <kbd>cmd+ctrl+x</kbd>
- Linux: <kbd>ctrl+alt+x</kbd>
- Windows: <kbd>ctrl+alt+x</kbd>

如下图：

![image](https://raw.githubusercontent.com/shede333/image-link/master/addRowIndex/gif_insert_char_after_cursor_and_esc.gif)

#### 快捷键2：

- OS X: <kbd>cmd+ctrl+**shift**+x</kbd>
- Linux: <kbd>ctrl+alt+**shift**+x</kbd>
- Windows: <kbd>ctrl+alt+**shift**+x</kbd>

然后使用 <kbd>上、下方向键</kbd> 选择，如下图

![image](https://raw.githubusercontent.com/shede333/image-link/master/addRowIndex/gif_kbd_show_select.gif)

### 方法2：使用 Command Palette

menu -> Tool -> Command Palette，(或者使用快捷键打开Command Palette)

在弹出框 输入 __“add row index”__ ，回车即可

![image](https://raw.githubusercontent.com/shede333/image-link/master/addRowIndex/gif_show_command_palette.gif)

1. **command-1** `AddRowIndex: add row index` : 根据插件的设置，在每行的行首插入相应的数字索引
2. **command-2** `AddRowIndex: add row index, 0,1,2,3...` : 插入：0,1,2,3...
3. **command-3** `AddRowIndex: add row index, 1,2,3,4...` : 插入：1,2,3,4...
4. **command-4** `AddRowIndex: add row index, a,b,c,d...` : 插入：a,b,c,d...z，超出z的行，不插入字符
5. **command-5** `AddRowIndex: add row index, A,B,C,D...` : 插入：A,B,C,D...Z，超出Z的行，不插入字符
6. **command-6** `AddRowIndexWithPopup: add row index with popup menu` : 弹出选择菜单，等同于`快捷键 2`

---
## 设置说明

默认设置：**sublime text** -> **Preferences** -> **Package Settings** -> **AddRowIndex** -> **Settings – Default**  

自定义设置：**sublime text** -> **Preferences** -> **Package Settings** -> **AddRowIndex** -> **Settings – User**

**设置选项：**

下面文字为测试用例，假设下面的三行文字为**选中状态**，原文如下：

```
第一行
第二行
第三行

```

#### add_digit_index_start_number

默认值为：0

在每行的行首插入数字的时候的**起始数字**，  

当`add_digit_index_start_number`为0时，插入数字后的效果如下：


```
0第一行
1第二行
2第三行

```

当`add_digit_index_start_number`为1时，插入数字后的效果如下：


```
1第一行
2第二行
3第三行

```

	
#### add_digit_index_step

默认值为：1

在每行插入数字时，数字的`递增的步长`

当`add_digit_index_step`为1时，插入数字后的效果如下：


```
0第一行
1第二行
2第三行

```

当`add_digit_index_step`为2时，插入数字后的效果如下：


```
0第一行
2第二行
4第三行

```

	
#### add_digit_index_is_parse_first_row

默认值为：true

检测第一行的**行首**，是否有数字，有的话，使用此数字作为 `add_digit_index_start_number`

测试用例原文如下，假设下面的文件是**选中状态**：

```
  2 第一行
第二行
第三行

```

当`add_digit_index_is_parse_first_row`为 true 时，插入数字后的效果如下：  
这里检测到第一行的行首有数字**“2”**，所以就使用**2**做为起始数字


```
  2 第一行
3第二行
4第三行

```

当`add_digit_index_is_parse_first_row`为 false 时，插入数字后的效果如下：  
这里忽略了第一行的数字**2**，使用默认设置，从**0**开始计数

```
0  2 第一行
1第二行
2第三行

```

#### change_cursor_location_after_insert_index

默认值为：true
    
对每行插入数字后，在数字后面也插入光标，以便用户继续操作：插入其它符号，    
如果不需要再插入字符，那么使用`ESC`就可以取消光标

![image](https://raw.githubusercontent.com/shede333/image-link/master/addRowIndex/gif_insert_char_after_cursor_and_esc.gif)

---
## 注意：

如果要让该插件的`快捷键`或者`command Palette`生效，那么需要选择多行文本（即选择的行数 >= 2），  
否则的话，`快捷键`会无效，`command Palette`也不会显示可用的的选项

只要改行有选中的文本，那么改行就算是被选中，没必要把改行的文字全部选中，如下图：

![image](https://raw.githubusercontent.com/shede333/image-link/master/addRowIndex/gif_select_much_row.gif)

另外，光标多选也算，即只要本行有光标插入也可，如下图：

![image](https://raw.githubusercontent.com/shede333/image-link/master/addRowIndex/gif_select_much_cursor.gif)



[gif_select_much_cursor]: https://raw.githubusercontent.com/shede333/image-link/master/addRowIndex/gif_select_much_cursor.gif

[gif_select_much_row]: https://raw.githubusercontent.com/shede333/image-link/master/addRowIndex/gif_select_much_row.gif

[gif_insert_char_after_cursor_and_esc]: https://raw.githubusercontent.com/shede333/image-link/master/addRowIndex/gif_insert_char_after_cursor_and_esc.gif

[gif_show_command_palette]: https://raw.githubusercontent.com/shede333/image-link/master/addRowIndex/gif_show_command_palette.gif

[gif_kbd_show_select]: https://raw.githubusercontent.com/shede333/image-link/master/addRowIndex/gif_kbd_show_select.gif


