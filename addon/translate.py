import bpy

translations_dict = {
    "ja_JP": {
        # preferences
        ("*", "Select the active language"): "アクティブな言語を選択",
        ("*", "Select the default language"): "デフォルト言語を選択",
        ("*", "Select the secondary language"): "第二言語を選択",
        ("*", "Translate tooltips"): "ツールチップを翻訳",
        ("*", "Translate interface"): "インターフェイスを翻訳",
        ("*", "Translate reports"): "エラーメッセージ等を翻訳",
        ("*", "Translate new data"): "新しいデータブロックを翻訳",
        # operators
        ("*", "Enable secondary language"): "第二言語に切り替えます",
        ("*", "Open Addon Preferences"): "アドオン設定を開く",
        ("Operator", "Keymap Preferences"): "キーマップ設定",
        ("*", "Open Keymap Preferences"): "キーマップ設定を開く",
    }
}


def register():
    bpy.app.translations.register(__name__, translations_dict)


def unregister():
    bpy.app.translations.unregister(__name__)
