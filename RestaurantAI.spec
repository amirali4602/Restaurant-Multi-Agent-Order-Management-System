# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_submodules


hiddenimports = (
    collect_submodules('agents')
    + collect_submodules('gui')
    + collect_submodules('services')
    + collect_submodules('models')
    + collect_submodules('messaging')
)


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('assets', 'assets'),
        ('config', 'config'),
    ],
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)


pyz = PYZ(
    a.pure
)


exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='RestaurantAI',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon='assets/icon.ico',
)


coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    [],
    name='RestaurantAI',
)