#!/usr/bin/env python3

# import anki features
from anki import hooks
from aqt import utils
from aqt.utils import showInfo
from aqt.qt import *
from aqt import mw

# import from other files
from .vault import vault

def refresh_obsidian_database():
	showInfo("Database Refreshed")
	new_vault = vault("/Users/xiuxuan/Library/Mobile Documents/iCloud~org~zrey~metion/Documents/Knowledge Base")
	
action = QAction("Import from Obsidian", mw)
action.triggered.connect(refresh_obsidian_database)
mw.form.menuTools.addAction(action)