init python:
    from game import Location, NPCmain, Griffon, Clue, Print, Blood, Note, WeaponClue, Item, Weapon, Case, Murder

"Test Screens"

screen test_case_screen:
    frame:
        xpos 10
        vbox:
            text "Имя : [test_case.name]"
            text "Мотив : [test_case.motivation]"
            text "Убийца: [test_case.guilty.name] [test_case.guilty.surname]"
            text "Жертва: [test_case.victim.name] [test_case.victim.surname]"
            text "[weapon]"

    frame:
        xpos 1020
        vbox:
            textbutton "Протестировать сбор улик" action Jump("test_clue_location")
            textbutton "Протестировать осмотр тела" action Jump("test_body_review")

screen test_body_review:
    frame:
        xpos 740
        vbox:
            textbutton "Осмотерть голову" action (SetVariable("body_part_review", victim_head),
                                                Hide("test_body_review"),
                                                Show("test_bodypart_review"))

    frame:
        xpos 740
        ypos 530
        vbox:
            textbutton "Осмотерть торс" action (SetVariable("body_part_review", victim_torso),
                                                Hide("test_body_review"),
                                                Show("test_bodypart_review"))

    frame:
        xpos 740
        ypos 530
        vbox:
            textbutton "Осмотерть торс" action (SetVariable("body_part_review", victim_torso),
                                                Hide("test_body_review"),
                                                Show("test_bodypart_review"))
    frame:
        xpos 240
        ypos 530
        vbox:
            textbutton "Осмотерть руки" action (SetVariable("body_part_review", victim_hands),
                                                Hide("test_body_review"),
                                                Show("test_bodypart_review"))
    frame:
        xpos 1140
        ypos 530
        vbox:
            textbutton "Осмотерть руки" action (SetVariable("body_part_review", victim_hands),
                                                Hide("test_body_review"),
                                                Show("test_bodypart_review"))
    frame:
        xpos 740
        ypos 900
        vbox:
            textbutton "Осмотерть ноги" action (SetVariable("body_part_review", victim_legs),
                                                Hide("test_body_review"),
                                                Show("test_bodypart_review"))

    frame:
        xpos 1040
        ypos 900
        vbox:
            textbutton "Назад" action (Jump("test_case_location"))

screen test_bodypart_review:
    frame:
        xpos 740
        ypos 530
        vbox:
            text "[body_part_review]"
            textbutton "Назад" action (Hide("test_bodypart_review"), Show("test_body_review"))

label start:

    $ test_case = Murder()
    python:
        test_case.test_create_murder()
        test_case.name = "Тестовое дело об убийстве"
        clue_list = [i.name for i in test_case.clues]
        weapon = "none"
        for i in test_case.clues:
            if i.type == "weapon":
                weapon = i.name

    $ body_part_review = "None"
    $ victim_head = test_case.victim.param["head"]
    $ victim_torso = test_case.victim.param["torso"]
    $ victim_hands = test_case.victim.param["hands"]
    $ victim_legs = test_case.victim.param["legs"]

    jump test_case_location



label test_case_location:

    call screen test_case_screen
    with dissolve

label test_clue_location:

    

label test_body_review:

    call screen test_body_review
    with dissolve