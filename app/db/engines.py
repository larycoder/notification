import sqlite3
from utils.file_util import FileUtil


global sqlite_engine
sqlite_engine = sqlite3.connect(FileUtil.getConfig()['db'], check_same_thread=False)