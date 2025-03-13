# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# �ռ�����Python�ļ�����Դ
a = Analysis(
    ['gui/main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('ai', 'ai'),
        ('bot', 'bot'),          # ȷ��botĿ¼������
        ('config.json', '.'),
        ('resources', 'resources'),
        ('memory.json', '.'),    # �������
    ],
    hiddenimports=[
        'ai.agent',
        'ai.deepseek_api',
        'ai.memory',
        'ai.learning',
        'ai.prompts',
        'test_connection',
        'PyQt6',
        'requests'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

# ������ִ���ļ�
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='MinecraftAI',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='resources/icon.ico'
)
