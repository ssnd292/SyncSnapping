bl_info = {
    "name" : "SyncSnapping",
    "author" : "Sebastian Schneider",
    "description" : "Syncs enabling and disabling snapping in both 3D View and UV Window",
    "blender" : (3, 6, 2),
    'version': (0, 1, 0 ,0),
    "location" : "View3D",
    "warning" : "",
    "category" : "View3D"
}

import bpy
from bpy.utils import register_class, unregister_class

from bpy.types import AddonPreferences
from bpy.props import (PointerProperty)

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
