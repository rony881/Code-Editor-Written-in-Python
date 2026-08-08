from ui.base.menu_base import MenuBaseWidget, MenuItem, MenuStructure
from ui.themes.color_theme import APP_MENUBAR_STYLE


class EditorMenuBar(MenuBaseWidget):
    """
    Menu bar for a code editor: File | Edit | View | Settings | About | Help
    """
    def __init__(self, window, parent=None):
        super().__init__(parent)
        self.main_window = window
        self.build(self._structure())
        self.setStyleSheet(APP_MENUBAR_STYLE)

    def _structure(self) -> MenuStructure:
        win = self.main_window
        return {
            "File": [
                MenuItem("New", handler=win.new_file, shortcut="Ctrl+N"),
                MenuItem("Open...", handler=win.open_file, shortcut="Ctrl+O"),
                MenuItem("Save", handler=win.save_file, shortcut="Ctrl+S"),
                MenuItem("Save As...", handler=win.save_file_as, shortcut="Ctrl+Shift+S"),
                None,
                MenuItem("Close Tab", handler=win.close_tab, shortcut="Ctrl+W"),
                None,
                MenuItem("Exit", handler=win.close, shortcut="Ctrl+Q"),
            ],
            "Edit": [
                MenuItem("Undo", handler=win.undo, shortcut="Ctrl+Z"),
                MenuItem("Redo", handler=win.redo, shortcut="Ctrl+Y"),
                None,
                MenuItem("Cut", handler=win.cut, shortcut="Ctrl+X"),
                MenuItem("Copy", handler=win.copy, shortcut="Ctrl+C"),
                MenuItem("Paste", handler=win.paste, shortcut="Ctrl+V"),
                None,
                MenuItem("Find...", handler=win.find_, shortcut="Ctrl+F"),
                MenuItem("Replace...", handler=win.replace, shortcut="Ctrl+H"),
                MenuItem("Go to Line...", handler=win.go_to_line, shortcut="Ctrl+G"),
            ],
            "View": [
                MenuItem("Toggle Sidebar", handler=win.toggle_sidebar, shortcut="Ctrl+B"),
                MenuItem("Toggle Terminal", handler=win.toggle_terminal, shortcut="Ctrl+`"),
                MenuItem("Toggle Minimap", handler=win.toggle_minimap),
                None,
                MenuItem("Zoom In", handler=win.zoom_in, shortcut="Ctrl+="),
                MenuItem("Zoom Out", handler=win.zoom_out, shortcut="Ctrl+-"),
                MenuItem("Reset Zoom", handler=win.reset_zoom, shortcut="Ctrl+0"),
            ],
            "Settings": [
                MenuItem("Preferences...", handler=win.open_preferences, shortcut="Ctrl+,"),
                MenuItem("Keyboard Shortcuts...", handler=win.open_shortcuts_editor),
                MenuItem("Theme...", handler=win.open_theme_settings),
            ],
            "About": [
                MenuItem("About Editor", handler=win.show_about_dialog),
                MenuItem("Check for Updates...", handler=win.check_for_updates),
            ],
            "Help": [
                MenuItem("Documentation", handler=win.open_docs, shortcut="F1"),
                MenuItem("Report Issue...", handler=win.report_issue),
            ],
        }