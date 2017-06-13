# This is a sample .feature file
# Squish feature files use the Gherkin language for describing features, a short example
# is given below. You can find a more extensive introduction to the Gherkin format at
# https://github.com/cucumber/cucumber/wiki/Gherkin
Feature: Dodawanie nowych wpisów w aplikacji adressbook 

    Scenario: Utworzenie tabeli

        Given adresbook jest uruchomiony 
         When Dodam nową tabele
         Then Wtedy mamy pustą table
    
    Scenario: Dodanie pierwszych wpisow
        
        Given adresbook jest uruchomiony
        And Tabela jest otwarta
        When Dodam nowa pozycje w tabeli
        Then W tabeli sa nowe pozycje
        
    Scenario:
        
        Given adresbook jest uruchomiony 3
        And Tabela jest otwarta 2
        And Tabela jest uzupelniona
        When Zmienie dane
        Then Dane zostaly zmienione