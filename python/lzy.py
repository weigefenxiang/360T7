#!/usr/bin/python
#
# Copyright (c) 2023 @weigefenxiang
#
import re
import datetime
import sys
import os
from lanzou.api import LanZouCloud

ylogin = sys.argv[1]
phpdisk_info = sys.argv[2]
LZ_folder_name = sys.argv[3]
MOVE_dir = sys.argv[4]
Github_path = sys.argv[5]
num = int(sys.argv[6])

cookie = {'ylogin': f'{ylogin}', 'phpdisk_info': f'{phpdisk_info}'}


def exID(folder_name):
    ex = f"FolderId\(name='{folder_name}', id=(\d+)\)"
    return ex


def show_progress(file_name, total_size, now_size):
    """显示进度的回调函数"""
    percent = now_size / total_size
    bar_len = 40  # 进度条长总度
    bar_str = '>' * round(bar_len * percent) + '=' * round(bar_len * (1 - percent))
    print('\r{:.2f}%\t[{}] {:.1f}/{:.1f}MB | {} '.format(
        percent * 100, bar_str, now_size / 1048576, total_size / 1048576, file_name), end='')
    if total_size == now_size:
        print('')  # 下载完成换行


class lanzou(object):
    def __init__(self):
        self.lzy = LanZouCloud()
        res = self.lzy.login_by_cookie(cookie)
        if res == 0:
            print(f'蓝奏云登录成功')
        else:
            print(f'蓝奏云登录 failed！\nERROR：  res= {res}')

    def __del__(self):
        pass

    def get_FOLDERS(self):
        folders = self.lzy.get_move_folders()
        return folders

    def get_FOLDER_ID(self, folder_name):
        folders = self.lzy.get_move_folders()
        ex = exID(folder_name)
        folder_id = int(re.findall(ex, str(folders.find_by_name(folder_name)), re.S)[0])
        return folder_id

    def get_FILE_list(self, folder_name):
        folder_id = self.get_FOLDER_ID(folder_name)
        file_list = self.lzy.get_file_list(folder_id)
        if len(str(file_list)) <= 7:
            return False
        else:
            file_id = int(re.findall('id=(\d+),', str(file_list), re.S)[0])
            return file_id

    def MOVE_folder(self, folder_ID, parent_folder_id):
        try:
            res = self.lzy.move_folder(int(folder_ID), int(parent_folder_id))
        except TypeError:
            print(f'文件夹并未改变位置，移动失败\nparent_folder_id: {parent_folder_id}')
        except Exception as result:
            print("未知错误 %s" % result)
        else:
            if res == 0:
                print(f'已将文件夹 {folder_ID} 成功转义')
            elif res == -1:
                print(f'移动失败 文件夹 {folder_ID} 位于同级目录')
            else:
                print(f'移动失败 res： {res}')

    def MOVE_file(self, folder_id, parent_folder_id):
        res = self.lzy.move_file(int(folder_id), int(parent_folder_id))
        if res == 0:
            print(f'文件 {int(folder_id)} 已成功转移')
        else:
            print(f'移动文件错误，res: {res}')

    def MKDIR_files_from_folder(self, folder_name, new_folder_name):
        while True:
            file_id = self.get_FILE_list(folder_name)
            if file_id == False:
                print(f'文件夹 {folder_name} 内的文件已转移完毕')
                break
            new_folder_id = self.get_FOLDER_ID(new_folder_name)
            self.MOVE_file(file_id, new_folder_id)

    def MKDIR_folder(self, parent_id, folder_name, desc=''):
        fid = self.lzy.mkdir(parent_id, folder_name, desc)
        if fid == False:
            print('创建文件夹失败')
        else:
            return fid

    def RENAME_dir(self, folder_id, folder_name):
        if self.lzy.rename_dir(int(folder_id), folder_name) == 0:
            print(f'已将 {int(folder_id)} 重命名为 {folder_name}')

    def SET_desc(self, fid, desc, is_file=False):
        if self.lzy.set_desc(int(fid), desc, is_file) == 0:
            print(f'修改文件(夹) {int(fid)} 描述信息为 {desc}')

    def SET_passwd(self, fid, passwd='', is_file=False):
        if self.lzy.set_passwd(int(fid), passwd, is_file) == 0:
            print(f'修改文件(夹) {int(fid)} 提取码为 {passwd}')

    def show_failed(self, code, filename):
        print(f"下载失败,错误码: {code}, 文件名: {filename}")

    def handler(self, fid, is_file, desc=''):
        if is_file:
            self.lzy.set_desc(fid, desc, is_file=True)
            self.lzy.set_passwd(fid, '', is_file=True)

    def UPLOAD_file(self, file_path, parent_name):
        folder_id = self.get_FOLDER_ID(parent_name)
        file_name = file_path.split("/")[-1]
        code = self.lzy.upload_file(file_path, folder_id, callback=None, uploaded_handler=self.handler)
        if code == 0:
            print(f'上传文件 {file_name} 成功')
        else:
            print(f'文件 {file_name} 上传失败  错误代码{self.lzy.FAILED}')

    def UPLOAD_dir(self, dir_path, parent_name, callback=None, failed_callback=None, uploaded_handler=None):
        folder_id = self.get_FOLDER_ID(parent_name)
        print(f'dir_path: {dir_path}\nfolder_id: {folder_id}\nfolder_name:  {parent_name}')
        handler = lanzou._handler(folder_id, False)
        code = self.lzy.upload_dir(dir_path, int(folder_id), callback=show_progress, uploaded_handler=self.handler)
        if code == 0:
            print(f'上传 {dir_path} 成功 folder_id:{folder_id}')

    def UPLOAD_files_from_DIR(self, file_dir, parent_name):
        for root, dirs, files_list in os.walk(file_dir):
            print("files_list", files_list)  # 当前路径下所有非目录子文件
        for i in files_list:
            file_path = file_dir + '/' + i
            print(file_path)
            self.UPLOAD_file(file_path, parent_name)


def main():
    lz = lanzou()
    nowtime = str(datetime.datetime.now().strftime('%Y-%m-%d_%H_%M.%S'))
    father_id = lz.get_FOLDER_ID(LZ_folder_name)
    if num == 0:
        lz.MKDIR_folder(father_id, nowtime, f'历史资料')
        lz.MKDIR_files_from_folder(MOVE_dir, nowtime)
    lz.UPLOAD_files_from_DIR(Github_path, MOVE_dir)


if __name__ == '__main__':
    main()
