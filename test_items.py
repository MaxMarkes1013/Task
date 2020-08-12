import time
def test_we_should_add_a_book(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_css_selector('.btn-add-to-basket')
    assert button, "Кнопка добавления товара отсутствует на сайте"