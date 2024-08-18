import os
import sys
from Disk.SystemFile.ui import StartUi, Vset
import Disk.SystemFile.SoftSup
import traceback
import art

path = os.getcwd()
os.system("cls")
version = "2.0.1"
edvol = []
with open(f"{path}\\Disk\\SystemFile\\cominfo.txt", mode="r+", encoding="utf-8") as edvo:
    edvol.append(edvo.read().split("\n"))
    dme = str(edvol[0][3].split(":")[1]) # dme:开发者模式开启情况
with open(f"{path}\\Disk\\SystemFile\\cominfo.txt") as oinfo:
    if oinfo.read().find("computername") == -1:
        StartUi.once(path, version)
    else:
        StartUi.notonce(path, version)

os.system("cls")
art.tprint(f"Aceur - {version}")
print("----------------------------------")
print("在任意应用输入\"command\"以查看命令\n")
while True:
    try:
        cmd = input("main-cmd> ")
        cs = cmd.split(" ")
        if cs[0].lower() == "soft":
            Disk.SystemFile.SoftSup.RunBuild(cs[1], version, dme, pathr=path, version=version)

        elif cs[0].lower() == "cos":
            Disk.SystemFile.SoftSup.RunCos(cs[1], version, dme, version=version)

        elif cs[0].lower() == "att":
            Disk.SystemFile.SoftSup.AttrSoft(path, cs[1], version)

        elif cs[0].lower() == "command":
            os.system("cls")
            with open(f"{path}\\Disk\\SystemFile\\main-cmd.txt", encoding="utf-8") as opencmd:
                print(opencmd.read())

            input("输入回车关闭帮助> ")
            os.system("cls")
            print(f"Aceur {version}")
            print("在任意应用输入\"command\"以查看命令\n")

        elif cs[0].lower() == "pas":
            print("\nBuild-in App:")
            asl = os.listdir(f"{path}\\Disk\\SystemFile\\BuildinApp\\")
            asl.remove("__pycache__")
            if asl:
                for a in asl:
                    print(f"\t{a}")
            else:
                print("\t无")
            print("Custom App:")
            acl = os.listdir(f"{path}\\Disk\\UserFile\\Cos\\")
            acl.remove("__pycache__")
            if acl:
                for c in acl:
                    print(f"\t{c}")
            else:
                print("\t无")
            print("\n")

        elif cs[0].lower() == "vset":
            Vset.main(version, path)

        elif cs[0].lower() == "dvo":
            if dme.rstrip() == "false":
                os.system("cls")
                yorn = input("启用开发者模式(y/n): ")
                if yorn.rstrip().lower() == "y":
                    os.system("cls")

                    with open(f"{path}\\Disk\\SystemFile\\cominfo.txt", mode="w", encoding="utf-8") as edvot:
                        for i in range(0, 3):
                            edvot.write(f"{str(edvol[0][i])}\n")
                        edvot.write("DM:true")

                    dme = "true"
                    print("开发者模式已开启\n")
                    input("输入Enter返回")

                os.system("cls")
                print(f"Aceur {version}")
                print("在任意应用输入\"command\"以查看命令\n")

            elif dme.rstrip() == "true":
                os.system("cls")
                yornt = input("关闭开发者模式(y/n): ")
                if yornt.rstrip().lower() == "y":
                    os.system("cls")

                    with open(f"{path}\\Disk\\SystemFile\\cominfo.txt", mode="w", encoding="utf-8") as edvot:
                        for i in range(0, 3):
                            edvot.write(f"{str(edvol[0][i])}\n")
                        edvot.write("DM:false")

                    dme = "false"
                    print("开发者模式已关闭\n")
                    input("输入Enter返回")

                os.system("cls")
                print(f"Aceur {version}")
                print("在任意应用输入\"command\"以查看命令\n")

            else:
                os.system("cls")
                print(f"Aceur {version}")
                print("在任意应用输入\"command\"以查看命令\n")

        elif cs[0].lower() == "cls":
            os.system("cls")
            art.tprint(f"Aceur - {version}")
            print("----------------------------------")
            print("在任意应用输入\"command\"以查看命令\n")

        elif cs[0].lower() == "quit":
            break

        else:
            pass

    except KeyboardInterrupt:
        os.system("cls")
        sys.exit("\nAceur closed\n")

    except Exception as e:
        if dme == "false":
            print(f"Error:{e}")
        elif dme == "true":
            print("[Developer Output]")
            traceback.print_exc()

os.system("cls")
sys.exit("\n\tAceur closed\n")