init python:
    from game import Location, NPCmain, Griffon, Clue, Print, Blood, Note, WeaponClue, Item, Weapon, Case, Murder

label start:

    $ test_case = Murder()
    python:
        test_case.test_create_murder()

    return
