#!/usr/bin/python3
"""initializzing the package"""

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
