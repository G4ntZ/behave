import allure
from behave import *
from selenium import webdriver
import allure
from allure_commons.types import AttachmentType

import os

@given('launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
    context.driver.maximize_window()


@when('carga portal sucursal virtual')
def openSucursalVirtual(context):
    context.driver.get("https://nuevaweb.qa.afphabitat.cl/seguridad/autenticacion/internet/login/nw/autenticar")

@when('Ingresar rut {rut}')
def setRut(context, rut):
    xpath = "/html/body/afp-habitat-sitio-privado-root/afp-habitat-sitio-privado-app-login/section/div[1]/div/form/div[1]/input"
    status = context.driver.find_element("xpath", xpath).is_displayed()
    context.driver.implicitly_wait(1)
    assert status is True
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    context.driver.find_element("xpath", xpath).send_keys(rut)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


@when('Ingresar password {password}')
def setPass(context, password):
    xpath = "/html/body/afp-habitat-sitio-privado-root/afp-habitat-sitio-privado-app-login/section/div[1]/div/form/div[2]/input"
    status = context.driver.find_element("xpath", xpath).is_displayed()
    context.driver.implicitly_wait(1)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    assert status is True
    context.driver.find_element("xpath", xpath).send_keys(str(password))
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

@when('Click en boton ingresar')
def step_impl(context):
    xpath = "/html/body/afp-habitat-sitio-privado-root/afp-habitat-sitio-privado-app-login/section/div[1]/div/form/button"
    status = context.driver.find_element("xpath", xpath).is_displayed()
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    assert status is True
    context.driver.find_element("xpath", xpath).click()
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


@then('valida ingreso')
def closeBrwoser(context):
    xpath = "/html/body/afp-habitat-sitio-privado-root/div/div[4]/div[1]/afp-habitat-sitio-privado-widgets-despliegue-cuentas/div/div[1]/div/ul/li[1]/div"
    context.driver.implicitly_wait(15)
    iframe = context.driver.find_element("xpath", '//*[@id="iframeResponsive"]')
    context.driver.switch_to.frame(iframe)
    context.driver.implicitly_wait(20)
    try:
        textobienvenida = context.driver.find_element("xpath", xpath).text
    except:
        context.driver.close()
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        print(f'no se ecuentra elemento: {xpath}')
        assert False, "Test fallido"
    print(f'textobienvenida capturado: {textobienvenida}')
    context.driver.switch_to.default_content()
    assert textobienvenida == "Evolución de tu Estado de Cuenta"
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    context.driver.close()

