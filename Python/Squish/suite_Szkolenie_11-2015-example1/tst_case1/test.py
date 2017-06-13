# -*- coding: utf-8 -*-

def main():
    startApplication("Addressbook")
    mouseClick(waitForObject(":Open_ToolbarItem"))
    mouseClick(waitForObject(":_Edit_2"), 69, 14, MouseButton.PrimaryButton)
    clickButton(waitForObject(":Address Book - Choose File.Open_Button"))
    doubleClick(waitForObject(":2_1_TableCell"), 76, 11, MouseButton.PrimaryButton)
    mouseClick(waitForObject(":2_1_TableCell"))
    type(waitForObject(":_Edit"), "Adam")
    doubleClick(waitForObject(":2_2_TableCell"), 55, 12, MouseButton.PrimaryButton)
    mouseClick(waitForObject(":2_2_TableCell"))
    type(waitForObject(":_Edit"), "Kuc")
    doubleClick(waitForObject(":2_3_TableCell"), 57, 12, MouseButton.PrimaryButton)
    mouseClick(waitForObject(":2_3_TableCell"))
    type(waitForObject(":_Edit"), "adam@nonexist.com")
    doubleClick(waitForObject(":2_4_TableCell"), 12, 10, MouseButton.PrimaryButton)
    mouseClick(waitForObject(":2_4_TableCell"))
    type(waitForObject(":_Edit"), "1112223330")
    mouseClick(waitForObject(":2_4_TableCell"))
    #test.vp("V1")
    
    pass
    mouseClick(waitForObjectItem(":Address Book - MyAddresses.adr_Menubar", "File"))
    mouseClick(waitForObject(":File.Quit_MenuItem"))
