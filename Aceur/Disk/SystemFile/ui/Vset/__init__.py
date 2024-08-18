def main(version, path):
    import random
    import os

    def get_size(start_path=f"{path}\\"):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                # skip if it is symbolic link
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)
        int(total_size)
        total_size = str(total_size / 1024)[0:5]

        return total_size


    with open(f"{path}\\Disk\\SystemFile\\cominfo.txt") as ocom:
        cominfo = ocom.readline().rstrip().split(":")[1]
        userinfo = ocom.readline().rstrip().split(":")[1]

    print(f"计算机名称：{cominfo}")
    print(f"系统版本：Tesford {version}")
    print(f"系统标识码：{random.randint(10000000, 99999999)}")
    print(f"系统安装文件夹：{path}\n")
    print(f"用户：{userinfo}\n")
    print(f"磁盘：{get_size()} KB/ 1024 KB")