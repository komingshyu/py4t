# 模組區 ----------------
from 海龜模組 import *

# 全域變數 ----------------

# 函式區 ----------------
def 初始設定() :
    左轉(90)
    
def 遞迴(層) :
    if 層 > 5 :
        畫點(10, 'red')
        return
    
    向前(50)
    畫點(10, 'black')
    右轉(20)
    
    遞迴(層 + 1)
    
    左轉(20)
    向後(50)
        
# 主程式 ----------------
初始設定()
遞迴(1)
完成()