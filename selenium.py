from selenium import webdriver
from time import sleep
import unittest    #导入单元测试库
from selenium.webdriver.support.wait import WebDriverWait    #导入显式等待的库
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select    #导入下拉框定位库

class lei(unittest.TestCase):
    def setUp(self):
        # chromedriver="C:\Program Files(x86)\Google\Chrome\Application\chromedriver.exe"
        # os.environ=["webdriver.chrome.driver"]=chromedriver
        self.dr = webdriver.Chrome()
        self.dr.implicitly_wait(20)    #隐式等待，最长20秒
        self.dr.get('http://sansimstest.zyosoft.cn')    #进入后台管理登录界面
        self.dr.maximize_window()    #全屏，不然后面运行不了，理解不能
        sleep(2)
        self.dr.find_element_by_id('uid').send_keys('xxx@brand')    #用户名
        self.dr.find_element_by_id('pswd').send_keys('123456')    #密码
        self.dr.find_element_by_xpath('//*[@id="login-box"]/div/div/form/fieldset/div[2]/button/span').click()    #点击LOGIN登录按钮
        try:
            WebDriverWait(self.dr,20,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="navbar"]/div/div[1]/div[2]/ul/li')))
        finally:
            self.dr.find_element_by_xpath('//*[@id="navbar"]/div/div[1]/div[2]/ul/li').click()    #使用显式等待，点击右上角的头像框按钮:
        sleep(2)
        self.dr.find_element_by_xpath('//*[@id="navbar"]/div/div[1]/div[2]/ul/li/ul/li[1]').click()    #在下拉框中选中“切换分校”
        self.dr.find_element_by_xpath('//*[@id="xxx-01"]/table/tbody/tr[1]/td[3]/a').click()    #选中“测试校”，点击进入

    def tearDown(self):
        sleep(5)
        self.dr.close()
        self.dr.quit()

    def a(self, x, xpath):
        xpath_str = '//*[@id="navbar"]/div/div[2]/nav/ul/li[%d]%s' % (x, xpath)
        return xpath_str
    def b(self, arg):
        find_way = self.dr.find_element_by_xpath(arg).click()
        return find_way            #将“点击上方任务栏XX”以及“选中下拉框中的XXXX”事件写成函数

    def test_A(self):    #新增员工流程
        xpath1=self.a(2,'')
        self.b(xpath1)    #选中上方任务栏“人事”按钮
        #self.dr.find_element_by_xpath('//*[@id="navbar"]/div/div[2]/nav/ul/li[2]').click()
        xpath2=self.a(2,'/ul/li/div/div/div[2]/ul/li[2]/a')
        try:
            WebDriverWait(self.dr,20,0.5).until(EC.presence_of_element_located((By.XPATH,xpath2)))
        finally:
            self.b(xpath2)        #使用显式等待，在下拉框中选中“员工列表”按钮
        #self.dr.find_element_by_xpath('//*[@id="navbar"]/div/div[2]/nav/ul/li[2]/ul/li/div/div/div[2]/ul/li[2]/a').click()
        self.dr.find_element_by_xpath('//*[@id="main-container"]/div[1]/div/div[2]/div[1]/div[3]/a[1]/i').click()    #点击右方的新建员工“+”按钮
        sleep(2)
        self.dr.find_element_by_id('Mstr_emp_chi').send_keys('员工三号')    #在中文名填空处输入名字
        Select(self.dr.find_element_by_id('Mstr_code_person_sex')).select_by_visible_text('男')    #在性别下拉框中选择性别
        Select(self.dr.find_element_by_id('Mstr_code_person_cert')).select_by_visible_text('身份证')    #在证件下拉框中选择“身份证”
        self.dr.find_element_by_id('Mstr_cert_num').send_keys('11111101')    #在证件号码填空处输入号码
        self.dr.find_element_by_id('Mstr_emp_phone').send_keys('13156420861')    #在联系电话填空处输入手机号码（伪）
        self.dr.find_element_by_id('Mstr_change_date').send_keys('2019-07-20')    #在入职时间填空处输入日期
        self.dr.find_element_by_id('Mstr_birth_date').send_keys('2000-06-01')
        self.dr.find_element_by_xpath('//*[@id="modalForm"]/div[3]/div/div[2]/button[2]').click()    #点击“提交”按钮
        sleep(2)
        try:
            self.dr.switch_to.alert.accept()  # 消除弹窗
        except:
            print("没有弹窗")


    def test_B(self):    #新增学生流程
        xpath3=self.a(1,'')
        self.b(xpath3)    #选中上方任务栏“班务”按钮
        xpath4=self.a(1,'/ul/li/div/div/div[2]/ul/li[2]/a')
        sleep(2)
        self.b(xpath4)    #在下拉框中选中“学生列表”按钮
        self.dr.find_element_by_xpath('//*[@id="main-container"]/div[1]/div/div[2]/div[1]/div[3]/a[1]').click()    #点击右方的新建学生“+”按钮
        sleep(2)
        self.dr.find_element_by_id('Stud_stud_chi').send_keys('学生三号')    #在中文名填空处输入名字
        Select(self.dr.find_element_by_id('Stud_code_person_sex')).select_by_visible_text('男')    #在性别下拉框中选择性别
        self.dr.find_element_by_id('Stud_birth_date').send_keys('2015-06-01')    #在生日填空处输入生日日期
        self.dr.find_element_by_id('Stud_con_tel_1').send_keys('13165087421')    #在联系电话填空处输入手机号码（伪）
        self.dr.find_element_by_id('Stud_con_user_1').send_keys('爸爸')
        self.dr.find_element_by_xpath('//*[@id="modalForm"]/div[3]/div/div[2]/button[2]').click()    #点击“提交”按钮
        sleep(2)
        try:
            self.dr.switch_to.alert.accept()  # 消除弹窗
        except:
            print("没有弹窗")

    def test_C(self):    #新增班级流程
        xpath3=self.a(1,'')
        self.b(xpath3)    #选中上方任务栏“班务”按钮
        xpath5=self.a(1,'/ul/li/div/div/div[2]/ul/li[3]/a')
        sleep(2)
        self.b(xpath5)    #在下拉框中选中“班级列表”按钮
        self.dr.find_element_by_xpath('//*[@id="main-container"]/div[1]/div/div[2]/div/div/div[1]/div[3]/a[1]').click()    #点击右方的新建班级“+”按钮
        sleep(2)
        self.dr.find_element_by_xpath('//*[@id="modalForm"]/div[2]/div/div[1]/div/div/span').click()    #点击选择课程的“放大镜”按钮
        sleep(2)
        self.dr.find_element_by_xpath('//*[@id="jsnode-t0-xxx-aa"]/i').click()    #点击“测试”课程的展开“+”按钮
        self.dr.find_element_by_id('jsnode-t1-xxx-cc_anchor').click()    #选中“测试2班”
        self.dr.find_element_by_id('divHeader').click()    #点击一个空白的地方消去这个下拉框以进行后续操作
        self.dr.find_element_by_id('Mstr_class_chi').send_keys('班级三号')    #在中文名填空处输入名称
        self.dr.find_element_by_xpath('//*[@id="selectRoomDiv"]/div/div/span').click()    #点击选择班主任的“放大镜”按钮
        sleep(2)
        self.dr.find_element_by_xpath('//*[@id="mytable-user"]/tbody/tr[1]').click()    #点击刚刚创建的新员工作为班主任
        self.dr.find_element_by_xpath('//*[@id="modalForm"]/div[3]/div/div[2]/button[2]').click()    #点击“提交”按钮
        sleep(2)
        try:
            self.dr.switch_to.alert.accept()  # 消除弹窗
        except:
            print("没有弹窗")

if __name__=='__main__':
    unittest.main()