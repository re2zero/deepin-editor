# deepin-editor YAML 用例生成计划

## 1. 概述

基于 `文本编辑器V25-用例.xlsx` 中的 150 条测试用例，生成 YouQu YAML 格式自动化测试用例。

**源文件**: `autotest/casefile/文本编辑器V25-用例.xlsx`
**目标**: `autotest/yaml/` 下按功能模块分目录组织
**格式**: YAML (YouQu 2.17.2)

## 2. 统计

| 类别 | 数量 | 说明 |
|------|------|------|
| 总用例 | 150 | |
| 可自动化 | 131 | 生成完整 YAML 测试步骤 |
| 跳过 | 19 | 生成 `skip` 字段标记的 YAML |

**Skip 分布**:

| 跳过类别 | 数量 | 用例 ID | Skip 原因 |
|----------|------|---------|-----------|
| LINGLONG | 13 | 014-026 | skip-玲珑环境不支持自动化 |
| REBOOT | 4 | 055, 072, 100, 114 | skip-重启类场景需要letmego支持 |
| PERF | 1 | 045 | skip-性能压测类不支持自动化 |
| GESTURE | 1 | 143 | skip-触摸操作无法自动化 |

## 3. 应用信息

- **应用名**: deepin-editor
- **二进制路径**: `/home/zero/work/repo/github/deepin-editor/build/src/deepin-editor`
- **AT-SPI 注册名**: deepin-editor
- **DTK 框架**: DMainWindow, DTitlebar, DMenu (transient popup)
- **快捷键**: Ctrl+F(查找), Ctrl+H(替换), Ctrl+S(保存), Ctrl+A(全选), Ctrl+Z(撤销), Ctrl+Y(重做), Ctrl+P(打印), Ctrl+G(跳到行), Ctrl+/(注释), F11(全屏), F1(帮助), Ctrl+Shift+/(快捷键预览)

### 3.1 主菜单结构 (DTitlebarDWindowOptionButton 触发)

| 菜单项 (中文) | 源码 tr() key | 用途 |
|---------------|---------------|------|
| 新窗口 | New window | 新建窗口 |
| 新标签页 | New tab | 新建标签 |
| 打开文件 | Open file | 打开文件 |
| 保存 | Save | 保存 |
| 另存为 | Save as | 另存为 |
| 打印 | Print | 打印 |
| 切换主题 | Switch theme | 主题切换 |
| 设置 | Settings | 打开设置 |

### 3.2 编辑区右键菜单结构

| 菜单项 | 子菜单 | 源码 key |
|--------|--------|----------|
| 撤销 | | Undo |
| 重做 | | Redo |
| 剪切 | | Cut |
| 复制 | | Copy |
| 粘贴 | | Paste |
| 删除 | | Delete |
| 全选 | | Select All |
| 查找 | | Find |
| 替换 | | Replace |
| 跳到行 | | Go to Line |
| 开启/关闭只读模式 | | Turn on/off Read-Only mode |
| 添加注释/取消注释 | | Add/Remove Comment |
| 全屏/退出全屏 | | Fullscreen/Exit fullscreen |
| 在文件管理器中显示 | | Display in file manager |
| 语音朗读 | | Text to Speech |
| 语音听写 | | Speech to Text |
| 文本翻译 | | Translate |
| 列编辑模式 | | Column Mode |
| 添加书签/清除书签/上一个书签/下一个书签/清除所有书签 | | Add/Remove/Prev/Next/Clear All bookmark |
| 折叠所有层次/折叠当前层次/展开所有层次/展开当前层次 | | Fold/Unfold All/Current Level |
| 颜色标记 | 添加标记/标记所有/清除上次标记/清除所有标记 | Color Mark > Mark/Mark All/Clear Last/Clear All |
| 切换大小写 | 大写/小写/首字母大写 | Change Case > Upper/Lower/Capitalize |

### 3.3 标签栏右键菜单

| 菜单项 | 子菜单 |
|--------|--------|
| 关闭标签页 | |
| 关闭其他标签页 | |
| 更多关闭方式 | 关闭左侧所有标签页/关闭右侧所有标签页/关闭所有未修改标签页 |

### 3.4 AT-SPI 树要点

- 主窗口: `frame: "DMainWindow"`
- 菜单按钮: `button: "DTitlebarDWindowOptionButton"` (主菜单入口)
- 新建标签按钮: `button: "DTabBarAddButton"`
- 标签页: `page tab list` → `page tab: "<文件名>"`
- 编辑区: `text: ""` (空名，用 role 定位)
- 状态栏: `label: "行 X 列 Y"`, `label: "字数 N"`, `label: "NN%"`, `label: "插入"/"覆盖"`
- 重新载入按钮: `button: "重新载入"`
- 另存为按钮: `button: "另存为"`
- DTK 菜单为 transient popup，通过 `main_menu_comb` / `context_menu_comb` 键盘导航

## 4. 目录结构

```
autotest/yaml/
├── elements.yaml              # 共享元素注册表 (所有 ref 的唯一来源)
├── index.yaml                 # youqu 索引
├── find_replace/              # 查找替换 (11 cases)
├── voice/                     # 语音功能 (7 cases)
├── edit/                      # 编辑操作 (19 cases)
├── file_ops/                  # 文件操作 (20 cases)
├── workspace/                 # 工作区/状态栏 (13 cases)
├── tab_bar/                   # 标签栏管理 (8 cases)
├── settings/                  # 设置 (18 cases)
├── shortcuts/                 # 快捷键 (3 cases)
├── bookmark_mark/             # 书签/颜色标记/折叠 (6 cases)
├── readonly/                  # 只读模式 (3 cases)
├── window_mgmt/               # 窗口/主菜单/关机 (15 cases)
├── security/                  # 安全性/内存 (2 cases)
├── hardware/                  # 硬件交互 (6 cases)
└── skip/                      # 跳过用例 (19 cases)
```

## 5. 批次生成计划

共 19 个批次，按模块顺序生成。每个 YAML 文件命名为 `test_<module>_<id>.yaml`，
`<id>` 为原始 xlsx 3 位用例编号。

### Batch 1: elements.yaml + 基础框架 (0 cases, 基础设施)
- 创建 `elements.yaml` — 注册所有 UI 元素
- 删除 sample 文件 `test_deepin-editor_001.yaml`

### Batch 2: find_replace/ — 查找替换 (11 cases)
| ID | 文件名 | 标题 | 主要操作 |
|----|--------|------|----------|
| 002 | test_find_replace_002.yaml | 查找替换-多匹配项中特定选中状态保留 | Ctrl+F查找→替换按钮 |
| 003 | test_find_replace_003.yaml | 查找替换-替换弹窗填充选中内容及状态保留 | 右键→查找→替换 |
| 004 | test_find_replace_004.yaml | 替换按钮切换后与Ctrl+H一致性 | Ctrl+F→替换 vs Ctrl+H |
| 005 | test_find_replace_005.yaml | 已选中文本时点击替换按钮 | 选中文本→Ctrl+F→替换 |
| 006 | test_find_replace_006.yaml | 点击替换按钮切换至替换弹窗(未选中) | Ctrl+F→替换 |
| 007 | test_find_replace_007.yaml | 查找弹窗中替换按钮可见性 | Ctrl+F→观察按钮 |
| 008 | test_find_replace_008.yaml | 替换(右键菜单) | 右键→替换→各按钮 |
| 101 | test_find_replace_101.yaml | 替换(主菜单) | 主菜单→替换 |
| 102 | test_find_replace_102.yaml | 查找_不按压enter键 | Ctrl+F→输入→不按enter |
| 103 | test_find_replace_103.yaml | 查找_更换查找词 | Ctrl+F→输入→更换 |
| 141 | test_find_replace_141.yaml | 替换_查询结果包含大小写 | Ctrl+H→勾选大小写 |

### Batch 3: voice/ — 语音功能 (7 cases)
| ID | 文件名 | 标题 | 主要操作 |
|----|--------|------|----------|
| 009 | test_voice_009.yaml | 语音朗读-全选文字 | Ctrl+A→右键→语音朗读 |
| 010 | test_voice_010.yaml | 语音朗读/听写-未安装uos-ai | 右键→语音朗读(无AI环境) |
| 011 | test_voice_011.yaml | 语音朗读-音频设备缺失 | 右键→语音朗读(无音频) |
| 012 | test_voice_012.yaml | 语音听写-音频设备缺失 | 右键→语音听写 |
| 013 | test_voice_013.yaml | 重复选择语音朗读 | 多次右键→语音朗读 |
| 118 | test_voice_118.yaml | 语音朗读 | 右键→语音朗读 |
| 119 | test_voice_119.yaml | 语音听写 | 右键→语音听写 |

### Batch 4: edit/ — 编辑操作 Part 1 (10 cases)
| ID | 文件名 | 标题 |
|----|--------|------|
| 000 | test_edit_000.yaml | Shift+Tab缩进文本 |
| 088 | test_edit_088.yaml | 全选复制粘贴回车交互 |
| 104 | test_edit_104.yaml | 语法高亮 |
| 105 | test_edit_105.yaml | 输入内容 |
| 107 | test_edit_107.yaml | 文件内容_输入特殊字符 |
| 108 | test_edit_108.yaml | 支持换行符 |
| 111 | test_edit_111.yaml | 大文件复制粘贴 |
| 112 | test_edit_112.yaml | Insert覆盖输入 |
| 120 | test_edit_120.yaml | 全选 |
| 121 | test_edit_121.yaml | 跳到行 |

### Batch 5: edit/ — 编辑操作 Part 2 (9 cases)
| ID | 文件名 | 标题 |
|----|--------|------|
| 122 | test_edit_122.yaml | 重做 |
| 123 | test_edit_123.yaml | 转换大写 |
| 124 | test_edit_124.yaml | 转换小写 |
| 125 | test_edit_125.yaml | 首字母大写 |
| 132 | test_edit_132.yaml | 不同源代码文件注释 |
| 133 | test_edit_133.yaml | 列编辑操作 |
| 135 | test_edit_135.yaml | 切换注释&撤销的交互 |
| 137 | test_edit_137.yaml | 列编辑操作_Delete键删除 |
| 138 | test_edit_138.yaml | 切换大小写&撤销的交互 |

### Batch 6: file_ops/ — 文件操作 Part 1 (10 cases)
| ID | 文件名 | 标题 |
|----|--------|------|
| 001 | test_file_ops_001.yaml | 修改编辑保存bashrc文件 |
| 028 | test_file_ops_028.yaml | 保存编码文件场景补充 |
| 037 | test_file_ops_037.yaml | 记住最后的操作路径_打开新文件 |
| 038 | test_file_ops_038.yaml | 记住最后的操作路径_保存新文档 |
| 039 | test_file_ops_039.yaml | 与当前文件保存一致_首次打开新文件 |
| 040 | test_file_ops_040.yaml | 与当前文件保存一致_首次保存新文件 |
| 041 | test_file_ops_041.yaml | 自定义操作路径_打开新文件 |
| 042 | test_file_ops_042.yaml | 自定义操作路径_保存新文档 |
| 062 | test_file_ops_062.yaml | 打开无效文件 |
| 063 | test_file_ops_063.yaml | 打开U盘硬盘smb文件 |

### Batch 7: file_ops/ — 文件操作 Part 2 (10 cases)
| ID | 文件名 | 标题 |
|----|--------|------|
| 064 | test_file_ops_064.yaml | 打开GB18030编码方式文件 |
| 065 | test_file_ops_065.yaml | 打开.crt格式文件 |
| 066 | test_file_ops_066.yaml | 打开.md文本类型格式文件 |
| 067 | test_file_ops_067.yaml | 打开BIG5格式文件 |
| 068 | test_file_ops_068.yaml | 打开大文件_1G+ |
| 092 | test_file_ops_092.yaml | 打开文件(主菜单) |
| 093 | test_file_ops_093.yaml | 保存(主菜单) |
| 094 | test_file_ops_094.yaml | 另存为(主菜单) |
| 116 | test_file_ops_116.yaml | 重新载入被其他应用修改的根源文件 |
| 117 | test_file_ops_117.yaml | 保存网络文件 |

### Batch 8: workspace/ — 工作区 Part 1 (7 cases)
| ID | 文件名 | 标题 |
|----|--------|------|
| 032 | test_workspace_032.yaml | 文件加载进度条_新开大文件 |
| 033 | test_workspace_033.yaml | 点击行号_最后一行 |
| 034 | test_workspace_034.yaml | 复制含有跨行符文本_查找框 |
| 035 | test_workspace_035.yaml | 设置中缩放字号_缩放比例显示 |
| 043 | test_workspace_043.yaml | 字数展示_UI |
| 046 | test_workspace_046.yaml | 大文件加载过程中交互_查找 |
| 047 | test_workspace_047.yaml | 关闭应用自动保存现场_label页高亮 |

### Batch 9: workspace/ — 工作区 Part 2 (6 cases)
| ID | 文件名 | 标题 |
|----|--------|------|
| 048 | test_workspace_048.yaml | Tip框显示文件路径 |
| 049 | test_workspace_049.yaml | Tip框显示文件路径_长文件名 |
| 050 | test_workspace_050.yaml | 恢复现场后保存临时文件 |
| 051 | test_workspace_051.yaml | 根源文件删除 |
| 052 | test_workspace_052.yaml | 打印预览2.0接口_存为PDF |
| 106 | test_workspace_106.yaml | 大文件加载中编码和文本类型按钮 |

### Batch 10: tab_bar/ — 标签栏管理 (8 cases)
| ID | 文件名 | 标题 |
|----|--------|------|
| 060 | test_tab_bar_060.yaml | +标签 |
| 061 | test_tab_bar_061.yaml | 批量拖拽 |
| 091 | test_tab_bar_091.yaml | 新建标签(主菜单) |
| 109 | test_tab_bar_109.yaml | 标签管理_异常保存_切换编码 |
| 110 | test_tab_bar_110.yaml | 切换编码_数据错误 |
| 115 | test_tab_bar_115.yaml | 未保存时关闭标签 |
| 126 | test_tab_bar_126.yaml | 标签栏的右键菜单 |
| 127 | test_tab_bar_127.yaml | 有左右标签时查看更多关闭方式 |

### Batch 11: settings/ — 设置 Part 1 (9 cases)
| ID | 文件名 | 标题 |
|----|--------|------|
| 036 | test_settings_036.yaml | 取消勾选允许鼠标中键执行粘贴 |
| 053 | test_settings_053.yaml | 重做快捷键恢复为Ctrl+Y |
| 069 | test_settings_069.yaml | 设置按钮 |
| 070 | test_settings_070.yaml | 字号大小设置 |
| 071 | test_settings_071.yaml | 键盘映射 |
| 073 | test_settings_073.yaml | 自动换行 |
| 074 | test_settings_074.yaml | 恢复默认 |
| 075 | test_settings_075.yaml | 代码折叠标志 |
| 076 | test_settings_076.yaml | 显示行号 |

### Batch 12: settings/ — 设置 Part 2 (9 cases)
| ID | 文件名 | 标题 |
|----|--------|------|
| 077 | test_settings_077.yaml | Tab字符宽度 |
| 078 | test_settings_078.yaml | 空白字符/制表符 |
| 079 | test_settings_079.yaml | 窗口设置_新窗口路径 |
| 080 | test_settings_080.yaml | Tab字符宽度_首行的显示 |
| 081 | test_settings_081.yaml | 窗口设置_关闭应用保留现场 |
| 082 | test_settings_082.yaml | 字体类型设置 |
| 083 | test_settings_083.yaml | 快捷键编辑 |
| 084 | test_settings_084.yaml | 快捷键编辑_小键盘 |
| 085 | test_settings_085.yaml | 设置快捷键 |

### Batch 13: shortcuts/ — 快捷键 (3 cases)
| ID | 文件名 | 标题 |
|----|--------|------|
| 086 | test_shortcuts_086.yaml | 文件查找快捷键 |
| 087 | test_shortcuts_087.yaml | 跳转到行快捷键 |
| 089 | test_shortcuts_089.yaml | 查找按压enter键 |

### Batch 14: bookmark_mark/ — 书签/颜色标记/折叠 (6 cases)
| ID | 文件名 | 标题 |
|----|--------|------|
| 128 | test_bookmark_mark_128.yaml | 颜色标记_清除所有标记 |
| 129 | test_bookmark_mark_129.yaml | 展开所有层次 |
| 130 | test_bookmark_mark_130.yaml | 添加书签 |
| 131 | test_bookmark_mark_131.yaml | 上一个书签/下一个书签 |
| 140 | test_bookmark_mark_140.yaml | 标记所有后继续添加标记 |
| 142 | test_bookmark_mark_142.yaml | 列编辑交互颜色标记 |

### Batch 15: readonly/ — 只读模式 (3 cases)
| ID | 文件名 | 标题 |
|----|--------|------|
| 134 | test_readonly_134.yaml | 只读模式_切换文件属性 |
| 136 | test_readonly_136.yaml | 只读模式_关闭应用后切换文件属性 |
| 139 | test_readonly_139.yaml | 只读模式_全选复制 |

### Batch 16: window_mgmt/ — 窗口管理 Part 1 (8 cases)
| ID | 文件名 | 标题 |
|----|--------|------|
| 029 | test_window_mgmt_029.yaml | 不保留现场_关闭应用 |
| 030 | test_window_mgmt_030.yaml | 不保留现场_多窗口关闭 |
| 031 | test_window_mgmt_031.yaml | 强制退出后再次打开 |
| 054 | test_window_mgmt_054.yaml | 软件安装 |
| 056 | test_window_mgmt_056.yaml | 软件卸载 |
| 057 | test_window_mgmt_057.yaml | dock右键菜单 |
| 058 | test_window_mgmt_058.yaml | 最小化后从桌面再次打开 |
| 059 | test_window_mgmt_059.yaml | 最小化后从启动器打开 |

### Batch 17: window_mgmt/ — 窗口管理 Part 2 (7 cases)
| ID | 文件名 | 标题 |
|----|--------|------|
| 090 | test_window_mgmt_090.yaml | 新建窗口(主菜单) |
| 095 | test_window_mgmt_095.yaml | 打印(主菜单) |
| 096 | test_window_mgmt_096.yaml | 切换主题(主菜单) |
| 097 | test_window_mgmt_097.yaml | 帮助(主菜单) |
| 098 | test_window_mgmt_098.yaml | 关于弹窗 |
| 099 | test_window_mgmt_099.yaml | 退出(主菜单) |
| 113 | test_window_mgmt_113.yaml | 休眠待机锁屏不阻止 |

### Batch 18: security/ — 安全性 (2 cases)
| ID | 文件名 | 标题 |
|----|--------|------|
| 027 | test_security_027.yaml | 内存释放检查 |
| 044 | test_security_044.yaml | 无内存泄漏 |

### Batch 19: hardware/ — 硬件交互 (6 cases)
| ID | 文件名 | 标题 |
|----|--------|------|
| 144 | test_hardware_144.yaml | 二指滚动 |
| 145 | test_hardware_145.yaml | 上下滑动 |
| 146 | test_hardware_146.yaml | 左右滑动 |
| 147 | test_hardware_147.yaml | 主菜单子菜单键盘交互 |
| 148 | test_hardware_148.yaml | 编码方式菜单调整_高分屏 |
| 149 | test_hardware_149.yaml | 高分屏_拖拽标签页 |

### Batch 20: skip/ — 跳过用例 (19 cases)
| ID 范围 | 类别 | Skip 原因 |
|---------|------|-----------|
| 014-026 | LINGLONG | skip-玲珑环境不支持自动化 |
| 045 | PERF | skip-性能压测类不支持自动化 |
| 055 | REBOOT | skip-重启类场景需要letmego支持 |
| 072 | REBOOT | skip-重启类场景需要letmego支持 |
| 100 | REBOOT | skip-重启类场景需要letmego支持 |
| 114 | REBOOT | skip-重启类场景需要letmego支持 |
| 143 | GESTURE | skip-触摸操作无法自动化 |

## 6. elements.yaml 设计

### 6.1 主菜单元素 (main_menu_comb)

```yaml
# 主菜单项 — 通过 DTitlebarDWindowOptionButton 触发
menu_new_window:
  menu: ["新窗口"]
menu_new_tab:
  menu: ["新标签页"]
menu_open_file:
  menu: ["打开文件"]
menu_save:
  menu: ["保存"]
menu_save_as:
  menu: ["另存为"]
menu_print:
  menu: ["打印"]
menu_theme:
  menu: ["切换主题"]
menu_settings:
  menu: ["设置"]
```

### 6.2 右键菜单元素 (context_menu_comb)

```yaml
# 编辑区中心坐标 (右键菜单触发点)
edit_area_center:
  x: 500
  y: 300

# 右键菜单项
ctx_undo:
  x: 500
  y: 300
  menu: ["撤销"]
ctx_redo:
  x: 500
  y: 300
  menu: ["重做"]
# ... (复制/粘贴/删除/全选/查找/替换/跳到行等)
ctx_voice_read:
  x: 500
  y: 300
  menu: ["语音朗读"]
ctx_color_mark:
  x: 500
  y: 300
  menu: ["颜色标记", "添加标记"]
ctx_change_case_upper:
  x: 500
  y: 300
  menu: ["切换大小写", "大写"]
# ...
```

### 6.3 标签栏右键菜单元素

```yaml
# 标签栏中心坐标
tab_center:
  x: 200
  y: 45

ctx_close_tab:
  x: 200
  y: 45
  menu: ["关闭标签页"]
ctx_more_close_left:
  x: 200
  y: 45
  menu: ["更多关闭方式", "关闭左侧所有标签页"]
```

### 6.4 全局变量

```yaml
vars:
  BUILD_DIR: "${PROJECT_ROOT}/build"
  APP_PATH: "${BUILD_DIR}/src/deepin-editor"
  TEST_FILES_DIR: "${PROJECT_ROOT}/test_files"
```

## 7. 技术决策

### 7.1 菜单操作
- **主菜单**: 使用 `main_menu_comb` + `menu` 路径 (键盘导航)
- **右键菜单**: 使用 `context_menu_comb` + `x/y` + `menu` 路径
- 坐标使用编辑区中心 `(500, 300)` 作为右键触发点

### 7.2 键盘操作
- 快捷键: `keyboard_hot_key` (如 `"ctrl,f"`, `"ctrl,h"`, `"ctrl,s"`)
- 单键: `keyboard_press` (如 `"Return"`, `"Escape"`, `"F11"`, `"Insert"`)
- 文本输入: `keyboard_type`

### 7.3 特殊处理
- **文件操作类**: 使用 `${TEST_FILES_DIR}` 变量引用测试文件，需提前准备
- **安装卸载类 (054, 056)**: 需要 shell 命令配合，YAML 中仅描述编辑器内操作
- **高分屏类 (148, 149)**: 需要切换缩放比例，YAML 中使用设置操作
- **休眠待机 (113)**: 无法在 YAML 中触发系统休眠，标记为需要人工确认
- **外部应用修改文件 (116)**: 使用 `dbus_call` 或在 setup 中用文件操作模拟

### 7.4 断言策略
- 进程状态: `process_running` / `process_not_running`
- 元素可见性: `element_visible` / `element_not_visible`
- 元素文本: `element_text` (状态栏字数、行列等)
- 文件存在: `file_exists` / `file_not_exists`
- OCR: `ocr_exist` / `ocr_not_exist` (对话提示文本)

### 7.5 时序规范
- `session_start.wait`: 1.0s
- 步骤 `wait`: 0.3s
- `wait_for.timeout`: 3000ms
- 最后一步必有 `wait` + `assert`

## 8. 验证计划

每个批次生成后执行:
```bash
cd autotest && youqu run --collect-only
```

最终验证:
- [ ] YAML 文件数 == 150 (131 automatable + 19 skip)
- [ ] 所有 `ref` 在 elements.yaml 中有定义
- [ ] 所有 YAML 包含完整 metadata (name/description/module/feature/tags/vars)
- [ ] skip 用例有 `skip` 字段
- [ ] 文件命名 `test_<module>_<id>.yaml` 一致
- [ ] `youqu run --collect-only` 无错误
