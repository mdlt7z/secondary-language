import bpy


def set_language(lang_code):
    prefs = bpy.context.preferences.addons[__package__].preferences
    view = bpy.context.preferences.view

    view.language = lang_code
    view.use_translate_tooltips = prefs.trans_tooltips
    view.use_translate_interface = prefs.trans_interface
    view.use_translate_reports = prefs.trans_reports
    view.use_translate_new_dataname = prefs.trans_new_dataname


def update_active_language(self, context):
    if self.active_language == "default":
        set_language(self.default_language)
    else:
        set_language(self.secondary_language)


def update_default_language(self, context):
    if self.active_language == "default":
        set_language(self.default_language)


def update_secondary_language(self, context):
    if self.active_language == "secondary":
        set_language(self.secondary_language)
