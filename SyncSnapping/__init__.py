# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

# INFO about the addon in USERPREFS
bl_info = {
    "name" : "SyncSnapping",
    "author" : "Sebastian Schneider",
    "description" : "Syncs enabling and disabling snapping in both 3D View and UV Window. Shortcut on S. Can be changed at any time in the Keymap menu.",
    "blender" : (3, 6, 5),
    'version': (0, 1, 0 ,0),
    "location" : "View3D",
    "warning" : "",
    "category" : "View3D"
}

import bpy
from bpy.utils import register_class, unregister_class

class SNAP_OT_SwitchSnapping(bpy.types.Operator):
    bl_idname = "snap.switchsnapping"
    bl_label = "Sync Snapping"
    bl_description = "Enable or disable snapping in 3D View & UV workspace at the same time"
    bl_options = {'REGISTER', 'UNDO'}

    def enable_snapping(self, context):
        toolSettings = bpy.context.scene.tool_settings   
        if toolSettings.use_snap == False:
            toolSettings.use_snap = True
        else:
            toolSettings.use_snap = False
            
        if toolSettings.use_snap_uv == False:
            toolSettings.use_snap_uv = True
        else:
            toolSettings.use_snap_uv = False

    def execute(self, context):
        self.enable_snapping(context)
        return{'FINISHED'}


addon_keymaps = []

def register():
    register_class(SNAP_OT_SwitchSnapping)

    # Add the hotkey
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = wm.keyconfigs.addon.keymaps.new(name='Window', space_type='EMPTY')
        kmi = km.keymap_items.new(SNAP_OT_SwitchSnapping.bl_idname, type='S', value='PRESS', ctrl=False)
        addon_keymaps.append((km, kmi))



def unregister():
    unregister_class(SNAP_OT_SwitchSnapping)

    # Remove the hotkey
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

if __name__ == "__main__":
    register()
