import xbmcaddon
import xbmcgui
import xbmc

 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
 
keymap_path = xbmc.translatePath('special://userdata/keymaps')

keymap_xml = """<keymap>
    <global>
        <keyboard>
            <play_pause>ContextMenu</play_pause>
        </keyboard>
    </global>
    <fullscreenvideo>
        <keyboard>
            <play_pause>PlayPause</play_pause>
            <key id="61448">stop</key>
        </keyboard>
    </fullscreenvideo>
</keymap>
"""


target = open(keymap_path + "/nexus.xml", "w")
target.write(keymap_xml)
target.close()



line1 = "Nexus Player Remote Re-Mapped"
line2 = "PLAY button is now mapped to Context"
line3 = "EXIT Kodi and restart to have new keymap take affect"
 
xbmcgui.Dialog().ok(addonname, line1, line2, line3)
