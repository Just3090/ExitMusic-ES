define persistent.demo = False
define persistent.steam = False
define config.developer = False

python early:
    import singleton
    me = singleton.SingleInstance()

init python:

    config.keymap['hide_windows'].append('mouseup_3')
    config.keymap['self_voicing'] = []
    config.keymap['clipboard_voicing'] = []
    config.keymap['toggle_skip'] = []
    renpy.music.register_channel("background", "sfx", True)
    renpy.music.register_channel("music_poem", mixer="music", tight=True)
    def get_pos(channel='music'):
        pos = renpy.music.get_pos(channel=channel)
        if pos: return pos
        return 0
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)
    def delete_character(name):
        import os
        try: os.remove(config.basedir + "/characters/" + name + ".chr")
        except: pass
    def restore_all_characters():
        try: renpy.file("../characters/monika.chr")
        except: open(config.basedir + "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
        try: renpy.file("../characters/natsuki.chr")
        except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
        try: renpy.file("../characters/yuri.chr")
        except: open(config.basedir + "/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())
        try: renpy.file("../characters/sayori.chr")
        except: open(config.basedir + "/characters/sayori.chr", "wb").write(renpy.file("sayori.chr").read())
    def pause(time=None):
        if not time:
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
            return
        if time <= 0: return
        renpy.pause(time)


define audio.t1 = "<loop 22.073>bgm/1.ogg"
define audio.t2 = "<loop 4.499>bgm/2.ogg"
define audio.t2g = "bgm/2g.ogg"
define audio.t2g2 = "<from 4.499 loop 4.499>bgm/2.ogg"
define audio.t2g3 = "<loop 4.492>bgm/2g2.ogg"
define audio.t3 = "<loop 4.618>bgm/3.ogg"
define audio.t3g = "<to 15.255>bgm/3g.ogg"
define audio.t3g2 = "<from 15.255 loop 4.618>bgm/3.ogg"
define audio.t3g3 = "<loop 4.618>bgm/3g2.ogg"
define audio.t3m = "<loop 4.618>bgm/3.ogg"
define audio.t4 = "<loop 19.451>bgm/4.ogg"
define audio.t4g = "<loop 1.000>bgm/4g.ogg"
define audio.t5 = "<loop 4.444>bgm/5.ogg"
define audio.t5b = "<loop 4.444>bgm/5.ogg"
define audio.t5c = "<loop 4.444>bgm/5.ogg"
define audio.t6 = "<loop 10.893>bgm/6.ogg"
define audio.t6g = "<loop 10.893>bgm/6g.ogg"
define audio.t6r = "<to 39.817 loop 0>bgm/6r.ogg"
define audio.t6s = "<loop 43.572>bgm/6s.ogg"
define audio.t7 = "<loop 2.291>bgm/7.ogg"
define audio.t7a = "<loop 4.316 to 12.453>bgm/7.ogg"
define audio.t7g = "<loop 31.880>bgm/7g.ogg"
define audio.t8 = "<loop 9.938>bgm/8.ogg"
define audio.t9 = "<loop 3.172>bgm/9.ogg"
define audio.t9g = "<loop 1.532>bgm/9g.ogg"
define audio.t10 = "<loop 5.861>bgm/10.ogg"
define audio.t10y = "<loop 0>bgm/10-yuri.ogg"
define audio.td = "<loop 36.782>bgm/d.ogg"



define audio.yawa = "<loop 109.729>mod_assets/audio/yawa.ogg" ##########
define audio.daydreaming = "<loop 105.813>mod_assets/audio/daydreaming.ogg" #########
define audio.decksdark = "<loop 6.910>mod_assets/audio/decksdark.ogg" ##########
define audio.fulstop = "<loop 254.773>mod_assets/audio/fulstop.ogg" ############
define audio.tinkertailor = "<loop 92.645>mod_assets/audio/ttssrmpmbmt.ogg" ##########
define audio.mps = "<loop 39.184>mod_assets/audio/mps.ogg" ##########
define audio.presenttense = "<loop 180.981>mod_assets/audio/presenttense.ogg" ###########
define audio.thenumbers = "<loop 48.882>mod_assets/audio/thenumbers.ogg" #############
define audio.tlw = "<loop 23.423>mod_assets/audio/tlw.ogg" ###############
define audio.tlwamsp = "<loop 7.059>mod_assets/audio/tlwamsp.ogg" ###############
define audio.glasseyes = "<loop 4.777>mod_assets/audio/glasseyes.ogg" ################
define audio.illwind = "<loop 98.863>mod_assets/audio/illwind.ogg" ##############
define audio.climbingup = "<loop 12.713>mod_assets/audio/climbingup.ogg" ##############
define audio.giveup = "<loop 37.637>mod_assets/audio/giveup.ogg" ##############

define audio.natsuki = "<loop 0.000>mod_assets/audio/natsuki.ogg"

define audio.m1 = "<loop 0>bgm/m1.ogg"
define audio.mend = "<loop 6.424>bgm/monika-end.ogg"

define audio.ghostmenu = "<loop 0>bgm/ghostmenu.ogg"
define audio.g1 = "<loop 0>bgm/g1.ogg"
define audio.g2 = "<loop 0>bgm/g2.ogg"
define audio.hb = "<loop 0>bgm/heartbeat.ogg"

define audio.closet_open = "sfx/closet-open.ogg"
define audio.closet_close = "sfx/closet-close.ogg"
define audio.page_turn = "sfx/pageflip.ogg"
define audio.fall = "sfx/fall.ogg"
define audio.smack = "sfx/smack.ogg"

image black = "#000000"
image dark = "#000000e4"
image darkred = "#110000c8"
image memory = "mod_assets/bg/memory.png"
image memory2 = "mod_assets/bg/memory2.png"
image white = "#ffffff"
image splash = "bg/splash.png"

image flashcard:
    truecenter
    "gui/flash_card.png"
image thatsall:
    truecenter
    "gui/thatsall.png"
image monday:
    truecenter
    "gui/days/monday.png"
image tuesday:
    truecenter
    "gui/days/tuesday.png"
image wednesday:
    truecenter
    "gui/days/wednesday.png"
image thursday:
    truecenter
    "gui/days/thursday.png"
image friday:
    truecenter
    "gui/days/friday.png"
image saturday:
    truecenter
    "gui/days/saturday.png"
image sunday:
    truecenter
    "gui/days/sunday.png"

image end:
    truecenter
    "gui/end.png"

image bg residential_day = "bg/residential.png"
image bg class_day = "bg/class.png"
image bg corridor = "bg/corridor.png"
image bg club_day = "bg/club.png"
image bg club_day2 = "bg club_day"
image bg closet = "bg/closet.png"
image bg bedroom = "bg/bedroom.png"
image bg sayori_bedroom = "bg/sayori_bedroom.png"
image bg house = "bg/house.png"
image bg kitchen = "bg/kitchen.png"




image bg housen = "mod_assets/bg/housen.png"


image bg bedrooms = "mod_assets/bg/bedrooms.png"
image bg bedroomn = "mod_assets/bg/bedroomn.png"



image bg hospital = "mod_assets/bg/hospital.png"
image bg nurse = "mod_assets/bg/nurse.png"
image bg nursen = "mod_assets/bg/nursen.png"



image bg nhome = "mod_assets/bg/nhome.png"
image bg nhomen = "mod_assets/bg/nhomen.png"



image bg nbedroom = "mod_assets/bg/nroom.png"
image bg nbedroomn = "mod_assets/bg/nroomn.png"



image bg street = "mod_assets/bg/street.png"
image bg streetrain = "mod_assets/bg/streetrain.png"
image bg streetn = "mod_assets/bg/streetn.png"



image bg hallway = "mod_assets/bg/hallway.png"
image bg hallwayn = "mod_assets/bg/hallwayn.png"



image bg mclivingroom = "mod_assets/bg/mclivingroom.png"
image bg mclivingroomn = "mod_assets/bg/mclivingroomn.png"



image bg spareroom = "mod_assets/bg/spareroom.png"
image bg spareroomn = "mod_assets/bg/spareroomn.png"



image bg bathroom = "mod_assets/bg/bathroom.png"



image bg courtyard = "mod_assets/bg/courtyard.png"



image bg windowsill = "mod_assets/bg/windowsill.png"



image bg courtyardrain = "mod_assets/bg/courtyard_rain.png"
image bg clubrain = "mod_assets/bg/club_rain.png"
image bg houserain = "mod_assets/bg/house_rain.png"
image bg residentialrain = "mod_assets/bg/residential_rain.png"
image bg corridorrain = "mod_assets/bg/corridor_rain.png"
image bg closetrain = "mod_assets/bg/closet_rain.png"



image bg residentialsnow = "mod_assets/bg/residentialsnow.png"
image bg residentialsnown = "mod_assets/bg/residentialsnown.png"
image bg housesnow = "mod_assets/bg/housesnow.png"



image bg clothingstore = "mod_assets/bg/clothingstore.png"



image bg cafe = "mod_assets/bg/cafe.png"



image bg memory = "mod_assets/bg/memory.png"



image bg bridge = "mod_assets/bg/bridge.png"
image bg sky = "mod_assets/bg/sky.png"



image bg creditnote = "mod_assets/bg/creditnote.png"



image bg notebook = "bg/notebook.png"
image bg notebook-glitch = "bg/notebook-glitch.png"

image bg glitch = LiveTile("bg/glitch.jpg")

image blackscene = im.Composite((1280, 720), (0, 0), "mod_assets/black.png")

image glitch_color:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.7
        linear 0.45 alpha 0


image glitch_color2:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.7
        linear 0.45 alpha 0



image mc 1a = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/a.png")
image mc 1b = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/b.png")
image mc 1c = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/c.png")
image mc 1d = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/d.png")
image mc 1e = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/e.png")
image mc 1f = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/f.png")
image mc 1g = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/g.png")
image mc 1h = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/h.png")
image mc 1i = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/i.png")
image mc 1j = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/j.png")
image mc 1k = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/k.png")
image mc 1l = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/l.png")
image mc 1m = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/m.png")
image mc 1n = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/n.png")
image mc 1o = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/o.png")
image mc 1p = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/p.png")
image mc 1q = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/q.png")
image mc 1r = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/r.png")
image mc 1s = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/s.png")
image mc 1t = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/t.png")
image mc 1u = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/u.png")
image mc 1v = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/v.png")
image mc 1w = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/w.png")
image mc 1x = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/x.png")
image mc 1y = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/y.png")
image mc 1z = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/z.png")

image mc 2a = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/a.png")
image mc 2b = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/b.png")
image mc 2c = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/c.png")
image mc 2d = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/d.png")
image mc 2e = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/e.png")
image mc 2f = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/f.png")
image mc 2g = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/g.png")
image mc 2h = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/h.png")
image mc 2i = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/i.png")
image mc 2j = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/j.png")
image mc 2k = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/k.png")
image mc 2l = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/l.png")
image mc 2m = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/m.png")
image mc 2n = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/n.png")
image mc 2o = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/o.png")
image mc 2p = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/p.png")
image mc 2q = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/q.png")
image mc 2r = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/r.png")
image mc 2s = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/s.png")
image mc 2t = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/t.png")
image mc 2u = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/u.png")
image mc 2v = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/v.png")
image mc 2w = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/w.png")
image mc 2x = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/x.png")
image mc 2y = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/y.png")
image mc 2z = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/z.png")

image mc 3a = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/a.png")
image mc 3b = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/b.png")
image mc 3c = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/c.png")
image mc 3d = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/d.png")
image mc 3e = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/e.png")
image mc 3f = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/f.png")
image mc 3g = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/g.png")
image mc 3h = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/h.png")
image mc 3i = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/i.png")
image mc 3j = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/j.png")
image mc 3k = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/k.png")
image mc 3l = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/l.png")
image mc 3m = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/m.png")
image mc 3n = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/n.png")
image mc 3o = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/o.png")
image mc 3p = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/p.png")
image mc 3q = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/q.png")
image mc 3r = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/r.png")
image mc 3s = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/s.png")
image mc 3t = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/t.png")
image mc 3u = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/u.png")
image mc 3v = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/v.png")
image mc 3w = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/w.png")
image mc 3x = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/x.png")
image mc 3y = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/y.png")
image mc 3z = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/z.png")

image mc 4a = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/a.png")
image mc 4b = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/b.png")
image mc 4c = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/c.png")
image mc 4d = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/d.png")
image mc 4e = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/e.png")
image mc 4f = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/f.png")
image mc 4g = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/g.png")
image mc 4h = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/h.png")
image mc 4i = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/i.png")
image mc 4j = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/j.png")
image mc 4k = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/k.png")
image mc 4l = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/l.png")
image mc 4m = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/m.png")
image mc 4n = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/n.png")
image mc 4o = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/o.png")
image mc 4p = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/p.png")
image mc 4q = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/q.png")
image mc 4r = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/r.png")
image mc 4s = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/s.png")
image mc 4t = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/t.png")
image mc 4u = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/u.png")
image mc 4v = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/v.png")
image mc 4w = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/w.png")
image mc 4x = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/x.png")
image mc 4y = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/y.png")
image mc 4z = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/z.png")



image sayori 1 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1b = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 1c = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 1d = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 1e = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 1f = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 1g = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 1h = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 1i = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 1j = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 1k = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 1l = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 1m = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 1n = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 1o = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 1p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 1q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 1r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 1s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 1t = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 1u = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 1v = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 1w = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 1x = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 1y = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png")

image sayori 2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 2a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 2b = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 2c = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 2d = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 2e = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 2f = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 2g = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 2h = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 2i = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 2j = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 2k = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 2l = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 2m = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 2n = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 2o = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 2p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 2q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 2r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 2s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 2t = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 2u = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 2v = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 2w = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 2x = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 2y = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png")

image sayori 3 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 3a = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 3b = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 3c = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 3d = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 3e = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 3f = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 3g = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 3h = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 3i = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 3j = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 3k = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 3l = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 3m = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 3n = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 3o = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 3p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 3q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 3r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 3s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 3t = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 3u = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 3v = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 3w = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 3x = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 3y = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png")

image sayori 4 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 4a = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 4b = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 4c = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 4d = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 4e = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 4f = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 4g = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 4h = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 4i = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 4j = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 4k = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 4l = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 4m = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 4n = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 4o = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 4p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 4q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 4r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 4s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 4t = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 4u = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 4v = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 4w = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 4x = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 4y = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png")

image sayori 5 = im.Composite((960, 960), (0, 0), "sayori/3a.png")
image sayori 5a = im.Composite((960, 960), (0, 0), "sayori/3a.png")
image sayori 5b = im.Composite((960, 960), (0, 0), "sayori/3b.png")
image sayori 5c = im.Composite((960, 960), (0, 0), "sayori/3c.png")
image sayori 5d = im.Composite((960, 960), (0, 0), "sayori/3d.png")

image sayori 1ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 1bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 1bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 1bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 1be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 1bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 1bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 1bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 1bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 1bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 1bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 1bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 1bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 1bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 1bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 1bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 1bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 1br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 1bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 1bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 1bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 1bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 1bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 1bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 1by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 2ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 2bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 2bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 2bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 2be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 2bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 2bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 2bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 2bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 2bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 2bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 2bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 2bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 2bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 2bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 2bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 2bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 2br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 2bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 2bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 2bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 2bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 2bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 2bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 2by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

image sayori 3ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 3bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 3bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 3bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 3be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 3bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 3bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 3bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 3bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 3bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 3bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 3bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 3bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 3bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 3bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 3bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 3bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 3br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 3bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 3bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 3bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 3bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 3bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 3bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 3by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 4ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 4bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 4bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 4bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 4be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 4bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 4bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 4bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 4bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 4bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 4bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 4bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 4bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 4bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 4bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 4bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 4bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 4br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 4bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 4bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 4bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 4bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 4bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 4bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 4by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")



image sayori 1ca = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/a.png")
image sayori 1cb = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/b.png")
image sayori 1cc = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/c.png")
image sayori 1cd = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/d.png")
image sayori 1ce = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/e.png")
image sayori 1cf = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/f.png")
image sayori 1cg = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/g.png")
image sayori 1ch = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/h.png")
image sayori 1ci = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/i.png")
image sayori 1cj = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/j.png")
image sayori 1ck = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/k.png")
image sayori 1cl = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/l.png")
image sayori 1cm = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/m.png")
image sayori 1cn = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/n.png")
image sayori 1co = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/o.png")
image sayori 1cp = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/p.png")
image sayori 1cq = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/q.png")
image sayori 1cr = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/r.png")
image sayori 1cs = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/s.png")
image sayori 1ct = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/t.png")
image sayori 1cu = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/u.png")
image sayori 1cv = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/v.png")
image sayori 1cw = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/w.png")
image sayori 1cx = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/x.png")
image sayori 1cy = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/y.png")

image sayori 2ca = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/a.png")
image sayori 2cb = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/b.png")
image sayori 2cc = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/c.png")
image sayori 2cd = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/d.png")
image sayori 2ce = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/e.png")
image sayori 2cf = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/f.png")
image sayori 2cg = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/g.png")
image sayori 2ch = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/h.png")
image sayori 2ci = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/i.png")
image sayori 2cj = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/j.png")
image sayori 2ck = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/k.png")
image sayori 2cl = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/l.png")
image sayori 2cm = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/m.png")
image sayori 2cn = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/n.png")
image sayori 2co = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/o.png")
image sayori 2cp = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/p.png")
image sayori 2cq = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/q.png")
image sayori 2cr = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/r.png")
image sayori 2cs = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/s.png")
image sayori 2ct = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/t.png")
image sayori 2cu = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/u.png")
image sayori 2cv = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/v.png")
image sayori 2cw = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/w.png")
image sayori 2cx = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/x.png")
image sayori 2cy = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/1l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/y.png")

image sayori 3ca = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/a.png")
image sayori 3cb = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/b.png")
image sayori 3cc = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/c.png")
image sayori 3cd = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/d.png")
image sayori 3ce = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/e.png")
image sayori 3cf = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/f.png")
image sayori 3cg = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/g.png")
image sayori 3ch = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/h.png")
image sayori 3ci = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/i.png")
image sayori 3cj = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/j.png")
image sayori 3ck = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/k.png")
image sayori 3cl = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/l.png")
image sayori 3cm = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/m.png")
image sayori 3cn = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/n.png")
image sayori 3co = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/o.png")
image sayori 3cp = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/p.png")
image sayori 3cq = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/q.png")
image sayori 3cr = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/r.png")
image sayori 3cs = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/s.png")
image sayori 3ct = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/t.png")
image sayori 3cu = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/u.png")
image sayori 3cv = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/v.png")
image sayori 3cw = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/w.png")
image sayori 3cx = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/x.png")
image sayori 3cy = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/1r.png", (0, 0), "sayori/y.png")

image sayori 4ca = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/a.png")
image sayori 4cb = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/b.png")
image sayori 4cc = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/c.png")
image sayori 4cd = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/d.png")
image sayori 4ce = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/e.png")
image sayori 4cf = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/f.png")
image sayori 4cg = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/g.png")
image sayori 4ch = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/h.png")
image sayori 4ci = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/i.png")
image sayori 4cj = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/j.png")
image sayori 4ck = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/k.png")
image sayori 4cl = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/l.png")
image sayori 4cm = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/m.png")
image sayori 4cn = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/n.png")
image sayori 4co = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/o.png")
image sayori 4cp = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/p.png")
image sayori 4cq = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/q.png")
image sayori 4cr = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/r.png")
image sayori 4cs = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/s.png")
image sayori 4ct = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/t.png")
image sayori 4cu = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/u.png")
image sayori 4cv = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/v.png")
image sayori 4cw = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/w.png")
image sayori 4cx = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/x.png")
image sayori 4cy = im.Composite((960, 960), (0, 0), "mod_assets/sayori/pyjama/2l.png", (0, 0), "mod_assets/sayori/pyjama/2r.png", (0, 0), "sayori/y.png")



image sayori 1da = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/a.png")
image sayori 1db = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/b.png")
image sayori 1dc = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/c.png")
image sayori 1dd = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/d.png")
image sayori 1de = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/e.png")
image sayori 1df = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/f.png")
image sayori 1dg = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/g.png")
image sayori 1dh = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/h.png")
image sayori 1di = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/i.png")
image sayori 1dj = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/j.png")
image sayori 1dk = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/k.png")
image sayori 1dl = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/l.png")
image sayori 1dm = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/m.png")
image sayori 1dn = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/n.png")
image sayori 1do = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/o.png")
image sayori 1dp = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/p.png")
image sayori 1dq = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/q.png")
image sayori 1dr = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/r.png")
image sayori 1ds = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/s.png")
image sayori 1dt = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/t.png")
image sayori 1du = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/u.png")
image sayori 1dv = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/v.png")
image sayori 1dw = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/w.png")
image sayori 1dx = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/x.png")
image sayori 1dy = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/y.png")

image sayori 2da = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/a.png")
image sayori 2db = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/b.png")
image sayori 2dc = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/c.png")
image sayori 2dd = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/d.png")
image sayori 2de = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/e.png")
image sayori 2df = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/f.png")
image sayori 2dg = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/g.png")
image sayori 2dh = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/h.png")
image sayori 2di = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/i.png")
image sayori 2dj = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/j.png")
image sayori 2dk = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/k.png")
image sayori 2dl = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/l.png")
image sayori 2dm = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/m.png")
image sayori 2dn = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/n.png")
image sayori 2do = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/o.png")
image sayori 2dp = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/p.png")
image sayori 2dq = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/q.png")
image sayori 2dr = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/r.png")
image sayori 2ds = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/s.png")
image sayori 2dt = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/t.png")
image sayori 2du = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/u.png")
image sayori 2dv = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/v.png")
image sayori 2dw = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/w.png")
image sayori 2dx = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/x.png")
image sayori 2dy = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/1l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/y.png")

image sayori 3da = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/a.png")
image sayori 3db = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/b.png")
image sayori 3dc = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/c.png")
image sayori 3dd = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/d.png")
image sayori 3de = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/e.png")
image sayori 3df = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/f.png")
image sayori 3dg = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/g.png")
image sayori 3dh = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/h.png")
image sayori 3di = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/i.png")
image sayori 3dj = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/j.png")
image sayori 3dk = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/k.png")
image sayori 3dl = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/l.png")
image sayori 3dm = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/m.png")
image sayori 3dn = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/n.png")
image sayori 3do = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/o.png")
image sayori 3dp = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/p.png")
image sayori 3dq = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/q.png")
image sayori 3dr = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/r.png")
image sayori 3ds = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/s.png")
image sayori 3dt = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/t.png")
image sayori 3du = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/u.png")
image sayori 3dv = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/v.png")
image sayori 3dw = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/w.png")
image sayori 3dx = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/x.png")
image sayori 3dy = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/1r.png", (0, 0), "sayori/y.png")

image sayori 4da = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/a.png")
image sayori 4db = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/b.png")
image sayori 4dc = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/c.png")
image sayori 4dd = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/d.png")
image sayori 4de = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/e.png")
image sayori 4df = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/f.png")
image sayori 4dg = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/g.png")
image sayori 4dh = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/h.png")
image sayori 4di = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/i.png")
image sayori 4dj = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/j.png")
image sayori 4dk = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/k.png")
image sayori 4dl = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/l.png")
image sayori 4dm = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/m.png")
image sayori 4dn = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/n.png")
image sayori 4do = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/o.png")
image sayori 4dp = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/p.png")
image sayori 4dq = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/q.png")
image sayori 4dr = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/r.png")
image sayori 4ds = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/s.png")
image sayori 4dt = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/t.png")
image sayori 4du = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/u.png")
image sayori 4dv = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/v.png")
image sayori 4dw = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/w.png")
image sayori 4dx = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/x.png")
image sayori 4dy = im.Composite((960, 960), (0, 0), "mod_assets/sayori/funeral/2l.png", (0, 0), "mod_assets/sayori/funeral/2r.png", (0, 0), "sayori/y.png")

image sayori glitch:
    "sayori/glitch1.png"
    pause 0.01666
    "sayori/glitch2.png"
    pause 0.01666
    repeat


image natsuki 1 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 1a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/a.png")
image natsuki 1b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/b.png")
image natsuki 1c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/c.png")
image natsuki 1cry = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/natsuki/cry.png")
image natsuki 1d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/d.png")
image natsuki 1d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/e.png")
image natsuki 1e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/f.png")
image natsuki 1f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/g.png")
image natsuki 1h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/h.png")
image natsuki 1i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/i.png")
image natsuki 1j = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/j.png")
image natsuki 1k = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/k.png")
image natsuki 1l = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/l.png")
image natsuki 1m = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/m.png")
image natsuki 1n = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/n.png")
image natsuki 1o = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/o.png")
image natsuki 1p = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/p.png")
image natsuki 1q = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/q.png")
image natsuki 1r = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/r.png")
image natsuki 1s = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/s.png")
image natsuki 1t = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/t.png")
image natsuki 1u = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/u.png")
image natsuki 1v = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png")
image natsuki 1w = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png")
image natsuki 1x = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png")
image natsuki 1y = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png")
image natsuki 1z = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png")

image natsuki 2 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 2a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/a.png")
image natsuki 2b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/b.png")
image natsuki 2c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/c.png")
image natsuki 2cry = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/natsuki/cry.png")
image natsuki 2d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/d.png")
image natsuki 2d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/e.png")
image natsuki 2e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/f.png")
image natsuki 2f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/g.png")
image natsuki 2h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/h.png")
image natsuki 2i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/i.png")
image natsuki 2j = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/j.png")
image natsuki 2k = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/k.png")
image natsuki 2l = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/l.png")
image natsuki 2m = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/m.png")
image natsuki 2n = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/n.png")
image natsuki 2o = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/o.png")
image natsuki 2p = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/p.png")
image natsuki 2q = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/q.png")
image natsuki 2r = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/r.png")
image natsuki 2s = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/s.png")
image natsuki 2t = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/t.png")
image natsuki 2u = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/u.png")
image natsuki 2v = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png")
image natsuki 2w = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png")
image natsuki 2x = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png")
image natsuki 2y = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png")
image natsuki 2z = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png")

image natsuki 3 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 3a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/a.png")
image natsuki 3b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/b.png")
image natsuki 3c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/c.png")
image natsuki 3cry = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/natsuki/cry.png")
image natsuki 3d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/d.png")
image natsuki 3d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/e.png")
image natsuki 3e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/f.png")
image natsuki 3f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/g.png")
image natsuki 3h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/h.png")
image natsuki 3i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/i.png")
image natsuki 3j = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/j.png")
image natsuki 3k = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/k.png")
image natsuki 3l = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/l.png")
image natsuki 3m = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/m.png")
image natsuki 3n = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/n.png")
image natsuki 3o = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/o.png")
image natsuki 3p = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/p.png")
image natsuki 3q = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/q.png")
image natsuki 3r = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/r.png")
image natsuki 3s = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/s.png")
image natsuki 3t = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/t.png")
image natsuki 3u = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/u.png")
image natsuki 3v = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png")
image natsuki 3w = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png")
image natsuki 3x = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png")
image natsuki 3y = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png")
image natsuki 3z = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png")

image natsuki 4 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 4a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/a.png")
image natsuki 4b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/b.png")
image natsuki 4c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/c.png")
image natsuki 4cry = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/natsuki/cry.png")
image natsuki 4d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/d.png")
image natsuki 4d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/e.png")
image natsuki 4e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/f.png")
image natsuki 4f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/g.png")
image natsuki 4h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/h.png")
image natsuki 4i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/i.png")
image natsuki 4j = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/j.png")
image natsuki 4k = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/k.png")
image natsuki 4l = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/l.png")
image natsuki 4m = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/m.png")
image natsuki 4n = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/n.png")
image natsuki 4o = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/o.png")
image natsuki 4p = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/p.png")
image natsuki 4q = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/q.png")
image natsuki 4r = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/r.png")
image natsuki 4s = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/s.png")
image natsuki 4t = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/t.png")
image natsuki 4u = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/u.png")
image natsuki 4v = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png")
image natsuki 4w = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png")
image natsuki 4x = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png")
image natsuki 4y = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png")
image natsuki 4z = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png")

image natsuki 12 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2t.png")
image natsuki 12a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2ta.png")
image natsuki 12b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tb.png")
image natsuki 12c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tc.png")
image natsuki 12d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2td.png")
image natsuki 12e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2te.png")
image natsuki 12f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tf.png")
image natsuki 12g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tg.png")
image natsuki 12h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2th.png")
image natsuki 12i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2ti.png")

image natsuki 42 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2t.png")
image natsuki 42a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2ta.png")
image natsuki 42b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tb.png")
image natsuki 42c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tc.png")
image natsuki 42d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2td.png")
image natsuki 42e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2te.png")
image natsuki 42f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tf.png")
image natsuki 42g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tg.png")
image natsuki 42h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2th.png")
image natsuki 42i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2ti.png")

image natsuki 51 = im.Composite((960, 960), (18, 22), "natsuki/1t.png", (0, 0), "natsuki/3.png")
image natsuki 5a = im.Composite((960, 960), (18, 22), "natsuki/a.png", (0, 0), "natsuki/3.png")
image natsuki 5b = im.Composite((960, 960), (18, 22), "natsuki/b.png", (0, 0), "natsuki/3.png")
image natsuki 5c = im.Composite((960, 960), (18, 22), "natsuki/c.png", (0, 0), "natsuki/3.png")
image natsuki 5d = im.Composite((960, 960), (18, 22), "natsuki/d.png", (0, 0), "natsuki/3.png")
image natsuki 5e = im.Composite((960, 960), (18, 22), "natsuki/e.png", (0, 0), "natsuki/3.png")
image natsuki 5f = im.Composite((960, 960), (18, 22), "natsuki/f.png", (0, 0), "natsuki/3.png")
image natsuki 5g = im.Composite((960, 960), (18, 22), "natsuki/g.png", (0, 0), "natsuki/3.png")
image natsuki 5h = im.Composite((960, 960), (18, 22), "natsuki/h.png", (0, 0), "natsuki/3.png")
image natsuki 5i = im.Composite((960, 960), (18, 22), "natsuki/i.png", (0, 0), "natsuki/3.png")
image natsuki 5j = im.Composite((960, 960), (18, 22), "natsuki/j.png", (0, 0), "natsuki/3.png")
image natsuki 5k = im.Composite((960, 960), (18, 22), "natsuki/k.png", (0, 0), "natsuki/3.png")
image natsuki 5l = im.Composite((960, 960), (18, 22), "natsuki/l.png", (0, 0), "natsuki/3.png")
image natsuki 5m = im.Composite((960, 960), (18, 22), "natsuki/m.png", (0, 0), "natsuki/3.png")
image natsuki 5n = im.Composite((960, 960), (18, 22), "natsuki/n.png", (0, 0), "natsuki/3.png")
image natsuki 5o = im.Composite((960, 960), (18, 22), "natsuki/o.png", (0, 0), "natsuki/3.png")
image natsuki 5p = im.Composite((960, 960), (18, 22), "natsuki/p.png", (0, 0), "natsuki/3.png")
image natsuki 5q = im.Composite((960, 960), (18, 22), "natsuki/q.png", (0, 0), "natsuki/3.png")
image natsuki 5r = im.Composite((960, 960), (18, 22), "natsuki/r.png", (0, 0), "natsuki/3.png")
image natsuki 5s = im.Composite((960, 960), (18, 22), "natsuki/s.png", (0, 0), "natsuki/3.png")
image natsuki 5t = im.Composite((960, 960), (18, 22), "natsuki/t.png", (0, 0), "natsuki/3.png")
image natsuki 5u = im.Composite((960, 960), (18, 22), "natsuki/u.png", (0, 0), "natsuki/3.png")
image natsuki 5v = im.Composite((960, 960), (18, 22), "natsuki/v.png", (0, 0), "natsuki/3.png")
image natsuki 5w = im.Composite((960, 960), (18, 22), "natsuki/w.png", (0, 0), "natsuki/3.png")
image natsuki 5x = im.Composite((960, 960), (18, 22), "natsuki/x.png", (0, 0), "natsuki/3.png")
image natsuki 5y = im.Composite((960, 960), (18, 22), "natsuki/y.png", (0, 0), "natsuki/3.png")
image natsuki 5z = im.Composite((960, 960), (18, 22), "natsuki/z.png", (0, 0), "natsuki/3.png")

image natsuki 12ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bta.png")
image natsuki 12bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btb.png")
image natsuki 12bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btc.png")
image natsuki 12bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btd.png")
image natsuki 12be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bte.png")
image natsuki 12bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btf.png")
image natsuki 12bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btg.png")
image natsuki 12bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bth.png")
image natsuki 12bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bti.png")

image natsuki 42ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bta.png")
image natsuki 42bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btb.png")
image natsuki 42bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btc.png")
image natsuki 42bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btd.png")
image natsuki 42be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bte.png")
image natsuki 42bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btf.png")
image natsuki 42bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btg.png")
image natsuki 42bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bth.png")
image natsuki 42bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bti.png")

image natsuki 5ba = im.Composite((960, 960), (18, 22), "natsuki/a.png", (0, 0), "natsuki/3b.png")
image natsuki 5bb = im.Composite((960, 960), (18, 22), "natsuki/b.png", (0, 0), "natsuki/3b.png")
image natsuki 5bc = im.Composite((960, 960), (18, 22), "natsuki/c.png", (0, 0), "natsuki/3b.png")
image natsuki 5bd = im.Composite((960, 960), (18, 22), "natsuki/d.png", (0, 0), "natsuki/3b.png")
image natsuki 5be = im.Composite((960, 960), (18, 22), "natsuki/e.png", (0, 0), "natsuki/3b.png")
image natsuki 5bf = im.Composite((960, 960), (18, 22), "natsuki/f.png", (0, 0), "natsuki/3b.png")
image natsuki 5bg = im.Composite((960, 960), (18, 22), "natsuki/g.png", (0, 0), "natsuki/3b.png")
image natsuki 5bh = im.Composite((960, 960), (18, 22), "natsuki/h.png", (0, 0), "natsuki/3b.png")
image natsuki 5bi = im.Composite((960, 960), (18, 22), "natsuki/i.png", (0, 0), "natsuki/3b.png")
image natsuki 5bj = im.Composite((960, 960), (18, 22), "natsuki/j.png", (0, 0), "natsuki/3b.png")
image natsuki 5bk = im.Composite((960, 960), (18, 22), "natsuki/k.png", (0, 0), "natsuki/3b.png")
image natsuki 5bl = im.Composite((960, 960), (18, 22), "natsuki/l.png", (0, 0), "natsuki/3b.png")
image natsuki 5bm = im.Composite((960, 960), (18, 22), "natsuki/m.png", (0, 0), "natsuki/3b.png")
image natsuki 5bn = im.Composite((960, 960), (18, 22), "natsuki/n.png", (0, 0), "natsuki/3b.png")
image natsuki 5bo = im.Composite((960, 960), (18, 22), "natsuki/o.png", (0, 0), "natsuki/3b.png")
image natsuki 5bp = im.Composite((960, 960), (18, 22), "natsuki/p.png", (0, 0), "natsuki/3b.png")
image natsuki 5bq = im.Composite((960, 960), (18, 22), "natsuki/q.png", (0, 0), "natsuki/3b.png")
image natsuki 5br = im.Composite((960, 960), (18, 22), "natsuki/r.png", (0, 0), "natsuki/3b.png")
image natsuki 5bs = im.Composite((960, 960), (18, 22), "natsuki/s.png", (0, 0), "natsuki/3b.png")
image natsuki 5bt = im.Composite((960, 960), (18, 22), "natsuki/t.png", (0, 0), "natsuki/3b.png")
image natsuki 5bu = im.Composite((960, 960), (18, 22), "natsuki/u.png", (0, 0), "natsuki/3b.png")
image natsuki 5bv = im.Composite((960, 960), (18, 22), "natsuki/v.png", (0, 0), "natsuki/3b.png")
image natsuki 5bw = im.Composite((960, 960), (18, 22), "natsuki/w.png", (0, 0), "natsuki/3b.png")
image natsuki 5bx = im.Composite((960, 960), (18, 22), "natsuki/x.png", (0, 0), "natsuki/3b.png")
image natsuki 5by = im.Composite((960, 960), (18, 22), "natsuki/y.png", (0, 0), "natsuki/3b.png")
image natsuki 5bz = im.Composite((960, 960), (18, 22), "natsuki/z.png", (0, 0), "natsuki/3b.png")

image natsuki 1ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/a.png")
image natsuki 1bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/b.png")
image natsuki 1bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/c.png")
image natsuki 1bcry = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/cry.png")
image natsuki 1bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/d.png")
image natsuki 1be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/e.png")
image natsuki 1bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/f.png")
image natsuki 1bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/g.png")
image natsuki 1bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/h.png")
image natsuki 1bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/i.png")
image natsuki 1bj = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/j.png")
image natsuki 1bk = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/k.png")
image natsuki 1bl = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/l.png")
image natsuki 1bm = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/m.png")
image natsuki 1bn = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/n.png")
image natsuki 1bo = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/o.png")
image natsuki 1bp = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/p.png")
image natsuki 1bq = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/q.png")
image natsuki 1br = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/r.png")
image natsuki 1bs = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/s.png")
image natsuki 1bt = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/t.png")
image natsuki 1bu = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/u.png")
image natsuki 1bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png")
image natsuki 1bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png")
image natsuki 1bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png")
image natsuki 1by = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png")
image natsuki 1bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png")

image natsuki 2ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/a.png")
image natsuki 2bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/b.png")
image natsuki 2bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/c.png")
image natsuki 2bcry = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/natsuki/cry.png")
image natsuki 2bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/d.png")
image natsuki 2be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/e.png")
image natsuki 2bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/f.png")
image natsuki 2bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/g.png")
image natsuki 2bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/h.png")
image natsuki 2bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/i.png")
image natsuki 2bj = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/j.png")
image natsuki 2bk = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/k.png")
image natsuki 2bl = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/l.png")
image natsuki 2bm = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/m.png")
image natsuki 2bn = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/n.png")
image natsuki 2bo = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/o.png")
image natsuki 2bp = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/p.png")
image natsuki 2bq = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/q.png")
image natsuki 2br = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/r.png")
image natsuki 2bs = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/s.png")
image natsuki 2bt = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/t.png")
image natsuki 2bu = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/u.png")
image natsuki 2bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png")
image natsuki 2bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png")
image natsuki 2bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png")
image natsuki 2by = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png")
image natsuki 2bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png")

image natsuki 3ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/a.png")
image natsuki 3bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/b.png")
image natsuki 3bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/c.png")
image natsuki 3bcry = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/cry.png")
image natsuki 3bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/d.png")
image natsuki 3be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/e.png")
image natsuki 3bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/f.png")
image natsuki 3bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/g.png")
image natsuki 3bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/h.png")
image natsuki 3bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/i.png")
image natsuki 3bj = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/j.png")
image natsuki 3bk = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/k.png")
image natsuki 3bl = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/l.png")
image natsuki 3bm = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/m.png")
image natsuki 3bn = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/n.png")
image natsuki 3bo = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/o.png")
image natsuki 3bp = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/p.png")
image natsuki 3bq = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/q.png")
image natsuki 3br = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/r.png")
image natsuki 3bs = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/s.png")
image natsuki 3bt = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/t.png")
image natsuki 3bu = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/u.png")
image natsuki 3bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png")
image natsuki 3bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png")
image natsuki 3bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png")
image natsuki 3by = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png")
image natsuki 3bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png")

image natsuki 4ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/a.png")
image natsuki 4bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/b.png")
image natsuki 4bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/c.png")
image natsuki 4bcry = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/natsuki/cry.png")
image natsuki 4bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/d.png")
image natsuki 4be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/e.png")
image natsuki 4bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/f.png")
image natsuki 4bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/g.png")
image natsuki 4bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/h.png")
image natsuki 4bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/i.png")
image natsuki 4bj = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/j.png")
image natsuki 4bk = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/k.png")
image natsuki 4bl = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/l.png")
image natsuki 4bm = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/m.png")
image natsuki 4bn = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/n.png")
image natsuki 4bo = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/o.png")
image natsuki 4bp = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/p.png")
image natsuki 4bq = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/q.png")
image natsuki 4br = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/r.png")
image natsuki 4bs = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/s.png")
image natsuki 4bt = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/t.png")
image natsuki 4bu = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/u.png")
image natsuki 4bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png")
image natsuki 4bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png")
image natsuki 4bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png")
image natsuki 4by = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png")
image natsuki 4bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png")

image natsuki 1 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 2 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 3 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 4 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 5 = im.Composite((960, 960), (18, 22), "natsuki/1t.png", (0, 0), "natsuki/3.png")



image natsuki 1ca = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/a.png")
image natsuki 1cb = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/b.png")
image natsuki 1cc = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/c.png")
image natsuki 1ccry = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "mod_assets/natsuki/cry.png")
image natsuki 1cd = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/d.png")
image natsuki 1ce = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/e.png")
image natsuki 1cf = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/f.png")
image natsuki 1cg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/g.png")
image natsuki 1ch = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/h.png")
image natsuki 1ci = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/i.png")
image natsuki 1cj = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/j.png")
image natsuki 1ck = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/k.png")
image natsuki 1cl = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/l.png")
image natsuki 1cm = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/m.png")
image natsuki 1cn = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/n.png")
image natsuki 1co = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/o.png")
image natsuki 1cp = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/p.png")
image natsuki 1cq = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/q.png")
image natsuki 1cr = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/r.png")
image natsuki 1cs = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/s.png")
image natsuki 1ct = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/t.png")
image natsuki 1cu = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/u.png")
image natsuki 1cv = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/v.png")
image natsuki 1cw = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/w.png")
image natsuki 1cx = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/x.png")
image natsuki 1cy = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/y.png")
image natsuki 1cz = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/z.png")

image natsuki 2ca = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/a.png")
image natsuki 2cb = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/b.png")
image natsuki 2cc = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/c.png")
image natsuki 2ccry = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "mod_assets/natsuki/cry.png")
image natsuki 2cd = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/d.png")
image natsuki 2ce = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/e.png")
image natsuki 2cf = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/f.png")
image natsuki 2cg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/g.png")
image natsuki 2ch = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/h.png")
image natsuki 2ci = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/i.png")
image natsuki 2cj = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/j.png")
image natsuki 2ck = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/k.png")
image natsuki 2cl = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/l.png")
image natsuki 2cm = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/m.png")
image natsuki 2cn = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/n.png")
image natsuki 2co = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/o.png")
image natsuki 2cp = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/p.png")
image natsuki 2cq = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/q.png")
image natsuki 2cr = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/r.png")
image natsuki 2cs = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/s.png")
image natsuki 2ct = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/t.png")
image natsuki 2cu = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/u.png")
image natsuki 2cv = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/v.png")
image natsuki 2cw = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/w.png")
image natsuki 2cx = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/x.png")
image natsuki 2cy = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/y.png")
image natsuki 2cz = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/z.png")

image natsuki 3ca = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/a.png")
image natsuki 3cb = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/b.png")
image natsuki 3cc = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/c.png")
image natsuki 3ccry = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "mod_assets/natsuki/cry.png")
image natsuki 3cd = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/d.png")
image natsuki 3ce = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/e.png")
image natsuki 3cf = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/f.png")
image natsuki 3cg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/g.png")
image natsuki 3ch = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/h.png")
image natsuki 3ci = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/i.png")
image natsuki 3cj = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/j.png")
image natsuki 3ck = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/k.png")
image natsuki 3cl = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/l.png")
image natsuki 3cm = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/m.png")
image natsuki 3cn = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/n.png")
image natsuki 3co = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/o.png")
image natsuki 3cp = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/p.png")
image natsuki 3cq = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/q.png")
image natsuki 3cr = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/r.png")
image natsuki 3cs = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/s.png")
image natsuki 3ct = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/t.png")
image natsuki 3cu = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/u.png")
image natsuki 3cv = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/v.png")
image natsuki 3cw = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/w.png")
image natsuki 3cx = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/x.png")
image natsuki 3cy = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/y.png")
image natsuki 3cz = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/z.png")

image natsuki 4ca = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/a.png")
image natsuki 4cb = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/b.png")
image natsuki 4cc = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/c.png")
image natsuki 4ccry = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "mod_assets/natsuki/cry.png")
image natsuki 4cd = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/d.png")
image natsuki 4ce = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/e.png")
image natsuki 4cf = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/f.png")
image natsuki 4cg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/g.png")
image natsuki 4ch = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/h.png")
image natsuki 4ci = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/i.png")
image natsuki 4cj = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/j.png")
image natsuki 4ck = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/k.png")
image natsuki 4cl = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/l.png")
image natsuki 4cm = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/m.png")
image natsuki 4cn = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/n.png")
image natsuki 4co = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/o.png")
image natsuki 4cp = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/p.png")
image natsuki 4cq = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/q.png")
image natsuki 4cr = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/r.png")
image natsuki 4cs = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/s.png")
image natsuki 4ct = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/t.png")
image natsuki 4cu = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/u.png")
image natsuki 4cv = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/v.png")
image natsuki 4cw = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/w.png")
image natsuki 4cx = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/x.png")
image natsuki 4cy = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/y.png")
image natsuki 4cz = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/2l.png", (0, 0), "mod_assets/natsuki/loose/2r.png", (0, 0), "natsuki/z.png")

image natsuki 1cta = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/2bt.png")
image natsuki 1ctb = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/2btb.png")
image natsuki 1ctc = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/2btc.png")
image natsuki 1ctd = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/2btd.png")
image natsuki 1cte = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/2bte.png")
image natsuki 1ctf = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/2btf.png")
image natsuki 1ctg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/2btg.png")
image natsuki 1cth = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/2bth.png")
image natsuki 1cti = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/loose/1l.png", (0, 0), "mod_assets/natsuki/loose/1r.png", (0, 0), "natsuki/2bti.png")



image natsuki 1bba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/bruise/nb1.png")
image natsuki 1bbb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/bruise/nb2.png")
image natsuki 1bbc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/bruise/nb3.png")
image natsuki 1bbd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/bruise/nb4.png")
image natsuki 1bbe = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/bruise/e.png")



image natsuki 1od = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/attempt/2bj.png")
image natsuki 2od = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/natsuki/attempt/2bt.png")
image natsuki vomitb = "mod_assets/natsuki/attempt/vomitb.png"



image natsuki 1da = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/a.png")
image natsuki 1db = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/b.png")
image natsuki 1dc = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/c.png")
image natsuki 1dcry = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "mod_assets/natsuki/cry.png")
image natsuki 1dd = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/d.png")
image natsuki 1de = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/e.png")
image natsuki 1df = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/f.png")
image natsuki 1dg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/g.png")
image natsuki 1dh = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/h.png")
image natsuki 1di = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/i.png")
image natsuki 1dj = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/j.png")
image natsuki 1dk = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/k.png")
image natsuki 1dl = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/l.png")
image natsuki 1dm = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/m.png")
image natsuki 1dn = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/n.png")
image natsuki 1do = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/o.png")
image natsuki 1dp = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/p.png")
image natsuki 1dq = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/q.png")
image natsuki 1dr = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/r.png")
image natsuki 1ds = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/s.png")
image natsuki 1dt = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/t.png")
image natsuki 1du = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/u.png")
image natsuki 1dv = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/v.png")
image natsuki 1dw = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/w.png")
image natsuki 1dx = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/x.png")
image natsuki 1dy = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/y.png")
image natsuki 1dz = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/z.png")

image natsuki 2da = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/a.png")
image natsuki 2db = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/b.png")
image natsuki 2dc = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/c.png")
image natsuki 2dcry = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "mod_assets/natsuki/cry.png")
image natsuki 2dd = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/d.png")
image natsuki 2de = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/e.png")
image natsuki 2df = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/f.png")
image natsuki 2dg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/g.png")
image natsuki 2dh = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/h.png")
image natsuki 2di = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/i.png")
image natsuki 2dj = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/j.png")
image natsuki 2dk = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/k.png")
image natsuki 2dl = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/l.png")
image natsuki 2dm = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/m.png")
image natsuki 2dn = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/n.png")
image natsuki 2do = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/o.png")
image natsuki 2dp = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/p.png")
image natsuki 2dq = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/q.png")
image natsuki 2dr = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/r.png")
image natsuki 2ds = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/s.png")
image natsuki 2dt = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/t.png")
image natsuki 2du = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/u.png")
image natsuki 2dv = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/v.png")
image natsuki 2dw = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/w.png")
image natsuki 2dx = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/x.png")
image natsuki 2dy = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/y.png")
image natsuki 2dz = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/1l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/z.png")

image natsuki 3da = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/a.png")
image natsuki 3db = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/b.png")
image natsuki 3dc = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/c.png")
image natsuki 3dcry = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "mod_assets/natsuki/cry.png")
image natsuki 3dd = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/d.png")
image natsuki 3de = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/e.png")
image natsuki 3df = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/f.png")
image natsuki 3dg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/g.png")
image natsuki 3dh = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/h.png")
image natsuki 3di = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/i.png")
image natsuki 3dj = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/j.png")
image natsuki 3dk = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/k.png")
image natsuki 3dl = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/l.png")
image natsuki 3dm = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/m.png")
image natsuki 3dn = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/n.png")
image natsuki 3do = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/o.png")
image natsuki 3dp = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/p.png")
image natsuki 3dq = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/q.png")
image natsuki 3dr = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/r.png")
image natsuki 3ds = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/s.png")
image natsuki 3dt = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/t.png")
image natsuki 3du = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/u.png")
image natsuki 3dv = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/v.png")
image natsuki 3dw = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/w.png")
image natsuki 3dx = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/x.png")
image natsuki 3dy = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/y.png")
image natsuki 3dz = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/1r.png", (0, 0), "natsuki/z.png")

image natsuki 4da = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/a.png")
image natsuki 4db = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/b.png")
image natsuki 4dc = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/c.png")
image natsuki 4dcry = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "mod_assets/natsuki/cry.png")
image natsuki 4dd = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/d.png")
image natsuki 4de = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/e.png")
image natsuki 4df = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/f.png")
image natsuki 4dg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/g.png")
image natsuki 4dh = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/h.png")
image natsuki 4di = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/i.png")
image natsuki 4dj = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/j.png")
image natsuki 4dk = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/k.png")
image natsuki 4dl = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/l.png")
image natsuki 4dm = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/m.png")
image natsuki 4dn = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/n.png")
image natsuki 4do = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/o.png")
image natsuki 4dp = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/p.png")
image natsuki 4dq = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/q.png")
image natsuki 4dr = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/r.png")
image natsuki 4ds = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/s.png")
image natsuki 4dt = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/t.png")
image natsuki 4du = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/u.png")
image natsuki 4dv = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/v.png")
image natsuki 4dw = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/w.png")
image natsuki 4dx = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/x.png")
image natsuki 4dy = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/y.png")
image natsuki 4dz = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/coat/2l.png", (0, 0), "mod_assets/natsuki/coat/2r.png", (0, 0), "natsuki/z.png")



image natsuki 1ea = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/a.png")
image natsuki 1eb = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/b.png")
image natsuki 1ec = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/c.png")
image natsuki 1ecry = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "mod_assets/natsuki/cry.png")
image natsuki 1ed = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/d.png")
image natsuki 1ee = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/e.png")
image natsuki 1ef = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/f.png")
image natsuki 1eg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/g.png")
image natsuki 1eh = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/h.png")
image natsuki 1ei = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/i.png")
image natsuki 1ej = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/j.png")
image natsuki 1ek = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/k.png")
image natsuki 1el = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/l.png")
image natsuki 1em = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/m.png")
image natsuki 1en = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/n.png")
image natsuki 1eo = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/o.png")
image natsuki 1ep = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/p.png")
image natsuki 1eq = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/q.png")
image natsuki 1er = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/r.png")
image natsuki 1es = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/s.png")
image natsuki 1et = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/t.png")
image natsuki 1eu = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/u.png")
image natsuki 1ev = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/v.png")
image natsuki 1ew = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/w.png")
image natsuki 1ex = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/x.png")
image natsuki 1ey = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/y.png")
image natsuki 1ez = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/z.png")

image natsuki 2ea = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/a.png")
image natsuki 2eb = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/b.png")
image natsuki 2ec = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/c.png")
image natsuki 2ecry = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "mod_assets/natsuki/cry.png")
image natsuki 2ed = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/d.png")
image natsuki 2ee = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/e.png")
image natsuki 2ef = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/f.png")
image natsuki 2eg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/g.png")
image natsuki 2eh = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/h.png")
image natsuki 2ei = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/i.png")
image natsuki 2ej = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/j.png")
image natsuki 2ek = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/k.png")
image natsuki 2el = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/l.png")
image natsuki 2em = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/m.png")
image natsuki 2en = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/n.png")
image natsuki 2eo = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/o.png")
image natsuki 2ep = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/p.png")
image natsuki 2eq = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/q.png")
image natsuki 2er = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/r.png")
image natsuki 2es = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/s.png")
image natsuki 2et = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/t.png")
image natsuki 2eu = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/u.png")
image natsuki 2ev = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/v.png")
image natsuki 2ew = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/w.png")
image natsuki 2ex = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/x.png")
image natsuki 2ey = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/y.png")
image natsuki 2ez = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/1l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/z.png")

image natsuki 3ea = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/a.png")
image natsuki 3eb = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/b.png")
image natsuki 3ec = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/c.png")
image natsuki 3ecry = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "mod_assets/natsuki/cry.png")
image natsuki 3ed = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/d.png")
image natsuki 3ee = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/e.png")
image natsuki 3ef = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/f.png")
image natsuki 3eg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/g.png")
image natsuki 3eh = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/h.png")
image natsuki 3ei = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/i.png")
image natsuki 3ej = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/j.png")
image natsuki 3ek = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/k.png")
image natsuki 3el = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/l.png")
image natsuki 3em = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/m.png")
image natsuki 3en = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/n.png")
image natsuki 3eo = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/o.png")
image natsuki 3ep = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/p.png")
image natsuki 3eq = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/q.png")
image natsuki 3er = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/r.png")
image natsuki 3es = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/s.png")
image natsuki 3et = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/t.png")
image natsuki 3eu = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/u.png")
image natsuki 3ev = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/v.png")
image natsuki 3ew = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/w.png")
image natsuki 3ex = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/x.png")
image natsuki 3ey = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/y.png")
image natsuki 3ez = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/1r.png", (0, 0), "natsuki/z.png")

image natsuki 4ea = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/a.png")
image natsuki 4eb = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/b.png")
image natsuki 4ec = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/c.png")
image natsuki 4ecry = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "mod_assets/natsuki/cry.png")
image natsuki 4ed = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/d.png")
image natsuki 4ee = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/e.png")
image natsuki 4ef = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/f.png")
image natsuki 4eg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/g.png")
image natsuki 4eh = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/h.png")
image natsuki 4ei = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/i.png")
image natsuki 4ej = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/j.png")
image natsuki 4ek = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/k.png")
image natsuki 4el = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/l.png")
image natsuki 4em = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/m.png")
image natsuki 4en = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/n.png")
image natsuki 4eo = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/o.png")
image natsuki 4ep = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/p.png")
image natsuki 4eq = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/q.png")
image natsuki 4er = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/r.png")
image natsuki 4es = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/s.png")
image natsuki 4et = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/t.png")
image natsuki 4eu = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/u.png")
image natsuki 4ev = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/v.png")
image natsuki 4ew = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/w.png")
image natsuki 4ex = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/x.png")
image natsuki 4ey = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/y.png")
image natsuki 4ez = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/scarf/2l.png", (0, 0), "mod_assets/natsuki/scarf/2r.png", (0, 0), "natsuki/z.png")



image natsuki 1fa = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/a.png")
image natsuki 1fb = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/b.png")
image natsuki 1fc = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/c.png")
image natsuki 1fcry = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "mod_assets/natsuki/cry.png")
image natsuki 1fd = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/d.png")
image natsuki 1fe = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/e.png")
image natsuki 1ff = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/f.png")
image natsuki 1fg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/g.png")
image natsuki 1fh = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/h.png")
image natsuki 1fi = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/i.png")
image natsuki 1fj = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/j.png")
image natsuki 1fk = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/k.png")
image natsuki 1fl = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/l.png")
image natsuki 1fm = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/m.png")
image natsuki 1fn = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/n.png")
image natsuki 1fo = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/o.png")
image natsuki 1fp = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/p.png")
image natsuki 1fq = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/q.png")
image natsuki 1fr = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/r.png")
image natsuki 1fs = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/s.png")
image natsuki 1ft = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/t.png")
image natsuki 1fu = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/u.png")
image natsuki 1fv = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/v.png")
image natsuki 1fw = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/w.png")
image natsuki 1fx = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/x.png")
image natsuki 1fy = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/y.png")
image natsuki 1fz = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/z.png")

image natsuki 2fa = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/a.png")
image natsuki 2fb = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/b.png")
image natsuki 2fc = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/c.png")
image natsuki 2fcry = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "mod_assets/natsuki/cry.png")
image natsuki 2fd = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/d.png")
image natsuki 2fe = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/e.png")
image natsuki 2ff = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/f.png")
image natsuki 2fg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/g.png")
image natsuki 2fh = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/h.png")
image natsuki 2fi = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/i.png")
image natsuki 2fj = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/j.png")
image natsuki 2fk = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/k.png")
image natsuki 2fl = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/l.png")
image natsuki 2fm = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/m.png")
image natsuki 2fn = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/n.png")
image natsuki 2fo = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/o.png")
image natsuki 2fp = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/p.png")
image natsuki 2fq = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/q.png")
image natsuki 2fr = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/r.png")
image natsuki 2fs = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/s.png")
image natsuki 2ft = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/t.png")
image natsuki 2fu = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/u.png")
image natsuki 2fv = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/v.png")
image natsuki 2fw = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/w.png")
image natsuki 2fx = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/x.png")
image natsuki 2fy = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/y.png")
image natsuki 2fz = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/z.png")

image natsuki 3fa = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/a.png")
image natsuki 3fb = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/b.png")
image natsuki 3fc = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/c.png")
image natsuki 3fcry = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "mod_assets/natsuki/cry.png")
image natsuki 3fd = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/d.png")
image natsuki 3fe = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/e.png")
image natsuki 3ff = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/f.png")
image natsuki 3fg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/g.png")
image natsuki 3fh = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/h.png")
image natsuki 3fi = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/i.png")
image natsuki 3fj = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/j.png")
image natsuki 3fk = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/k.png")
image natsuki 3fl = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/l.png")
image natsuki 3fm = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/m.png")
image natsuki 3fn = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/n.png")
image natsuki 3fo = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/o.png")
image natsuki 3fp = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/p.png")
image natsuki 3fq = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/q.png")
image natsuki 3fr = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/r.png")
image natsuki 3fs = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/s.png")
image natsuki 3ft = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/t.png")
image natsuki 3fu = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/u.png")
image natsuki 3fv = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/v.png")
image natsuki 3fw = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/w.png")
image natsuki 3fx = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/x.png")
image natsuki 3fy = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/y.png")
image natsuki 3fz = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/z.png")

image natsuki 4fa = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/a.png")
image natsuki 4fb = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/b.png")
image natsuki 4fc = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/c.png")
image natsuki 4fcry = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "mod_assets/natsuki/cry.png")
image natsuki 4fd = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/d.png")
image natsuki 4fe = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/e.png")
image natsuki 4ff = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/f.png")
image natsuki 4fg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/g.png")
image natsuki 4fh = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/h.png")
image natsuki 4fi = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/i.png")
image natsuki 4fj = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/j.png")
image natsuki 4fk = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/k.png")
image natsuki 4fl = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/l.png")
image natsuki 4fm = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/m.png")
image natsuki 4fn = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/n.png")
image natsuki 4fo = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/o.png")
image natsuki 4fp = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/p.png")
image natsuki 4fq = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/q.png")
image natsuki 4fr = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/r.png")
image natsuki 4fs = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/s.png")
image natsuki 4ft = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/t.png")
image natsuki 4fu = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/u.png")
image natsuki 4fv = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/v.png")
image natsuki 4fw = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/w.png")
image natsuki 4fx = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/x.png")
image natsuki 4fy = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/y.png")
image natsuki 4fz = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/2l.png", (0, 0), "mod_assets/natsuki/jumper/2r.png", (0, 0), "natsuki/z.png")

image natsuki 1fta = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/2t.png")
image natsuki 1ftb = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/2tb.png")
image natsuki 1ftc = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/2tc.png")
image natsuki 1ftd = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/2td.png")
image natsuki 1fte = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/2te.png")
image natsuki 1ftf = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/2tf.png")
image natsuki 1ftg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/2tg.png")
image natsuki 1fth = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/2th.png")
image natsuki 1fti = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/jumper/1l.png", (0, 0), "mod_assets/natsuki/jumper/1r.png", (0, 0), "natsuki/2ti.png")



image natsuki 1ga = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/cuts/1l.png", (0, 0), "mod_assets/natsuki/cuts/1r.png", (0, 0), "natsuki/a.png")
image natsuki 1gb = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/cuts/1l.png", (0, 0), "mod_assets/natsuki/cuts/1r.png", (0, 0), "natsuki/b.png")
image natsuki 1gc = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/cuts/1l.png", (0, 0), "mod_assets/natsuki/cuts/1r.png", (0, 0), "natsuki/c.png")
image natsuki 1gcry = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/cuts/1l.png", (0, 0), "mod_assets/natsuki/cuts/1r.png", (0, 0), "mod_assets/natsuki/cry.png")
image natsuki 1gd = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/cuts/1l.png", (0, 0), "mod_assets/natsuki/cuts/1r.png", (0, 0), "natsuki/d.png")
image natsuki 1ge = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/cuts/1l.png", (0, 0), "mod_assets/natsuki/cuts/1r.png", (0, 0), "natsuki/e.png")
image natsuki 1gf = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/cuts/1l.png", (0, 0), "mod_assets/natsuki/cuts/1r.png", (0, 0), "natsuki/f.png")
image natsuki 1gg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/cuts/1l.png", (0, 0), "mod_assets/natsuki/cuts/1r.png", (0, 0), "natsuki/g.png")
image natsuki 1gh = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/cuts/1l.png", (0, 0), "mod_assets/natsuki/cuts/1r.png", (0, 0), "natsuki/h.png")
image natsuki 1gi = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/cuts/1l.png", (0, 0), "mod_assets/natsuki/cuts/1r.png", (0, 0), "natsuki/i.png")
image natsuki 1gj = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/cuts/1l.png", (0, 0), "mod_assets/natsuki/cuts/1r.png", (0, 0), "natsuki/j.png")
image natsuki 1gk = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/cuts/1l.png", (0, 0), "mod_assets/natsuki/cuts/1r.png", (0, 0), "natsuki/k.png")
image natsuki 1gl = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/cuts/1l.png", (0, 0), "mod_assets/natsuki/cuts/1r.png", (0, 0), "natsuki/l.png")
image natsuki 1gm = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/cuts/1l.png", (0, 0), "mod_assets/natsuki/cuts/1r.png", (0, 0), "natsuki/m.png")
image natsuki 1gn = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/cuts/1l.png", (0, 0), "mod_assets/natsuki/cuts/1r.png", (0, 0), "natsuki/n.png")
image natsuki 1go = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/cuts/1l.png", (0, 0), "mod_assets/natsuki/cuts/1r.png", (0, 0), "natsuki/o.png")
image natsuki 1gp = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/cuts/1l.png", (0, 0), "mod_assets/natsuki/cuts/1r.png", (0, 0), "natsuki/p.png")
image natsuki 1gq = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/cuts/1l.png", (0, 0), "mod_assets/natsuki/cuts/1r.png", (0, 0), "natsuki/q.png")
image natsuki 1gr = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/cuts/1l.png", (0, 0), "mod_assets/natsuki/cuts/1r.png", (0, 0), "natsuki/r.png")
image natsuki 1gs = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/cuts/1l.png", (0, 0), "mod_assets/natsuki/cuts/1r.png", (0, 0), "natsuki/s.png")
image natsuki 1gscream = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/cuts/1l.png", (0, 0), "mod_assets/natsuki/cuts/1r.png", (0, 0), "natsuki/scream.png")
image natsuki 1gt = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/cuts/1l.png", (0, 0), "mod_assets/natsuki/cuts/1r.png", (0, 0), "natsuki/t.png")
image natsuki 1gu = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/cuts/1l.png", (0, 0), "mod_assets/natsuki/cuts/1r.png", (0, 0), "natsuki/u.png")
image natsuki 1gv = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/cuts/1l.png", (0, 0), "mod_assets/natsuki/cuts/1r.png", (0, 0), "natsuki/v.png")
image natsuki 1gw = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/cuts/1l.png", (0, 0), "mod_assets/natsuki/cuts/1r.png", (0, 0), "natsuki/w.png")
image natsuki 1gx = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/cuts/1l.png", (0, 0), "mod_assets/natsuki/cuts/1r.png", (0, 0), "natsuki/x.png")
image natsuki 1gy = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/cuts/1l.png", (0, 0), "mod_assets/natsuki/cuts/1r.png", (0, 0), "natsuki/y.png")
image natsuki 1gz = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/cuts/1l.png", (0, 0), "mod_assets/natsuki/cuts/1r.png", (0, 0), "natsuki/z.png")

image natsuki 1gta = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/cuts/1l.png", (0, 0), "mod_assets/natsuki/cuts/1r.png", (0, 0), "natsuki/2t.png")
image natsuki 1gtb = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/cuts/1l.png", (0, 0), "mod_assets/natsuki/cuts/1r.png", (0, 0), "natsuki/2tb.png")
image natsuki 1gtc = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/cuts/1l.png", (0, 0), "mod_assets/natsuki/cuts/1r.png", (0, 0), "natsuki/2tc.png")
image natsuki 1gtd = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/cuts/1l.png", (0, 0), "mod_assets/natsuki/cuts/1r.png", (0, 0), "natsuki/2td.png")
image natsuki 1gte = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/cuts/1l.png", (0, 0), "mod_assets/natsuki/cuts/1r.png", (0, 0), "natsuki/2te.png")
image natsuki 1gtf = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/cuts/1l.png", (0, 0), "mod_assets/natsuki/cuts/1r.png", (0, 0), "natsuki/2tf.png")
image natsuki 1gtg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/cuts/1l.png", (0, 0), "mod_assets/natsuki/cuts/1r.png", (0, 0), "natsuki/2tg.png")
image natsuki 1gth = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/cuts/1l.png", (0, 0), "mod_assets/natsuki/cuts/1r.png", (0, 0), "natsuki/2th.png")
image natsuki 1gti = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/cuts/1l.png", (0, 0), "mod_assets/natsuki/cuts/1r.png", (0, 0), "natsuki/2ti.png")



image natsuki 1ha = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/a.png")
image natsuki 1hb = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/b.png")
image natsuki 1hc = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/c.png")
image natsuki 1hcry = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/cry.png")
image natsuki 1hd = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/d.png")
image natsuki 1he = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/e.png")
image natsuki 1hf = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/f.png")
image natsuki 1hg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/g.png")
image natsuki 1hh = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/h.png")
image natsuki 1hi = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/i.png")
image natsuki 1hj = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/j.png")
image natsuki 1hk = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/k.png")
image natsuki 1hl = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/l.png")
image natsuki 1hm = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/m.png")
image natsuki 1hn = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/n.png")
image natsuki 1ho = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/o.png")
image natsuki 1hp = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/p.png")
image natsuki 1hq = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/q.png")
image natsuki 1hr = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/r.png")
image natsuki 1hs = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/s.png")
image natsuki 1hscream = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/scream.png")
image natsuki 1ht = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/t.png")
image natsuki 1hu = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/u.png")
image natsuki 1hv = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/v.png")
image natsuki 1hw = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/w.png")
image natsuki 1hx = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/x.png")
image natsuki 1hy = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/y.png")
image natsuki 1hz = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/z.png")

image natsuki 2ha = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/a.png")
image natsuki 2hb = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/b.png")
image natsuki 2hc = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/c.png")
image natsuki 2hcry = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/cry.png")
image natsuki 2hd = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/d.png")
image natsuki 2he = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/e.png")
image natsuki 2hf = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/f.png")
image natsuki 2hg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/g.png")
image natsuki 2hh = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/h.png")
image natsuki 2hi = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/i.png")
image natsuki 2hj = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/j.png")
image natsuki 2hk = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/k.png")
image natsuki 2hl = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/l.png")
image natsuki 2hm = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/m.png")
image natsuki 2hn = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/n.png")
image natsuki 2ho = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/o.png")
image natsuki 2hp = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/p.png")
image natsuki 2hq = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/q.png")
image natsuki 2hr = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/r.png")
image natsuki 2hs = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/s.png")
image natsuki 2hscream = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/scream.png")
image natsuki 2ht = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/t.png")
image natsuki 2hu = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/u.png")
image natsuki 2hv = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/v.png")
image natsuki 2hw = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/w.png")
image natsuki 2hx = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/x.png")
image natsuki 2hy = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/y.png")
image natsuki 2hz = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/1l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/z.png")

image natsuki 3ha = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/a.png")
image natsuki 3hb = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/b.png")
image natsuki 3hc = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/c.png")
image natsuki 3hcry = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/cry.png")
image natsuki 3hd = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/d.png")
image natsuki 3he = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/e.png")
image natsuki 3hf = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/f.png")
image natsuki 3hg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/g.png")
image natsuki 3hh = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/h.png")
image natsuki 3hi = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/i.png")
image natsuki 3hj = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/j.png")
image natsuki 3hk = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/k.png")
image natsuki 3hl = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/l.png")
image natsuki 3hm = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/m.png")
image natsuki 3hn = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/n.png")
image natsuki 3ho = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/o.png")
image natsuki 3hp = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/p.png")
image natsuki 3hq = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/q.png")
image natsuki 3hr = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/r.png")
image natsuki 3hs = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/s.png")
image natsuki 3hscream = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/scream.png")
image natsuki 3ht = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/t.png")
image natsuki 3hu = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/u.png")
image natsuki 3hv = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/v.png")
image natsuki 3hw = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/w.png")
image natsuki 3hx = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/x.png")
image natsuki 3hy = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/y.png")
image natsuki 3hz = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/1r.png", (0, 0), "mod_assets/natsuki/towel/z.png")

image natsuki 4ha = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/a.png")
image natsuki 4hb = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/b.png")
image natsuki 4hc = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/c.png")
image natsuki 4hcry = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/cry.png")
image natsuki 4hd = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/d.png")
image natsuki 4he = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/e.png")
image natsuki 4hf = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/f.png")
image natsuki 4hg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/g.png")
image natsuki 4hh = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/h.png")
image natsuki 4hi = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/i.png")
image natsuki 4hj = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/j.png")
image natsuki 4hk = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/k.png")
image natsuki 4hl = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/l.png")
image natsuki 4hm = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/m.png")
image natsuki 4hn = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/n.png")
image natsuki 4ho = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/o.png")
image natsuki 4hp = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/p.png")
image natsuki 4hq = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/q.png")
image natsuki 4hr = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/r.png")
image natsuki 4hs = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/s.png")
image natsuki 4hscream = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/scream.png")
image natsuki 4ht = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/t.png")
image natsuki 4hu = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/u.png")
image natsuki 4hv = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/v.png")
image natsuki 4hw = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/w.png")
image natsuki 4hx = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/x.png")
image natsuki 4hy = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/y.png")
image natsuki 4hz = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/towel/2l.png", (0, 0), "mod_assets/natsuki/towel/2r.png", (0, 0), "mod_assets/natsuki/towel/z.png")



image natsuki sexy1 = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/sexy/1l.png", (0, 0), "mod_assets/natsuki/sexy/1r.png", (0, 0), "mod_assets/natsuki/sexy/a.png")
image natsuki sexy2 = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/sexy/2l.png", (0, 0), "mod_assets/natsuki/sexy/2r.png", (0, 0), "mod_assets/natsuki/sexy/a.png")



image natsuki mouth = LiveComposite((960, 960), (0, 0), "natsuki/0.png", (390, 340), "n_rects_mouth", (480, 334), "n_rects_mouth")

image n_rects_mouth:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    size (20, 25)

image n_moving_mouth:
    "images/natsuki/mouth.png"
    pos (615, 305)
    xanchor 0.5 yanchor 0.5
    parallel:
        choice:
            ease 0.10 yzoom 0.2
        choice:
            ease 0.05 yzoom 0.2
        choice:
            ease 0.075 yzoom 0.2
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        pass
        choice:
            ease 0.10 yzoom 1
        choice:
            ease 0.05 yzoom 1
        choice:
            ease 0.075 yzoom 1
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        repeat
    parallel:
        choice:
            0.2
        choice:
            0.4
        choice:
            0.6
        ease 0.2 xzoom 0.4
        ease 0.2 xzoom 0.8
        repeat

image natsuki_ghost_blood:
    "#00000000"
    "natsuki/ghost_blood.png" with ImageDissolve("images/menu/wipedown.png", 80.0, ramplen=4, alpha=True)
    pos (620,320) zoom 0.80

image natsuki ghost_base:
    "natsuki/ghost1.png"
image natsuki ghost1:
    "natsuki 11"
    "natsuki ghost_base" with Dissolve(20.0, alpha=True)
image natsuki ghost2 = Image("natsuki/ghost2.png")
image natsuki ghost3 = Image("natsuki/ghost3.png")
image natsuki ghost4:
    "natsuki ghost3"
    parallel:
        easeout 0.25 zoom 4.5 yoffset 1200
    parallel:
        ease 0.025 xoffset -20
        ease 0.025 xoffset 20
        repeat
    0.25
    "black"
image natsuki glitch1:
    "natsuki/glitch1.png"
    zoom 1.25
    block:
        yoffset 300 xoffset 100 ytile 2
        linear 0.15 yoffset 200
        repeat
    time 0.75
    yoffset 0 zoom 1 xoffset 0 ytile 1
    "natsuki 4e"

image natsuki scream = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/scream.png")
image natsuki vomit = "natsuki/vomit.png"
image n_blackeyes = "images/natsuki/blackeyes.png"
image n_eye = "images/natsuki/eye.png"


image yuri 1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png")
image yuri 2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 3 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 4 = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/a2.png")

image yuri 1a = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png")
image yuri 1b = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/b.png")
image yuri 1c = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/c.png")
image yuri 1d = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/d.png")
image yuri 1e = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/e.png")
image yuri 1f = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/f.png")
image yuri 1g = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/g.png")
image yuri 1h = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/h.png")
image yuri 1i = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/i.png")
image yuri 1j = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/j.png")
image yuri 1k = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/k.png")
image yuri 1l = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/l.png")
image yuri 1m = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/m.png")
image yuri 1n = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/n.png")
image yuri 1o = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/o.png")
image yuri 1p = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/p.png")
image yuri 1q = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/q.png")
image yuri 1r = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/r.png")
image yuri 1s = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/s.png")
image yuri 1t = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/t.png")
image yuri 1u = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/u.png")
image yuri 1v = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/v.png")
image yuri 1w = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/w.png")

image yuri 1y1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y1.png")
image yuri 1y2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y2.png")
image yuri 1y3 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y3.png")
image yuri 1y4 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y4.png")
image yuri 1y5 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y5.png")
image yuri 1y6 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y6.png")
image yuri 1y7 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y7.png")

image yuri 2a = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 2b = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/b.png")
image yuri 2c = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png")
image yuri 2d = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png")
image yuri 2e = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/e.png")
image yuri 2f = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/f.png")
image yuri 2g = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/g.png")
image yuri 2h = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/h.png")
image yuri 2i = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/i.png")
image yuri 2j = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/j.png")
image yuri 2k = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png")
image yuri 2l = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png")
image yuri 2m = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png")
image yuri 2n = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/n.png")
image yuri 2o = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/o.png")
image yuri 2p = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/p.png")
image yuri 2q = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/q.png")
image yuri 2r = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/r.png")
image yuri 2s = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/s.png")
image yuri 2t = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/t.png")
image yuri 2u = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/u.png")
image yuri 2v = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/v.png")
image yuri 2w = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png")

image yuri 2y1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png")
image yuri 2y2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png")
image yuri 2y3 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png")
image yuri 2y4 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png")
image yuri 2y5 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png")
image yuri 2y6 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png")
image yuri 2y7 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png")

image yuri 3a = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 3b = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/b.png")
image yuri 3c = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png")
image yuri 3d = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png")
image yuri 3e = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/e.png")
image yuri 3f = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/f.png")
image yuri 3g = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/g.png")
image yuri 3h = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/h.png")
image yuri 3i = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/i.png")
image yuri 3j = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/j.png")
image yuri 3k = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png")
image yuri 3l = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png")
image yuri 3m = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png")
image yuri 3n = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/n.png")
image yuri 3o = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/o.png")
image yuri 3p = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/p.png")
image yuri 3q = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/q.png")
image yuri 3r = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/r.png")
image yuri 3s = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/s.png")
image yuri 3t = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/t.png")
image yuri 3u = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/u.png")
image yuri 3v = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/v.png")
image yuri 3w = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png")

image yuri 3y1 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png")
image yuri 3y2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png")
image yuri 3y3 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png")
image yuri 3y4 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png")
image yuri 3y5 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png")
image yuri 3y6 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png")
image yuri 3y7 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png")

image yuri 4a = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/a2.png")
image yuri 4b = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/b2.png")
image yuri 4c = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/c2.png")
image yuri 4d = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/d2.png")
image yuri 4e = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/e2.png")

image yuri 1ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")

image yuri 1by1 = im.Composite((960, 960), (0, 0), "yuri/y1.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1by3 = im.Composite((960, 960), (0, 0), "yuri/y1.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1by2 = im.Composite((960, 960), (0, 0), "yuri/y3.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1by4 = im.Composite((960, 960), (0, 0), "yuri/y4.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1by5 = im.Composite((960, 960), (0, 0), "yuri/y5.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1by6 = im.Composite((960, 960), (0, 0), "yuri/y6.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1by7 = im.Composite((960, 960), (0, 0), "yuri/y7.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")

image yuri 2ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")

image yuri 2by1 = im.Composite((960, 960), (0, 0), "yuri/y1.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2by3 = im.Composite((960, 960), (0, 0), "yuri/y1.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2by2 = im.Composite((960, 960), (0, 0), "yuri/y3.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2by4 = im.Composite((960, 960), (0, 0), "yuri/y4.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2by5 = im.Composite((960, 960), (0, 0), "yuri/y5.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2by6 = im.Composite((960, 960), (0, 0), "yuri/y6.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2by7 = im.Composite((960, 960), (0, 0), "yuri/y7.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")

image yuri 3ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")

image yuri 3by1 = im.Composite((960, 960), (0, 0), "yuri/y1.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3by3 = im.Composite((960, 960), (0, 0), "yuri/y1.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3by2 = im.Composite((960, 960), (0, 0), "yuri/y3.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3by4 = im.Composite((960, 960), (0, 0), "yuri/y4.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3by5 = im.Composite((960, 960), (0, 0), "yuri/y5.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3by6 = im.Composite((960, 960), (0, 0), "yuri/y6.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3by7 = im.Composite((960, 960), (0, 0), "yuri/y7.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")

image yuri 4ba = im.Composite((960, 960), (0, 0), "yuri/a2.png", (0, 0), "yuri/3b.png")
image yuri 4bb = im.Composite((960, 960), (0, 0), "yuri/b2.png", (0, 0), "yuri/3b.png")
image yuri 4bc = im.Composite((960, 960), (0, 0), "yuri/c2.png", (0, 0), "yuri/3b.png")
image yuri 4bd = im.Composite((960, 960), (0, 0), "yuri/d2.png", (0, 0), "yuri/3b.png")
image yuri 4be = im.Composite((960, 960), (0, 0), "yuri/e2.png", (0, 0), "yuri/3b.png")



image yuri 5a = im.Composite((960, 960), (0, 0), "mod_assets/yuri/cry/1a.png", (0, 0), "yuri/3.png")
image yuri 5b = im.Composite((960, 960), (0, 0), "mod_assets/yuri/cry/1b.png", (0, 0), "yuri/3.png")
image yuri 5c = im.Composite((960, 960), (0, 0), "mod_assets/yuri/cry/1c.png", (0, 0), "yuri/3.png")
image yuri 5d = im.Composite((960, 960), (0, 0), "mod_assets/yuri/cry/1d.png", (0, 0), "yuri/3.png")
image yuri 5e = im.Composite((960, 960), (0, 0), "mod_assets/yuri/cry/1e.png", (0, 0), "yuri/3.png")
image yuri 5f = im.Composite((960, 960), (0, 0), "mod_assets/yuri/cry/1f.png", (0, 0), "yuri/3.png")
image yuri 5g = im.Composite((960, 960), (0, 0), "mod_assets/yuri/cry/1g.png", (0, 0), "yuri/3.png")
image yuri 5h = im.Composite((960, 960), (0, 0), "mod_assets/yuri/cry/1h.png", (0, 0), "yuri/3.png")



image yuri 1ca = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/1r.png")
image yuri 1cb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/1r.png")
image yuri 1cc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/1r.png")
image yuri 1cd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/1r.png")
image yuri 1ce = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/1r.png")
image yuri 1cf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/1r.png")
image yuri 1cg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/1r.png")
image yuri 1ch = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/1r.png")
image yuri 1ci = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/1r.png")
image yuri 1cj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/1r.png")
image yuri 1ck = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/1r.png")
image yuri 1cl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/1r.png")
image yuri 1cm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/1r.png")
image yuri 1cn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/1r.png")
image yuri 1co = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/1r.png")
image yuri 1cp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/1r.png")
image yuri 1cq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/1r.png")
image yuri 1cr = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/1r.png")
image yuri 1cs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/1r.png")
image yuri 1ct = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/1r.png")
image yuri 1cu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/1r.png")
image yuri 1cv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/1r.png")
image yuri 1cw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/1r.png")

image yuri 1cy1 = im.Composite((960, 960), (0, 0), "yuri/y1.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/1r.png")
image yuri 1cy2 = im.Composite((960, 960), (0, 0), "yuri/y2.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/1r.png")
image yuri 1cy3 = im.Composite((960, 960), (0, 0), "yuri/y3.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/1r.png")
image yuri 1cy4 = im.Composite((960, 960), (0, 0), "yuri/y4.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/1r.png")
image yuri 1cy5 = im.Composite((960, 960), (0, 0), "yuri/y5.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/1r.png")
image yuri 1cy6 = im.Composite((960, 960), (0, 0), "yuri/y6.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/1r.png")
image yuri 1cy7 = im.Composite((960, 960), (0, 0), "yuri/y7.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/1r.png")

image yuri 1cy1b = im.Composite((960, 960), (0, 0), "mod_assets/yuri/y2b.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/1r.png")
image yuri 1cy2b = im.Composite((960, 960), (0, 0), "mod_assets/yuri/y4b.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/1r.png")
image yuri 1cy3b = im.Composite((960, 960), (0, 0), "mod_assets/yuri/y7b.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/1r.png")

image yuri 2ca = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 2cb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 2cc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 2cd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 2ce = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 2cf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 2cg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 2ch = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 2ci = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 2cj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 2ck = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 2cl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 2cm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 2cn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 2co = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 2cp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 2cq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 2cr = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 2cs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 2ct = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 2cu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 2cv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 2cw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")

image yuri 2cy1 = im.Composite((960, 960), (0, 0), "yuri/y1.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 2cy2 = im.Composite((960, 960), (0, 0), "yuri/y2.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 2cy3 = im.Composite((960, 960), (0, 0), "yuri/y3.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 2cy4 = im.Composite((960, 960), (0, 0), "yuri/y4.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 2cy5 = im.Composite((960, 960), (0, 0), "yuri/y5.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 2cy6 = im.Composite((960, 960), (0, 0), "yuri/y6.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 2cy7 = im.Composite((960, 960), (0, 0), "yuri/y7.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")

image yuri 2cy1b = im.Composite((960, 960), (0, 0), "mod_assets/yuri/y2b.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 2cy2b = im.Composite((960, 960), (0, 0), "mod_assets/yuri/y4b.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 2cy3b = im.Composite((960, 960), (0, 0), "mod_assets/yuri/y7b.png", (0, 0), "mod_assets/yuri/funeral/1l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")

image yuri 3ca = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "mod_assets/yuri/funeral/2l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 3cb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "mod_assets/yuri/funeral/2l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 3cc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "mod_assets/yuri/funeral/2l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 3cd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "mod_assets/yuri/funeral/2l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 3ce = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "mod_assets/yuri/funeral/2l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 3cf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "mod_assets/yuri/funeral/2l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 3cg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "mod_assets/yuri/funeral/2l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 3ch = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "mod_assets/yuri/funeral/2l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 3ci = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "mod_assets/yuri/funeral/2l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 3cj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "mod_assets/yuri/funeral/2l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 3ck = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "mod_assets/yuri/funeral/2l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 3cl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "mod_assets/yuri/funeral/2l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 3cm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "mod_assets/yuri/funeral/2l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 3cn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "mod_assets/yuri/funeral/2l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 3co = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "mod_assets/yuri/funeral/2l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 3cp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "mod_assets/yuri/funeral/2l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 3cq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "mod_assets/yuri/funeral/2l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 3cr = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "mod_assets/yuri/funeral/2l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 3cs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "mod_assets/yuri/funeral/2l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 3ct = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "mod_assets/yuri/funeral/2l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 3cu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "mod_assets/yuri/funeral/2l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 3cv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "mod_assets/yuri/funeral/2l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 3cw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "mod_assets/yuri/funeral/2l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")

image yuri 3cy1 = im.Composite((960, 960), (0, 0), "yuri/y1.png", (0, 0), "mod_assets/yuri/funeral/2l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 3cy2 = im.Composite((960, 960), (0, 0), "yuri/y2.png", (0, 0), "mod_assets/yuri/funeral/2l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 3cy3 = im.Composite((960, 960), (0, 0), "yuri/y3.png", (0, 0), "mod_assets/yuri/funeral/2l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 3cy4 = im.Composite((960, 960), (0, 0), "yuri/y4.png", (0, 0), "mod_assets/yuri/funeral/2l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 3cy5 = im.Composite((960, 960), (0, 0), "yuri/y5.png", (0, 0), "mod_assets/yuri/funeral/2l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 3cy6 = im.Composite((960, 960), (0, 0), "yuri/y6.png", (0, 0), "mod_assets/yuri/funeral/2l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 3cy7 = im.Composite((960, 960), (0, 0), "yuri/y7.png", (0, 0), "mod_assets/yuri/funeral/2l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")

image yuri 3cy1b = im.Composite((960, 960), (0, 0), "mod_assets/yuri/y2b.png", (0, 0), "mod_assets/yuri/funeral/2l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 3cy2b = im.Composite((960, 960), (0, 0), "mod_assets/yuri/y4b.png", (0, 0), "mod_assets/yuri/funeral/2l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")
image yuri 3cy3b = im.Composite((960, 960), (0, 0), "mod_assets/yuri/y7b.png", (0, 0), "mod_assets/yuri/funeral/2l.png", (0, 0), "mod_assets/yuri/funeral/2r.png")

image yuri 4ca = im.Composite((960, 960), (0, 0), "yuri/a2.png", (0, 0), "mod_assets/yuri/funeral/3.png")
image yuri 4cb = im.Composite((960, 960), (0, 0), "yuri/b2.png", (0, 0), "mod_assets/yuri/funeral/3.png")
image yuri 4cc = im.Composite((960, 960), (0, 0), "yuri/c2.png", (0, 0), "mod_assets/yuri/funeral/3.png")
image yuri 4cd = im.Composite((960, 960), (0, 0), "yuri/d2.png", (0, 0), "mod_assets/yuri/funeral/3.png")
image yuri 4ce = im.Composite((960, 960), (0, 0), "yuri/e2.png", (0, 0), "mod_assets/yuri/funeral/3.png")

image yuri 5ca = im.Composite((960, 960), (0, 0), "mod_assets/yuri/cry/1a.png", (0, 0), "mod_assets/yuri/funeral/3.png")
image yuri 5cb = im.Composite((960, 960), (0, 0), "mod_assets/yuri/cry/1b.png", (0, 0), "mod_assets/yuri/funeral/3.png")
image yuri 5cc = im.Composite((960, 960), (0, 0), "mod_assets/yuri/cry/1c.png", (0, 0), "mod_assets/yuri/funeral/3.png")
image yuri 5cd = im.Composite((960, 960), (0, 0), "mod_assets/yuri/cry/1d.png", (0, 0), "mod_assets/yuri/funeral/3.png")
image yuri 5ce = im.Composite((960, 960), (0, 0), "mod_assets/yuri/cry/1e.png", (0, 0), "mod_assets/yuri/funeral/3.png")
image yuri 5cf = im.Composite((960, 960), (0, 0), "mod_assets/yuri/cry/1f.png", (0, 0), "mod_assets/yuri/funeral/3.png")
image yuri 5cg = im.Composite((960, 960), (0, 0), "mod_assets/yuri/cry/1g.png", (0, 0), "mod_assets/yuri/funeral/3.png")
image yuri 5ch = im.Composite((960, 960), (0, 0), "mod_assets/yuri/cry/1h.png", (0, 0), "mod_assets/yuri/funeral/3.png")



image yuri 1da = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/1r.png")
image yuri 1db = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/1r.png")
image yuri 1dc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/1r.png")
image yuri 1dd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/1r.png")
image yuri 1de = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/1r.png")
image yuri 1df = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/1r.png")
image yuri 1dg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/1r.png")
image yuri 1dh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/1r.png")
image yuri 1di = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/1r.png")
image yuri 1dj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/1r.png")
image yuri 1dk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/1r.png")
image yuri 1dl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/1r.png")
image yuri 1dm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/1r.png")
image yuri 1dn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/1r.png")
image yuri 1do = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/1r.png")
image yuri 1dp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/1r.png")
image yuri 1dq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/1r.png")
image yuri 1dr = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/1r.png")
image yuri 1ds = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/1r.png")
image yuri 1dt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/1r.png")
image yuri 1du = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/1r.png")
image yuri 1dv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/1r.png")
image yuri 1dw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/1r.png")

image yuri 1dy1 = im.Composite((960, 960), (0, 0), "yuri/y1.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/1r.png")
image yuri 1dy2 = im.Composite((960, 960), (0, 0), "yuri/y2.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/1r.png")
image yuri 1dy3 = im.Composite((960, 960), (0, 0), "yuri/y3.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/1r.png")
image yuri 1dy4 = im.Composite((960, 960), (0, 0), "yuri/y4.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/1r.png")
image yuri 1dy5 = im.Composite((960, 960), (0, 0), "yuri/y5.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/1r.png")
image yuri 1dy6 = im.Composite((960, 960), (0, 0), "yuri/y6.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/1r.png")
image yuri 1dy7 = im.Composite((960, 960), (0, 0), "yuri/y7.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/1r.png")

image yuri 1dy1b = im.Composite((960, 960), (0, 0), "mod_assets/yuri/y2b.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/1r.png")
image yuri 1dy2b = im.Composite((960, 960), (0, 0), "mod_assets/yuri/y4b.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/1r.png")
image yuri 1dy3b = im.Composite((960, 960), (0, 0), "mod_assets/yuri/y7b.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/1r.png")

image yuri 2da = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 2db = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 2dc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 2dd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 2de = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 2df = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 2dg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 2dh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 2di = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 2dj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 2dk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 2dl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 2dm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 2dn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 2do = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 2dp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 2dq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 2dr = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 2ds = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 2dt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 2du = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 2dv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 2dw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")

image yuri 2dy1 = im.Composite((960, 960), (0, 0), "yuri/y1.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 2dy2 = im.Composite((960, 960), (0, 0), "yuri/y2.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 2dy3 = im.Composite((960, 960), (0, 0), "yuri/y3.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 2dy4 = im.Composite((960, 960), (0, 0), "yuri/y4.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 2dy5 = im.Composite((960, 960), (0, 0), "yuri/y5.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 2dy6 = im.Composite((960, 960), (0, 0), "yuri/y6.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 2dy7 = im.Composite((960, 960), (0, 0), "yuri/y7.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")

image yuri 2dy1b = im.Composite((960, 960), (0, 0), "mod_assets/yuri/y2b.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 2dy2b = im.Composite((960, 960), (0, 0), "mod_assets/yuri/y4b.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 2dy3b = im.Composite((960, 960), (0, 0), "mod_assets/yuri/y7b.png", (0, 0), "mod_assets/yuri/unbutton/1l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")

image yuri 3da = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "mod_assets/yuri/unbutton/2l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 3db = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "mod_assets/yuri/unbutton/2l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 3dc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "mod_assets/yuri/unbutton/2l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 3dd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "mod_assets/yuri/unbutton/2l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 3de = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "mod_assets/yuri/unbutton/2l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 3df = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "mod_assets/yuri/unbutton/2l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 3dg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "mod_assets/yuri/unbutton/2l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 3dh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "mod_assets/yuri/unbutton/2l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 3di = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "mod_assets/yuri/unbutton/2l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 3dj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "mod_assets/yuri/unbutton/2l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 3dk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "mod_assets/yuri/unbutton/2l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 3dl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "mod_assets/yuri/unbutton/2l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 3dm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "mod_assets/yuri/unbutton/2l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 3dn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "mod_assets/yuri/unbutton/2l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 3do = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "mod_assets/yuri/unbutton/2l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 3dp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "mod_assets/yuri/unbutton/2l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 3dq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "mod_assets/yuri/unbutton/2l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 3dr = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "mod_assets/yuri/unbutton/2l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 3ds = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "mod_assets/yuri/unbutton/2l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 3dt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "mod_assets/yuri/unbutton/2l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 3du = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "mod_assets/yuri/unbutton/2l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 3dv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "mod_assets/yuri/unbutton/2l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 3dw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "mod_assets/yuri/unbutton/2l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")

image yuri 3dy1 = im.Composite((960, 960), (0, 0), "yuri/y1.png", (0, 0), "mod_assets/yuri/unbutton/2l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 3dy2 = im.Composite((960, 960), (0, 0), "yuri/y2.png", (0, 0), "mod_assets/yuri/unbutton/2l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 3dy3 = im.Composite((960, 960), (0, 0), "yuri/y3.png", (0, 0), "mod_assets/yuri/unbutton/2l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 3dy4 = im.Composite((960, 960), (0, 0), "yuri/y4.png", (0, 0), "mod_assets/yuri/unbutton/2l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 3dy5 = im.Composite((960, 960), (0, 0), "yuri/y5.png", (0, 0), "mod_assets/yuri/unbutton/2l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 3dy6 = im.Composite((960, 960), (0, 0), "yuri/y6.png", (0, 0), "mod_assets/yuri/unbutton/2l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 3dy7 = im.Composite((960, 960), (0, 0), "yuri/y7.png", (0, 0), "mod_assets/yuri/unbutton/2l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")

image yuri 3dy1b = im.Composite((960, 960), (0, 0), "mod_assets/yuri/y2b.png", (0, 0), "mod_assets/yuri/unbutton/2l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 3dy2b = im.Composite((960, 960), (0, 0), "mod_assets/yuri/y4b.png", (0, 0), "mod_assets/yuri/unbutton/2l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")
image yuri 3dy3b = im.Composite((960, 960), (0, 0), "mod_assets/yuri/y7b.png", (0, 0), "mod_assets/yuri/unbutton/2l.png", (0, 0), "mod_assets/yuri/unbutton/2r.png")






image y_glitch_head:
    "images/yuri/za.png"
    0.15
    "images/yuri/zb.png"
    0.15
    "images/yuri/zc.png"
    0.15
    "images/yuri/zd.png"
    0.15
    repeat

image yuri stab_1 = "yuri/stab/1.png"
image yuri stab_2 = "yuri/stab/2.png"
image yuri stab_3 = "yuri/stab/3.png"
image yuri stab_4 = "yuri/stab/4.png"
image yuri stab_5 = "yuri/stab/5.png"
image yuri stab_6 = LiveComposite((960,960), (0, 0), "yuri/stab/6-mask.png", (0, 0), "yuri stab_6_eyes", (0, 0), "yuri/stab/6.png")

image yuri stab_6_eyes:
    "yuri/stab/6-eyes.png"
    subpixel True
    parallel:
        choice:
            xoffset 0.5
        choice:
            xoffset 0
        choice:
            xoffset -0.5
        0.2
        repeat
    parallel:
        choice:
            yoffset 0.5
        choice:
            yoffset 0
        choice:
            yoffset -0.5
        0.2
        repeat
    parallel:
        2.05
        easeout 1.0 yoffset -15
        linear 10 yoffset -15


image yuri oneeye = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/oneeye.png", (0, 0), "yuri oneeye2")
image yuri oneeye2:
    "yuri/oneeye2.png"
    subpixel True
    pause 5.0
    linear 60 xoffset -50 yoffset 20

image yuri glitch:
    "yuri/glitch1.png"
    pause 0.1
    "yuri/glitch2.png"
    pause 0.1
    "yuri/glitch3.png"
    pause 0.1
    "yuri/glitch4.png"
    pause 0.1
    "yuri/glitch5.png"
    pause 0.1
    repeat
image yuri glitch2:
    "yuri/0a.png"
    pause 0.1
    "yuri/0b.png"
    pause 0.5
    "yuri/0a.png"
    pause 0.3
    "yuri/0b.png"
    pause 0.3
    "yuri 1"

image yuri eyes = LiveComposite((1280, 720), (0, 0), "yuri/eyes1.png", (0, 0), "yuripupils")

image yuri eyes_base = "yuri/eyes1.png"

image yuripupils:
    "yuri/eyes2.png"
    yuripupils_move

image yuri cuts = "yuri/cuts.png"

image yuri dragon:
    "yuri 3"
    0.25
    parallel:
        "yuri/dragon1.png"
        0.01
        "yuri/dragon2.png"
        0.01
        repeat
    parallel:
        0.01
        choice:
            xoffset -1
            xoffset -2
            xoffset -5
            xoffset -6
            xoffset -9
            xoffset -10
        0.01
        xoffset 0
        repeat
    time 0.55
    xoffset 0
    "yuri 3"


image monika 1 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 2 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 3 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 4 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 5 = im.Composite((960, 960), (0, 0), "monika/3a.png")

image monika 1a = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 1b = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png")
image monika 1c = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png")
image monika 1d = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png")
image monika 1e = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png")
image monika 1f = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png")
image monika 1g = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png")
image monika 1h = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png")
image monika 1i = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png")
image monika 1j = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
image monika 1k = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
image monika 1l = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
image monika 1m = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png")
image monika 1n = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png")
image monika 1o = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png")
image monika 1p = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png")
image monika 1q = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
image monika 1r = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")
image monika 1s = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/s.png")
image monika 1t = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/t.png")
image monika 1u = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/u.png")
image monika 1v = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/v.png")
image monika 1w = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/w.png")
image monika 1x = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/x.png")
image monika 1y = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/y.png")

image monika 2a = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 2b = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/b.png")
image monika 2c = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/c.png")
image monika 2d = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/d.png")
image monika 2e = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/e.png")
image monika 2f = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/f.png")
image monika 2g = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/g.png")
image monika 2h = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/h.png")
image monika 2i = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/i.png")
image monika 2j = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png")
image monika 2k = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png")
image monika 2l = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png")
image monika 2m = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/m.png")
image monika 2n = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/n.png")
image monika 2o = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/o.png")
image monika 2p = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/p.png")
image monika 2q = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png")
image monika 2r = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png")
image monika 2s = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/s.png")
image monika 2t = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/t.png")
image monika 2u = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/u.png")
image monika 2v = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/v.png")
image monika 2w = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/w.png")
image monika 2x = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/x.png")
image monika 2y = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/y.png")

image monika 3a = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 3b = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png")
image monika 3c = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png")
image monika 3d = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png")
image monika 3e = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png")
image monika 3f = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png")
image monika 3g = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png")
image monika 3h = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png")
image monika 3i = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png")
image monika 3j = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
image monika 3k = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
image monika 3l = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
image monika 3m = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png")
image monika 3n = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png")
image monika 3o = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png")
image monika 3p = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png")
image monika 3q = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
image monika 3r = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")
image monika 3s = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/s.png")
image monika 3t = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/t.png")
image monika 3u = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/u.png")
image monika 3v = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/v.png")
image monika 3w = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/w.png")
image monika 3x = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/x.png")
image monika 3y = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/monika/y.png")

image monika 4a = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 4b = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/b.png")
image monika 4c = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/c.png")
image monika 4d = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/d.png")
image monika 4e = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/e.png")
image monika 4f = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/f.png")
image monika 4g = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/g.png")
image monika 4h = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/h.png")
image monika 4i = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/i.png")
image monika 4j = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png")
image monika 4k = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png")
image monika 4l = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png")
image monika 4m = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/m.png")
image monika 4n = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/n.png")
image monika 4o = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/o.png")
image monika 4p = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/p.png")
image monika 4q = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png")
image monika 4r = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png")
image monika 4s = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/s.png")
image monika 4t = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/t.png")
image monika 4u = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/u.png")
image monika 4v = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/v.png")
image monika 4w = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/w.png")
image monika 4x = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/x.png")
image monika 4y = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/monika/y.png")

image monika 5a = im.Composite((960, 960), (0, 0), "monika/3a.png")
image monika 5b = im.Composite((960, 960), (0, 0), "monika/3b.png")



image monika 1ba = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/ua.png")
image monika 1bb = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/ub.png")
image monika 1bc = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/uc.png")
image monika 1bd = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/ud.png")
image monika 1be = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/ue.png")
image monika 1bf = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/uf.png")
image monika 1bg = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/ug.png")
image monika 1bh = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/uh.png")
image monika 1bi = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/ui.png")
image monika 1bj = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/uj.png")
image monika 1bk = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/uk.png")
image monika 1bl = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/ul.png")
image monika 1bm = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/um.png")
image monika 1bn = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/un.png")
image monika 1bo = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/uo.png")
image monika 1bp = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/up.png")
image monika 1bq = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/uq.png")
image monika 1br = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/ur.png")
image monika 1bs = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/us.png")
image monika 1bt = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/ut.png")
image monika 1bu = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/uu.png")
image monika 1bv = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/uv.png")

image monika 2ba = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/ua.png")
image monika 2bb = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/ub.png")
image monika 2bc = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/uc.png")
image monika 2bd = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/ud.png")
image monika 2be = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/ue.png")
image monika 2bf = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/uf.png")
image monika 2bg = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/ug.png")
image monika 2bh = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/uh.png")
image monika 2bi = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/ui.png")
image monika 2bj = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/uj.png")
image monika 2bk = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/uk.png")
image monika 2bl = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/ul.png")
image monika 2bm = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/um.png")
image monika 2bn = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/un.png")
image monika 2bo = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/uo.png")
image monika 2bp = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/up.png")
image monika 2bq = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/uq.png")
image monika 2br = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/ur.png")
image monika 2bs = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/us.png")
image monika 2bt = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/ut.png")
image monika 2bu = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/uu.png")
image monika 2bv = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/1l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/uv.png")

image monika 3ba = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/ua.png")
image monika 3bb = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/ub.png")
image monika 3bc = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/uc.png")
image monika 3bd = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/ud.png")
image monika 3be = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/ue.png")
image monika 3bf = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/uf.png")
image monika 3bg = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/ug.png")
image monika 3bh = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/uh.png")
image monika 3bi = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/ui.png")
image monika 3bj = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/uj.png")
image monika 3bk = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/uk.png")
image monika 3bl = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/ul.png")
image monika 3bm = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/um.png")
image monika 3bn = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/un.png")
image monika 3bo = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/uo.png")
image monika 3bp = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/up.png")
image monika 3bq = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/uq.png")
image monika 3br = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/ur.png")
image monika 3bs = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/us.png")
image monika 3bt = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/ut.png")
image monika 3bu = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/uu.png")
image monika 3bv = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/1r.png", (0, 0), "mod_assets/monika/casual/uv.png")

image monika 4ba = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/ua.png")
image monika 4bb = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/ub.png")
image monika 4bc = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/uc.png")
image monika 4bd = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/ud.png")
image monika 4be = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/ue.png")
image monika 4bf = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/uf.png")
image monika 4bg = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/ug.png")
image monika 4bh = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/uh.png")
image monika 4bi = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/ui.png")
image monika 4bj = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/uj.png")
image monika 4bk = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/uk.png")
image monika 4bl = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/ul.png")
image monika 4bm = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/um.png")
image monika 4bn = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/un.png")
image monika 4bo = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/uo.png")
image monika 4bp = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/up.png")
image monika 4bq = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/uq.png")
image monika 4br = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/ur.png")
image monika 4bs = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/us.png")
image monika 4bt = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/ut.png")
image monika 4bu = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/uu.png")
image monika 4bv = im.Composite((960, 960), (0, 0), "mod_assets/monika/casual/2l.png", (0, 0), "mod_assets/monika/casual/2r.png", (0, 0), "mod_assets/monika/casual/uv.png")



image monika 1ca = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/a.png")
image monika 1cb = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/b.png")
image monika 1cc = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/c.png")
image monika 1cd = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/d.png")
image monika 1ce = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/e.png")
image monika 1cf = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/f.png")
image monika 1cg = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/g.png")
image monika 1ch = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/h.png")
image monika 1ci = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/i.png")
image monika 1cj = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/j.png")
image monika 1ck = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/k.png")
image monika 1cl = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/l.png")
image monika 1cm = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/m.png")
image monika 1cn = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/n.png")
image monika 1co = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/o.png")
image monika 1cp = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/p.png")
image monika 1cq = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/q.png")
image monika 1cr = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/r.png")
image monika 1cs = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/s.png")
image monika 1ct = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/t.png")
image monika 1cu = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/u.png")
image monika 1cv = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/v.png")

image monika 2ca = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/a.png")
image monika 2cb = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/b.png")
image monika 2cc = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/c.png")
image monika 2cd = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/d.png")
image monika 2ce = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/e.png")
image monika 2cf = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/f.png")
image monika 2cg = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/g.png")
image monika 2ch = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/h.png")
image monika 2ci = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/i.png")
image monika 2cj = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/j.png")
image monika 2ck = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/k.png")
image monika 2cl = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/l.png")
image monika 2cm = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/m.png")
image monika 2cn = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/n.png")
image monika 2co = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/o.png")
image monika 2cp = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/p.png")
image monika 2cq = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/q.png")
image monika 2cr = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/r.png")
image monika 2cs = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/s.png")
image monika 2ct = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/t.png")
image monika 2cu = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/u.png")
image monika 2cv = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/1l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/v.png")

image monika 3ca = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/a.png")
image monika 3cb = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/b.png")
image monika 3cc = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/c.png")
image monika 3cd = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/d.png")
image monika 3ce = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/e.png")
image monika 3cf = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/f.png")
image monika 3cg = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/g.png")
image monika 3ch = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/h.png")
image monika 3ci = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/i.png")
image monika 3cj = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/j.png")
image monika 3ck = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/k.png")
image monika 3cl = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/l.png")
image monika 3cm = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/m.png")
image monika 3cn = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/n.png")
image monika 3co = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/o.png")
image monika 3cp = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/p.png")
image monika 3cq = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/q.png")
image monika 3cr = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/r.png")
image monika 3cs = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/s.png")
image monika 3ct = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/t.png")
image monika 3cu = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/u.png")
image monika 3cv = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/1r.png", (0, 0), "mod_assets/monika/funeral/v.png")

image monika 4ca = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/a.png")
image monika 4cb = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/b.png")
image monika 4cc = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/c.png")
image monika 4cd = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/d.png")
image monika 4ce = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/e.png")
image monika 4cf = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/f.png")
image monika 4cg = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/g.png")
image monika 4ch = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/h.png")
image monika 4ci = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/i.png")
image monika 4cj = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/j.png")
image monika 4ck = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/k.png")
image monika 4cl = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/l.png")
image monika 4cm = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/m.png")
image monika 4cn = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/n.png")
image monika 4co = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/o.png")
image monika 4cp = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/p.png")
image monika 4cq = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/q.png")
image monika 4cr = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/r.png")
image monika 4cs = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/s.png")
image monika 4ct = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/t.png")
image monika 4cu = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/u.png")
image monika 4cv = im.Composite((960, 960), (0, 0), "mod_assets/monika/funeral/2l.png", (0, 0), "mod_assets/monika/funeral/2r.png", (0, 0), "mod_assets/monika/funeral/v.png")

image monika g1:
    "monika/g1.png"
    xoffset 35 yoffset 55
    parallel:
        zoom 1.00
        linear 0.10 zoom 1.03
        repeat
    parallel:
        xoffset 35
        0.20
        xoffset 0
        0.05
        xoffset -10
        0.05
        xoffset 0
        0.05
        xoffset -80
        0.05
        repeat
    time 1.25
    xoffset 0 yoffset 0 zoom 1.00
    "monika 3"

image monika g2:
    block:
        choice:
            "monika/g2.png"
        choice:
            "monika/g3.png"
        choice:
            "monika/g4.png"
    block:
        choice:
            pause 0.05
        choice:
            pause 0.1
        choice:
            pause 0.15
        choice:
            pause 0.2
    repeat


define narrator = Character(ctc="ctc", ctc_position="fixed")
define mc = DynamicCharacter('player', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define s = DynamicCharacter('s_name', image='sayori', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define m = DynamicCharacter('m_name', image='monika', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define n = DynamicCharacter('n_name', image='natsuki', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define y = DynamicCharacter('y_name', image='yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define ny = Character('Nat & Yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

default persistent.playername = ""
default player = persistent.playername
default persistent.playthrough = 0
default persistent.yuri_kill = 0
default persistent.seen_eyes = None
default persistent.seen_sticker = None
default persistent.ghost_menu = None
default persistent.seen_ghost_menu = None
default seen_eyes_this_chapter = False
default persistent.anticheat = 0
default persistent.clear = [False, False, False, False, False, False, False, False, False, False]
default persistent.special_poems = None
default persistent.clearall = None
default persistent.menu_bg_m = None
default persistent.first_load = None
default persistent.first_poem = None
default persistent.seen_colors_poem = None
default persistent.monika_back = None
default in_sayori_kill = None
default in_yuri_kill = None
default anticheat = 0
define config.mouse = None
default allow_skipping = True
default basedir = config.basedir
default chapter = 0
default currentpos = 0
default faint_effect = None

default s_name = "Sayori"
default m_name = "Monika"
default n_name = "Natsuki"
default y_name = "Yuri"



default n_poemappeal = [0, 0, 0]
default s_poemappeal = [0, 0, 0]
default y_poemappeal = [0, 0, 0]
default m_poemappeal = [0, 0, 0]


default poemwinner = ['sayori', 'sayori', 'sayori']


default s_readpoem = False
default n_readpoem = False
default y_readpoem = False
default m_readpoem = False


default poemsread = 0



default n_appeal = 0
default s_appeal = 0
default y_appeal = 0
default m_appeal = 0



default n_exclusivewatched = False
default y_exclusivewatched = False


default y_gave = False
default y_ranaway = False


default ch1_choice = "sayori"


default help_sayori = None
default help_monika = None


default ch4_scene = "yuri"
default ch4_name = "Yuri"
default sayori_confess = True


default natsuki_23 = None
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
