import time
from xgolib import XGO
from xgoedu import XGOEDU
import random

# 初始化机器狗和头部控制接口
xgo = XGO("xgolite")
XGO_edu = XGOEDU()

# 前进
xgo.move_x(15)
time.sleep(3) # 前进3秒
xgo.move_x(0)

# 撒尿
xgo.action(11, wait=True) # 撒尿的id为11

# 趴下
xgo.action(1, wait=True) # 趴下的id为1

# 再次撒尿
xgo.action(11, wait=True) # 撒尿的id为11

# 复位机器狗，准备下一个动作
xgo.reset()