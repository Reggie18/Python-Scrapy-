import gooey
gooey_root = os.path.dirname(gooey.__file__)
gooey_languages = Tree(os.path.join(gooey_root, 'languages'), prefix = 'gooey/languages')

a = Analysis(['quote.py'],
             pathex=['C:\\Users\\Colton\\.virtualenvs\\bot-bot-JBkeVQQB\\Scripts', 'C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\ucrt\\DLLs\\x86'],
             hiddenimports=[],
             hookspath=['.\\hooks\\'],
             runtime_hooks=None,
             datas=[('.\\spiders\\','.\\spiders\\'), ('.\\settings.py','.'),
                    ('.\\scrapy.cfg','.'), ('.\\items.py','.'),
                    ('.\\middlewares.py','.'), ('.\\pipelines.py','.')
                   ]
             )
pyz = PYZ(a.pure)

options = [('u', None, 'OPTION'), ('u', None, 'OPTION'), ('u', None, 'OPTION')]

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          options,
          gooey_languages, # Add them in to collected files
          gooey_images, # Same here.
          name='quotes',
          debug=False,
          strip=None,
          upx=True,
          console=False,
          windowed=True,
          icon=os.path.join(gooey_root, 'images', 'program_icon.ico'))

coll = COLLECT(exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    options,
    gooey_languages, # Add them in to collected files
    gooey_images, # Same here.
    name='quotes',
    debug=False,
    strip=False,
    upx=True,
    console=False,
    windowed=True,
    icon=os.path.join(gooey_root, 'images', 'program_icon.ico'))