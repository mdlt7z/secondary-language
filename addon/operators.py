import bpy
from bpy.types import Operator


class SECONDARY_LANGUAGE_OT_Toggle(Operator):
    bl_idname = "secondary_language.toggle"
    bl_label = "Secondary Language"
    bl_description = "Enable secondary language"

    def execute(self, context):
        prefs = context.preferences.addons[__package__].preferences

        if prefs.active_language == "default":
            prefs.active_language = "secondary"
        else:
            prefs.active_language = "default"

        return {"FINISHED"}


class SECONDARY_LANGUAGE_OT_OpenAddonPreferences(Operator):
    bl_idname = "secondary_language.open_addon_prefs"
    bl_label = "Preferences"
    bl_description = "Open Addon Preferences"

    def execute(self, context):
        bpy.ops.preferences.addon_show(module=__package__)

        return {"FINISHED"}


class SECONDARY_LANGUAGE_OT_OpenKeymapPreferences(Operator):
    bl_idname = "secondary_language.open_keymap_prefs"
    bl_label = "Keymap Preferences"
    bl_description = "Open Keymap Preferences"

    def execute(self, context):
        bpy.ops.screen.userpref_show()
        bpy.context.preferences.active_section = "KEYMAP"

        for area in bpy.context.window.screen.areas:
            if area.type == "PREFERENCES":
                space = area.spaces.active
                space.filter_type = "NAME"
                space.filter_text = "secondary_language.toggle"

        return {"FINISHED"}


classes = [
    SECONDARY_LANGUAGE_OT_Toggle,
    SECONDARY_LANGUAGE_OT_OpenAddonPreferences,
    SECONDARY_LANGUAGE_OT_OpenKeymapPreferences,
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
