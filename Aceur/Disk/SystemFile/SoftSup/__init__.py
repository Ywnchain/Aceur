import importlib
import os
import time
import traceback
import art

def RunBuild(soft, blver, dme, pathr, version):
    try:
        path = f"Disk.SystemFile.BuildinApp.{soft}"
        module = importlib.import_module(path)
        os.system("cls")
        try:
            chll = []
            with open(f"{pathr}\\Disk\\SystemFile\\BuildinApp\\{soft}\\CONFIG.txt",  mode="r+") as chlk:
                for c in chlk.read().split("\n"):
                    chll.append(c.rstrip())

                if chll[0].split(":")[1].rstrip() == "TRUE":
                    os.system("cls")
                    print("该程序已被锁定，输入\"Enter\"回到主界面")
                    input("> ")

                    os.system("cls")
                    art.tprint(f"Tesford - {version}")
                    print("----------------------------------")
                    print("在任意应用输入\"command\"以查看命令\n")


            module.main(blver)
        except Exception as errt:
            os.system("cls")
            print(f"Error in \"{soft}\"\n")
            print(f"info:{errt}")
            print("--------------------------")
            cb = input("返回Tesford/再次运行(r/s)> ")
            if cb.rstrip().lower() == "s":
                module.main(blver)
            else:
                pass
        else:
            print("\n")
            time.sleep(1.5)
            print("程序运行结束")
            cb = input("返回Tesford/再次运行(r/s)> ")
            if cb.rstrip().lower() == "s":
                module.main(blver)
            else:
                pass

        os.system("cls")
        art.tprint(f"Tesford - {version}")
        print("----------------------------------")
        print("在任意应用输入\"command\"以查看命令\n")

    except ImportError:
        print(f"没有名为{soft}的内置程序")
    except ImportWarning as iw:
        print(f"运行出现异常：\"{iw}\"")
    except Exception as e:
        if dme == "false":
            print(f"Error:{e}")
        elif dme == "true":
            print("[Developer Output]")
            traceback.print_exc()


def RunCos(soft, blver, dme, version):
    try:
        path = f"Disk.UserFile.Cos.{soft}"
        module = importlib.import_module(path)
        os.system("cls")
        try:
            module.cosmain()
        except Exception as errt:
            os.system("cls")
            print(f"Error in \"{soft}\"\n")
            print(f"info:{errt}")
            cb = input("返回Tesford/再次运行(r/s)> ")
            if cb.rstrip().lower() == "s":
                module.cosmain()
            else:
                pass

        else:
            print("\n")
            time.sleep(1.5)
            cb = input("返回Tesford/再次运行(r/s)> ")
            if cb.rstrip().lower() == "s":
                module.cosmain()
            else:
                pass

        os.system("cls")
        art.tprint(f"Tesford - {version}")
        print("----------------------------------")
        print("在任意应用输入\"command\"以查看命令\n")

    except ImportError:
        print(f"没有名为{soft}的用户自定程序")
    except ImportWarning as iw:
        print(f"此程序出现问题：\"{iw}\"")
    except AttributeError:
        print("\n你遇到了一个开发者错误：")
        print("\t·如果你是用户，那么请通知开发者该程序存在问题")
        print("\t·如果你是开发者，请确定程序是基于\"cosmain()\"")


def AttrSoft(path, soft, version):
    # 先测试buildin
    try:
        with open(f"{path}\\Disk\\SystemFile\\BuildinApp\\{soft}\\CONFIG.txt", encoding="utf-8") as opconf:
            for i in range(4):
                l = opconf.readline()
                ll = l.split(":")
                attr = ll[0]
                value = ll[1]

                if attr == "Lockable":
                    print(f"程序锁定:{value}")
                elif attr == "Changeable":
                    print(f"程序可更改:{value}")
                elif attr == "Developer":
                    print(f"开发者:{value}")
                elif attr == "Version":
                    print(f"程序版本:{value}")

    except FileNotFoundError:
        try:
            with open(f"{path}\\Disk\\UserFile\\Cos\\{soft}\\CONFIG.txt", encoding="utf-8") as opconf:
                for i in range(4):
                    l = opconf.readline()
                    ll = l.split(":")
                    attr = ll[0]
                    value = ll[1]

                    if attr == "Lockable":
                        print(f"程序锁定:{value}")
                    elif attr == "Changeable":
                        print(f"程序可更改:{value}")
                    elif attr == "Developer":
                        print(f"开发者:{value}")
                    elif attr == "Version":
                        print(f"程序版本:{value}")

                    print("程序不存在，输入\"Enter\"回到主界面")
                    input("> ")
                    os.system("cls")
                    print(f"Tesford {version}")
                    print("在任意应用输入\"command\"以查看命令\n")

        except FileNotFoundError:
            print("程序不存在，输入\"Enter\"回到主界面")
            input("> ")
            os.system("cls")
            art.tprint(f"Tesford - {version}")
            print("----------------------------------")
            print("在任意应用输入\"command\"以查看命令\n")