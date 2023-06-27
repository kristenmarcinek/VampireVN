screen gallery():
    tag menu

    imagemap:
        ground "gui/gallery.png"
        hover "gui/gallery h.png"
        selected_idle "gui/gallery h.png"

        hotspot (79, 301, 255, 69) action Return()
        hotspot (76, 383, 199, 65) action ShowMenu("save")
        hotspot (76, 463, 207, 66) action ShowMenu("load")
        hotspot (72, 539, 302, 75) action ShowMenu("preferences")
        hotspot (77, 626, 205, 63) action MainMenu()
        hotspot (77, 703, 201, 77) action Quit(confirm=True)



    imagemap: #laila cg 1

        xpos 50
        ypos 141
        ground Null()
        hover Null()

        if persistent.laila1:
            ground "gui/laila 1 gal.png"
            hover "gui/laila 1 galh.png"

            hotspot (0, 0, 1280, 720) action ShowMenu ('lailagal1')


    imagemap: #laila cg 2

        xpos 341
        ypos 141
        ground Null()
        hover Null()

        if persistent.laila2:
            ground "gui/laila 2 gal.png"
            hover "gui/laila 2 galh.png"

            hotspot (0, 0, 1280, 720) action ShowMenu ('lailagal2')


    imagemap: #cass cg 1

        xpos 670
        ypos 141
        ground Null()
        hover Null()

        if persistent.cass1:
            ground "gui/cass 1 gal.png"
            hover "gui/cass 1 galh.png"

            hotspot (0, 0, 1280, 720) action ShowMenu ('cassgal1')

    imagemap: #cass cg 2

        xpos 960
        ypos 141
        ground Null()
        hover Null()

        if persistent.cass2:
            ground "gui/cass 2 gal.png"
            hover "gui/cass 2 galh.png"

            hotspot (0, 0, 1280, 720) action ShowMenu ('cassgal2')

screen lailagal1:
    tag menu
    imagemap:
        ground "/cg/laila cg 1.png"
        hover "/cg/laila cg 1.png"
        yalign 0.0

        hotspot (0, 0, 1280, 720) action ShowMenu('gallery')

screen lailagal2:
    tag menu
    imagemap:
        ground "/cg/laila cg 2.png"
        hover "/cg/laila cg 2.png"
        yalign 0.0

        hotspot (0, 0, 1280, 720) action ShowMenu('gallery')

screen cassgal1:
    tag menu
    imagemap:
        ground "/cg/cass cg 1.png"
        hover "/cg/cass cg 1.png"
        yalign 0.0

        hotspot (0, 0, 1280, 720) action ShowMenu('gallery')

screen cassgal2:
    tag menu
    imagemap:
        ground "/cg/cass cg 2.png"
        hover "/cg/cass cg 2.png"
        yalign 0.0

        hotspot (0, 0, 1280, 720) action ShowMenu('gallery')
