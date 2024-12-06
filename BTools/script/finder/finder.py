# -*- coding: utf-8 -*-
"""
文件查找
@author: bx33661
@date: 2024-11-25
"""
import os
import sys

def search_files_by_name(directory, keyword):
    """
    在指定目录中搜索文件名包含特定关键词的文件

    :param directory: 要搜索的目录路径
    :param keyword: 要搜索的关键词
    :return: 包含关键词的文件路径列表
    """
    matched_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if keyword in file:
                matched_files.append(os.path.join(root, file))
    return matched_files

def search_files_by_content(directory, keyword):
    """
    在指定目录中搜索文件内容包含特定关键词的文件

    :param directory: 要搜索的目录路径
    :param keyword: 要搜索的关键词
    :return: 包含关键词的文件路径列表
    """
    matched_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    if keyword in f.read():
                        matched_files.append(file_path)
            except (UnicodeDecodeError, FileNotFoundError, PermissionError):
                continue
    return matched_files

def print_usage():
    print("用法: python 1.py <目录路径> <关键词> [模式] [-o <输出文件路径>]")
    print("模式: name (文件名匹配), content (文件内容匹配)。默认模式为 'name'。")
    print("示例:")
    print("  python finder.py C:\\Downloads\\ dx")
    print("  python finder.py C:\\Downloads\\ dx content")
    print("  python finder.py C:\\Downloads\\ dx content -o results.txt")
    print("  python finder.py -h  # 显示帮助信息")

def main():
    print("""
$$$$$$$\  $$\   $$\         $$$$$$$$\ $$\                 $$
$$  __$$\ $$ |  $$ |        $$  _____|\__|                $$ |
$$ |  $$ |\$$\ $$  |        $$ |      $$\ $$$$$$$\   $$$$$$$ | $$$$$$\   $$$$$$
$$$$$$$\ | \$$$$  / $$$$$$\ $$$$$\    $$ |$$  __$$\ $$  __$$ |$$  __$$\ $$  __$$
$$  __$$\  $$  $$<  \______|$$  __|   $$ |$$ |  $$ |$$ /  $$ |$$$$$$$$ |$$ |  \__|
$$ |  $$ |$$  /\$$\         $$ |      $$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |
$$$$$$$  |$$ /  $$ |        $$ |      $$ |$$ |  $$ |\$$$$$$$ |\$$$$$$$\ $$ |
\_______/ \__|  \__|        \__|      \__|\__|  \__| \_______| \_______|\__|
""")
    if len(sys.argv) < 3 or sys.argv[1] == '-h':
        print_usage()
        sys.exit(1)

    directory = sys.argv[1]
    keyword = sys.argv[2]
    mode = 'name'
    output_file = None

    i = 3
    while i < len(sys.argv):
        if sys.argv[i] == '-o':
            if i + 1 < len(sys.argv):
                output_file = sys.argv[i + 1]
                i += 2
            else:
                print("错误: -o 参数需要一个输出文件路径。")
                print_usage()
                sys.exit(1)
        elif sys.argv[i] in ['name', 'content']:
            mode = sys.argv[i]
            i += 1
        else:
            print("无效的参数: {}".format(sys.argv[i]))
            print_usage()
            sys.exit(1)

    if mode not in ['name', 'content']:
        print("无效的模式。请使用 'name' 或 'content'。")
        print_usage()
        sys.exit(1)

    if mode == 'name':
        results = search_files_by_name(directory, keyword)
    elif mode == 'content':
        results = search_files_by_content(directory, keyword)

    if results:
        print("找到以下文件包含关键词 '{}':".format(keyword))
        for result in results:
            print(result)

        if output_file:
            if not os.path.dirname(output_file):
                output_file = os.path.join(os.getcwd(), output_file)
            try:
                with open(output_file, 'w', encoding='utf-8') as f:
                    for result in results:
                        f.write(result + '\n')
                print("结果已保存到: {}".format(output_file))
            except Exception as e:
                print("保存结果时出错: {}".format(e))
    else:
        print("没有找到包含关键词 '{}' 的文件。".format(keyword))

if __name__ == "__main__":
    main()