Feature: Funcionalidade EspecieDocumental


  Background: Em todos os testes o usuário deve estar logado.
    Given Eu sou um usuario logado

  Scenario: Cadastrar campos vazios
  Given Estou na pagina de cadastro de uma especie documental
   When Submeto o cadastro de uma nova especie documental deixando o campo em branco
   Then Nao conseguirei cadastrar a especie ate que eu preencha o campo nome.

  Scenario: Cadastrar nova EspecieDocumental
  Given Estou na pagina de cadastro de uma especie documental
   When Informo um nome ainda nao cadastrado no sistema
    And Submeto o cadastro de uma nova especie
   Then Sou redirecionado para a pagina principal de especie documental
    And A especie devera estar devidamente cadastrada.

  Given Estou na pagina de cadastro de uma especie documental
   When Informo um nome ja cadastrado no sistema
    And Submeto o cadastro de uma nova especie
   Then Recebo uma mensagem de erro informando que o nome ja existe.
    And Nao conseguirei cadastrar a especie ate que eu preencha o com um nome diferente.

  Scenario:  Editar Especie documental
  Given Estou na pagina com a lista de especies documentais
    And Possue uma ou mais especies documentais cadastradas
   When Seleciono o botao editar de uma especie documental
    And Sou redirecionado para a pagina com seus dados ja preenchidos
    And Preencho o campo especie documental com um novo nome
    And Clico no botao salvar
   Then Sou redirecionado para a pagina principal de especie documental

  Given Estou na pagina com a lista de especies documentais
    And Possue uma ou mais especies documentais cadastradas
   When Seleciono o botao editar de uma especie documental
    And Sou redirecionado para a pagina com seus dados ja preenchidos
    And Edito o campo especie documental e o deixo em branco
    And Clico no botao salvar
   Then Nao conseguirei editar a especie ate que preencha o campo nome

    Given Estou na pagina com a lista de especies documentais
    And Possue uma ou mais especies documentais cadastradas
   When Seleciono o botao editar de uma especie documental
    And Sou redirecionado para a pagina com seus dados ja preenchidos
    And Edito o nome e coloco um nome que ja esta cadastrado
    And Clico no botao salvar
   Then Nao conseguirei salvar a especie ate que eu a preencha com um nome diferente.

  Given Estou na pagina com a lista de especies documentais
    And Possue uma ou mais especies documentais cadastradas
   When Seleciono o botao editar de uma especie documental
    And Sou redirecionado para a pagina com seus dados ja preenchidos
    And Nao altero a especie documental deixando com o nome ja preenchido
    And Clico no botao salvar
   Then Nao conseguirei salvar a especie ate que eu a preencha com um nome diferente.

  Scenario: Visualizar Especie Documental
  Given Uma especie documental foi cadastrada
  When  Sou redirecionado para a pagina principal de especie documental
  Then  A especie documental devera aparecer na lista.

  Given Estou na pagina principal do sistema
    And Possue uma ou mais especies documentais cadastradas
  When  clico no botao visualizar especie documental
  Then  Sou redirecionado para a pagina principal de especie documental

  Scenario: Excluir especie documental
   Given Estou na pagina com a lista de especies documentais
     And que existem especies documentais cadastradas
    When clico no botao excluir
    Then a especie documental deixara de existir.

