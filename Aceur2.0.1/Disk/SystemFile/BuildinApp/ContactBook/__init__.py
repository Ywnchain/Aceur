def main(blver):
    import os
    path = os.getcwd()
    version = "0.2"
    blver = blver

    os.system("cls")
    print(f"ContactBook {version}")
    print("输入\"return\"以回到主界面\n")

    while True:
        try:
            cmd = input("ContactBook-cmd> ")
            cs = cmd.split(" ")
            if cs[0].lower() == "create":
                print("添加联系人：")
                firstn = input("姓：")
                lastn = input("名：")
                tel = input("电话：")
                mail = input("邮箱：")
                addr = input("地址：")
                with open(f"{path}\\Disk\\UserFile\\ContactBook\\{firstn}{lastn}.blcon", mode="x+") as cet:
                    cet.write(f"{firstn} {lastn}\n{tel}\n{mail}\n{addr}")

            elif cs[0].lower() == "search":
                sear = input("搜索内容：")
                with open(f"{path}\\Disk\\UserFile\\ContactBook\\{sear}.blcon", mode="r")as ser:
                    print("联系人信息：")
                    print(ser.read())

            if cs[0] == "return":
                break
        except IndexError:
            print("缺少必要的参数")