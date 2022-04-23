# -*- coding: utf-8 -*-
# 读取数据库文件进行解析,, 主函数 模块. 能解析 sybase12.x,15.x

import struct, time
import init

s = struct.unpack


class Unload_DB():
    def __init__(self):  # 解析函数
        super(Unload_DB, self).__init__()

    # 文件信息
    def file_init(self, fn):
        self.files = []
        for f_name in fn:  # 每个文件头信息
            f = open(f_name, 'rb')
            data = f.read(8192)
            file_info = init.file_blk_0(data)
            f.seek(8192 * 9)
            data = f.read(8192)
            version1, version2, first_07, db_name = init.file_blk_9(data)
            file_info.f_name = f_name
            file_info.file = f
            file_info.version1 = version1
            file_info.version2 = version2
            file_info.boot = first_07
            file_info.db_name = db_name
            self.files.append(file_info)
        return self.files

    def unload_db(self, file_infos, db):
        print("Datetime: " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))  # current time
        first_07 = file_infos[0].boot
        f = file_infos[0].file
        version = file_infos[0].version1
        tab_data_07 = init.init_07(file_infos[0], first_07)
        print("tab_data_07/02 over ....")
        if version[3:] != '0':
            print("tab_data_29 in ....")
            tab_data_29 = init.init_29(f, tab_data_07)
            print("tab_data_29 over ....")
            tab_data_22, tab_data_05 = init.init_22_05(f, tab_data_07, tab_data_29)
            print("tab_data_22,tab_data_05 over ....")
            tab_all, view_all, program_all, trigger_all, default_all = init.init_all_2008(f, tab_data_22, tab_data_29,
                                                                                          tab_data_05,
                                                                                          tab_data_07)  # 获得所有表的结构
            print("unload all over")
        elif version[3:] == '0':
            tab_data_2 = tab_data_07
            tab_data_1, tab_data_3 = init.init_1_3(f, tab_data_2)
            print("init_1_3 over ....")
            tab_all, view_all, program_all, trigger_all, default_all = init.init_all_2000(f, tab_data_1, tab_data_2,
                                                                                          tab_data_3)
            print("init_all_2000 over ....")

        return tab_all, view_all, program_all, trigger_all, default_all

    def unload_tab(self, file_infos, tab, db):
        f = file_infos[0].file
        tab_data = init.unload_tab(f, tab)
        return tab_data

    # save table
    def save_tab(self, tab_data, tab, db):
        if tab.tab_name != 'sysowners':
            init.save_tab(tab_data, tab, db)
