init python:
    from game import Location, NPCmain, Griffon, Clue, Print, Blood, Note, WeaponClue, Item, Weapon, Case, Murder

"Test Screens"

screen test_case_screen:
    frame:
        xpos 100
        vbox:
            text "Имя : [test_case.name]"
            text "Мотив : [test_case.motivation]"
            text "Убийца: [test_case.guilty.name] [test_case.guilty.surname]"
            text "Жертва: [test_case.victim.name] [test_case.victim.surname]"
            text "[weapon]"


label start:

    $ test_case = Murder()
    python:
        test_case.test_create_murder()
        test_case.name = "Тестовое дело об убийстве"
        clue_list = [i.name for i in test_case.clues]
        weapon = "None"
        for i in test_case.clues:
            if i.type == "weapon":
                weapon = i.name

    jump test_case_loc



label test_case_loc:

    "Тестовое окно будет здесь"

    call screen test_case_screen