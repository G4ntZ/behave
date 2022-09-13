Feature: Seguro de motos
  Background: common steps seguro motos
    Given launch chrome browser
    When carga portal principal
    And Selecciona cotizar seguro
    And Seleccion seguro de moto
    And Click en boton cotizar

  Scenario: Seguro de motos valida ingreso
    Then valida ingreso seguro de moto

  Scenario Outline: Seguro de motos comienza a cotizar tu seguro ahora
    Then click full protegido
    And Ingresar rut <rut>
    And Ingresar nombre <nombre>
    And Ingresar apellido paterno <apaterno>
    And Ingresar fecha nacimiento <fnacimiento>
    And Ingresar main <mail>
    And Ingresar celular <celular>
    And Aceptar terminos
    And Click cotizar ahora
    And Validar seguro moto full protegido

    Examples:
      | rut        | nombre   | apaterno | fnacimiento | mail | celular |
      | 13964644-4 | Felipe   | Garnica  | 14-09-1994  | gersongarcia@package.cl | 950726673 |
      | 18870569-3 | Gerson   | Garcia  | 14-09-1994  | gersongarcia@package.cl | 950726673 |