def main(blver):
    import os
    version = "2.0"
    path = os.getcwd().split("Aceur")[0]

    os.system("cls")
    print(f"Codister {version} - use DocManager 2.41")
    print("输入\"return\"以回到主界面\n")
    while True:
        try:
            cmd = input("CDS-cmd> ")
            cs = cmd.split(" ")
            if cs[0] == "command":
                print("create <程序名> 创建一个程序")
                print("uninst <程序名> 卸载一个程序")
                print()
            elif cs[0].lower() == "create":
                #创建配置文件
                os.system("cls")
                print("配置程序")
                while True:
                    developer = input("\t[str]开发者> ")
                    changeable = input("\t[bool]程序可更改(TRUE/DISABLED)> ")
                    lockable = input("\t[bool]程序锁定(TRUE/DISABLED)> ")
                    version_ = input("\t[str]程序版本号：")
                    if changeable.rstrip() == "TRUE" or changeable.rstrip() == "DISABLED":
                        if changeable.rstrip() == "TRUE" or changeable.rstrip() == "DISABLED":
                            break
                    os.system("cls")
                    print("请注意：\n[程序可更改]及[程序锁定]栏目仅支持bool(TRUE/DISABLED)，且无需添加引号")
                    input("输入\"Enter\"重试> ")
                    os.system("cls")


                #创建项目文件夹
                proname = cs[1]
                os.mkdir(f"{path}Aceur\\Disk\\UserFile\\Cos\\{proname}")

                os.system("cls")
                print("请注意：\n请务必在程序内创建一个cosmain()函数，程序运行（如有）仅在cosmain()中进行\n")
                input("输入\"Enter\"继续> ")

                #编辑文件
                with open(f"{path}Aceur\\Disk\\UserFile\\Cos\\{proname}\\__init__.py", mode="w+", encoding="utf-8") as nw:
                    print("请编辑该项目 *输入2次Enter* 结束编辑")
                    all_code = []
                    l = 1
                    while True:
                        c = input(f"line {l}> ")
                        if c:
                            all_code.append(c)
                            l += 1
                        else:
                            break

                with open(f"{path}Aceur\\Disk\\UserFile\\Cos\\{proname}\\__init__.py", mode="w+", encoding="utf-8") as na:
                    for ac in all_code:
                        na.write(f"{ac}\n")

                with open(f"{path}Aceur\\Disk\\UserFile\\Cos\\{proname}\\CONFIG.txt", mode="w+", encoding="utf-8") as wconf:
                    wconf.write(f"Lockable:\"{lockable}\"\n")
                    wconf.write(f"Changeable:\"{changeable}\"\n")
                    wconf.write(f"Developer:\"{developer}\"\n")
                    wconf.write(f"Version:\"{version_}\"")

            elif cs[0].lower() == "uninst":
                unin = cs[1]
                if not os.path.exists(f"{path}Aceur\\Disk\\UserFile\\Cos\\{unin}"):
                    print("以此命名的程序不存在")
                os.system("cls")
                print(f"您确定要卸载\"{unin}\"?")
                input("输入\"Enter\"继续> ")

                file_path = os.path.join(f"{path}Aceur\\Disk\\UserFile\\Cos\\", f"{unin}")
                os.remove(f"{path}Aceur\\Disk\\UserFile\\Cos\\{unin}\\__init__.py")
                os.remove(f"{path}Aceur\\Disk\\UserFile\\Cos\\{unin}\\CONFIG.txt")

                os.rmdir(f"{path}Aceur\\Disk\\UserFile\\Cos\\{unin}")

                os.system("cls")
                print("程序已卸载")
                input("输入\"Enter\"继续> ")
                os.system("cls")
                print(f"Codister {version}")
                print("输入\"return\"以回到主界面\n")

            elif cs[0].lower() == "return":
                break

        except IndexError:
            print("Error:缺少必要的参数")

        except FileExistsError:
            print("Error:以此命名的程序已存在")

        except FileNotFoundError as f:
            print("Error:以此命名的程序不存在")
            print(f)