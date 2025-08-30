import bpy
from bl_i18n_utils.settings import LANGUAGES
from bpy.props import BoolProperty, EnumProperty
from bpy.types import AddonPreferences

from .utils import (
    get_use_secondary,
    set_use_secondary,
    update_active_language,
    update_default_language,
    update_secondary_language,
)

languages = [(lang[2], lang[1], "") for lang in LANGUAGES]


class SecondaryLanguagePreferences(AddonPreferences):
    bl_idname = __package__

    use_secondary_language: BoolProperty(
        name="Secondary Language",
        description="Use secondary language",
        get=get_use_secondary,
        set=set_use_secondary,
    )

    active_language: EnumProperty(
        items=[("default", "Default", ""), ("secondary", "Secondary", "")],
        name="Active Language",
        description="Select the active language",
        default="default",
        update=update_active_language,
    )

    default_language: EnumProperty(
        items=languages,
        name="Default",
        description="Select the default language",
        default="en_US",
        update=update_default_language,
    )
    secondary_language: EnumProperty(
        items=languages,
        name="Secondary",
        description="Select the secondary language",
        default="ja_JP",
        update=update_secondary_language,
    )

    trans_tooltips: BoolProperty(
        name="Tooltips",
        description="Translate tooltips",
        default=True,
        update=update_active_language,
    )
    trans_interface: BoolProperty(
        name="Interface",
        description="Translate interface",
        default=True,
        update=update_active_language,
    )
    trans_reports: BoolProperty(
        name="Reports",
        description="Translate reports",
        default=True,
        update=update_active_language,
    )
    trans_new_dataname: BoolProperty(
        name="New Data",
        description="Translate new data",
        default=True,
        update=update_active_language,
    )

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True

        row = layout.row(align=True)
        row.prop(self, "active_language", expand=True)

        col = layout.column(align=True)
        col.prop(self, "default_language")
        col.prop(self, "secondary_language")

        col = layout.column(heading="Translate", heading_ctxt="Preferences")
        col.prop(self, "trans_tooltips")
        col.prop(self, "trans_interface")
        col.prop(self, "trans_reports")
        col.prop(self, "trans_new_dataname")

        layout.operator("wm.secondary_language_keymap_open")


def register():
    bpy.utils.register_class(SecondaryLanguagePreferences)


def unregister():
    bpy.utils.unregister_class(SecondaryLanguagePreferences)
