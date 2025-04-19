import os
import time
import messagebox
import zipfile
import shutil

# 获得当前时间戳
tick = int(time.time())
# 转换日期格式
timeArray = time.localtime(tick)
formatted_time = time.strftime("%Y-%m-%d-%H-%M", timeArray)



# ----------------------------------------------------------------------------------------- #

backupfiles = {'behavior_packs', 'resource_packs', 'worlds', 'plugins'}  # 备份的原始文件(文件名存于字典里）!!（使用时向括号里添加文件名即可)（确保文件/文件夹在同一路径下）!!
oripath = "E:/Minecraft/MC_Server-lib/bedrock_server"      # 要备份文件的原始目录
namae = "[" + formatted_time + "]" + "ikivTivat" + '.zip'       # 压缩包文件命名
tarpath = "E:/Documents/MCbackup/Bedrock/World存档/伊久提瓦特Tivat"      # 目标目录

# ----------------------------------------------------------------------------------------- #



if not os.path.exists(oripath):  # 如果原始目录不存在
    messagebox.showerror("BackupTool", "Origin Path did not found.原始文件夹不存在")  # 错误弹窗
else:  # 如果原始目录存在
    if not tarpath:  # 如果目标目录不存在
        os.makedirs(tarpath)
        os.chdir(oripath)  # 新建目录并定位至原始目录
    else:  # 如果目标目录已经存在
        os.chdir(oripath)   # 定位至原始目录

        # 判断原始文件是否存在
        check = 0
        for key in backupfiles:
            if not os.path.exists(key):
                check = False
                break
            else:
                check = True

        if check:
            # 如果存在
            # 创建一个新的zip文件并向里添加备份文件，之后剪切到目标文件夹
            with zipfile.ZipFile(namae, "w", zipfile.ZIP_DEFLATED) as zipf:  # 创建压缩包
                for key in backupfiles:  # 写入文件至压缩包
                    zipf.write(key)
            if os.path.exists(namae):  # 如果原始目录内有压缩包便将其复制到目标文件夹并删除
                shutil.copy(namae, tarpath)
                os.remove(namae)
            # 检查是否正常复制
            os.chdir(tarpath)  # 定位至目标目录
            if not os.path.exists(namae):  # 检查压缩包是否剪切成功
                messagebox.showerror("BackupTool", "Check not passed,Please try again.检查未通过，请再试一次")
            messagebox.showinfo("BackupTool", "Backup has been Completed.备份已完成^^")
        else:
            # 如果不存在
            messagebox.showerror("BackupTool", "Some Files Couldn't be Found.文件未找到:(")
