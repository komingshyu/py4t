from 海龜模組 import *

縮減 = 0.8
角度 = 30  

def 樹枝(長, 層, 顏色=255):
    if 層 == 0:
        畫點(5, 'white')
        return
    
    畫筆尺寸(層)
    畫筆顏色(顏色, 顏色, 顏色, )
    
    向前(長)
    畫點(7, 'white')
    
    右轉(角度)
    樹枝(長*縮減, 層-1, 顏色 - 20)
    
    左轉(角度 * 2)
    樹枝(長*縮減, 層-1, 顏色 - 20)
    
    右轉(角度)
    向後(長)

背景顏色('black')
畫筆顏色('white')
設定方向(90)
速度(0)

樹枝(層=8, 長 =100) 
