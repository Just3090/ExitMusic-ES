default persistent.monika_present = 1
default persistent.yuri_present = 1
default persistent.natsuki_present = 1
default persistent.sayori_present = 1

default persistent.language = None

screen choose_language():
    default local_lang = _preferences.language
    default chosen_lang = _preferences.language

    modal True
    style_prefix "radio"

    add "gui/overlay/confirm.png"

    frame:
        style "confirm_frame"

        vbox:
            xalign .5
            yalign .5
            xsize 760
            spacing 30

            label _("Please select a language"):
                style "confirm_prompt"
                xalign 0.5

            vbox:
                style_prefix "radio"
                label _("Language")

                # Real languages should go in alphabetical order by English name.
                textbutton "English" text_font "DejaVuSans.ttf" action [
                    Language(None),
                    SetField(persistent, "language", "english"),
                    SetScreenVariable("chosen_lang", "english"),
                    Show("dialog", message="It is recommended to restart to apply the changes.", ok_action=Quit())
                ]
                textbutton "Español" text_font "DejaVuSans.ttf" action [
                    Language("spanish"),
                    SetField(persistent, "language", "spanish"),
                    SetScreenVariable("chosen_lang", "spanish"),
                    Show("dialog", message="Se recomienda reiniciar el juego\npara aplicar los cambios.", ok_action=Quit())
                ]
                # textbutton "Español (MX)" text_font "DejaVuSans.ttf" action [
                #     Language("spanish_mx"),
                #     SetField(persistent, "language", "spanish_mxF"),
                #     SetScreenVariable("chosen_lang", "spanish_mx"),
                #     Show("dialog", message="Se recomienda reiniciar el juego\npara aplicar los cambios.", ok_action=Quit())
                # ]
                # textbutton "Português (BR)" text_font "DejaVuSans.ttf" action [
                #     Language("ptBR"),
                #     SetField(persistent, "language", "ptBR"),
                #     SetScreenVariable("chosen_lang", "ptBR"),
                #     Show("dialog", message="Recomenda-se reiniciar para aplicar as alterações.", ok_action=Quit())
                # ]

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("OK") action [
                    Language(None),
                    SetField(persistent, "language", "english"),
                    SetScreenVariable("chosen_lang", "english"),
                    Show("dialog", message="It is recommended to restart to apply the changes.", ok_action=[Hide("dialog"), Return()])
                    ] style "ok_button_custom"

# Define el estilo personalizado para el botón "OK"
style ok_button_custom is button:
    background None  # Sin fondo
    foreground None  # Sin borde o efecto de selección
    hover_background None  # Sin efecto al pasar el mouse
    hover_foreground None  # Sin borde al pasar el mouse
    insensitive_background None  # Sin efecto cuando está deshabilitado
    insensitive_foreground None

# Music Room

# init python:
#     """
#     where:
#         mr.add - to define the audio files
#         mr.Play - play the selected track

#         in the music list:
#             "path/to/file": ['title for the song']
#     """

#     mr = MusicRoom(fadeout=0.5)

#     mr.add("bgm/1.ogg", always_unlocked=True)
#     mr.add("bgm/2.ogg")
#     mr.add("bgm/4.ogg")
#     mr.add("bgm/5.ogg")
#     mr.add("bgm/6.ogg")
#     mr.add("bgm/7.ogg")
#     mr.add("bgm/8.ogg")
#     mr.add("bgm/9.ogg")
#     mr.add("bgm/10.ogg")
#     mr.add("bgm/credits.ogg")
#     mr.add("bgm/m1.ogg")
#     mr.add("bgm/monika-end.ogg")
#     mr.add("bgm/d.ogg")


#     musicList = {
#         "bgm/1.ogg": ["Doki Doki Literature Club!"],
#         "bgm/2.ogg": ["Ohayou Sayori!"],
#         "bgm/4.ogg": ["Dreams Of Love and Literature"],
#         "bgm/5.ogg": ["Okay, Everyone!"],
#         "bgm/6.ogg": ["Play With Me"],
#         "bgm/7.ogg": ["Poem Panic!"],
#         "bgm/8.ogg": ["Daijoubu!"],
#         "bgm/9.ogg": ["My Feelings"],
#         "bgm/10.ogg": ["My Confession"],
#         "bgm/credits.ogg": ["Your Reality"],
#         "bgm/m1.ogg": ["Just Monika"],
#         "bgm/monika-end.ogg": ["I Still Love You"],
#         "bgm/d.ogg": ["Sayo-nara"]
#     }


# screen music_room():
#     tag menu
#     add "menu_bg"

#     use game_menu(_("Music")):
#         style_prefix "music_room"

#         viewport id "mp":
#             area (25, 0, 500, 475)

#             scrollbars "vertical"
#             mousewheel True
#             draggable True
#             has vbox

#             vbox:
#                 xoffset 10
#                 yoffset 0
#                 spacing 20

#                 # here add the songs
#                 for path, data in musicList.items():
#                     textbutton _(data[0]) action mr.Play(path)


#         vbar value YScrollValue(viewport="mp") style "poem_vbar"
#         if renpy.music.get_playing() is not None:
#             $ playing_track = renpy.music.get_playing()
#             $ cleaned_track = playing_track.replace("<loop 0>", "").replace("<loop 3.150>", "").replace("<loop 4.77>", "").replace("<loop 22.073>", "")



#             if cleaned_track in musicList:
#                 $ currentTrack = musicList[cleaned_track]
#                 text (currentTrack[0]):
#                     xpos 300
#                     ypos -90
#                     size 33
#                     font "gui/font/Halogen.ttf"
#                     color "#fff"
#                 $ lastPlayed = cleaned_track
#             else:
#                 text "Track desconocido":
#                     xpos 300
#                     ypos -90
#                     size 40
#                     font "gui/font/Halogen.ttf"
#                     color "#fff"
#         else:
#             text " ":
#                 xpos 200
#                 ypos -80
#         text "Playing:":
#             xpos 0
#             ypos -100
#             size 35
#             font "gui/font/RifficFree-Bold.ttf"
#             color "#fff"

#         textbutton "Next":
#             action mr.Next()
#             xalign 0.8
#             yalign 0.98
#         textbutton "Pause":
#             action mr.Stop()
#             xalign 0.55
#             yalign 0.98

#         if renpy.music.get_playing() not in musicList:
#             $ original = "bgm/1.ogg"
#         else:
#             $ original = renpy.music.get_playing()

#         if original:
#             $ fixed1 = original.replace("<loop 0>", "")
#             $ fixed2 = fixed1.replace("<loop 3.150>", "")
#             $ fixed3 = fixed2.replace("<loop 4.77>", "")

#         textbutton "Play":
#             action mr.Play(fixed3)
#             xalign 0.3
#             yalign 0.98
#         textbutton "Previous":
#             action mr.Previous()
#             xalign 0.0
#             yalign 0.98

#     on "replace" action mr.Play("bgm/1.ogg")
#     on "replaced" action Play("music", "bgm/1.ogg")

# style music_room_vbox is vbox
# style music_room_button_text is gui_button_text

# style music_room_button_text:
#     properties gui.button_text_properties("navigation_button")
#     font "gui/font/RifficFree-Bold.ttf"
#     color "#fff"
#     outlines [(4, text_outline_color, 0, 0), (2, text_outline_color, 2, 2)]
#     hover_outlines [(4, "#fac", 0, 0), (2, "#fac", 2, 2)]
#     insensitive_outlines [(4, "#fce", 0, 0), (2, "#fce", 2, 2)]






# # Galeria

# image lockedthumb = "/images/lockedthumb.png"


# init python:

#     def MaxScale(img, minwidth=config.screen_width, minheight=config.screen_height):
#         currwidth, currheight = renpy.image_size(img)
#         xscale = float(minwidth) / currwidth
#         yscale = float(minheight) / currheight
        
#         if xscale > yscale:
#             maxscale = xscale
#         else:
#             maxscale = yscale
        
#         return im.FactorScale(img, maxscale, maxscale)

#     def MinScale(img, maxwidth=config.screen_width, maxheight=config.screen_height):
#         currwidth, currheight = renpy.image_size(img)
#         xscale = float(maxwidth) / currwidth
#         yscale = float(maxheight) / currheight
        
#         if xscale < yscale:
#             minscale = xscale
#         else:
#             minscale = yscale
        
#         return im.FactorScale(img, minscale, minscale)

#     maxnumx = 2
#     maxnumy = 3
#     maxthumbx = config.screen_width / (maxnumx + 1)
#     maxthumby = config.screen_height / (maxnumy + 1)
#     maxperpage = maxnumx * maxnumy
#     gallery_page = 0
#     closeup_page = 0

#     class GalleryItem:
#         def __init__(self, name, images, thumb, locked="lockedthumb"):
#             self.name = name
#             self.images = images
#             self.thumb = thumb
#             self.locked = locked
#             self.refresh_lock()
#         def num_images(self):
#             return len(self.images)
        
#         def refresh_lock(self):
#             self.num_unlocked = 0
#             lockme = False
#             for img in self.images:
#                 if not renpy.seen_image(img):
#                     lockme = True
#                 else:
#                     self.num_unlocked += 1
#             self.is_locked = lockme

#     gallery_items = []
#     """
#     where:
#         1st: generic name to include in python
#         2nd: renpy argument/file image where you show the image in any label
#         3rd: image preview (285px x 160px) definition to show in the gallery
#     """
#     # BGs
#     gallery_items.append(GalleryItem("residential_day", ["bg residential_day"], "residential_day_preview"))
#     gallery_items.append(GalleryItem("bedroom", ["bg bedroom"], "bedroom_preview"))
#     gallery_items.append(GalleryItem("classrom", ["bg class_day"], "classroom_preview"))
#     gallery_items.append(GalleryItem("closet", ["bg closet"], "closet_preview"))
#     gallery_items.append(GalleryItem("club", ["bg club_day"], "club_preview"))
#     gallery_items.append(GalleryItem("corridor", ["bg corridor"], "corridor_preview"))
#     gallery_items.append(GalleryItem("house", ["bg house"], "house_preview"))
#     gallery_items.append(GalleryItem("kitchen", ["bg kitchen"], "kitchen_preview"))

#     # CGs
#     gallery_items.append(GalleryItem("n_cg1_android", ["n_cg1_android"], "n_cg1_android_preview"))
#     gallery_items.append(GalleryItem("n_cg2", ["n_cg2_full"], "n_cg2_preview"))
#     gallery_items.append(GalleryItem("n_cg3", ["n_cg3_base"], "n_cg3_preview"))
#     gallery_items.append(GalleryItem("s_cg1", ["s_cg1"], "s_cg1_preview"))
#     gallery_items.append(GalleryItem("s_cg2", ["s_cg2_base2"], "s_cg2_preview"))
#     gallery_items.append(GalleryItem("s_cg3", ["s_cg3"], "s_cg3_preview"))
#     gallery_items.append(GalleryItem("s_bedroom", ["s_kill_bg"], "s_kill_bg_preview"))
#     gallery_items.append(GalleryItem("y_cg1", ["y_cg1_base"], "y_cg1_preview"))
#     gallery_items.append(GalleryItem("y_cg2", ["y_cg2_full"], "y_cg2_preview"))
#     gallery_items.append(GalleryItem("y_cg3", ["y_cg3_base"], "y_cg3_preview"))



# # BGs previews
# image residential_day_preview = "residential.png"
# image bedroom_preview = "bedroom_preview.png"
# image classroom_preview = "class_preview.png"
# image closet_preview = "closet_preview.png"
# image club_preview = "club_preview.png"
# image corridor_preview = "corridor_preview.png"
# image house_preview = "house_preview.png"
# image kitchen_preview = "kitchen_preview.png"

# #CGs previews
# image n_cg1_android_preview = "n_cg1_android.png"
# image n_cg2_preview = "n_cg2_preview.png"
# image n_cg3_preview = "n_cg3_preview.png"
# image s_cg1_preview = "s_cg1_preview.png"
# image s_cg2_preview = "s_cg2_preview.png"
# image s_cg3_preview = "s_cg3_preview.png"
# image s_kill_bg_preview = "s_kill_bg_preview.png"
# image y_cg1_preview = "y_cg1_preview.png"
# image y_cg2_preview = "y_cg2_preview.png"
# image y_cg3_preview = "y_cg3_preview.png"





# screen gallery():
#     tag menu
#     add "menu_bg"

#     $ start = gallery_page * maxperpage
#     $ end = min(start + maxperpage - 1, len(gallery_items) - 1)

#     use game_menu(_("Gallery")):
#         style_prefix "gallery"
#         vbox:
#             xoffset 10
#             yoffset -45






#             grid maxnumx maxnumy:
#                 xfill True
#                 yfill True

#                 for i in range(start, end + 1):
#                     $ gallery_items[i].refresh_lock()
#                     if gallery_items[i].is_locked:
#                         add gallery_items[i].locked:
#                             xalign 0.5
#                             yalign 0.5
#                     else:
#                         imagebutton idle gallery_items[i].thumb:
#                             action Show("gallery_closeup", dissolve, gallery_items[i].images)
#                             xalign 0.5
#                             yalign 0.5

#                 for i in range(end + 1, start + maxperpage):
#                     null

#         hbox:
#             xalign 0.825
#             yalign 0.98
#             spacing 20

#             if gallery_page > 0:
#                 textbutton "Previous":
#                     action SetVariable("gallery_page", gallery_page - 1)
#             if (gallery_page + 1) * maxperpage < len(gallery_items):
#                 textbutton "Next":
#                     action SetVariable("gallery_page", gallery_page + 1)






# screen gallery_closeup(images):

#     imagebutton:
#         idle images[closeup_page]
#         action [SetVariable("closeup_page", 0), Hide("gallery_closeup", dissolve)]
#         at truecenter




# style gallery_vbox is vbox

# style gallery_button_text is gui_button_text

# style gallery_button_text:
#     size 30
#     properties gui.button_text_properties("navigation_button")
#     font "gui/font/RifficFree-Bold.ttf"
#     color "#fff"
#     outlines [(4, text_outline_color, 0, 0), (2, text_outline_color, 2, 2)]
#     hover_outlines [(4, "#fac", 0, 0), (2, "#fac", 2, 2)]
#     insensitive_outlines [(4, "#fce", 0, 0), (2, "#fce", 2, 2)]