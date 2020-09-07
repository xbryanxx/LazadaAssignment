from behave import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given(u'We go to homepage and login')
def launchBrower(context):
    # go to redmart homepage
    context.driver = webdriver.Chrome(executable_path='/Users/pilotbryan/automation/LazadaAutoPython/chromedriver')

    # context.driver = webdriver.Firefox()
    context.driver.get('https://redmart.lazada.sg/')
    assert 'Online Grocery Shopping' in context.driver.title

    # Login
    context.driver.find_element_by_id('anonLogin').click()
    context.driver.find_element_by_css_selector('.mod-input input').send_keys('promisenuous0708@gmail.com')
    context.driver.find_element_by_css_selector('input[type="password" i]').send_keys('HappyTesting1')
    context.driver.implicitly_wait(5)
    # move slider
    slider = context.driver.find_element_by_css_selector('.nc-container')
    move = ActionChains(context.driver)
    move.click_and_hold(slider).move_by_offset(300, 0).release().perform()
    # there is an error(error:R19qj7) after sliding done
    # tentative to manually login
    context.driver.implicitly_wait(100)

@when(u'We navigate to the Beverages and Water')
def naviToBeverages(context):
    # Start to add Beverages
    context.driver.find_element_by_link_text('Beverages').click()
    context.driver.find_element_by_class_name('RedmartProductCard-title').click()
    context.driver.implicitly_wait(10)

@then(u'Add one Item from Beverages and Water')
def addBeverages(context):
    # add beverages
    context.driver.find_element_by_css_selector(
        '.pdp-redmart-add-to-cart .redmart-cart-btn .pdp-button, .pdp-redmart-add-to-cart .redmart-cart-btn .redmart-cart-picker').click()

    # Go to shopping cart
    context.driver.find_element_by_id('topActionCartNumber').click()
    context.driver.implicitly_wait(10)

    # Check correct item is added
    assert 'Pokka No Sugar Oolong Tea' in context.driver.page_source
    context.driver.close()

@when(u'We navigate to the Spirits')
def naviToSpirits(context):
    context.driver.find_element_by_link_text('Wines, Beers & Spirits').click()
    context.driver.find_element_by_class_name('RedmartProductCard-title').click()
    context.driver.implicitly_wait(10)

@then(u'Add one Item from Spirits')
def addSpirits(context):
    wait = WebDriverWait(context.driver, 30)
    # choose over 18
    context.driver.find_element_by_class_name('age-restriction-btn-over').click()

    # add spirits
    addItem = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body[@class=' pdp-layout-column-1 ']/div[@id='container']/div[@id='root']/div[@id='block-5zbLNIJMQW']/div[@id='block-hsxQi_uThr']/div[@id='block-2RDx452Tes']/div[@id='block-Nxdgv83WSSK']/div[@id='module_redmart_add_to_cart']/div[@class='pdp-redmart-add-to-cart']/div[@class='redmart-cart-btn']/button[@class='pdp-button pdp-button_type_text pdp-button_theme_red-redmart pdp-button_size_l2']")))
    addItem.click()

    # Go to shopping cart
    cart = wait.until(EC.visibility_of_element_located((By.ID, 'topActionCartNumber')))
    cart.click()

    # Check correct item is added
    assert "Sainsbury's Cava Brut Sparkling Wine" in context.driver.page_source
    context.driver.close()

@when(u'Update number of items')
def updateItems(context):
    # Go to shopping cart
    wait = WebDriverWait(context.driver, 30)
    cart = wait.until(EC.visibility_of_element_located((By.ID, 'topActionCartNumber')))
    cart.click()

    # update number of Beverages to be 3
    addItem = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'next-number-picker-handler-up-inner')))
    addItem.click()
    addItem.click()

    # remove 2nd item
    remove = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'operations')))
    remove.click()

@then(u'Check out items')
def checkoutItems(context):
    wait = WebDriverWait(context.driver, 30)

    # proceed to checkout
    checkAll = wait.until(EC.visibility_of_element_located((By.XPATH,
        "/html/body[@class='venture-SG p-vogayer']/div[@class='lzd-playground']/div[@class='lzd-playground-main']/div[@id='container']/div/div[@class='root']/div[@id='container_C']/div[@id='leftContainer_CL']/div[@id='listHeader_H']/div[@class='list-header-container']/div[@class='list-header-main']/div[@class='checkbox-wrap']")))
    checkAll.click()
    checkoutButton = wait.until(EC.visibility_of_element_located((By.XPATH,
        "/html/body[@class='venture-SG p-vogayer']/div[@class='lzd-playground']/div[@class='lzd-playground-main']/div[@id='container']/div/div[@class='root']/div[@id='container_C']/div[@id='rightContainer_CR']/div[@class='summary-section']/div[@class='summary-section-content']/div[@class='  checkout-summary']/div[@class=' checkout-order-total']/button[@class='next-btn next-btn-primary next-btn-large checkout-order-total-button automation-checkout-order-total-button-button']")))
    checkoutButton.click()

    context.driver.close()

