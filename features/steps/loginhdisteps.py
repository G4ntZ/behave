import allure
from behave import *
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import allure
from allure_commons.types import AttachmentType
import time

@when('carga portal principal')
def step_impl(context):
    context.driver.get("https://www.hdi.cl/")


@when('Selecciona cotizar seguro')
def step_impl(context):
    xpath = '//*[@id="cotizar"]/div/div[1]/div[1]/select'
    status = context.driver.find_element("xpath", xpath).is_displayed()
    assert status is True

@when('Seleccion seguro de moto')
def step_impl(context):
    xpath = '//*[@id="cotizar"]/div/div[1]/div[1]/select'
    select = Select(context.driver.find_element("xpath", xpath))
    select.select_by_visible_text("Seguro de Moto")
    
@when('Click en boton cotizar')
def step_impl(context):
    xpath = '//*[@id="btn_CotizarSeguro"]/span'
    status = context.driver.find_element("xpath", xpath).is_displayed()
    assert status is True
    context.driver.find_element("xpath", xpath).click()

@then('valida ingreso seguro de moto')
def step_impl(context):
    xpath = '/html/body/app-root/app-full-layout/div/div[2]/div/div/div/app-product-list/section[3]/div/div[2]/div/form/div[2]/div/button'
    status = context.driver.find_element("xpath", xpath).is_displayed()
    assert status is True

@then('click full protegido')
def step_impl(context):
    xpath = '/html/body/app-root/app-full-layout/div/div[2]/div/div/div/app-product-list/section[3]/div/div[2]/div/form/div[2]/div/button'
    context.driver.find_element("xpath", xpath).click()

@then('Ingresar rut {rut}')
def step_impl(context, rut):
    xpath = '/html/body/app-root/app-full-layout/div/div[2]/div/div/div/app-product-list/section[3]/div/div[2]/div/app-create-quotation-form/app-fieldset-party/div/form/div/div/div[1]/div/div/input'
    context.driver.find_element("xpath", xpath).send_keys(rut)


@then('Ingresar nombre {nombre}')
def step_impl(context, nombre):
    xpath = '/html/body/app-root/app-full-layout/div/div[2]/div/div/div/app-product-list/section[3]/div/div[2]/div/app-create-quotation-form/app-fieldset-party/div/form/div/div/div[2]/div[1]/div/input'
    context.driver.find_element("xpath", xpath).send_keys(nombre)


@then('Ingresar apellido paterno {apaterno}')
def step_impl(context, apaterno):
    xpath = '/html/body/app-root/app-full-layout/div/div[2]/div/div/div/app-product-list/section[3]/div/div[2]/div/app-create-quotation-form/app-fieldset-party/div/form/div/div/div[2]/div[2]/div/input'
    context.driver.find_element("xpath", xpath).send_keys(apaterno)

@then('Ingresar fecha nacimiento {fnacimiento}')
def step_impl(context, fnacimiento):
    xpath = '/html/body/app-root/app-full-layout/div/div[2]/div/div/div/app-product-list/section[3]/div/div[2]/div/app-create-quotation-form/app-fieldset-party/div/form/div/div/div[2]/div[3]/div/div/input'
    context.driver.find_element("xpath", xpath).send_keys(fnacimiento)

@then('Ingresar main {mail}')
def step_impl(context, mail):
    xpath = '/html/body/app-root/app-full-layout/div/div[2]/div/div/div/app-product-list/section[3]/div/div[2]/div/app-create-quotation-form/app-fieldset-contact-preference/div/form/div/div/div[1]/div/input'
    context.driver.find_element("xpath", xpath).send_keys(mail)

@then('Ingresar celular {celular}')
def step_impl(context, celular):
    xpath = '/html/body/app-root/app-full-layout/div/div[2]/div/div/div/app-product-list/section[3]/div/div[2]/div/app-create-quotation-form/app-fieldset-contact-preference/div/form/div/div/div[2]/div/input'
    context.driver.find_element("xpath", xpath).send_keys(celular)

@then('Aceptar terminos')
def step_impl(context):
    xpath = '/html/body/app-root/app-full-layout/div/div[2]/div/div/div/app-product-list/section[3]/div/div[2]/div/div/div/label'
    context.driver.find_element("xpath", xpath).click()

@then('Click cotizar ahora')
def step_impl(context):
    xpath = '/html/body/app-root/app-full-layout/div/div[2]/div/div/div/app-product-list/section[3]/div/div[2]/div/button/div/span'
    context.driver.find_element("xpath", xpath).click()

@then('Validar seguro moto full protegido')
def step_impl(context):
    xpath = '/html/body/app-root/app-full-layout/div/div[2]/div/div/div/app-quotation-detail/div[3]/div/div/div[2]/app-insured-object/div/div/div[1]/div/div'
    status = context.driver.find_element("xpath", xpath).is_displayed()
    assert status is True