Feature: Cadastrar EspecieDocumental

  Scenario: Add a new EspecieDocumental
  Given I am a logged user
  When I submit a valid especieDocumental page
  Then I am redirected to the especieDocumental_list page
