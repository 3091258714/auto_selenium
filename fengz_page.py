from base_page import base_page
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class fengz_page(base_page):
    dl_loc=(By.CLASS_NAME,'link-login')#登录
    qqdl=(By.CLASS_NAME,'QQ-icon')#qq图标
    kj=(By.ID,'ptlogin_iframe')
    tx=(By.ID,'img_out_3091258714')#头像
    # 加入购物车定位
    xq=(By.CLASS_NAME,'lazyimg_img')#商品详情
    zcxq=(By.CLASS_NAME,'seckill_mod_goods_link_img')#再次进入详情
    gwc=(By.XPATH,'//*[@id="InitCartUrl"]')#加入购物车
    # 购物车
    wdgcw=(By.LINK_TEXT,'我的购物车')
    qjs=(By.XPATH,'/html/body/div[4]/div[1]/div[19]/div/div[2]/div/div/div/div[2]/div[2]/div/div[1]/a/b')
    # 搜索
    ssk=(By.ID,'key')
    def caoz_01(self):#登录业务
        self.driver.find_element(*self.dl_loc).click()#登录
        sleep(2)
    def caoz_02(self):
        self.driver.find_element(*self.qqdl).click()#QQ登录
        sleep(2)
    def caoz_03(self):
        self.driver.switch_to.frame(self.find_element(*self.kj))#框架、
        self.driver.find_element(*self.tx).click()#点击头像登录
        sleep(2)


    def jrgwc_01(self):#加入购物车
        self.driver.find_element(*self.dl_loc).click()  # 登录
        sleep(2)
    def jrgwc_02(self):
        self.driver.find_element(*self.qqdl).click()  # QQ登录
        sleep(2)
    def jrgwc_03(self):
        self.driver.switch_to.frame(self.find_element(*self.kj))  # 框架
        sleep(3)
    def jrgwc_04(self):
        self.driver.find_element(*self.tx).click()  # 点击头像登录
        sleep(2)
    def jrgwc_05(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        sleep(2)
    def jrgwc_06(self):
        self.driver.execute_script('window.scrollTo(0,300)')
        sleep(2)
    def jrgwc_07(self):
        self.driver.find_element(*self.xq).click()#进入商品详情
        sleep(2)
    def jrgwc_08(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        sleep(2)
    def jrgwc_09(self):
        self.driver.find_element(*self.zcxq).click()  #再次进入详情
        sleep(2)
    def jrgwc_10(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        sleep(2)
    def jrgwc_11(self):
        self.driver.execute_script('window.scrollTo(0,300)')
        sleep(2)
    def jrgwc_12(self):
        self.driver.find_element(*self.gwc).click()  #点击加入购物车
        sleep(2)

    def gmsp_01(self):#购买商品业务
        self.driver.find_element(*self.dl_loc).click()  # 登录
        sleep(2)
    def gmsp_02(self):
        self.driver.find_element(*self.qqdl).click()  # QQ登录
        sleep(2)
    def gmsp_03(self):
        self.driver.switch_to.frame(self.find_element(*self.kj))  # 框架
        sleep(3)
    def gmsp_04(self):
        self.driver.find_element(*self.tx).click()  # 点击头像登录
        sleep(2)
    def gmsp_05(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        sleep(2)
    def gmsp_06(self):
        self.driver.find_element(*self.wdgcw).click()  #我的购物车
        sleep(2)
    def gmsp_07(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        sleep(2)
    def gmsp_08(self):
        self.driver.find_element(*self.qjs).click()  #去结算
        sleep(2)


    def ss_01(self):#搜索业务
        self.driver.find_element(*self.dl_loc).click()  # 登录
        sleep(2)
    def ss_02(self):
        self.driver.find_element(*self.qqdl).click()  # QQ登录
        sleep(2)
    def ss_03(self):
        self.driver.switch_to.frame(self.find_element(*self.kj))  # 框架
        sleep(3)
    def ss_04(self):
        self.driver.find_element(*self.tx).click()  # 点击头像登录
        sleep(2)
    def ss_05(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        sleep(2)
    def ss_06(self):
        self.driver.find_element(*self.ssk).send_keys('香蕉',Keys.ENTER) # 点击头像登录
        sleep(2)
    def luoji1(self):
        self.open_url('https://www.jd.com/')
        sleep(2)
        self.caoz_01()
        self.caoz_02()
        self.caoz_03()
        self.caoz_04()
    def luoji2(self):
        self.open_url('https://www.jd.com/')
        sleep(2)
        self.jrgwc_01()
        self.jrgwc_02()
        self.jrgwc_03()
        self.jrgwc_04()
        self.jrgwc_05()
        self.jrgwc_06()
        self.jrgwc_07()
        self.jrgwc_08()
        self.jrgwc_09()
        self.jrgwc_10()
        self.jrgwc_11()
        self.jrgwc_12()
    def luoji3(self):
        self.open_url('https://www.jd.com/')
        sleep(2)
        self.gmsp_01()
        self.gmsp_02()
        self.gmsp_03()
        self.gmsp_04()
        self.gmsp_05()
        self.gmsp_06()
        self.gmsp_07()
        self.gmsp_08()
    def luoji4(self):
        self.ss_01()
        self.ss_02()
        self.ss_03()
        self.ss_04()
        self.ss_05()
        self.ss_06()




