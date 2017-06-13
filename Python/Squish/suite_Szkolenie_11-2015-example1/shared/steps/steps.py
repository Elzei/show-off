# -*- coding: utf-8 -*-

import __builtin__
@Given("adresbook jest uruchomiony")
def step(context):
    startApplication("Addressbook")
    waitFor("object.exists(':Address Book - Unnamed_Window')", 20000)
    test.compare(findObject(":Address Book - Unnamed_Window").enabled, True)

@When("Dodam nową tabele")
def step(context):
    mouseClick(waitForObject(":Address Book - Unnamed_Window"), 113, 14, MouseButton.PrimaryButton)
    mouseClick(waitForObject(":New_ToolbarItem"))
    waitFor("object.exists(':Address Book - Unnamed_Table')", 20000)
    test.compare(findObject(":Address Book - Unnamed_Table").enabled, True)

@Then("Wtedy mamy pustą table")
def step(context):
    waitFor("object.exists(':Address Book - Unnamed_Table')", 20000)
    test.compare(findObject(":Address Book - Unnamed_Table").rowCount, 0)
    mouseClick(waitForObject(":Save_ToolbarItem"))
    type(waitForObject(":Address Book - Save As_Edit"), "MojaNowaTabela")
    clickButton(waitForObject(":Address Book - Save As.Save_Button"))


@Given("Tabela jest otwarta")
def step(context):
    mouseClick(waitForObject(":Open_ToolbarItem"))
    mouseClick(waitForObject(":Open_ToolbarItem"))
    mouseClick(waitForObject(":_Edit_2"), 47, 7, MouseButton.PrimaryButton)
    clickButton(waitForObject(":Address Book - Choose File.Open_Button"))
    waitFor("object.exists(':Address Book - MojaNowaTabela.adr_Table')", 20000)
    test.compare(findObject(":Address Book - MojaNowaTabela.adr_Table").enabled, True)

@When("Dodam nowa pozycje w tabeli")
def step(context):
    mouseClick(waitForObject(":Add_ToolbarItem_2"))
    mouseClick(waitForObject(":Add_ToolbarItem_2"))
    type(waitForObject(":Address Book - Add.Forename:_Edit"), "Adam")
    type(waitForObject(":Address Book - Add.Forename:_Edit"), "Nowak")
    type(waitForObject(":Address Book - Add.Email:_Edit"), "adam@nowak.com")
    type(waitForObject(":Address Book - Add.Phone:_Edit"), "123456789")
    clickButton(waitForObject(":Address Book - Add.OK_Button"))
    mouseClick(waitForObject(":Add_ToolbarItem_2"))
    type(waitForObject(":Address Book - Add.Forename:_Edit"), "Anna")
    type(waitForObject(":Address Book - Add.Surname:_Edit"), "Kowalik")
    type(waitForObject(":Address Book - Add.Email:_Edit"), "Anna@Kowalik.com")
    type(waitForObject(":Address Book - Add.Phone:_Edit"), "987654321")
    clickButton(waitForObject(":Address Book - Add.OK_Button"))

@Then("W tabeli sa nowe pozycje")
def step(context):
    mouseClick(waitForObject(":Save_ToolbarItem_2"))
    waitFor("object.exists(':Address Book - MojaNowaTabela.adr_Table')", 20000)
    test.compare(findObject(":Address Book - MojaNowaTabela.adr_Table").rowCount, 2)
