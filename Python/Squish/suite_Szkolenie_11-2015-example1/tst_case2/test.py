# -*- coding: utf-8 -*-

def main():
    for i in range(0,1):
        startApplication("Addressbook")
        mouseClick(waitForObject(":New_ToolbarItem"))
        new_adressys = [["Zenek","Jajczarski","zenus@domena.com","123123123"],
                        ["Maniek","Miotla","maniek@domena.com","123456789"],
                        ["Honorata","Niepotrzebna","x@xx.xx","098765432"]]
        
        for i in range(0, len(new_adressys)):
            mouseClick(waitForObject(":Add_ToolbarItem"))
            type(waitForObject(":Address Book - Add.Forename:_Edit"), new_adressys[i][0])
            type(waitForObject(":Address Book - Add.Surname:_Edit"), new_adressys[i][1])
            type(waitForObject(":Address Book - Add.Email:_Edit"), new_adressys[i][2])
            type(waitForObject(":Address Book - Add.Phone:_Edit"), new_adressys[i][3])
            clickButton(waitForObject(":Address Book - Add.OK_Button"))
        
        #Inner test
        test.vp("VP1")