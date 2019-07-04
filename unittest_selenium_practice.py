# import unittest
# from  time import sleep
# from selenium import webdriver
# class YoujiuyeTest(unittest.TestCase):
#     def setUp(self):
#         self.chrome=webdriver.Chrome()
#         self.chrome.get("http://xue.ujiuye.com/foreuser/login/")
#     def test_login_password(self):
#         username_dl=self.chrome.find_element_by_id("username_dl")
#         password_dl=self.chrome.find_elements_by_id("password_dl")
#         button=self.chrome.find_elements_by_class_name("loginbutton1")
#         username_dl.send_keys("13313361216")
#         password_dl.seng_keys("111")
#         button[0].click()
#         text=self.chrome.find_element_by_id("J_usernameTip").text
#         self.assertEqual("密码应该为6-20位！",text,"密码太短提示内容有误")
#     def test_login_username(self):
#         username_dl = self.chrome.find_element_by_id("username_dl")
#         password_dl = self.chrome.find_elements_by_id("password_dl")
#         button = self.chrome.find_elements_by_class_name("loginbutton1")
#         username_dl.send_keys("13313361216")
#         password_dl.send_keys("123456789")
#         button[0].click()
#         text = self.chrome.find_element_by_id("J_usernameTip").text
#         self.assertEqual("账号不存在！", text, "提示内容有误")
#     def tearDown(self):
#         sleep(10)
#         self.chrome.close()
# if __name__ == '__main__':
#     unittest.main()
import unittest
from time import sleep
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
class Ujiuye_test(unittest.TestCase):
    def setUp(self):
        self.chrome=webdriver.Chrome()
        self.chrome.get("http://xue.ujiuye.com/foreuser/login/")

    def login(self,iusername,ipassword):
        username=self.chrome.find_element_by_id("username_dl")
        password=self.chrome.find_element_by_id("password_dl")
        button=self.chrome.find_elements_by_class_name("loginbutton1")
        username.send_keys(iusername)
        password.send_keys(ipassword)
        button[0].click()
        text=self.chrome.find_element_by_id("J_usernameTip")
        return text
    def test_login_password(self):
        text=self.login("13313361216","123")
        self.assertEqual("密码应该为6-20位之间",text,'密码太短提示内容有误')
    def test_login_username(self):
        text=self.login("13313361216","123456789")
        self.assertEqual("账号不存在",text,"提示内容有误")
    def tearDown(self):
        sleep(10)
        self.chrome.close()

if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(Ujiuye_test("test_login_username"))
    suite.addTest(Ujiuye_test("test_login_password"))
    with open("report.html","wb")as f :
        runner=HTMLTestRunner(
            stream=f,
            title="教学测试",
            description="就是一个教学测试"

        )
        runner.run(suite)

