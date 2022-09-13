Feature: Login en nuevaweb

  Scenario Outline: Visualizar portal sucursal virtual
    Given launch chrome browser
    When carga portal sucursal virtual
    And Ingresar rut <rut>
    And Ingresar password <password>
    And Click en boton ingresar
    Then valida ingreso

    Examples:
      | rut        | password |
      | 13964644-4 | 111111   |