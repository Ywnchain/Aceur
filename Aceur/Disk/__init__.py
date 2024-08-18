def main(blver):
    import os

    def start():

        os.system("cls")
        version = '2.31'
        print(f"DocManager {version}")
        print("输入\"return\"以回到主界面\n")

        # 创建用户文件夹
        path = os.getcwd()
        current_dir = os.path.join(f"{path}\\Disk\\UserFile")  # 设置当前目录为用户文件夹路径
        os.path.join(f"{path}\\Disk\\UserFile")

        while True:
            try:
                user_input = input(f"{current_dir.split('Aceur')[1][1:]}\\> ")
                us = user_input.split(" ")

                if us[0] == "command":
                    show_help()
                elif us[0] == "ls":
                    list_files(current_dir)
                elif us[0] == "getpath":
                    print(f"当前目录：{current_dir}")
                elif us[0] == "mkdir":
                    create_folder(current_dir, us[1])
                elif us[0] == "touch":
                    create_file(current_dir, us[1])
                elif us[0] == "edit":
                    edit_file(f"{current_dir}\\{us[1]}")
                elif us[0] == "mv":
                    move_file_or_folder(us[1], us[1])
                elif us[0] == "rm":
                    delete_file_or_folder(us[1])
                elif us[0] == "cd":
                    if not us[1].rstrip() == "..":
                        folder_path = os.path.join(current_dir, us[1].rstrip())
                        if not os.path.exists(folder_path):
                            print(f"目录不存在：{folder_path}")
                        else:
                            current_dir = folder_path
                    else:
                        rsu = ""
                        slpdir = current_dir.split("\\")
                        slpdir.remove(slpdir[-1])
                        for sd in slpdir:
                            rsu += f"{sd}\\"
                        rsu = rsu[:-1]
                        os.path.join(rsu)
                        current_dir = rsu
                elif us[0] == "return":
                    break
                else:
                    print(f"命令\"{user_input}\"不存在，使用\"command\"命令查看所有命令")

            except FileNotFoundError:
                print(f"文件不存在：{current_dir}\\")
                os.path.join(f"{path}\\Disk\\UserFile\\")
                current_dir = f"{path}\\Disk\\UserFile"

    def show_help():
        print("您可以通过输入以下命令来操作文件：")
        print("ls: 列出当前目录下的所有文件和文件夹。")
        print("getpath: 打印当前路径")
        print("mkdir: 创建新的文件夹。")
        print("touch: 创建新的空白文件。")
        print("edit: 编辑已有文件并保存更改。")
        print("mv: 移动或重命名文件或文件夹。")
        print("rm: 删除指定的文件或文件夹。")
        print("cd: 进入指定的文件夹。")

    def list_files(directory):
        files = os.listdir(directory)
        if len(files) == 0:
            print("当前目录为空。")
        else:
            print(f"当前目录下共有{len(files)}个文件和文件夹：")
            for f in files:
                print(f)

    def create_folder(directory, folder_name):
        folder_path = os.path.join(directory, folder_name)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
            print(f"已创建文件夹：{folder_name}")
        else:
            print("文件夹已存在。")

    def create_file(directory, file_name):
        if file_name.rstrip() == "CONFIG.txt" or file_name.rstrip() == "__init__.py":
            print("不可创建系统配置文件")
        else:
            file_path = os.path.join(directory, file_name)
            if not os.path.exists(file_path):
                with open(file_path, 'w+') as f:
                    pass
                print(f"已创建空白文件：{file_name}")
            else:
                print("文件已存在。")

    def edit_file(file):
        if file[-10:].rstrip() == "CONFIG.txt":
            print("此为系统配置文件，不可编辑")
        elif file[-11:].rstrip() == "__init__.py":
            print("此为系统配置文件，不可编辑")
        else:
            if os.path.exists(file):
                with open(f"{file}", 'r+') as f:
                    content = f.read()
                print(f"当前文件内容为：\n{content}\n")
                print("请输入新的文件内容，然后按两次Enter键保存：\n")
                new_content = []
                l = 1
                while True:
                    cul = input(f"{l}|")
                    if cul == "":
                        break
                    else:
                        new_content.append(cul)
                        l += 1

                with open(file, 'a') as f:
                    for n in new_content:
                        f.write(f"{n}\n")
                print("文件编辑成功。")
            else:
                print("指定的文件不存在。")

    def move_file_or_folder(old_path, new_path):
        if os.path.exists(old_path):
            os.rename(old_path, new_path)
            print("移动/重命名成功。")
        else:
            print("指定的文件或文件夹不存在。")

    def delete_file_or_folder(path):
        os.path.join(f"{create_dir}")
        if os.path.exists(path):
            if os.path.isdir(path):
                os.rmdir(path)
                print("文件夹删除成功。")

    start()