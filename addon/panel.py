import bpy
from bpy.types import Panel


class SECONDARY_LANGUAGE_PT_Panel(Panel):
    bl_space_type = "TOPBAR"
    bl_region_type = "HEADER"
    bl_label = "Secondary Language"

    def draw(self, context):
        layout = self.layout
        prefs = context.preferences.addons[__package__].preferences

        row = layout.row(align=True)
        row.label(text="Secondary Language")
        row.operator("wm.secondary_language_prefs_open", icon="PREFERENCES", text="")

        row = layout.row(align=True)
        row.prop(
            prefs,
            "use_secondary_language",
            text="",
            icon="WORLD",
            toggle=True,
        )
        row.prop(prefs, "secondary_language", text="")


def draw_secondary_language(self, context):
    if context.region.alignment != "RIGHT":
        return

    layout = self.layout
    prefs = context.preferences.addons[__package__].preferences

    row = layout.row(align=True)
    row.prop(
        prefs,
        "use_secondary_language",
        text="",
        icon="WORLD",
        toggle=True,
    )
    row.popover(panel="SECONDARY_LANGUAGE_PT_Panel", text="")


def register():
    bpy.utils.register_class(SECONDARY_LANGUAGE_PT_Panel)
    bpy.types.TOPBAR_HT_upper_bar.append(draw_secondary_language)


def unregister():
    bpy.utils.unregister_class(SECONDARY_LANGUAGE_PT_Panel)
    bpy.types.TOPBAR_HT_upper_bar.remove(draw_secondary_language)
