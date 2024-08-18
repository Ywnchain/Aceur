def main(blver):
    import os

    os.system("cls")
    version = '2.41'
    print(f"DocManager {version}")
    print("输入\"return\"以回到主界面\n")

    # 创建用户文件夹
    path = os.getcwd()
    current_dir = os.path.join(f"{path}\\Disk\\UserFile")  # 设置当前目录为用户文件夹路径
    os.path.join(f"{path}\\Disk\\UserFile")
    while True:
        try:
            command = input(f"{current_dir.split('Aceur')[1][1:]}\\> ")
            cmd = command.split(" ")

            if cmd[0] == "command":
                print("您可以通过输入以下命令来操作文件：")
                print("cat <filename> <encoding> 打印文件内容")
                print("cd <directory_name> 进入指定的文件夹。")
                print("ls 列出当前目录下的所有文件和文件夹。")
                print("pwd 打印当前路径")
                print("mkdir <directory_name>创建新的文件夹。")
                print("touch <filename>创建新的空白文件。")
                print("edit <filename>编辑已有文件并保存更改。")
                print("mv: 移动或重命名文件或文件夹。")
                print("rm: 删除指定的文件")
                print("rmdir: 删除指定的文件夹")
            elif cmd[0] == "ls":
                dir_cnt = 0
                file_cnt = 0
                dirl = []
                filel = []
                print("\n-----------------------------")
                for f in os.listdir(current_dir.rstrip()):
                    if os.path.isdir(f"{current_dir}\\{f}"):
                        dir_cnt += 1
                        dirl.append(f)
                    else:
                        file_cnt += 1
                        filel.append(f)
                print(f"Directories:{dir_cnt} | Files:{file_cnt}     |")
                print("-----------------------------")
                if not dir_cnt == 0 and not file_cnt == 0:
                    for dl in dirl:
                        print(f"[dir]{dl}")
                    for fl in filel:
                        print(f"[file]{fl}")
                    print("-----------------------------\n")
                elif dir_cnt == 0:
                    for fl in filel:
                        print(f"[file]{fl}")
                    print("-----------------------------\n")
                elif file_cnt == 0:
                    for dl in dirl:
                        print(f"[dir]{dl}")
                    print("-----------------------------\n")
                else:
                    print("\n")

            elif cmd[0] == "pwd":
                print(f"WorkDirectory:{current_dir}")

            elif cmd[0] == "cat":
                with open(f"{current_dir}\\{cmd[1].rstrip()}", mode="r+", encoding=cmd[2].rstrip()) as catf:
                    print("\n-----Print file content------")
                    print(f"Encoding method:{cmd[2].rstrip()}")
                    print("-----Print file content------")
                    for cf in catf.readlines():
                        print(cf.rstrip("\n"))
                    print("-----------------------------\n")

            elif cmd[0] == "mkdir":
                folder_path = os.path.join(current_dir, cmd[1])
                if not os.path.exists(folder_path):
                    os.mkdir(folder_path)
                    print("Successful create folder")
                else:
                    print("Folder has existed")

            elif cmd[0] == "touch":
                if cmd[1].rstrip() == "CONFIG.txt" or cmd[1].rstrip() == "__init__.py":
                    print("不可创建系统配置文件")
                else:
                    file_path = os.path.join(current_dir, cmd[1].rstrip())
                    if not os.path.exists(file_path):
                        with open(file_path, 'w+') as f:
                            pass
                        print(f"Successful create file")
                    else:
                        print("File has existed")

            elif cmd[0] == "edit":
                file = f"{current_dir}\\{cmd[1].rstrip()}"
                if file[-10:].rstrip() == "CONFIG.txt":
                    print("Unable to change configuration file")
                elif file[-11:].rstrip() == "__init__.py":
                    print("Unable to change configuration file")
                else:
                    os.system("cls")
                    if os.path.exists(file):
                        with open(f"{file}", 'r+') as f:
                            content = f.read()
                        print(f"-------Current content-------\n{content}\n")
                        print("-----------------------------")
                        cgmod = input("请选择更改模式:\n覆写文件/追加/逐行更改(f/a/z)> ")
                        os.system("cls")
                        if cgmod.rstrip().lower() == "f" or cgmod.rstrip().lower() == "a":
                            print("------------------------------------")
                            print("请输入新的文件内容，然后按Enter保存|")
                            print("------------------------------------")
                            new_content = []
                            l = 1
                            while True:
                                cul = input(f"{l}|")
                                if cul == "":
                                    break
                                else:
                                    new_content.append(cul)
                                    l += 1
                            if cgmod.rstrip().lower() == "f":
                                with open(file, 'w') as f:
                                    for n in new_content:
                                        f.write(f"{n}\n")
                            else:
                                with open(file, 'a') as f:
                                    for n in new_content:
                                        f.write(f"{n}\n")
                        elif cgmod.rstrip().lower() == "z":
                            while True:
                                cnt = 1
                                with open(f"{current_dir}\\{cmd[1].rstrip()}", mode="r+") as edf:
                                    print("--------file content---------")
                                    for ef in edf.readlines():
                                        print(f"{cnt}| " + ef.rstrip('\n'))
                                        cnt += 1
                                    print("-----------------------------\n")
                                cl = int(input("请输入要更改的行数(输入return结束更改)> "))
                                if not str(cl).rstrip().lower() == "return":
                                    cc = input("内容> ")
                                    with open(f"{current_dir}\\{cmd[1].rstrip()}", mode="r+") as cdf:
                                        cdfl = []
                                        for c in cdf.readlines():
                                            cdfl.append(c.rstrip("\n"))
                                        cdfl.pop(cl - 1)
                                        cdfl.insert(cl - 1, cc)
                                    with open(f"{current_dir}\\{cmd[1].rstrip()}", mode="w+") as wdf:
                                        for c in cdfl:
                                            wdf.write(f"{c}\n")
                                    os.system("cls")
                                else:
                                    break

                        os.system("cls")
                        print(f"DocManager {version}")
                        print("输入\"return\"以回到主界面\n")
                        print("文件编辑成功。")
                    else:
                        print("指定的文件不存在。")
            elif cmd[0] == "mv":
                pass
            elif cmd[0] == "rm":
                pass
            elif cmd[0] == "cd":
                if not cmd[1].rstrip() == "..":
                    folder_path = os.path.join(current_dir, cmd[1].rstrip())
                    if not os.path.exists(folder_path):
                        print(f"Folder not exists")
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
            elif cmd[0] == "return":
                break
            else:
                print(f"命令\"{cmd}\"不存在，使用\"command\"命令查看所有命令")

        except FileNotFoundError:
            print(f"文件不存在：{current_dir}\\")
            os.path.join(f"{path}\\Disk\\UserFile\\")
            current_dir = f"{path}\\Disk\\UserFile"