import os
import time
import sys
import tqdm
import art

username = ""
password = ""

def jdt():
    for _ in tqdm.tqdm(range(1, 40 + 1)):
        time.sleep(0.1)

def once(path, version):
    global username, password

    os.system("cls")
    art.tprint(f"Aceur - {version}")
    print("----------------------------------")
    os.system("cls")
    input(f"Hi! 欢迎使用Tesford,下面让我们开始配置吧!\n按下回车确定> ")
    os.system("cls")

    comname = input("首先，你希望计算机叫什么名字？> ")
    os.system("cls")

    def userconfig():
        global username, password
        username = input("接着，我们来配置用户信息\n\t用户名> ")
        password = input("\t密码> ")
        os.system("cls")

    userconfig()
    yorn = input(f"最后，请确认你的用户名的密码\n\t用户名：{username}\n\t密码：{password}\n请确认(y,n)> ")
    if yorn.upper() == "Y":
        pass
    else:
        os.system("cls")
        userconfig()

    os.system("cls")
    print("我们需要一些时间来配置您的更改")
    jdt()

    with open(f"{path}\\Disk\\SystemFile\\cominfo.txt", mode="w+", encoding="utf-8") as wcom:
        wcom.write(f"computername:{comname}\nusername:{username}\npassword:{password}\nDM:false")

    return True

def notonce(path, version, nwp=None):
    import os
    info = []
    with open(f"{path}\\Disk\\SystemFile\\cominfo.txt", mode="r+", encoding="utf-8") as rcom:
        info.append(rcom.read().split("\n"))

    os.system("cls")
    art.tprint(f"Aceur - {version}")
    print("----------------------------------")
    time.sleep(1)
    print(f"用户：{info[0][1].split(':')[1]}")
    confirm_user = input("确认登陆(y/n)> ")
    if confirm_user == "y":
        login_state = False
        cnt = 0

        if not nwp:
            while not login_state:
                os.system("cls")
                art.tprint(f"Aceur - {version}")
                print("----------------------------------")
                getpass = input("\t密码> ")
                if cnt < 2:
                    if info[0][2].split(":")[1] == getpass:
                        os.system("cls")
                        art.tprint(f"Aceur - {version}")
                        print("----------------------------------")
                        print("登陆成功")
                        time.sleep(1)
                        break

                    else:
                        cnt += 1
                        continue
                else:
                    exit("\n登陆失败：密码错误超过三次\n")
        else:
            while not login_state:
                os.system("cls")
                print("请登录以进入Tesford\n")
                getpass = input("\t密码> ")
                if cnt < 2:
                    if str(nwp).rstrip() == getpass:
                        os.system("cls")
                        art.tprint(f"Aceur - {version}")
                        print("----------------------------------")
                        print("登陆成功")
                        time.sleep(1)
                        break

                    else:
                        cnt += 1
                        continue
                else:
                    exit("\n登陆失败：密码错误超过三次\n")

    elif confirm_user == "n":
        new_user(path=path, version=version)
    else:
        sys.exit("\nAceur closed\n")

def new_user(path, version):
    import os
    global username, password

    os.system("cls")
    os.system("cls")
    art.tprint(f"Aceur - {version}")
    print("----------------------------------")
    cs = input("您现在正在创建新用户，继续？(y/n)> ")
    os.system("cls")

    if cs.upper() == "Y":
        global username, password
        print("配置用户信息")
        username = input("\t用户名> ")
        password = input("\t密码> ")
        with open(f"{path}\\Disk\\SystemFile\\cominfo.txt", mode="r") as nur:
            comname = nur.read().split("\n")[0].split(":")[1].rstrip()
            nur.close()

        with open(f"{path}\\Disk\\SystemFile\\cominfo.txt", mode="w+") as nuw:
            nuw.write(f"computername:{comname}\nusername:{username}\npassword:{password}\nDM:false")
            nuw.close()

        os.system("cls")
        os.system("cls")
        print("我们需要一些时间来配置您的更改")
        jdt()
        notonce(path=path, nwp=password, version=version)

    else:
        notonce(path=path, version=version)