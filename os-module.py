import os

you_xiao_id = os.getuid()
print(you_xiao_id)

jin_cheng_id = os.getpid()
print(jin_cheng_id)

caozuo_system_data = os.uname()
print(caozuo_system_data)

dang_qian_mulu = os.getcwd()
print(dang_qian_mulu)

chang_dang_qian_mulu = os.chdir("mymodule")
print(chang_dang_qian_mulu)
