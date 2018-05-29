from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time

browser = webdriver.Edge()
# 元素查找与元素交互
# browser.get("http://taobao.com")
# print(browser.page_source)
# input_first = browser.find_element_by_id("q")
# input_second = browser.find_element_by_css_selector("#q")
# input_third = browser.find_element_by_xpath('//*[@id="q"]')
# print(input_first)
# print(input_second)
# print(input_third)

# input_first.send_keys("ddr4")
# time.sleep(1)
# input_first.clear()
# input_first.send_keys("ipad")
# button = browser.find_element_by_class_name('btn-search')
# button.click()

# browser.close()

# 将动作附加到动作链中串行执行(模拟鼠标操作)
'''
click(on_element=None) ——单击鼠标左键
click_and_hold(on_element=None) ——点击鼠标左键，不松开
context_click(on_element=None) ——点击鼠标右键
double_click(on_element=None) ——双击鼠标左键
drag_and_drop(source, target) ——拖拽到某个元素然后松开
drag_and_drop_by_offset(source, xoffset, yoffset) ——拖拽到某个坐标然后松开
key_down(value, element=None) ——按下某个键盘上的键
key_up(value, element=None) ——松开某个键
move_by_offset(xoffset, yoffset) ——鼠标从当前位置移动到某个坐标
move_to_element(to_element) ——鼠标移动到某个元素
move_to_element_with_offset(to_element, xoffset, yoffset) ——移动到距某个元素（左上角坐标）多少距离的位置
perform() ——执行链中的所有动作
release(on_element=None) ——在某个元素位置松开鼠标左键
send_keys(*keys_to_send) ——发送某个键到当前焦点的元素
send_keys_to_element(element, *keys_to_send) ——发送某个键到指定元素
'''

# browser.get("http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
# browser.switch_to.frame('iframeResult')
# source = browser.find_element_by_css_selector('#draggable')
# target = browser.find_element_by_css_selector('#droppable')
# actions = ActionChains(browser)
# actions.drag_and_drop(source, target)
# actions.perform()

# 执行JavaScript
# browser.get("http://www.zhihu.com/explore")

# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# browser.execute_script('alert("to bottom")')

# 获取元素属性
# logo = browser.find_element_by_id('zh-top-link-logo')
# print(logo.get_attribute('class'))

# 获取文本值, id, 位置，标签名，大小
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input.text)
# print(input.tag_name)
# print(input.size)
# print(input.id)
# print(input.location)

# Frame标签切入，切出
# browser.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
# browser.switch_to.frame('iframeResult')
# source = browser.find_element_by_css_selector('#draggable')
# print(source)
# try:
#     logo = browser.find_elements_by_class_name('logo')
# except NoSuchElementException:
#     print('no logo')
# browser.switch_to.parent_frame()
# logo = browser.find_elements_by_class_name('logo')
# print(logo)

# 隐式等待，如果没有找到元素，等待一段时间，如果还没有则抛出异常，浏览器会不断的刷新页面去寻找
# browser.implicitly_wait(2)
# browser.get('https://www.zhihu.com/explore')
# try:
#     input = browser.find_element_by_class_name('question')
#     print(input)
# except NoSuchElementException:
#     print('timeout')

# 显式等待，直到元素出现或元素可点击等条件才去操作，超时则报异常
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
presence_of_element_located（）是确认元素是否已经出现了
element_to_be_clickable（）是确认元素是否是可点击的
title_is 标题是某内容
title_contains 标题包含某内容
presence_of_element_located 元素加载出，传入定位元组，如(By.ID, 'p')
visibility_of_element_located 元素可见，传入定位元组
visibility_of 可见，传入元素对象
presence_of_all_elements_located 所有元素加载出
text_to_be_present_in_element 某个元素文本包含某文字
text_to_be_present_in_element_value 某个元素值包含某文字
frame_to_be_available_and_switch_to_it frame加载并切换
invisibility_of_element_located 元素不可见
element_to_be_clickable 元素可点击
staleness_of 判断一个元素是否仍在DOM，可判断页面是否已经刷新
element_to_be_selected 元素可选择，传元素对象
element_located_to_be_selected 元素可选择，传入定位元组
element_selection_state_to_be 传入元素对象以及状态，相等返回True，否则返回False
element_located_selection_state_to_be 传入定位元组以及状态，相等返回True，否则返回False
alert_is_present 是否出现Alert
'''

# browser.get('https://www.taobao.com/')
# wait = WebDriverWait(browser, 5)
# input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
# print(input, button)

# 浏览器前进和后退
# browser.get('https://www.baidu.com/')
# time.sleep(3)
# browser.get('https://www.taobao.com/')
# time.sleep(3)
# browser.get('https://www.python.org/')
# time.sleep(3)
# browser.back()
# time.sleep(3)
# browser.forward()
# time.sleep(3)
# browser.close()

# cookie操作
# browser.get('https://www.zhihu.com/explore')
# print(browser.get_cookies())
# time.sleep(3)
# browser.add_cookie({'name':'name', 'domain': 'www.zhihu.com', 'value': 'zhaofan'})
# print(browser.get_cookies())
# time.sleep(3)
# browser.delete_all_cookies()
# time.sleep(3)
# print(browser.get_cookies())

# 选项卡管理, 通过执行js命令window.open()实现新开选项卡, 不同的选项卡是存在列表里browser.window_handles
# browser.get('https://www.baidu.com')
# browser.execute_script('window.open()')
# print(browser.window_handles)
# browser.switch_to_window(browser.window_handles[1])
# browser.get('https://www.taobao.com')
# time.sleep(3)
# browser.switch_to_window(browser.window_handles[0])
# browser.get('https://python.org')
