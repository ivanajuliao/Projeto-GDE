Feature: Formulario de Login

  Scenario: Autenticacao no sistema

    Given Sou um usuario anonimo
    When Informo o siape e senha corretos
    Then Sou redirecionado para a pagina principal do usuario

    Given Sou um usuario anonimo
    When Informo o siape e senha incorretos
    Then Sou redirecionado para a pagina de login ate que eu informe siape e senha corretos