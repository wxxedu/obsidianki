#!/usr/bin/env python3

# import anki features
from anki import hooks
from aqt import utils
from aqt.utils import showInfo
from aqt.qt import *
from aqt import mw

# import from other files
from .vault import vault
from .settings import settings

def refresh_obsidian_database():
	showInfo("Database Refreshed")
	preferences = settings()
	showInfo(preferences.get_path_to_vault())
	new_vault = vault(preferences.get_path_to_vault())
	new_vault.get_folders_and_files()
	
action = QAction("Import from Obsidian", mw)
action.triggered.connect(refresh_obsidian_database)
mw.form.menuTools.addAction(action)